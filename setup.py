from setuptools import setup

# TODO: pipenv lock --requirements > requirements.txt

setup(
    setup_requires=['pbr'],
    install_requires=['beautifulsoup4', 'six'],
    pbr=True
)
