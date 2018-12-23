import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from ogp_parser.parser import parser
from setuptools import find_packages

parser('http://ogp.me')
