import os
from distutils.core import setup

root = os.path.dirname(os.path.realpath(__file__))
long_description = open(os.path.join(root, 'README.rst')).read()

setup(
    name='range-regex',
    version='1.0.2',
    description='Python numeric range regular expression generator',
    long_description=long_description,
    url='http://github.com/dimka665/range-regex',
    author='Dmitry Voronin',
    author_email='dimka665@gmail.com',
    license='Python Software Foundation License',
    packages=['range_regex'],
    platforms=['any'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Python Software Foundation License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)