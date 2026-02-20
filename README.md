# smart--eye-care-hub
Raspberry pi based smart eye care hub
# Smart Eye Care Hub

A Raspberry Pi based smart device that:

- Controls system volume using rotary encoder
- Displays status on OLED screen
- Supports mute toggle
- Optional distance-based eye safety detection

## Hardware Used

- Raspberry Pi 3B+ / Zero 2 W
- Rotary Encoder
- 0.96" OLED Display (SSD1306)
- Optional HC-SR04 Ultrasonic Sensor

## Installation

sudo apt update
sudo apt install xdotool alsa-utils
pip3 install -r requirements.txt

## Run

python3 main.py
