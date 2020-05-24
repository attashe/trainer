import re
from setuptools import setup, find_packages

with open("README.md") as f:
    readme = f.read()

with open("requirements.txt") as f:
    requirements = f.read().split()

with open("trainer/__init__.py") as f:
    VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
    version = re.search(VSRE, f.read()).group(1)

setup(
    name="trainer",
    version=version,
    author="Vladislav Mikhailov",
    author_email="yamihaiov@gmail.com",
    packages=find_packages(exclude=["tests", "docs", "examples"]),
    url="https://github.com/attashe/trainer",
    description="Tool box for PyTorch",
    long_description=readme,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    setup_requires=["setuptools_scm"],
    python_requires=">=3, <4",
    install_requires=requirements,
    license="MIT License",
)