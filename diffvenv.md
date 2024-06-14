# 1. Different ways to handle packages in Python

the problem with using pip to install packages is that it installs the packages globally. This can lead to conflicts between different packages and different versions of the same package. To solve this problem, we can use virtual environments. There are several ways to create virtual environments in Python. In this section, we will discuss some of the most popular ways to create virtual environments in Python.

## 1.1. venv

venv is a module in Python that provides support for creating lightweight “virtual environments” with their own site directories, optionally isolated from system site directories. Each virtual environment has its own Python binary (which matches the version of the binary that was used to create this environment) and can have its own independent set of installed Python packages in its site directories.

```bash
python3 -m venv <name>
```

with this command, a new directory will be created with the name you provided. This directory will contain a copy of the Python binary, the standard library, and various supporting files. It will also contain a copy of the pip library which you can use to install other packages.

To activate the virtual environment, you can use the following command:

```bash
source <name>/bin/activate
```

To deactivate the virtual environment, you can use the following command:

```bash
deactivate
```

To list the packages installed in the virtual environment, you can use the following command:

```bash
pip list
```

To know which venv you are using, you can use the following command:

```bash
pip -V
```

## 1.2. virtualenv wrapper

virtualenvwrapper is a set of extensions to Ian Bicking’s virtualenv tool. The extensions include wrappers for creating and deleting virtual environments and otherwise managing your development workflow, making it easier to work on more than one project at a time without introducing conflicts in their dependencies.

To install virtualenvwrapper, you can use the following command:

```bash
pyenv  virtualenvwrapper
```

To create a new virtual environment, you can use the following command:

```bash
mkvirtualenv <name>
```

To activate the virtual environment, you can use the following command:

```bash
workon <name>
```

To deactivate the virtual environment, you can use the following command:

```bash
deactivate
```

To list the packages installed in the virtual environment, you can use the following command:

```bash
pip list
```

To list all mkvirtualenv environments, list all virtualenvwrapper environments, you can use the following command:

```bash
lsvirtualenv
```
