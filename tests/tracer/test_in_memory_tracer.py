import contextlib
import os
import time
from collections.abc import Iterator

import pytest

from pharia_inference_sdk.core import (
    ErrorValue,
    InMemorySpan,
    InMemoryTaskSpan,
    InMemoryTracer,
    LogEntry,
    Task,
    utc_now,
)


def test_trace_id_exists_for_all_children_of_task_span() -> None:
    tracer = InMemoryTracer()
    parent_span = tracer.task_span("child", "input")
    parent_span.span("child2")

    assert isinstance(tracer.entries[0], InMemoryTaskSpan)
    assert isinstance(tracer.entries[0].entries[0], InMemorySpan)
    assert (
        tracer.entries[0].entries[0].context.trace_id
        == tracer.entries[0].context.trace_id
    )

    parent_span.task_span("child3", "input")
    assert isinstance(tracer.entries[0].entries[1], InMemoryTaskSpan)
    assert (
        tracer.entries[0].entries[1].context.trace_id
        == tracer.entries[0].context.trace_id
    )


def test_trace_id_exists_for_all_children_of_span() -> None:
    tracer = InMemoryTracer()
    parent_span = tracer.span("child")
    parent_span.span("child2")

    assert isinstance(tracer.entries[0], InMemorySpan)
    assert isinstance(tracer.entries[0].entries[0], InMemorySpan)
    assert (
        tracer.entries[0].entries[0].context.trace_id
        == tracer.entries[0].context.trace_id
    )

    parent_span.task_span("child3", "input")
    assert isinstance(tracer.entries[0].entries[1], InMemorySpan)
    assert (
        tracer.entries[0].entries[1].context.trace_id
        == tracer.entries[0].context.trace_id
    )


def test_can_add_child_tracer() -> None:
    tracer = InMemoryTracer()
    tracer.span("child")

    assert len(tracer.entries) == 1

    log = tracer.entries[0]
    assert isinstance(log, InMemoryTracer)
    assert log.name == "child"
    assert len(log.entries) == 0


def test_can_add_parent_and_child_entries() -> None:
    parent = InMemoryTracer()
    with parent.span("child") as child:
        child.log("Two", 2)

    assert isinstance(parent.entries[0], InMemoryTracer)
    assert isinstance(parent.entries[0].entries[0], LogEntry)


def test_task_logs_error_value() -> None:
    tracer = InMemoryTracer()

    with pytest.raises(ValueError), tracer.span("failing task"):
        raise ValueError("my bad, sorry")

    assert isinstance(tracer.entries[0], InMemorySpan)
    assert isinstance(tracer.entries[0].entries[0], LogEntry)
    error = tracer.entries[0].entries[0].value
    assert isinstance(error, ErrorValue)
    assert error.message == "my bad, sorry"
    assert error.error_type == "ValueError"
    assert error.stack_trace.startswith("Traceback")


def test_task_span_records_error_value() -> None:
    tracer = InMemoryTracer()

    with pytest.raises(ValueError), tracer.task_span("failing task", None):
        raise ValueError("my bad, sorry")

    assert isinstance(tracer.entries[0], InMemoryTaskSpan)
    error_log = tracer.entries[0].entries[0]
    assert isinstance(error_log, LogEntry)

    error = error_log.value
    assert isinstance(error, ErrorValue)
    assert error.message == "my bad, sorry"
    assert error.error_type == "ValueError"
    assert error.stack_trace.startswith("Traceback")


def test_task_automatically_logs_input_and_output(
    tracer_test_task: Task[str, str],
) -> None:
    input = "input"
    tracer = InMemoryTracer()
    output = tracer_test_task.run(input=input, tracer=tracer)

    assert len(tracer.entries) == 1
    task_span = tracer.entries[0]
    assert isinstance(task_span, InMemoryTaskSpan)
    assert task_span.name == type(tracer_test_task).__name__
    assert task_span.input == input
    assert task_span.output == output
    assert task_span.start_timestamp and task_span.end_timestamp
    assert task_span.start_timestamp < task_span.end_timestamp


def test_tracer_can_set_custom_start_time_for_log_entry() -> None:
    tracer = InMemoryTracer()
    timestamp = utc_now()

    with tracer.span("span") as span:
        span.log("log", "message", timestamp)

    assert isinstance(tracer.entries[0], InMemorySpan)
    assert isinstance(tracer.entries[0].entries[0], LogEntry)
    assert tracer.entries[0].entries[0].timestamp == timestamp


def test_tracer_can_set_custom_start_time_for_span() -> None:
    tracer = InMemoryTracer()
    start = utc_now()

    span = tracer.span("span", start)

    assert span.start_timestamp == start


def test_span_sets_end_timestamp() -> None:
    tracer = InMemoryTracer()
    start = utc_now()

    span = tracer.span("span", start)
    time.sleep(0.001)
    span.end()

    assert span.end_timestamp and span.start_timestamp < span.end_timestamp


def test_span_only_updates_end_timestamp_once() -> None:
    tracer = InMemoryTracer()

    span = tracer.span("span")
    end = utc_now()
    span.end(end)
    span.end()

    assert span.end_timestamp == end


# take from and modified: https://stackoverflow.com/questions/2059482/temporarily-modify-the-current-processs-environment
@contextlib.contextmanager
def set_env(name: str, value: str | None) -> Iterator[None]:
    old_environ = dict(os.environ)
    if value is None:
        if os.getenv(name, None) is not None:
            os.environ.pop(name)
    else:
        os.environ[name] = value
    try:
        yield
    finally:
        os.environ.clear()
        os.environ.update(old_environ)
