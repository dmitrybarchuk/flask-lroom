from setuptools import setup

setup(
    name='lroom',
    packages=['lroom'],
    include_package_data=True,
    install_requires=[
        'flask', 'sqlalchemy',
    ],
)
