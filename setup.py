from setuptools import setup, find_package

with open('README.rst', encoding='UTF-8') as f:
    readme = f.read()

setup(
        name='ngen',
        version='0.1.0',
        description='Interface to talk to keepass-xc'
        long_description=readme,
        author='Boris Quiroz',
        author_email='borisquiroz@pm.me',
        install_requires=['click'],
        packages=find_packages('src'),
        package_dir={'': 'src'},
        entry_points={
            'console_scripts': [
                'ngen=ngen.cli:main',
                ]
            },
        )
