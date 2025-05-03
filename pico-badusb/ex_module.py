import board
import digitalio
import neopixel_write
import array
import storage

class WS2812:
    def __init__(self, num_leds=1, pin=16, brightness=0.1):
        self.num_leds = num_leds
        self.brightness = brightness
        self.pixels = array.array("B", [0] * num_leds * 3)
        self.pin = self._get_pin(pin)

    def _get_pin(self, pin):
        pin_map = {
            16: board.GP16,
            17: board.GP17,
        }
        if isinstance(pin, int):
            try:
                return getattr(board, f"GP{pin}")
            except AttributeError:
                raise ValueError(f"Invalid pin number: {pin}. Must be a valid GPIO pin (e.g., 16 for GP16).")
        return pin

    def set_all_colors(self, r, g, b):
        r = int(r * self.brightness)
        g = int(g * self.brightness)
        b = int(b * self.brightness)
        for i in range(self.num_leds):
            self.pixels[i * 3] = g  # GRB format
            self.pixels[i * 3 + 1] = r
            self.pixels[i * 3 + 2] = b
        with digitalio.DigitalInOut(self.pin) as neo:
            neopixel_write.neopixel_write(neo, self.pixels)

class WriteFile:
    def __init__(self, filename="main_out.txt"):
        self.filename = filename

    def write_log(self, message, mode="a"):
        storage.disable_usb_drive()
        try:
            with open(self.filename, mode) as log:
                log.write(message + "\n")
        finally:
            storage.remount("/", readonly=False)
