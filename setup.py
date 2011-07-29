from setuptools import setup
import os

def read(*rnames):
        return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

setup(
    name='peeper',
    version='0.1.0',
    author='Chris Martin',
    author_email='ch.martin@gmail.com',
    maintainer='Matt Luongo',
    maintainer_email='mhluongo@gmail.com',
    description='A scraper to peep at a homepage, and pull and crop the first image with a detected face.',
    url = "http://packages.python.org/peeper",
    packages=['peeper',],
    include_package_data=True,
    zip_safe=False,
    long_description=read('README.rst'),
    platforms=['posix'],
    tests_require=read('test_requirements.txt').split('\n'),
    install_requires=read('requirements.txt').split('\n'),
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Programming Language :: Python'
    ]
)
