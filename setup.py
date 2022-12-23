from setuptools import setup

long_description = open("README.md").read()

setup(
    name="ast-export",
    version="1.0.0",
    author="Tom Draper",
    author_email="tomjdraper1@gmail.com",
    license="MIT",
    description="Export a Python AST to a dictionary.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tom-draper/ast-export",
    key_words="ast syntax trees export dict json dictionary",
    install_requires=[],
    packages=["api_analytics"],
    python_requires=">=3.6",
)