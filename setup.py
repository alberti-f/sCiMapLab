import setuptools


# Read the long description from the README file.
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="scimaplab",
    version="0.1",
    author="Francesco Alberti",
    author_email="fnc.alberti@gmail.com",
    description="sCiMapLab provides handy functions for generating Matplotlib style colormaps for scientific data.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alberti-f/sCiMapLab",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=[
        "numpy",
        "matplotlib"
    ],
    packages=setuptools.find_packages(),
)
