from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
  name = 'cebsyldec',
  packages = find_packages(),
  version = '0.0.5',
  description = "A Cebuano Syllabicator",
  long_description = long_description,
  long_description_content_type = "text/markdown",
  author = 'Eric John Emberda',
  author_email = 'eric.emberda@gmail.com',
  url = 'https://github.com/eemberda/Cebuano-Syllable-Decoder',
  download_url = 'https://github.com/eemberda/Cebuano-Syllable-Decoder/archive/0.0.5.tar.gz',
  keywords = ['syllabicator', 'cebuano', 'bisaya', 'syllabification'],
  classifiers = [
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
  ],
  python_requires = '>=3.7',
)
