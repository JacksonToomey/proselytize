from setuptools import setup
from src.proselytize import __VERSION__


setup(
    name='proselytize',
    version=__VERSION__,
    description='proselytize converts',
    url='',
    author='Jackson Toomey',
    author_email='jacksontoomey@gmail.com',
    license='MIT',
    packages=['proselytize'],
    package_dir={'': 'src'},
    zip_safe=False,
    install_requires=[
        'jmespath',
    ],
    include_package_data=True,
)
