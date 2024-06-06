from setuptools import setup, find_packages

setup(
    name='infoexporter',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'sqlalchemy',
        'reportlab',
    ],
    entry_points={
        'console_scripts': [
            'infoexporter=infoexporter.utils:generate_file',
        ],
    },
    author='Prema Latha Davis',
    author_email='your.email@example.com',
    description='A package for exporting data from a database to Excel or PDF.',
    url='https://github.com/yourusername/data_exporter',  # Update with your repository URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
