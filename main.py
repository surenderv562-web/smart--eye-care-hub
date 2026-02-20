import time
from display import DisplayManager
from encoder import EncoderManager
from distance import DistanceManager
from hid_control import HIDManager
from gpiozero import Buzzer

SAFE_DISTANCE = 40        
REFRESH_DELAY = 0.1      

display = DisplayManager()
encoder = EncoderManager()
distance = DistanceManager()
hid = HIDManager()
buzzer = Buzzer(18)

last_steps = encoder.get_steps()

display.boot_screen()
while True:
    try:
        current_steps = encoder.get_steps()

        if current_steps > last_steps:
            hid.volume_up()
            last_steps = current_steps

        elif current_steps < last_steps:
            hid.volume_down()
            last_steps = current_steps

        current_distance = distance.get_distance()

        if current_distance < SAFE_DISTANCE:
            buzzer.on()
            alert_text = "⚠ Too Close!"
        else:
            buzzer.off()
            alert_text = "Safe Distance"

        display.update(current_distance, alert_text)

        time.sleep(REFRESH_DELAY)

    except KeyboardInterrupt:
        buzzer.off()
        display.clear()
        print("Program Stopped")
        break