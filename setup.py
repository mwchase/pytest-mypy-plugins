from setuptools import setup

with open("README.md", "r") as f:
    readme = f.read()

dependencies = [
    "pytest>=6.0.0",
    "mypy>=0.900",
    "decorator",
    "pyyaml",
    "chevron",
    "regex",
    "dataclasses ; python_version<'3.7'",
]

setup(
    name="pytest-mypy-plugins",
    version="1.9.3",
    description="pytest plugin for writing tests for mypy plugins",
    long_description=readme,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/TypedDjango/pytest-mypy-plugins",
    author="Maksim Kurnikov",
    author_email="maxim.kurnikov@gmail.com",
    packages=["pytest_mypy_plugins"],
    # the following makes a plugin available to pytest
    entry_points={"pytest11": ["pytest-mypy-plugins = pytest_mypy_plugins.collect"]},
    install_requires=dependencies,
    python_requires=">=3.6",
    package_data={
        "pytest_mypy_plugins": ["py.typed"],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Typing :: Typed",
    ],
)
