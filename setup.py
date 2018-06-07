from cx_Freeze import setup, Executable
import os.path
import sys

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

base=None
if sys.platform=='win32':
    base="Win32GUI"

setup(
    name="Hello World EXECUTABLE",
    version = "1.0.0",
    options={"build_exe": {
        'packages': ["os", "sys", "ctypes"],
        'include_msvcr': True,"includes": ["tkinter"],
        'include_files':['C:/Users/e000864/AppData/Local/Programs/Python/Python36-32/DLLs/tcl86t.dll',
                         'C:/Users/e000864/AppData/Local/Programs/Python/Python36-32/DLLs/tk86t.dll'],
    }},
    description = ".py to .exe",
    shortcut_name = 'Importador TRANSFÁCIL',
    executables = [Executable("SelectFile.py",icon='iconTrans.ico',base=base)],
    package_dir={'': ''})

#python setup.py build
