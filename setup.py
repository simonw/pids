from setuptools import setup
import os


def get_long_description():
    with open(
        os.path.join(os.path.dirname(__file__), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="pids",
        version="0.1.2",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    description="A tiny Python library for generating public IDs from integers",
    author="Simon Willison",
    url="https://github.com/simonw/...",
    license="Apache License, Version 2.0",    
    py_modules=["pids"],
    extras_require={"test": ["pytest"]},
    tests_require=["pids[test]"],
)
