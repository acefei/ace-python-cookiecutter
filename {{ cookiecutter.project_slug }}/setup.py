from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs if 'git+' not in x]
dependency_links = [x.strip().replace('git+', '') for x in all_reqs if x.startswith('git+')]

setup(
    name='{{cookiecutter.project_slug}}',
    description='{{cookiecutter.project_name}}',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='BSD',
    author='{{cookiecutter.author}}',
    author_email='{{cookiecutter.email}}',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
    ],
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    install_requires=install_requires,
    dependency_links=dependency_links,
    zip_safe=False
)
