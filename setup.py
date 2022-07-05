from distutils.core import setup
import py2exe
import matplotlib
import numpy
import os
import sys
import FileDialog
def numpy_dll_paths_fix():
    paths = set()
    np_path = numpy.__path__[0]
    for dirpath, _, filenames in os.walk(np_path):
        for item in filenames:
            if item.endswith('.dll'):
                paths.add(dirpath)
    sys.path.append(*list(paths))
numpy_dll_paths_fix()
setup(windows=['Inter.py'],
      options={
               'py2exe': {
                          'packages' :  ['matplotlib', 'pytz', 'FileDialog'],
                          'dll_excludes': ['libgdk-win32-2.0-0.dll',
                                         'libgobject-2.0-0.dll',
                                         'libgdk_pixbuf-2.0-0.dll',
                                         'libgtk-win32-2.0-0.dll',
                                         'libglib-2.0-0.dll',
                                         'libcairo-2.dll',
                                         'libpango-1.0-0.dll',
                                         'libpangowin32-1.0-0.dll',
                                         'libpangocairo-1.0-0.dll',
                                         'libglade-2.0-0.dll',
                                         'libgmodule-2.0-0.dll',
                                         'libgthread-2.0-0.dll',
                                         'QtGui4.dll', 'QtCore.dll',
                                         'QtCore4.dll',
                                         'MSVCP90.dll'
                                        ],
                          }
                },
      data_files=matplotlib.get_py2exe_datafiles(),) 