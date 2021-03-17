from setuptools import setup
import sys,os
from requests import get

setup(
      name='vtools',
      version=get("https://api.github.com/repos/CastellaniDavide/vtools/tags").json()[0]['name'].replace("v", "") if len(get("https://api.github.com/repos/CastellaniDavide/vtools/tags").json()) > 0 else "0.0", # Lastest release
      description=get("https://api.github.com/repos/CastellaniDavide/vtools").json()['description'],
      long_description=get("https://raw.githubusercontent.com/CastellaniDavide/vtools/master/docs/README.md").text,
      long_description_content_type="text/markdown",
      url=get("https://api.github.com/repos/CastellaniDavide/vtools").json()['html_url'],
      author=get("https://api.github.com/repos/CastellaniDavide/vtools").json()['owner']['login'],
      author_email=get(f"https://api.github.com/users/{get('https://api.github.com/repos/CastellaniDavide/vtools').json()['owner']['login']}").json()['email'],
      license='GNU',
      packages = ['src'],
      python_requires=">=3.6",
      platforms="linux_distibution",
      install_requires=[i for i in get("https://raw.githubusercontent.com/CastellaniDavide/vtools/master/requirements/requirements.txt").text.split("\n") if not "#" in i and i != ''],
      zip_safe=True,
      entry_points = {
        'console_scripts': [
            'vtools=src.vtools:laucher']
            },
      )
