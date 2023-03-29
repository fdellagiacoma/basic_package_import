import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

print(long_description)

setuptools.setup(
    name='basic_package_import',
    version='1.0.0',
    author='Santo padre',
    author_email='',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/fdellagiacoma/basic_package_import',
    license='MIT',
    packages=setuptools.find_packages(include=['basic_package_import','pocalamadonna']),
    install_requires=['peppercorn'],
)
