project('pymt_heatf', 'fortran', 'cython')

py = import('python').find_installation(pure: false)
fc = meson.get_compiler('fortran')

incs = include_directories([
    'pymt_heatf',
    'pymt_heatf/lib',
    '/Users/mpiper/anaconda3/envs/mson/include',
    '/Users/mpiper/anaconda3/envs/mson/lib/python3.11/site-packages/numpy/core/include',
    ])

deps = [
    fc.find_library('bmif'),
    fc.find_library('heatf'),
    fc.find_library('bmiheatf'),
]

srcs = [
    'pymt_heatf/lib/bmi_interoperability.f90',
    'pymt_heatf/lib/heatmodelf.pyx',
]

# Files get copied to <python directory>/site-packages/<subdir>
install_bmi_srcs = [
    'pymt_heatf/__init__.py',
    'pymt_heatf/bmi.py',
]
py.install_sources(
    install_bmi_srcs,
    subdir: 'pymt_heatf',
)
install_lib_srcs = [
    'pymt_heatf/lib/__init__.py',
    'pymt_heatf/lib/heatmodelf.pyx',
]
py.install_sources(
    install_lib_srcs,
    subdir: 'pymt_heatf/lib',
)

install_subdir(
    'meta/HeatModelF',
    install_dir: py.get_install_dir() / 'pymt_heatf/data',
)

py.extension_module(
    'heatmodelf',
    srcs,
    dependencies: deps,
    include_directories: incs,
    install: true,
    subdir: 'pymt_heatf/lib',
)
