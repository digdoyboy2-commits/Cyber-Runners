import board
import busio
import digitalio
import time

# I2C setup for 0.96" OLED display (GPIO0 = SDA, GPIO1 = SCL)
i2c = busio.I2C(board.GP1, board.GP0)

# Button inputs setup (SW1 - SW4)
btn1 = digitalio.DigitalInOut(board.GP2)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.UP

btn2 = digitalio.DigitalInOut(board.GP3)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.UP

btn3 = digitalio.DigitalInOut(board.GP4)
btn3.direction = digitalio.Direction.INPUT
btn3.pull = digitalio.Pull.UP

btn4 = digitalio.DigitalInOut(board.GP5)
btn4.direction = digitalio.Direction.INPUT
btn4.pull = digitalio.Pull.UP

# LED indicators (D1, D2, D4)
led1 = digitalio.DigitalInOut(board.GP15)
led1.direction = digitalio.Direction.OUTPUT

print("Cyber-Runners Console Initialized!")

while True:
    # Example loop reading button state and toggling LED
    if not btn1.value:
        led1.value = True
    else:
        led1.value = False
    time.sleep(0.01)
