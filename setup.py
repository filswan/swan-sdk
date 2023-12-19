""" SwanSDK setup code """

from setuptools import setup, find_packages  # type: ignore
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "PIPRELEASEDOC.md").read_text()


# There are some placeholder for future needs
# TODO: Delete/Modify placeholders as needed
setup(
    name="swan-sdk",
    version="0.1.0",
    author="FilSwan",  # Placeholder for author's name
    author_email="author@email.com",  # Placeholder for author's email
    install_requires=["web3==5.31.1", "requests==2.28.1", "requests_toolbelt==0.10.1"],
    packages=find_packages(where="src"),  # Automatically find packages in src
    package_dir={"": "src"},  # Define the src directory as where to find packages
    license="MIT",
    include_package_data=True,
    description="A python software development kit for Swan services",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/username/package",  # Placeholder for URL
    python_requires=">=3.10",  # Specifies the required Python version
    classifiers=[
        "Development Status :: 1 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
    ]

)
