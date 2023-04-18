# Environment setup

**Create a new virtual environment** called `practice_env` and _activate_ it.

```bash
$ python3 -m venv ./practice_env
$ source ./practice_env/bin/activate
```

The `activate` script is for Bash and Zsh on Mac or Linux.
For other shells, such as Fish or Csh, see the [venv] documentation.

On Windows (assuming `cmd.exe`):

```batch
> python -m venv .\practice_env
> .\practice_env\Scripts\activate
```

Next, **install some requirements** into the activated virtual environment:

```bash
(practice_env) $ pip install -r practice_requirements.txt
```

[venv]: https://docs.python.org/3/library/venv.html