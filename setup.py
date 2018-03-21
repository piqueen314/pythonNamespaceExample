import os
import pip
from six import iteritems
from setuptools import setup
from setuptools.command.develop import develop
from setuptools.command.install import install

PACKAGE_NAME = 'allLibsNamespace'
SOURCES = {
    'allLibsNamespace.libA': 'microlibs/libA',
    'allLibsNamespace.libB': 'microlibs/libB',
}


def install_microlibs(sources, develop=False):
    """ Use pip to install all microlibraries.  """
    print("installing all microlibs in {} mode".format(
              "development" if develop else "normal"))
    wd = os.getcwd()
    for k, v in iteritems(sources):
        try:
            os.chdir(os.path.join(wd, v.root_dir))
            if develop:
                pip.main(['install', '-e', '.'])
            else:
                pip.main(['install', '.'])
        except Exception as e:
            print("Oops, something went wrong installing", k)
            print(e)
        finally:
            os.chdir(wd)


class DevelopCmd(develop):
    """ Add custom steps for the develop command """
    def run(self):
        install_microlibs(SOURCES, develop=True)
        develop.run(self)


class InstallCmd(install):
    """ Add custom steps for the install command """
    def run(self):
        install_microlibs(SOURCES, develop=False)
        install.run(self)


setup(
    name=PACKAGE_NAME,
    version="0.1.11",
    author="Cece",
    author_email="cecehedrick@gmail.com",
    description="Test namespace package",
    license="MIT",
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=[
        'future',
        'six',
        'allLibsNamespace.libA',
        'allLibsNamespace.libB',
    ],
    cmdclass={
        'install': InstallCmd,
        'develop': DevelopCmd,
    },
    py_modules=['libAsrc'],
)
# remove later