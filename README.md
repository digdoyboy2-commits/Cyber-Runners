# Cyber-Runners
Hey! This is Cyber-Runners, a custom handheld arcade console I built using a Raspberry Pi Pico. I designed the entire schematic and PCB layout from scratch in KiCad. The board features a 0.96-inch OLED display header connected to I2C0 (GPIO0 and GPIO1), four tactile push buttons for game controls, and three status LEDs for visual feedback. Everything is powered directly through the Pico's Micro-USB port.

The core KiCad source files—including the schematic, PCB layout, and project configurations—are included in this repository. Once the bare PCB is fabricated, the board is assembled by soldering the Pico, header socket for the OLED screen, push buttons, resistors, and LEDs. The console is designed to be programmed using CircuitPython or C++ to handle button inputs and render graphics on the display.

Pictures 



PCB Layout & Silkscreen
![Cyber-Runners PCB Layout](./images/pcb_layout.png)


---

Electrical Schematic
![Cyber-Runners Schematic](./images/schematic.png)
