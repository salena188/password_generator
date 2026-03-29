# from setuptools import setup, find_packages
#
# setup(
#     name="password_generator",
#     version="0.1",
#     packages=find_packages(),
#     install_requires=[],
#     author="Salina Shrestha",
#     description="Simple Password Generator Project",
# )
from setuptools import setup, find_packages

setup(
    name="password_generator",
    version="0.1.0",
    author="Salina Shrestha",
    author_email="=salenashresth18@gmail.com",
    description="simple password generator project built with python",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/salena188/password_generator",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)