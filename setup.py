from setuptools import setup, find_packages
import sys,os

setup(
      name='vtools',
      version="1.0",
      description="desc",
      long_description="aaa",
      long_description_content_type="text/markdown",
      url="a",#get("https://api.github.com/repos/CastellaniDavide/vtools").json()['html_url'],
      author="aaa",#get("https://api.github.com/repos/CastellaniDavide/vtools").json()['owner']['login'],
      author_email="aaa",#get(f"https://api.github.com/users/{get('https://api.github.com/repos/CastellaniDavide/vtools').json()['owner']['login']}").json()['email'],
      license='GNU',
      packages = ['src'],
      python_requires=">=3.6",
      platforms="linux_distibution",
      install_requires=[],#i for i in get("https://raw.githubusercontent.com/CastellaniDavide/vtools/master/requirements/requirements.txt").text.split("\n") if not "#" in i and i != ''],
      zip_safe=True,
      entry_points = {
        'console_scripts': [
            'vtools=src.vtools:vtools']
            },
      )
