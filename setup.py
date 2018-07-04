from setuptools import setup, find_packages


setup(
    name='index-hr',
    version='0.1',
    description='index.hr basic news content in the terminal',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    keywords='index hr terminal cli news croatia',
    url='https://github.com/marinko-peso/index-hr',
    author='Marinko Peso',
    author_email='marinko.peso@gmail.com',
    license='MIT',
    packages=find_packages(exclude=['tests*']),
    install_requires=[],
    zip_safe=False,
    scripts=['bin/index-hr'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ]
)
