#!/bin/sh
rm -rf dist/*
python -m build
python3 -m twine upload --repository testpypi dist/**