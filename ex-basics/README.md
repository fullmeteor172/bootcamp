# EX-BASICS-1,2,3
### Task Description: 1 (Setup of a New Application)
1.  Initialize an application for use with uv (`uv init`)
2.  Create a virtual environment `uv venv` and source it.
3.  Start your IDE in this environment
4.  Setup your IDE to use the virtual environment you setup.
5.  Create a module called `<yourname>-hello` in that folder.
6.  Write the code that says hello to the argument passed or world, by default.
7.  Publish the module in [TestPyPI for Package Testing](https://test.pypi.org/).

In your readme, please provide the link to the package. Also, do the readme.md well enough so that the package page looks good.

### Solution:
1. Initialized the project and setup the `.toml`.
```bash
> uv init --package ex-basics
> #Setup my python files in src/ex_basics_aganitha
```
2. Built my project using `uv build` and verified `/dist`'s contents.
3. Published my package using `uv publish` and entering my test pypi token when prompted.
---
### Task Description: 2 (Installing new packages)
Enhance the application with the following:

1.  Install the following modules in your environment from pypi: `rich`
2.  Enhance your code to use `rich` to print rich message

### Solution
1. Added rich using `uv add rich` and modified the print statement.
---
### Task Description: 3 (Writing command line application)
1.  Install `typer`
2.  Use it to write a command line application in the module
3.  Now, make the cli app as a part of the pyproject.toml so that it gets installed when we install the package.
4.  Record and show the demo where you install the package and run the command and show it.
### Solution
1. Installing typer using `uv add typer`.
2. Created a CLI using `typer.Typer()` and defined a command function decorated with `@app.command()` that accepts a `typer.Argument`.
3. Modifying the `.toml` to add the `say-hello` command definition. This makes the CLI available as an executable after installation.
```bash
# .../ex-basics-1/pyproject.toml
[project.scripts]
say-hello = "ex_basics_aganitha.main:app"
```
4. Testing it and verifying my result.
<img src="https://i.ibb.co/4ZzdMLG0/Screenshot-From-2025-08-21-08-31-22.png" alt="drawing" width="600"/>



