import setuptools

setuptools.setup(
    name='autotests',
    version='0.1',
    package_dir={'': 'src'},
    packages=setuptools.find_namespace_packages(where='src'),
    python_requires='>=3.6',
    install_requires=[
       "selenium",
       "pytest",
    ],
)