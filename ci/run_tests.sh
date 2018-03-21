#!/usr/bin/env bash
cd microlibs/libA
tox -e $(echo py$TRAVIS_PYTHON_VERSION | tr -d .)
cd ..
cd libB
tox -e $(echo py$TRAVIS_PYTHON_VERSION | tr -d .)
