from setuptools import setup, find_packages

package_name = 'py_variance_reduction'


setup(
    name=package_name,
    version='0.1.1',
    author='Andreas Klintberg',
    description='Python variance reduction for decision trees',
    packages=find_packages(),
    install_requires=[
        'setuptools',
        'pandas',
        'numpy'
    ],
    license='MIT',
    long_description=open('Readme.md').read(),
)