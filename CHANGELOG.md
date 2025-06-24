# Changelog

## [0.1.6](https://github.com/Aleph-Alpha/pharia-inference-sdk/compare/v0.1.5...v0.1.6) (2025-06-23)


### Documentation

* generate read the docs ([#34](https://github.com/Aleph-Alpha/pharia-inference-sdk/issues/34)) ([c872f50](https://github.com/Aleph-Alpha/pharia-inference-sdk/commit/c872f50314128a5de60c9740ab068af32c8d07f2))
* Update author to Engineering ([0d8d64b](https://github.com/Aleph-Alpha/pharia-inference-sdk/commit/0d8d64be056e1f1f7eaff56767016e4feeb65614))

## [0.1.5](https://github.com/Aleph-Alpha/pharia-inference-sdk/compare/v0.1.4...v0.1.5) (2025-06-19)


### Documentation

* fix the usage code example ([44ea4f6](https://github.com/Aleph-Alpha/pharia-inference-sdk/commit/44ea4f691ff049362bb43a7d0c0e3fbf14a09807))

## [0.1.4](https://github.com/Aleph-Alpha/pharia-inference-sdk/compare/v0.1.3...v0.1.4) (2025-06-18)


### Documentation

* add documentation notebooks ([#27](https://github.com/Aleph-Alpha/pharia-inference-sdk/issues/27)) ([111368b](https://github.com/Aleph-Alpha/pharia-inference-sdk/commit/111368bd4fdc1bf46b44c8078e713510f5463c66))
* fix typo and links in README.md ([4a98bf0](https://github.com/Aleph-Alpha/pharia-inference-sdk/commit/4a98bf02f202c402ce84b7bde23aa4d9ae921be6))

## [0.1.3](https://github.com/Aleph-Alpha/pharia-inference-sdk/compare/v0.1.2...v0.1.3) (2025-06-11)


### Documentation

* tidy up markdown files ([#20](https://github.com/Aleph-Alpha/pharia-inference-sdk/issues/20)) ([18d60c0](https://github.com/Aleph-Alpha/pharia-inference-sdk/commit/18d60c0cee83d0257be9b4e3bbfee2223b7a4e5a))

## [0.1.2](https://github.com/Aleph-Alpha/pharia-inference-sdk/compare/v0.1.1...v0.1.2) (2025-06-11)


### Features

* `FileInstructionFinetuningDataRepository` ([17babff](https://github.com/Aleph-Alpha/pharia-inference-sdk/commit/17babff5f08b6fdb19fa2215486374de354e3f1e))
* add `context_size`-property to `AlephAlphaModel` ([#820](https://github.com/Aleph-Alpha/pharia-inference-sdk/issues/820)) ([ae7e634](https://github.com/Aleph-Alpha/pharia-inference-sdk/commit/ae7e634189a5bbc45ec90d5815ac7ef0754d0cfb))
* Add `eot_token` property to `ControlModel` and derived classes. ([#906](https://github.com/Aleph-Alpha/pharia-inference-sdk/issues/906)) ([90291eb](https://github.com/Aleph-Alpha/pharia-inference-sdk/commit/90291ebea5aa79724c297e4ca3c3d45870f9a879))
* Add function to upload to trace viewer to Tracer. ([#870](https://github.com/Aleph-Alpha/pharia-inference-sdk/issues/870)) ([a571531](https://github.com/Aleph-Alpha/pharia-inference-sdk/commit/a571531e0f702ae136f560e111d6903d70574481))
* Add TextControl for Instruct and Chat models ([#1104](https://github.com/Aleph-Alpha/pharia-inference-sdk/issues/1104)) ([ceb1756](https://github.com/Aleph-Alpha/pharia-inference-sdk/commit/ceb1756a4dabe63b09ef891030de60e42f0ad0ec))
* harden model initialization ([#884](https://github.com/Aleph-Alpha/pharia-inference-sdk/issues/884)) ([6777c00](https://github.com/Aleph-Alpha/pharia-inference-sdk/commit/6777c00cdd8f51b8317e75d5c89823e45965eca5))
* Increased ruff checks for better code quality([#908](https://github.com/Aleph-Alpha/pharia-inference-sdk/issues/908)) ([d6c0311](https://github.com/Aleph-Alpha/pharia-inference-sdk/commit/d6c0311b08da2e3c2ae1d43cde898685b27e69cb))
* Introduce `InstructionFinetuningDataRepository` ([#1033](https://github.com/Aleph-Alpha/pharia-inference-sdk/issues/1033)) ([17babff](https://github.com/Aleph-Alpha/pharia-inference-sdk/commit/17babff5f08b6fdb19fa2215486374de354e3f1e))
* Introduce an unified trace format for exporting ([#844](https://github.com/Aleph-Alpha/pharia-inference-sdk/issues/844)) ([f765d27](https://github.com/Aleph-Alpha/pharia-inference-sdk/commit/f765d276d30986776586f80a2869af5807b1feeb))
* make ChatModels instruct capable ([#1064](https://github.com/Aleph-Alpha/pharia-inference-sdk/issues/1064)) ([f24a6c4](https://github.com/Aleph-Alpha/pharia-inference-sdk/commit/f24a6c4ece0bfd3d517489c072fa180cbe9a85fb))
* Replace langdetect with lingua ([#897](https://github.com/Aleph-Alpha/pharia-inference-sdk/issues/897)) ([a4d9be4](https://github.com/Aleph-Alpha/pharia-inference-sdk/commit/a4d9be4355d775f33f7c08fd4f46d080d06e155d))
* restructure tests according to src structure ([#872](https://github.com/Aleph-Alpha/pharia-inference-sdk/issues/872)) ([d1509fa](https://github.com/Aleph-Alpha/pharia-inference-sdk/commit/d1509faf97d91f1fb8188c16e94c3f791307e6d0))
* Studio integration of Trace Submission PHS-616 ([#975](https://github.com/Aleph-Alpha/pharia-inference-sdk/issues/975)) ([ff47799](https://github.com/Aleph-Alpha/pharia-inference-sdk/commit/ff477992aca0d04363acc975b7bdbe0089298039))
* Use urllib.urljoin where appropriate ([#986](https://github.com/Aleph-Alpha/pharia-inference-sdk/issues/986)) ([8772f88](https://github.com/Aleph-Alpha/pharia-inference-sdk/commit/8772f881e067c944faa2aca5294e1bc9a710d8cd))


### Bug Fixes

* `ExpandChunks` is fast even for large documents ([#842](https://github.com/Aleph-Alpha/pharia-inference-sdk/issues/842)) ([30b9441](https://github.com/Aleph-Alpha/pharia-inference-sdk/commit/30b9441e3d1f78a102cca78420bc30b0f00434da))
* allow negative min score in SearchQuery ([#1184](https://github.com/Aleph-Alpha/pharia-inference-sdk/issues/1184)) ([709a414](https://github.com/Aleph-Alpha/pharia-inference-sdk/commit/709a414379fea22375413ad7fde9db15cc76c726))
* lru_cache memory consumption ([#907](https://github.com/Aleph-Alpha/pharia-inference-sdk/issues/907)) ([30d1724](https://github.com/Aleph-Alpha/pharia-inference-sdk/commit/30d172429a91be1836cb87475a8bf30f4620912b))
* make highlight test stable ([#916](https://github.com/Aleph-Alpha/pharia-inference-sdk/issues/916)) ([20d2bd5](https://github.com/Aleph-Alpha/pharia-inference-sdk/commit/20d2bd5942266ba643b3417aadfd483aaefec63e))
* notebook test stability, PromptBasedClassify with Llama ([#1212](https://github.com/Aleph-Alpha/pharia-inference-sdk/issues/1212)) ([c967183](https://github.com/Aleph-Alpha/pharia-inference-sdk/commit/c96718366ee35f317d57675c395381cb1f586c26))
* remove llama3.0 from models and defaults ([#1054](https://github.com/Aleph-Alpha/pharia-inference-sdk/issues/1054)) ([24618cf](https://github.com/Aleph-Alpha/pharia-inference-sdk/commit/24618cfe1c2afa19bfe07e3477d822b436eb8636))
* SingleChunkQa crashing on specific prompt ordering ([#931](https://github.com/Aleph-Alpha/pharia-inference-sdk/issues/931)) ([dd801ff](https://github.com/Aleph-Alpha/pharia-inference-sdk/commit/dd801ff357d7a19f3f1598a40d39aa88f21411fd))
* Throw a warning instead of an error incase a non recommended model is selected for a ControlMode. ([#892](https://github.com/Aleph-Alpha/pharia-inference-sdk/issues/892)) ([7aab1d7](https://github.com/Aleph-Alpha/pharia-inference-sdk/commit/7aab1d77bf1c0711462a350bf11e1e8ec4d8b99c))
* tokenizer with no whitespace prefix will no longer fail ([#1195](https://github.com/Aleph-Alpha/pharia-inference-sdk/issues/1195)) ([96b0d47](https://github.com/Aleph-Alpha/pharia-inference-sdk/commit/96b0d47c0f9e69a775923bd9227b4afb96663ac0))
* update names of pharia-1 models to lowercase ([#1091](https://github.com/Aleph-Alpha/pharia-inference-sdk/issues/1091)) ([b7621d5](https://github.com/Aleph-Alpha/pharia-inference-sdk/commit/b7621d5110a979bdcfa9c450014a1f866e775e97))
* use "utf-8" encoding when reading FileTracer traces ([#1241](https://github.com/Aleph-Alpha/pharia-inference-sdk/issues/1241)) ([456dec0](https://github.com/Aleph-Alpha/pharia-inference-sdk/commit/456dec01bdf8fdf50291d946885d0d84412b966c))


### Documentation

* add NOTICE for Apache2.0 license ([7e240c1](https://github.com/Aleph-Alpha/pharia-inference-sdk/commit/7e240c13138a5b5c257d76b90bddaca842da5d06))
* add project repo url ([6d720b3](https://github.com/Aleph-Alpha/pharia-inference-sdk/commit/6d720b3c68e52ec8a8734b26b7c617f63bdc4bb8))
* add usage example in README.md ([2df7e0d](https://github.com/Aleph-Alpha/pharia-inference-sdk/commit/2df7e0d36c3b931bee69eb3f9bfb8d24b3b820b4))
* create CONTRIBUTING.md ([67515a1](https://github.com/Aleph-Alpha/pharia-inference-sdk/commit/67515a13e62653cbe70df048dbacfe9a950f554e))
* init README.md ([b4f6fad](https://github.com/Aleph-Alpha/pharia-inference-sdk/commit/b4f6fadde02d962e1146a48776583a5ffcd14383))

## [0.1.1](https://github.com/Aleph-Alpha/pharia-inference-sdk/compare/v0.1.0...v0.1.1) (2025-06-11)


### Features

* `FileInstructionFinetuningDataRepository` ([17babff](https://github.com/Aleph-Alpha/pharia-inference-sdk/commit/17babff5f08b6fdb19fa2215486374de354e3f1e))
* add `context_size`-property to `AlephAlphaModel` ([#820](https://github.com/Aleph-Alpha/pharia-inference-sdk/issues/820)) ([ae7e634](https://github.com/Aleph-Alpha/pharia-inference-sdk/commit/ae7e634189a5bbc45ec90d5815ac7ef0754d0cfb))
* Add `eot_token` property to `ControlModel` and derived classes. ([#906](https://github.com/Aleph-Alpha/pharia-inference-sdk/issues/906)) ([90291eb](https://github.com/Aleph-Alpha/pharia-inference-sdk/commit/90291ebea5aa79724c297e4ca3c3d45870f9a879))
* Add function to upload to trace viewer to Tracer. ([#870](https://github.com/Aleph-Alpha/pharia-inference-sdk/issues/870)) ([a571531](https://github.com/Aleph-Alpha/pharia-inference-sdk/commit/a571531e0f702ae136f560e111d6903d70574481))
* Add TextControl for Instruct and Chat models ([#1104](https://github.com/Aleph-Alpha/pharia-inference-sdk/issues/1104)) ([ceb1756](https://github.com/Aleph-Alpha/pharia-inference-sdk/commit/ceb1756a4dabe63b09ef891030de60e42f0ad0ec))
* harden model initialization ([#884](https://github.com/Aleph-Alpha/pharia-inference-sdk/issues/884)) ([6777c00](https://github.com/Aleph-Alpha/pharia-inference-sdk/commit/6777c00cdd8f51b8317e75d5c89823e45965eca5))
* Increased ruff checks for better code quality([#908](https://github.com/Aleph-Alpha/pharia-inference-sdk/issues/908)) ([d6c0311](https://github.com/Aleph-Alpha/pharia-inference-sdk/commit/d6c0311b08da2e3c2ae1d43cde898685b27e69cb))
* Introduce `InstructionFinetuningDataRepository` ([#1033](https://github.com/Aleph-Alpha/pharia-inference-sdk/issues/1033)) ([17babff](https://github.com/Aleph-Alpha/pharia-inference-sdk/commit/17babff5f08b6fdb19fa2215486374de354e3f1e))
* Introduce an unified trace format for exporting ([#844](https://github.com/Aleph-Alpha/pharia-inference-sdk/issues/844)) ([f765d27](https://github.com/Aleph-Alpha/pharia-inference-sdk/commit/f765d276d30986776586f80a2869af5807b1feeb))
* make ChatModels instruct capable ([#1064](https://github.com/Aleph-Alpha/pharia-inference-sdk/issues/1064)) ([f24a6c4](https://github.com/Aleph-Alpha/pharia-inference-sdk/commit/f24a6c4ece0bfd3d517489c072fa180cbe9a85fb))
* Replace langdetect with lingua ([#897](https://github.com/Aleph-Alpha/pharia-inference-sdk/issues/897)) ([a4d9be4](https://github.com/Aleph-Alpha/pharia-inference-sdk/commit/a4d9be4355d775f33f7c08fd4f46d080d06e155d))
* restructure tests according to src structure ([#872](https://github.com/Aleph-Alpha/pharia-inference-sdk/issues/872)) ([d1509fa](https://github.com/Aleph-Alpha/pharia-inference-sdk/commit/d1509faf97d91f1fb8188c16e94c3f791307e6d0))
* Studio integration of Trace Submission PHS-616 ([#975](https://github.com/Aleph-Alpha/pharia-inference-sdk/issues/975)) ([ff47799](https://github.com/Aleph-Alpha/pharia-inference-sdk/commit/ff477992aca0d04363acc975b7bdbe0089298039))
* Use urllib.urljoin where appropriate ([#986](https://github.com/Aleph-Alpha/pharia-inference-sdk/issues/986)) ([8772f88](https://github.com/Aleph-Alpha/pharia-inference-sdk/commit/8772f881e067c944faa2aca5294e1bc9a710d8cd))


### Bug Fixes

* `ExpandChunks` is fast even for large documents ([#842](https://github.com/Aleph-Alpha/pharia-inference-sdk/issues/842)) ([30b9441](https://github.com/Aleph-Alpha/pharia-inference-sdk/commit/30b9441e3d1f78a102cca78420bc30b0f00434da))
* allow negative min score in SearchQuery ([#1184](https://github.com/Aleph-Alpha/pharia-inference-sdk/issues/1184)) ([709a414](https://github.com/Aleph-Alpha/pharia-inference-sdk/commit/709a414379fea22375413ad7fde9db15cc76c726))
* lru_cache memory consumption ([#907](https://github.com/Aleph-Alpha/pharia-inference-sdk/issues/907)) ([30d1724](https://github.com/Aleph-Alpha/pharia-inference-sdk/commit/30d172429a91be1836cb87475a8bf30f4620912b))
* make highlight test stable ([#916](https://github.com/Aleph-Alpha/pharia-inference-sdk/issues/916)) ([20d2bd5](https://github.com/Aleph-Alpha/pharia-inference-sdk/commit/20d2bd5942266ba643b3417aadfd483aaefec63e))
* notebook test stability, PromptBasedClassify with Llama ([#1212](https://github.com/Aleph-Alpha/pharia-inference-sdk/issues/1212)) ([c967183](https://github.com/Aleph-Alpha/pharia-inference-sdk/commit/c96718366ee35f317d57675c395381cb1f586c26))
* remove llama3.0 from models and defaults ([#1054](https://github.com/Aleph-Alpha/pharia-inference-sdk/issues/1054)) ([24618cf](https://github.com/Aleph-Alpha/pharia-inference-sdk/commit/24618cfe1c2afa19bfe07e3477d822b436eb8636))
* SingleChunkQa crashing on specific prompt ordering ([#931](https://github.com/Aleph-Alpha/pharia-inference-sdk/issues/931)) ([dd801ff](https://github.com/Aleph-Alpha/pharia-inference-sdk/commit/dd801ff357d7a19f3f1598a40d39aa88f21411fd))
* Throw a warning instead of an error incase a non recommended model is selected for a ControlMode. ([#892](https://github.com/Aleph-Alpha/pharia-inference-sdk/issues/892)) ([7aab1d7](https://github.com/Aleph-Alpha/pharia-inference-sdk/commit/7aab1d77bf1c0711462a350bf11e1e8ec4d8b99c))
* tokenizer with no whitespace prefix will no longer fail ([#1195](https://github.com/Aleph-Alpha/pharia-inference-sdk/issues/1195)) ([96b0d47](https://github.com/Aleph-Alpha/pharia-inference-sdk/commit/96b0d47c0f9e69a775923bd9227b4afb96663ac0))
* update names of pharia-1 models to lowercase ([#1091](https://github.com/Aleph-Alpha/pharia-inference-sdk/issues/1091)) ([b7621d5](https://github.com/Aleph-Alpha/pharia-inference-sdk/commit/b7621d5110a979bdcfa9c450014a1f866e775e97))
* use "utf-8" encoding when reading FileTracer traces ([#1241](https://github.com/Aleph-Alpha/pharia-inference-sdk/issues/1241)) ([456dec0](https://github.com/Aleph-Alpha/pharia-inference-sdk/commit/456dec01bdf8fdf50291d946885d0d84412b966c))


### Documentation

* add NOTICE for Apache2.0 license ([7e240c1](https://github.com/Aleph-Alpha/pharia-inference-sdk/commit/7e240c13138a5b5c257d76b90bddaca842da5d06))
* add project repo url ([6d720b3](https://github.com/Aleph-Alpha/pharia-inference-sdk/commit/6d720b3c68e52ec8a8734b26b7c617f63bdc4bb8))
* add usage example in README.md ([2df7e0d](https://github.com/Aleph-Alpha/pharia-inference-sdk/commit/2df7e0d36c3b931bee69eb3f9bfb8d24b3b820b4))
* create CONTRIBUTING.md ([67515a1](https://github.com/Aleph-Alpha/pharia-inference-sdk/commit/67515a13e62653cbe70df048dbacfe9a950f554e))
* init README.md ([b4f6fad](https://github.com/Aleph-Alpha/pharia-inference-sdk/commit/b4f6fadde02d962e1146a48776583a5ffcd14383))
