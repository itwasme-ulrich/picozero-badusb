from badusb.command import Command
import ex_module

neoled = ex_module.WS2812(num_leds=1, pin=16, brightness=0.1)
logger = ex_module.WriteFile(filename="main_out.txt")

if __name__ == "__main__":
    logger.write_log("Starting main.py", mode="w")
    neoled.set_all_colors(255, 255, 255)
    Command().execute("payload.txt")

