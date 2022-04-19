"""
Flask-IPFilter
--------------

Flask-IPFilter lets you set up an IP Whitelist to restrict access to your site
to certain hosts and networks.
"""

from collections import OrderedDict
from setuptools import setup

setup(
    name="Flask-IPFilter",
    version="0.0.5",
    description="Limit access to a Flask website by IP address",
    long_description=__doc__,
    url="https://github.com/douganger/flask-ipfilter",
    project_urls=OrderedDict((
        ('Documentation', 'https://flask-ipfilter.readthedocs.io/en/stable/'),
        ('Code', 'https://github.com/douganger/flask-ipfilter'),
        ('Issue tracker', 'https://github.com/douganger/flask-ipfilter/issues'))),
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
