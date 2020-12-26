from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="PygQuery",
    version="0.0.3",
    author="M_Lbr",
    author_email="m.micky.lbr@gmail.com",
    description="Utils package for Google BigQuery",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mlabarrere/PygQuery",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent", "Natural Language :: English"
    ],
    install_requires=[
        'numpy', 'pandas', 'google-cloud-bigquery', 'google-api-python-client',
        'google-auth-httplib2', 'google-auth-oauthlib', 'pyarrow'
    ],
)
