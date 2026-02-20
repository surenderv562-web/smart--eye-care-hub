import os
import time

class HIDControl:

    def volume_up(self):
        os.system("amixer set Master 5%+")
        print("Volume Increased")

    def volume_down(self):
        os.system("amixer set Master 5%-")
        print("Volume Decreased")

    def mute_toggle(self):
        os.system("amixer set Master toggle")
        print("Mute Toggled")

    def scroll_up(self):
        os.system("xdotool click 4")
        print("Scroll Up")

    def scroll_down(self):
        os.system("xdotool click 5")
        print("Scroll Down")

    def press_key(self, key):
        os.system(f"xdotool key {key}")
        print(f"Pressed {key}")

    def next_tab(self):
        os.system("xdotool key ctrl+Tab")
        print("Next Tab")

    def prev_tab(self):
        os.system("xdotool key ctrl+shift+Tab")
        print("Previous Tab")

    def play_pause(self):
        os.system("xdotool key XF86AudioPlay")
        print("Play/Pause")

    def next_track(self):
        os.system("xdotool key XF86AudioNext")
        print("Next Track")

    def prev_track(self):
        os.system("xdotool key XF86AudioPrev")
        print("Previous Track")