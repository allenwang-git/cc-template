# cc-template


## QuickStart

### Dependencies

- [Bazel](#install-bazel)
- lcov
  
  ```bash
  sudo apt install lcov
  ```

### Define Tasks

Go to [`tasks.yaml`](./tasks.yaml) and add new tasks.

### Run Tasks

Use the CLI tool [`run`](run) to run predefined tasks:

```bash
Usage: ./run <task-name>
Options:
    --list    List all available tasks.
    --help    Print this help message.

```

## Install Bazel

- Install through [Bazelisk](https://github.com/bazelbuild/bazelisk/releases).
  
  ```bash
    wget https://github.com/bazelbuild/bazelisk/releases/download/v1.23.0/bazelisk-amd64.deb
    sudo dpkg -i bazelisk-amd64.deb
    which bazelisk
  ```

- Add [`.bazeliskrc`](.bazeliskrc) to choose Bazel version

  ```bash
    BAZELISK_HOME=.bazelisk
    USE_BAZEL_VERSION=6.5.0
  ```

- Check Bazel version
  
  ```bash
  bazel version
  bazelisk version
  ```

## Set up Bazel Workspace

- Create WORKSPACE.bazel
- Import common used functions
  
  ```bash
    load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")
    load("@bazel_tools//tools/build_defs/repo:git.bzl", "git_repository")
  ```

- Create [`BUILD.bazel`](BUILD.bazel) to mark the repo as a bazel pkg
- Create [`.bazelrc`](.bazelrc) to specify the bazel operation configurations

## Run Test and Coverage in Bazel

For cc codes, defined `cc_test` targets, while for python codes, define `py_test` targets.

- To run all tests in this repo, use `bazelisk test //... <options>`.

  NOTES: If use `py_test` to do integration test for cc codes, the tests cannot be used to calculate coverage for cc codes, unless use native `pytest` command. In other words, `cc_binary` targets cannot be test directly.

- To calculate unit test coverage, use `bazelisk coverage //python/... <options>` or `bazelisk coverage //cc/... <options>`

- To generate coverage report, use `genhtml` command.

