from setuptools import setup, find_packages  # Always prefer setuptools over distutils

import atmcorr

setup(
    name='atmcorr',
    version=atmcorr.__version__,
    url='https://github.com/indigo-ag/ee-atmcorr-timeseries',
    author='telluslabs',
    author_email='admin@telluslabs.com',
    description="TellusLabs Cassandra Connector",
    long_description=open('README.md', 'r').read(),
    license="Apache 2.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'py6s',
        'pandas',
        'earthengine-api',
    ],
)
