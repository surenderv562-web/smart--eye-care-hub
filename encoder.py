from gpiozero import RotaryEncoder, Button
from signal import pause

class EncoderManager:

    def __init__(self):
       
        self.encoder = RotaryEncoder(
            a=17,          
            b=27,          
            wrap=False,
            max_steps=0
        )

        self.button = Button(22)

    def get_steps(self):
        return self.encoder.steps

    def reset(self):
        self.encoder.steps = 0

    def is_pressed(self):
        return self.button.is_pressed