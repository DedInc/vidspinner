from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='vidspinner',
    version='1.0.3',
    author='Maehdakvan',
    author_email='visitanimation@google.com',
    description='Video uniqualizer.',
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
    install_requires = ['Pillow>=8.0'],
    python_requires='>=3.6'
)