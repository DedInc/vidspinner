from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='vidspinner',
    version='2.0.1',
    author='Maehdakvan',
    author_email='visitanimation@google.com',
    description='VidSpinner is a Python library for easily creating unique versions of videos using filters, text, and audio effects.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/DedInc/vidspinner',
    project_urls={
        'Bug Tracker': 'https://github.com/DedInc/vidspinner/issues',
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    include_package_data = True,
    install_requires = [],
    python_requires='>=3.6'
)