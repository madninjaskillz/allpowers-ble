#!/usr/bin/env python

# This is a shim to allow GitHub to detect the package, build is done with poetry
# Taken from https://github.com/Textualize/rich

import setuptools

__version__ = "0.1.0"

if __name__ == "__main__":
    setuptools.setup(name="allpowers-ble", version=__version__)
