from setuptools import setup, find_packages

setup(
    name="slurmify",
    version="0.1.0",
    packages=find_packages(),
    description="A package to manage Dask clusters on SLURM systems and execute functions with Dask parallelization.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Dennis Noll",
    author_email="github@nollde.de",
    url="https://github.com/nollde/slurmify",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)