#!/usr/bin/env bash
cd microlibs
tox -e $(echo py$TRAVIS_PYTHON_VERSION | tr -d .)
