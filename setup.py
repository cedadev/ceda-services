#!/usr/bin/env python3

import os, re
from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))


with open(os.path.join(here, 'README.md')) as f:
    README = f.read()

if __name__ == "__main__":
    setup(
        name = "ceda-services",
    version = "0.1.0",
    description = "Django application for registering and managing CEDA users.",
    author = "Rhys Evans",
    author_email = "rhys.r.evans@stfc.ac.uk",
    maintainer = "Rhys Evans",
    maintainer_email = "rhys.r.evans@stfc.ac.uk",
    url = "https://github.com/cedadev/ceda-services",
    license = "BSD - See ceda_example/LICENSE file for details",
    packages = find_packages(),
    install_requires = [
        'django',
        'jasmin-ldap-django',
        'jasmin-metadata',
        'jasmin-notifications',
        'django-bootstrap3',
        'django-markdown-deux',
        'python-dateutil',
        'django-polymorphic',
        'requests',
        "django-crispy-forms",
        "fwtheme-django",
        "fwtheme-django-ceda-serv",
    ],
    classifiers = [
        "Development Status :: 1 - Planning",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: BSD License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    zip_safe = False,
    )
