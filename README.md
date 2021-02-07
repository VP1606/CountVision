<span align="center">

# CountVision

</span>

**CountVision** is a computer vision system, for counting how many subjects pass a particular point in realtime using python and OpenCV. 

## About

- Current Version: **2021.05.02e**
- Developed by **VARCO**
- **E CODE: Experimental** internal build - for **Testing Usage only.**

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
git clone -b release/2021.05.02e --single-branch https://github.com/VP1606/CountVision.git
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

When prompted, enter the **full directory** of where you want the CSV file to be generated.

You should now get a desktop icon - use this to run the app.

## Running

1. Using the icon.
2. Via source file (Run command from **CountVision/src** folder) :
```shell
python3 RunUI.py
```

