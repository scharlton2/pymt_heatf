#! /usr/bin/env python
import pkg_resources

__version__ = pkg_resources.get_distribution("pymt_heatf").version


from .bmi import HeatBMI

__all__ = [
    "HeatBMI",
]
