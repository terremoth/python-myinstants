# Python MyInstants
[Myinstants](https://www.myinstants.com/) on terminal  

## Installation
- clone this repo
- Python version required/used: 3.11
- `$ python -m pip install -r requirements.txt`
- if you want to build yourself the binary (PE/Windows):
  - Download and install [Visual Studio 2022](https://visualstudio.microsoft.com/) OR [Mingw64](https://www.mingw-w64.org/)
  -  `$ python -m pip install nuitka imageio` to compile .py to .exe. For some reason nuitka does not fully support yet python 3.12 and above, so I used 3.11.
  -  then execute: `python.exe -m nuitka --onefile --windows-icon-from-ico=icon.png --mingw64 myinstants.py`
    - _note: ignore `--mingw64` if you are using Visual Studio_

 ## Usage
 - `python myinstants.py <term here>`
   - for eg.:
     - `python myinstants.py bolo de murango`
     - `python myinstants.py cavalo`
     - `python myinstants.py uepa`
