# icicle-plot
[![CI](https://github.com/yangm2/icicle-plot/actions/workflows/ci.yml/badge.svg?branch=main&event=push)](https://github.com/yangm2/icicle-plot/actions/workflows/ci.yml)

produce plot of hierarchical data

## Generate plot
```sh
% uv run src/main.py
```

## Development

- install locked version of project dependencies and tools
  ```sh
  % uv sync
  ```
- format code
  ```sh
  % uv run ruff format
  ```
- lint code
  ```sh
  % uv run ruff check
  ```
- typecheck code
  ```sh
  % uv run {mypy|pyrefly|ty} [TYPECHECK OPTIONS]
  ```
- upgrade locked version of project dependencies and tools
  ``` sh
  % uv lock --upgrade
  ```

## Development with [mise-en-place](https://mise.jdx.dev)

- run all checks
  ```sh
  % mise r all-checks
  ```
- list individual tasks
  ```sh
  % mise tasks ls
  ```
- Generate plot
  ```sh
  % mise r main --input examples/example1.toml
  ```