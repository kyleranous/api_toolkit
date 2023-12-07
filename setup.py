"""
Setup.py maintained for legacy systems
"""

"""
Setup.py maintained for legacy systems
"""

from setuptools import setup, find_packages


setup(
    name="api_toolkit",
    version="0.3.1",
    packages=find_packages(),
    install_requires=[
        'emoji',
        'requests'
    ]
)
