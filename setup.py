# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hopfield']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=7.0.0,<8.0.0', 'numpy>=1.18.1,<2.0.0']

setup_kwargs = {
    'name': 'hopfield',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Your Name',
    'author_email': 'you@example.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
