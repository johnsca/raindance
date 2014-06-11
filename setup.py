from setuptools import setup, find_packages
import os

version = '0.1'

with open(os.path.abspath('./README.md')) as readme:
    long_description = readme.read()

setup(name='raindance',
      version=version,
      description="Tools for turning bosh release info into juju bundles",
      long_description=long_description,
      classifiers=[],
      keywords='cloudfoundry',
      author='whit',
      author_email='whit.morriss at canonical.com',
      url='',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'path.py',
          'pyyaml',
          's3po',
          'subparse',
          'requests',
          'clint'
      ],
      entry_points="""
      [console_scripts]
      rd=raindance.cli:main
      """,
      )
