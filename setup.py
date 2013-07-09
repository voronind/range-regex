from distutils.core import setup

long_description = open('README.rst').read()

setup(
    name='range-regex',
    version='1.0.1',
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
        'Environment :: Web Environment',
    ],
)