from setuptools import setup
import os

# A Function to read the README.rst
def read(fname):
	return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='beeply',
    version='1.0.0',
    description='A python module that helps you produce musical notes using your computer\'s characteristic beep sounds',
	long_description=read('README.rst'),
    license='MIT',
    packages=['beeply'],
    author='Harshit Budhraja',
    author_email='harshitbudhraja1301@gmail.com',
	keywords='python winsound beep music notes command-line CLI',
    url='https://github.com/harshitbudhraja/beeply',
)