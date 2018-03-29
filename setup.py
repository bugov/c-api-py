import os

from setuptools import setup, Extension

requires = []
ext_kwargs = {}


def read(file_name):
    return open(os.path.join(os.path.dirname(__file__), file_name), encoding='utf-8').read()


setup(
    # Basic package information:
    name='secure-string',
    version='0.0.1',

    # Packaging options:
    zip_safe=False,
    include_package_data=True,

    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],

    # Package dependencies:
    requires=requires,
    tests_require=requires + ["pytest"],
    setup_requires=requires + ["pytest-runner"],
    install_requires=requires,

    # Metadata for PyPI:
    author='Georgy Bazhukov',
    author_email='georgy.bazhukov@gmail.com',
    license='BSD',
    url='https://github.com/bugov/secure-string',
    keywords='security string auth',
    description='',
    long_description=read('readme.md'),

    ext_modules=[
        Extension(
            'secure_string',
            ['src/secure_string.c'],
            **ext_kwargs
        )
    ],
)