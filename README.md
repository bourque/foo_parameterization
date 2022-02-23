# Foo Parameterization

This repository contains software and supporting materials for the complex yet ficticious Foo parameterization for
atmosphereic sea-spray physics.  Currently, the code simply calculates the volume of a sphere given a user-supplied
radius.

The main software to perform this calculation is contained within the `foo_parameterization` module.

## Installation

The software is intended to run in a Python 3 environment, however it has only been tested with Python 3.9 specifically.

To install the `foo_parameterization` package, simply run:

```
pip install foo_parameterization
```

This should install the package and any necessary dependencies.

Another option for installing the package and necessary dependencies is using `conda`.  More information about `conda` and how to
acquire/install it can be found here:

- [Miniconda](https://conda.io/miniconda.html) or
- [Anaconda](https://www.continuum.io/downloads)

With `conda` installed, users can install the environment by running:

```
conda env create -f environment.yml
```

and then install the package with:

```
python setup.py [install|develop]
```

## Usage

To run the software from the command line, do:

```
python foo_parameterization.py -r <radius>
```

where `<radius>` is the radius from which to calculate the volume of a sphere.

To run the software from within a python environment, do:

```python
from foo_parameterization import foo_parameterization
foo = foo_parameterization.FooParameterization()
result = foo.calculate(1.0)
```

## How to Contribute

If you would like to contribute changes to this repository, please do the following:

1. Make a local copy of the this repository by cloning the repository (e.g. `git@github.com:bourque/foo_parameterization.git`).

2. Create a branch on the clone to develop software changes on.
    1. `git branch <branchname>`
    2. `git checkout <branchname>`
    3. Perform local software changes using the nominal `git add`/`git commit -m` cycle:
       1. `git status` -  allows you to see which files have changed.
       2. `git add <new or changed files you want to commit>`
       3. `git commit -m 'Explanation of changes you've done with these files'`

3. Push the branch to the repository with `git push origin <branchname>`.

4. In the repository on GitHub, create a pull request for the recently pushed branch.

5. Assign the pull request a reviewer. They will review your pull request and either accept the request and merge, or ask for additional changes.

6. Iterate with your reviewer(s) on additional changes if necessary, addressing any comments on your pull request.

7. Once the pull request has been accepted, it will be merged.
