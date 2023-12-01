from setuptools import setup, find_packages


setup(
    name="api_toolkit",
    version="0.2.0",
    packages=find_packages(),
    install_requires=[
        'emoji',
        'requests'
    ]
)
