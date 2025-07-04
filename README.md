# Python Project Template

```BASH
git clone https://github.com/linem-davton/cpp-project-template.git myproject
cd myproject
rm -rf .git
git init
git add .
git commit -m "Initial commit"

# Setup and Install dependencies
./setup.sh
```

## Checklist

- [ ] Update the `README.md` file with your project details.
- [ ] Update the `pyproject.toml` file with your project details.
- [ ] Update requirements.txt files. Only used for development and CI environments.
- [ ] Update `.envrc` file correct `PYTHONPATH` env variable.

## Build

- Hatchling: Good for pure Python projects, no C/C++ extensions (`.so`).
- Setuptools: Good for projects with C/C++ extensions.

```BASH
python -m build
pip install -e . # For local development
`
```

## Publish

### TestPyPI

[TestPyPI](https://test.pypi.org/) is a sandboxed version of the real Python Package Index.
It’s for testing your packaging, upload, and install process to make sure everything works before publishing to the official [PyPI](https://pypi.org/).
Note that the package name must be unique across both TestPyPI and PyPI.

```BASH
twine upload --repository testpypi dist/* # Follow the prompt to enter your username/password
pip install --index-url https://test.pypi.org/simple/ <your-package-name> # By default, pip will install from the official PyPI repository
```

### PyPI

```BASH
twine upload dist/* # Follow the prompt to enter your username/password
```
