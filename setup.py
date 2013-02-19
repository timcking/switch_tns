from distutils.core import setup

# py2exe stuff
import py2exe, os
# find pythoncard resources, to add as 'data_files'
pycard_resources=[]
for filename in os.listdir('.'):
    if filename.find('.rsrc.')>-1:
        pycard_resources+=[filename]

# includes for py2exe
includes=[]
for comp in ['button','statictext','radiogroup']:
    includes += ['PythonCard.components.'+comp]
print 'includes',includes

opts = { 'py2exe': { 'includes':includes } }
print 'opts',opts
# end of py2exe stuff

setup(name='switch_tns',
    version='0.1',
    url='about:none',
    author='Elwood Hunt',
    author_email='elwood.hunt@gmail.com',
    package_dir={'switch_tns':'.'},
    packages=['switch_tns'],
    windows=[
      { "script": "switch_tns.py",
        "icon_resources": [(1, "icon-oracle.ico")]
      }
   ], 
    data_files=[('.',pycard_resources), (".",["switch_tns.ini",]), (".",["icon-oracle.ico",])],
    options=opts
    )
