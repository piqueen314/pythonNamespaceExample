import setuptools

setuptools.setup(
    name="allLibsNamespace.libB",
    version='0.92',
    url="https://github.com/piqueen314/pythonNamespaceExample.git",
    author="Cece Hedrick",
    author_email="cecehedrick@gmail.com",
    description="A test python package that has one function that report its name",
    namespace_packages=['allLibsNamespace'],
    packages=setuptools.find_packages(),
    py_modules=['libBsrc'],
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    package_dir={"libB": 'allLibsNamespace'},
)
