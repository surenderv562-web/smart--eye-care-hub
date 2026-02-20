import board
import busio
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont
import time

class DisplayManager:

    def __init__(self):
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.oled = adafruit_ssd1306.SSD1306_I2C(128, 64, self.i2c)

        self.width = self.oled.width
        self.height = self.oled.height

        self.image = Image.new("1", (self.width, self.height))
        self.draw = ImageDraw.Draw(self.image)
        self.font_small = ImageFont.load_default()

        self.oled.fill(0)
        self.oled.show()

    def boot_screen(self):
        self.clear()
        self.draw.text((20, 15), "SMART", font=self.font_small, fill=255)
        self.draw.text((20, 30), "EYE CARE HUB", font=self.font_small, fill=255)
        self.oled.image(self.image)
        self.oled.show()
        time.sleep(2)

        self.clear()
        self.draw.text((30, 25), "MEDIMOON", font=self.font_small, fill=255)
        self.oled.image(self.image)
        self.oled.show()
        time.sleep(2)

    def update(self, distance, alert):
        self.clear()

        self.draw.text((0, 0), f"Distance:", font=self.font_small, fill=255)
        self.draw.text((0, 12), f"{distance:.1f} cm", font=self.font_small, fill=255)

        self.draw.text((0, 30), alert, font=self.font_small, fill=255)

        self.draw.text((0, 50), "Eye Protection: ON", font=self.font_small, fill=255)

        self.oled.image(self.image)
        self.oled.show()

    def clear(self):
        self.draw.rectangle((0, 0, self.width, self.height), outline=0, fill=0)

    def shutdown(self):
        self.clear()
        self.draw.text((25, 25), "Shutting Down", font=self.font_small, fill=255)
        self.oled.image(self.image)
        self.oled.show()
        time.sleep(2)
        self.oled.fill(0)
        self.oled.show()