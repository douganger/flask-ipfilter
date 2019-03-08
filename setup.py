"""
Flask-IPFilter
--------------

Flask-IPFilter lets you set up an IP Whitelist to restrict access to your site
to certain hosts and networks.
"""

from setuptools import setup

setup(
    name="Flask-IPFilter",
    version="0.0.2",
    description="Limit access to a Flask website by IP address",
    long_description=__doc__,
    url="https://github.com/douganger/flask-ipfilter",
    author="Douglas Anger",
    author_email="douganger@gmail.com",
    license="MIT",
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content"
    ],
    packages=["flask_ipfilter"],
    include_package_data=True,
    install_requires=["Flask"],
    zip_safe=False
)
