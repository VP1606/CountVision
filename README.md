<span align="center">

# CountVision

</span>

**CountVision** is a computer vision system, for counting how many subjects pass a particular point in realtime using python and OpenCV. 

## About

- Current Version: **2021.06.01**
- Developed by **VARCO**

## Install

#### Baseline Requirements

- **Python 3** - Python3.8+ is recommended.
- **PIP is required for installing dependencies.**

### AIS Install (Recommended)

This is the **Automated Install System**. 
*Note: A virtual environment will be created.*

**MacOS**

Make script **executable**.
```shell
chmod +x ./AIS_MAC.zsh
```

**Run script.**
```shell
./AIS_MAC.zsh
```

#### Manual Installation

First, clone this git repository into the location you want it to be saved to. Ensure the filepath does not contain folders with spaces - **this will fail the installation.**
```shell
git clone -b 2021.06.01 --single-branch https://github.com/VP1606/CountVision.git
```

**Enter the CountVision Folder.**
```shell
cd CountVision
```
Install dependencies.
```shell
pip install -e .
```

Run **prepare.py**
```shell
python prepare.py
```

When prompted, enter the **full directory** of where you want the CSV file to be generated. Or, hit **ENTER** to save to the current folder.

## Running

1. Using the icon.
2. Via source file (Run command from **CountVision/src** folder) :
```shell
python3 RunUI.py
```

