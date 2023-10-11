==========
pymt_heatf
==========

This is an example of building a model,
written in Fortran and wrapped in Python with the *babelizer*,
with the *meson-python* build system
using a ``pyproject.toml`` file to describe the build.

Build/Install
-------------

This is a sketch of how to build and install this project.

1. Create the conda environment from `environment.yml`.
2. Build/install the `Fortran BMI specification <https://github.com/csdms/bmi-fortran/#buildinstall>`_
3. Build/install the `Fortran BMI example <https://github.com/csdms/bmi-example-fortran/#buildinstall>`_
4. Build/install this project with ``make install``

Use
---

Try the examples in the `examples` directory.
