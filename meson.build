project('pymt_heatf', 'cython', 'fortran', version: '0.1')

py = import('python').find_installation()

# Specify directories to be included - usually this is where your header files live.
# May be able to import bmi-fortran?
# May need to go deeper, to pymt_heatf/lib?
# What about CONDA_PREFIX env var? See old setup.py.
# /Users/mpiper/anaconda3/envs/meson/lib
# /Users/mpiper/anaconda3/envs/meson/include
includes = include_directories('pymt_heatf')

fc = meson.get_compiler('fortran')
libbmif = fc.find_library('bmif')
libheatf = fc.find_library('heatf')
libbmiheatf = fc.find_library('bmiheatf')

srcs = [
    'pymt_heatf/lib/bmi_interoperability.f90',
    'pymt_heatf/lib/heatmodelf.pyx',
]

# If some files (such as .py files) need to be copied to site-packages,
# this is where they get specified. Files get copied to
# <python directory>/site-packages/<subdir>
#py.install_sources(
#    'src/__init__.py',
#    subdir: 'spam',
#    pure: false,
#)

py.extension_module(
    'pymt_heatf',
    srcs,
#    dependencies: [
#        libbmif,
#        libheatf,
#        libbmiheatf,
#    ]
    dependencies: libbmif,
    subdir: 'pymt_heatf',
    include_directories: includes,
    install: true,
)
