# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['example']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'setup.py',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'abersheeran',
    'author_email': 'me@abersheeran.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/abersheeran/setup.py',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)

