from setuptools import setup, find_packages


def install_requires():
    with open('requirements.txt') as f:
        return list(f.read().strip().split('\n'))


config = dict(
      name='coursework',
      version='0.1.1',
      author='Ilya Kisil',
      author_email='ilyakisil@gmail.com',
      packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
      install_requires=install_requires(),
      include_package_data=True
)

setup(**config)