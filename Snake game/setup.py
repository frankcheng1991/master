# StepUp file
# method 1: python setup.py build
# method 2: to create a windows installer: python setup.py bdist_msi

from cx_Freeze import setup, Executable

base = None


executables = [Executable("Slither.pyw", base="Win32GUI")]

#packages = ["idna"]
options = {
    'build_exe': {

        'packages':['pygame', 'time', 'random'],
        'include_files': ["apple.png", "snack_head.png"]
    },

}

setup(
    name = "pygame_learn.py",
    options = options,
    version = "1.0.0",
    description = '<any description>',
    executables = executables
)