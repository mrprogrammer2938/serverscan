#!/usr/bin/bash
# This code write by (Ms.nope)
#   █████████████████████████████████████████████████████████████████
#   █─▄▄▄▄█▄─▄▄─█▄─▄▄▀█▄─█─▄█▄─▄▄─█▄─▄▄▀███─▄▄▄▄█─▄▄▄─██▀▄─██▄─▀█▄─▄█
#   █▄▄▄▄─██─▄█▀██─▄─▄██▄▀▄███─▄█▀██─▄─▄███▄▄▄▄─█─███▀██─▀─███─█▄▀─██
#   ▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▀▀▄▀▀▀▄▄▄▄▄▀▄▄▀▄▄▀▀▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▀▀▄▄▀
#                         (🅢🅔🅡🅥🅔🅡 🅢🅒🅐🅝)
clear
echo "installing..."
echo ""
echo "█████████████████████████████████████████████████████████████████"
echo "█─▄▄▄▄█▄─▄▄─█▄─▄▄▀█▄─█─▄█▄─▄▄─█▄─▄▄▀███─▄▄▄▄█─▄▄▄─██▀▄─██▄─▀█▄─▄█"
echo "█▄▄▄▄─██─▄█▀██─▄─▄██▄▀▄███─▄█▀██─▄─▄███▄▄▄▄─█─███▀██─▀─███─█▄▀─██"
echo "▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▀▀▄▀▀▀▄▄▄▄▄▀▄▄▀▄▄▀▀▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▀▀▄▄▀"
echo "                  (🅢🅔🅡🅥🅔🅡 🅢🅒🅐🅝)"
sudo apt install python
sudo apt install python3
sudo apt install pip
pip install --upgrade pip
pip install subprocess
chmod +x server
chmod +x uninstall
cd Update && chmod +x update
echo ""
echo "finish!"
echo ""
echo "usage: ./server"
echo ""
exit 1
