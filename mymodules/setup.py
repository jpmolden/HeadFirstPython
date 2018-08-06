from setuptools import setup

setup(
    name='vsearch',
    version='1.0',
    description='The Head First Python Search Tools',
    author='jpmolden',
    author_email='jpmolden@gmail.com',
    url='github.com/jpmolden',
    py_modules=['vsearch'],
)

## Windows dist:
## py -3 setup.py sdist
## py -3 -m pip install vsearch-1.0.tar.gz
