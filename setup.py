from setuptools import setup

setup(
        name='Passwd Fetcher',
        version='1.1',
        py_modules=['pass'],
        install_requires=[
            'Click',
            ],
        entry_points='''
            [console_scripts]
            pass=pass:cli
        ''',
)
