from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='npsample',
    version='0.0.1',
    description='An application to help you find a lucky home address number',
    long_description=readme,
    author='Nopporn Phantawee',
    author_email='n.phantawee@gmail.com',
    url='https://github.com/noppGithub/luckyhomenumber',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)