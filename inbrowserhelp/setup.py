import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="inbrowserhelp-autodesk",
    version="0.0.1",
    author="Autodesk Dude",
    author_email="some.dude@autodesk.com",
    description="inbrowserhelp sample",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://git.autodesk.com/windish/maxpythontutorials",
    packages=setuptools.find_packages(),
    entry_points={'3dsMax': 'startup=inbrowserhelp:startup'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "LICENSE :: OTHER/PROPRIETARY LICENSE",
        "Operating System :: Microsoft :: Windows"
    ],
    python_requires='>=3.6'
)
