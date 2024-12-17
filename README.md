# pymt_heatf

This is an example of building a model, written in Fortran and wrapped
in Python with the [babelizer](https://github.com/csdms/babelizer), with
the [meson-python](https://meson-python.readthedocs.io/en/latest/) build
system using only a *pyproject.toml* file for project metadata.

## Build/Install

This is a sketch of how to build and install this project with either
`conda` or `pip`.

### With conda

1.  Create a conda environment from the included *environment.yml* file
    and activate it

2.  Build/install the [Fortran BMI
    example](https://github.com/csdms/bmi-example-fortran/#buildinstall)

3.  Build/install the project with:

    ``` bash
    $ make install
    ```

### With pip

Make, CMake, and a Fortran compiler are required.

1.  Create a virtual environment

2.  Install the build system requirements through `pip`:

    ``` bash
    $ pip install meson-python meson ninja cython numpy bmipy
    ```

3.  Build/install the [Fortran BMI
    specification](https://github.com/csdms/bmi-fortran/#buildinstall)
    (it's not installable through `pip`)

4.  Build/install the [Fortran BMI
    example](https://github.com/csdms/bmi-example-fortran/#buildinstall)

5.  Build/install the project with:

    ``` bash
    $ make install
    ```

## Use

Import the standalone project into a Python session:

``` python
>>> import pymt_heatf
```

Import the *pymt* component:

``` python
>>> from pymt.MODELS import HeatModelF
```

Try the examples in the *examples* directory.
