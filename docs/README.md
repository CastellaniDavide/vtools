# vtools
[![GitHub license](https://img.shields.io/badge/license-GNU-green?style=flat)](https://github.com/CastellaniDavide/cpp-vtools/blob/master/LICENSE) ![Author](https://img.shields.io/badge/author-Castellani%20Davide-green?style=flat) ![Version](https://img.shields.io/badge/version-v1.0-blue?style=flat) ![Language Python](https://img.shields.io/badge/language-Python-yellowgreen?style=flat) [![vtools](https://snapcraft.io/vtools/badge.svg)](https://snapcraft.io/vtools) ![sys.platform supported](https://img.shields.io/badge/OS%20platform%20supported-All-blue?style=flat) [![On GitHub](https://img.shields.io/badge/on%20GitHub-True-green?style=flat&logo=github)](https://github.com/CastellaniDavide/vtools) 

## Description
Manage vitual machines, getting some informations (eg. OS).

## Required
 - choco/ snap
 - virtualbox (C:\Work\* if you are on windows)

## Installation
 - choco (Windows) (as Administartor)
   - download the vtools.01.01.nupkg file by the [selected version](https://github.com/CastellaniDavide/vtools/releases)
   - choco.exe install *.nupkg --force -y
 - snap (Linux)
   - snap install vtools
 
## Directories structure
 - .gitignore
 - setup.py
 - snapcraft.yaml
 - .github
   - ISSUE_TEMPLATE
     - bug_report.md
     - feature-request.md
   - workflows
     - on-push.yml
     - on-release.yml
 - choco
   - ReadMe.md
   - set.txt
   - vtools.nuspec
   - tools
     - chocolateyinstall.ps1
     - chocolateyuninstall.ps1
     - LICENSE.txt
     - VERIFICATION.txt
     - vtools-install.c
     - vtools-install.exe
     - vtools-install.o
     - vtools.c
     - vtools.exe
     - vtools.o
 - docs
   - LICENSE
   - logo.png
   - README.md
 - flussi (example output(s))
   - net.csv
   - OS.csv
 - log (example log(s))
   - trace.log
 - requirements
   - requirements.txt
 - src
   - test_vtools.py
   - vtools.py
   
### Execution examples  
 - python3 vtools.py
 - python3 test_vtools.py

# Changelog
 - [Version_1.0_2021-3-16](#Version_10_2021-3-16)

## Version_1.0_2021-3-16
 - Initial version

---
Made by Castellani Davide 
If you have any problem please contact me:
- help@castellanidavide.it
- [Issue](https://github.com/CastellaniDavide/vtools/issues)
