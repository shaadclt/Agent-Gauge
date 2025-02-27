# setup.py

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="agent-gauge",
    version="0.0.1",
    author="Mohamed Shaad",
    author_email="shaadclt@gmail.com",
    description="An operational monitoring library for Crew AI applications.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shaadclt/Agent-Gauge",  # Replace with your GitHub repo
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=[
        "psutil",
        "matplotlib",
        "streamlit",
        "tiktoken"
    ],
    include_package_data=True,
    package_data={
        # Include any additional files here
    },
)
