try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Think Python',
    'author': 'Andrew Antle',
    'author_email': 'andrew.antle@gmail.com',
    'url': 'Where to get it',
    'download_url': 'Where to download it',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['think-python'],
    'scripts': [],
    'name': 'think'
}

setup(**config)
