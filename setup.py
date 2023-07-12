from setuptools import setup, find_packages

with open('README.rst', encoding='UTF-8') as f:
    readme=f.read()

setup(
        name='ngen',
        version='0.2.1',
        description='CLI to talk to keepasscx-cli',
        long_description=readme,
        author='Boris Quiroz',
        author_email='borisquiroz@pm.me',
        install_requires=[
            'Click',
            'PyYAML',
        ],
        packages=find_packages('src'),
        package_dir={'': 'src'},
        entry_points={
            'console_scripts': [
                'ngen=ngen.cli:main'
                ]
            },
        )
