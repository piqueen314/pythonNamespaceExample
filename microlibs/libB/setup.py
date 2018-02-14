import setuptools

setuptools.setup(
    name="libB",
    version='0.90',
    url="https://github.com/piqueen314/pythonNamespaceExample.git",
    author="Cece Hedrick",
    author_email="cecehedrick@gmail.com",
    description="A test python package that has one function that report its name",
    packages=setuptools.find_packages(),
    py_modules=['libBsrc'],
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    package_dir={"libB": 'libBsrc'},
)
