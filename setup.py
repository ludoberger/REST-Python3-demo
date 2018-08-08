import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="huobiapi",
    version="1.0.0",
    author="HUOBI",
    author_email="huobi@huobipro.com",
    description="HUOBI REST Python API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ludoberger/REST-Python3-demo",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
