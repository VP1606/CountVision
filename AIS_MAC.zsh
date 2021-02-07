#!/bin/zsh

echo "------------------------------------------------"
echo "----------- COUNTVISION 2021.05.02e ------------"
echo "--- Automated Install Sequence for MACOS -------"
echo "------------------------------------------------"

echo "Creating Virtual Run Environment (2/6)"
python3 -m venv ./

echo "Entering VENV (3/6)"
source venv/bin/activate

echo "Cloning Version 2021.05.02e (4/6)"
git clone -b release/2021.05.02e --single-branch https://github.com/VP1606/CountVision.git

cd CountVision

echo "Installing Dependencies (5/6)"
pip3 install -e .

echo "Handing over to on-board install scripts (6/6)"
python3 prepare.py

echo "AIS Complete"