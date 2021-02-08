#!/bin/zsh

echo "------------------------------------------------"
echo "----------- COUNTVISION 2021.06.01 ------------"
echo "--⚡ Automated Install Sequence for MACOS ⚡------"
echo "------------------------------------------------"

echo "Creating Virtual Run Environment 💻"
python3 -m venv ./venv

echo "Entering VENV 🔑"
source venv/bin/activate

echo "Cloning Version 2021.06.01 📂"
git clone -b release/2021.06.01 --single-branch https://github.com/VP1606/CountVision.git

cd CountVision

echo "Installing Dependencies 🔗"
pip3 install -e .

echo "Handing over to on-board install scripts 📝"
python3 prepare.py

echo "AIS Complete ⚡️✅"