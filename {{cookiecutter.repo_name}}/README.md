# {{ cookiecutter.repo_name }}

{{ cookiecutter.description }}

## Dependencies
All the dependencies are in the `requirements.txt` file. Simply run
```
pip3 install -r requirements.txt
```

## Install

## Setup for development
0. Install Python {{ cookiecutter.python_version }}
```
pyenv install {{ cookiecutter.python_version }}
```
You may want to install [venv](https://docs.python.org/3/library/venv.html) 
or [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)
I recommend the latter.

2. Clone the repository
```
git clone git@github.com:hmrc/{{ cookiecutter.repo_name }}.git
cd {{ cookiecutter.repo_name }}
```

3. Install the dev requirements
```
pip3 install -r requirements-test.txt

```

3. To run linters and tests
```
tox
```

4. To run formatter
```
tox -e black
```

