# docker-python

python docker wrapper

Go-Task commands (Taskfile.yml)
- task build: Build the production image using docker buildx. Uses vars IMAGE, TAG, PLATFORMS.
- task run: Run the container with APP_MODULE env (default app.main:app).
- task dev-image: Build the dev image from the "dev" target.
- task dev: Start an interactive dev container with hot reload by bind-mounting ./app into /app/app.
- task test: Build the dev image (if needed) and run pytest inside the dev container mounting the repo at /app.

Python metadata and packaging
- pyproject.toml (src/helloworld/): Defines the helloworld project metadata, Python >=3.10, no deps, setuptools build backend.
- Package layout: src/helloworld is installed editable (-e) in Docker images and locally for development.
- Entry point: helloworld.main includes a main() that prints a greeting; runnable via python -m helloworld.main.
- requirements.txt: Runtime dependencies installed in the runtime image.
- requirements-dev.txt: Dev/test tooling installed in the dev image.
- pytest.ini: Configures pytest (pythonpath=src, testpaths=tests, -q -ra).

Common commands
- Local install (editable): pip install -r requirements.txt -r requirements-dev.txt && pip install -e src/helloworld
- Run: python -m helloworld.main
- Tests: pytest  | Single test: pytest tests/unit/test_main.py::test_hello_function

