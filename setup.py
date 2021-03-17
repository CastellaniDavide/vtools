from setuptools import setup
import sys,os

setup(
      name='vtools',
      version="1.0",
      description="vtools by Castellani Davide",
      long_description="Manage vitual machines, getting some informations (eg. OS).",
      long_description_content_type="text/markdown",
      url="https://github.com/CastellaniDavide/vtools",
      author="DavideC03",
      author_email="help@castellanidavide.it",
      license='GNU',
      packages = ['src'],
      python_requires=">=3.6",
      platforms="linux_distibution",
      install_requires=["tabular-log"],
      zip_safe=True,
      entry_points = {
        'console_scripts': [
            'vtools=src.vtools:vtools']
            },
      )
