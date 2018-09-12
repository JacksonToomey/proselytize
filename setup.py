from setuptools import setup


setup(
    name='proselytize',
    version='0.0.1',
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
