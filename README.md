# Jupyter Best Practices

This is an example of Jupyter best practices. I always can see that many developers only coding in Jupyter, this is not a good way. That will hard to linting, write testcases, use some automatic tools improving process, refactor our codes, etc. In my opinions, for every engineers, there are four basic things, we need to concerned, coding, testing, documenting and engineering. That's reasons why I create this repository, I hopo it can help someones.

## The tools I use

- [Visual Studio Code](https://code.visualstudio.com/)
- [pyenv](https://github.com/pyenv/pyenv) is a simple Python version management, and I always use it to make sure the local Python version is matched with `pyproject.toml`.
- [poetory](https://python-poetry.org/) is a Python dependency and virtual environment management, and I use it to replace pip and virtualenv.
- [tox](https://tox.wiki/) is a tool to auto testing, linting and run other commands.

## My VSCode Python's settings

```json
// python
{
  "[python]": {
    "editor.defaultFormatter": "charliermarsh.ruff",
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
      "source.fixAll": true,
      "source.organizeImports": true
    },
  },
  "notebook.formatOnSave.enabled": true,
  "notebook.codeActionsOnSave": {
    "source.fixAll": true,
    "source.organizeImports": true
  }
}
```

## The end

This exmaple also has some place can be improved. Such as, we can use [pre-commit](https://pre-commit.com/) to improve git process, we can write more testcases to improve system stability, we can use [Github Action](https://docs.github.com/en/actions) to be CI(Continuous Integration), we can use [Renovate](https://www.mend.io/renovate/) to auto update packages version, bla,bla,bla..

Whatever we going to do, I really really hope this repo can help you or give your some thoughts.
