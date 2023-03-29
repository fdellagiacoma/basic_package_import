import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='package',
    version='0.0.3',
    author='Santo padre',
    author_email='',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/fdellagiacoma/basic_package_import',
    license='MIT',
    packages=['requests'],
    install_requires=['requests'],
)
