from setuptools import setup, find_packages

setup(
    name='msbackup',
    version='0.0.1',
    author='Aissa Laribi',
    author_email='aissalaribi@yahoo.fr',
    description= 'An utility for backing up MySQL databases',
    url='https://github.com/aissa-laribi/msbackup',
    packages=find_packages('src'),
    package_dir={'':'src'},
    install_requires=['boto3'],
    entry_points={
        'console_scripts': [
            'msbackup=msbackup.cli:main',
            ],
    }
    )
