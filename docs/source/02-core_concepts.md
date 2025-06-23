# Core Concepts

## Task

At the heart of the Pharia Inference SDK is a generic concept called a `task`. A task transforms an input parameter to an output parameter, similar to a function in mathematics:

```
Task: Input -> Output
```

In Python, this is realized by an abstract class with type-parameters and the abstract method `do_run` in which the actual transformation is implemented:

```py
class Task(ABC, Generic[Input, Output]):

    @abstractmethod
    def do_run(self, input: Input, task_span: TaskSpan) -> Output:
        ...
```

`Input` and `Output` are normal Python datatypes that can be serialized from and to JSON. For this the Pharia Inference SDK relies on [Pydantic](https://docs.pydantic.dev/). The types used are defined in the form of type-aliases PydanticSerializable.

The second parameter `task_span` is used for [tracing](#trace), as described below.

`do_run` is the method that implements a concrete task and must be provided by you. It is executed by the external interface method `run` of a task:

```py
class Task(ABC, Generic[Input, Output]):
    @final
    def run(self, input: Input, tracer: Tracer) -> Output:
      ...
```

The signatures of the `do_run` and `run` methods differ only in the [tracing](#trace) parameters.

### Levels of abstraction

Even though the concept is generic, the main purpose for a task is of course to make use of an LLM for the transformation. Tasks are defined at different levels of abstraction. Higher level tasks (also called use cases) reflect a typical user problem, whereas lower level tasks are used to interface with an LLM on a generic or technical level.

Typical examples of higher level tasks (use cases) might be the following:

- Answering a question based on a given document: `QA: (Document, Question) -> Answer`
- Generate a summary of a given document: `Summary: Document -> Summary`

Examples of lower level tasks might be the following:

- Let the model generate text based on an instruction and some context: `Instruct: (Context, Instruction) -> Completion`
- Chunk a text in smaller pieces at optimized boundaries (typically to make it fit into an LLM's context-size): `Chunk: Text -> [Chunk]`

### Composability

Typically you build higher level tasks from lower level tasks. Given a task, you can draw a dependency graph that illustrates which subtasks it is using and in turn which subtasks they are using. This graph typically forms a hierarchy or, more generally, a directed acyclic graph. The following drawing shows this graph for the Intelligence Layer's `RecursiveSummarize` task:

![Studio Recursive Summary](../_static/assets/studio-recursive-summary.drawio.svg)

(trace)=
### Trace

A task implements a workflow. It processes its input, passes it on to subtasks, processes the outputs of the subtasks, and builds its own output. This workflow can be represented in a trace. For this, a task's `run` method takes a `Tracer` that takes care of storing details on the steps of this workflow, including the tasks that have been invoked along with their input and output and timing information.

To represent this tracing we use the following concepts:

- A `Tracer` is passed to a task's `run` method and provides methods for opening `Span`s or `TaskSpan`s.
- A `Span` is a `Tracer` that groups multiple logs and runtime durations together as a single, logical step in the workflow.
- A `TaskSpan` is a `Span` that groups multiple logs together with the task's specific input and output. An opened `TaskSpan` is passed to `Task.do_run`. Since a `TaskSpan` is a `Tracer` a `do_run` implementation can pass this instance on to `run` methods of subtasks.

The following diagram illustrates these relationships:

![Studio Tracer](../_static/assets/studio-tracer.drawio.svg)

Each of these concepts is implemented in form of an abstract base class and the Intelligence Layer provides several concrete implementations that store the actual traces in different backends. For each backend, each of the three abstract classes `Tracer`, `Span` and `TaskSpan` needs to be implemented. The top-level `Tracer` implementations are the following:

- The `NoOpTracer` is used when no tracing information is to be stored.
- The `InMemoryTracer` stores all traces in an in-memory data structure and is helpful in tests or Jupyter notebooks.
- The `FileTracer` stores all traces in a JSON-file.
- The `OpenTelemetryTracer` uses an OpenTelemetry
  [`Tracer`](https://opentelemetry-python.readthedocs.io/en/latest/api/trace.html#opentelemetry.trace.Tracer)
  to store the traces in an OpenTelemetry backend.