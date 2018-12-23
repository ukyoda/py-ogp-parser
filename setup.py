from setuptools import setup
from setuptools import find_packages

requires = [
    "requests>=2.14.2",
    "beautifulsoup4>=4.6.0"
]


setup(
    name='py-ogp-parser',
    version='0.1',
    description='Opengraph Protocol Parser',
    url='https://github.com/ukyoda/py-ogp-parser',
    author='ukyoda',
    author_email='black12172001@hotmail.co.jp',
    license='MIT',
    keywords='opengraph beautifulsoup4 requests scraping',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=requires,
    classifiers=[
        'Programming Language :: Python :: 3.6',
    ],
)
