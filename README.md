# icicle-plot
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

