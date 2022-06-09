import setuptools
from setuptools import setup

with open("readme.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='SuperAutoPets-AI',
    version='0.1',
    author='hunter',
    description='A copycat engine for the game Super Auto Pets, as well as AI learners capable of playing it',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/CallThemHunter/SuperAutoPetsAI',
    project_urls={
        "Bug Tracker": "https://github.com/CallThemHunter/SuperAutoPetsAI/issues"
    },
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    include_package_data=True,
    python_requires='>=3.10',
    license='',
    author_email=''
)
