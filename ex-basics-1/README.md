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
1. **Initialized the project and setup the** `.toml`
```bash
> uv init ex-basics-1
> #Setup my simple python file and my toml
```

```bash
# .../ex-basics-1/pyproject.toml

...
[tool.uv]
publish-url = "https://test.pypi.org/legacy/"
```

2. Built my project using `uv build` and verified `/dist`'s contents
3. Published my package using `uv publish` and entering my test pypi token when prompted.

---

### Task Description: 2 (Installing new packages)
Enhance the application with the following:

1.  Install the following modules in your environment from pypi: `rich`
2.  Enhance your code to use `rich` to print rich message

### Solution
1. Imported rich and modified the print statement