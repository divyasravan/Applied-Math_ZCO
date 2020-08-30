import setuptools

with open("README.md", "r") as f:
    Readme = f.read()

setuptools.setup(
    name="HOC_Sequence",
    version="1.0.0",
    description="Calculate Higher Order Crossings of a signal",
    long_description=Readme,
    long_description_content_type="text/markdown",
    author="Divya Saravana",
    author_email="dhivyasravan@gmail.com",
    licence="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.6',
    test_suite='nose.collector',
    tests_require=['nose'],
)
