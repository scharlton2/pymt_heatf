project(
    'pymt_heatf',
    'c', 'cython', 'fortran',
    version: '3.2.dev0',
    license: 'MIT',
)

py = import('python').find_installation(pure: false)
fc = meson.get_compiler('fortran')

python_inc = py.get_path('data') / 'include'
numpy_inc = run_command(
    py,
    [
        '-c',
        'import numpy; print(numpy.get_include())'
    ],
    check: true
).stdout().strip()
incs = include_directories(
    [
        'pymt_heatf/lib',
        python_inc,
        numpy_inc,
    ]
)

# gfortran on Linux/macOS can find these libraries with fc.find_library(); flang 19 on Windows cannot.
bmif_dep = dependency('bmif', method: 'pkg-config')
heatf_dep = dependency('heatf', method: 'pkg-config')
bmiheatf_dep = dependency('bmiheatf', method: 'pkg-config')
deps = [
    bmif_dep,
    heatf_dep,
    bmiheatf_dep,
    py.dependency(),
]

srcs = [
    'pymt_heatf/lib/bmi_interoperability.f90',
    'pymt_heatf/lib/heatmodelf.pyx',
]

# Files get copied to <python directory>/site-packages/<subdir>
install_pkg_srcs = [
    'pymt_heatf/__init__.py',
    'pymt_heatf/_bmi.py',
]
py.install_sources(
    install_pkg_srcs,
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

# This is a temporary fix for editable installs.
run_command('cp', '-r', 'pymt_heatf/data', 'build', check: false)
