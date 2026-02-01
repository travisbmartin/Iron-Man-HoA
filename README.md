# Iron-Man-HoA

<img src = "Pictures/Copy of Iron Man Hall of Armor (5).png">

<img src = "Pictures/20240916_155300.jpg">

File collection for a Marvel Legends scaled Iron Man Hall of Armor.

Designed to hold 12 Iron Man figures, with a replica H.O.M.E.R. panel and Elevator/Launch tube.

Project is designed to be 3D printed easily. Most of the bay parts are printed with FDM material, but I opted for resin printing to make HOMER, the front panels, and the ceilings.

## Demonstration

[(https://www.google.com/search?q=https://img.youtube.com/vi/XXk1AkZXeck/0.jpg)](https://www.youtube.com/watch%3Fv%3DXXk1AkZXeck)

[(https://www.google.com/search?q=https://img.youtube.com/vi/MWSStyxMDuw/0.jpg)](https://www.youtube.com/watch%3Fv%3DMWSStyxMDuw)

[(https://www.google.com/search?q=https://img.youtube.com/vi/htXjz3oLDX0/0.jpg)](https://www.youtube.com/watch%3Fv%3DhtXjz3oLDX0)

## 🚀 How it Works

The project functions as a physical wall clock where each armor bay represents one hour (1 through 12).

* **Master Control:** A Raspberry Pi 4 tracks the system time and enables a different Pico every hour via an "Enable" signal on GP18.
* **Bay Animation:** When enabled, the Pico runs diagnostics on the suit:
* **OLED Display:** Shows a rotating Arc Reactor. *Note: The rotation is intentionally jittery to simulate a diagnostic system lagging while processing data.*
* **Overhead Lighting:** Powers the bay's main spotlight via GP22.
* **Ambient Effects:** A central "HOMER" light pulses slowly using PWM to simulate a standby heartbeat.

Check the Pictures folder for a lot of WIP and finished shots that I think help with the build.

## 🕰️ Clock Logic (Minutes Display)

Each bay features a custom LED clock interface to display the minutes:

* **Single Minutes (Binary):** A bay of four lights counts from 0 to 9 in binary.
* **Tens of Minutes (Circular):** Five lights arranged in a circle represent blocks of ten. One light turns on for each 10-minute interval (10, 20, 30, 40, and 50).

## 🛠️ Hardware & Shopping List

### Microcontrollers 
* **1x Raspberry Pi 4B:** The master controller.
* **12x Raspberry Pi Pico:** Local controllers for each bay.

### Components 
* **12x 0.96" OLED Modules:** 128x64 I2C Blue displays.
* **Adafruit LED Sequins:** Ruby Red, Emerald Green, Royal Blue, and Warm White.
* **Magnets:** 3mm D x 4mm H Neodymium magnets (glued to Marvel Legends' feet).
* **Flooring:** 16-Gauge Perforated Steel Sheet (24" x 24").
* **Wiring:** Twisted pair wires harvested from Cat 5 Network Cables.

# Hall of Armor: Electrical & Wiring Guide

This guide outlines the wiring architecture for the Iron Man Hall of Armor diorama. The system uses a **Raspberry Pi 4B** as the master clock controller and **12 Raspberry Pi Picos** (one for each "hour" or armor bay) to handle local lighting and OLED displays.

**Note:** The wiring portion of this project can quickly become a mess. To make the wires fit through the holes in the armor bay I used single strands of CAT5 cable. Try to be uniform in what color you use where, and be aware that you'll have to double up using a color in places. Definiately write out a wiring plan before going for it. Also, arrange the groups of LEDS in a way that you can solder all of the grounds to one wire. The strip of four is easy, but the circle of five can be tricky, and I arranged mine to the inside of the circle shape to solder them together.

I've made wiring maps for the Pi and the Picos in Fritzing, but they aren't very good.

I reccommend wiring up a single pico and loading the code in as a test bed. That way you can practice how you want to handle the wiring.

## 1. System Architecture

* **Master (Raspberry Pi 4B):** Runs `Suit_diag_master.py`. It tracks the real-world time and sends an "Enable" signal to the Pico corresponding to the current hour.

* **Clients (12x Raspberry Pi Picos):** Run `code.py` (CircuitPython). Each Pico waits for a signal on its `GP18` pin. When high, it activates its local "Hall of Armor" animations, OLED arc reactor, and binary minute clock.

## 2. Master Raspberry Pi 4B Wiring

The Pi 4 manages the 12 Picos by toggling their `RUN` or `Enable` states via GPIO.

### Master Pinout (BCM Mode)

Based on `Suit_diag_master.py`, the following pins on the Pi 4 connect to the **Enable/GP18** pin of each Pico:

| Hour / Bay | Pi 4 GPIO (BCM) | Physical Pin |
| ----- | ----- | ----- |
| **12 (0)** | GPIO 6 | Pin 31 |
| **1** | GPIO 13 | Pin 33 |
| **2** | GPIO 19 | Pin 35 |
| **3** | GPIO 14 | Pin 8 |
| **4** | GPIO 18 | Pin 12 |
| **5** | GPIO 23 | Pin 16 |
| **6** | GPIO 25 | Pin 22 |
| **7** | GPIO 20 | Pin 38 |
| **8** | GPIO 9 | Pin 21 |
| **9** | GPIO 21 | Pin 40 |
| **10** | GPIO 11 | Pin 23 |
| **11** | GPIO 17 | Pin 11 |
| **HOMER (PWM)** | GPIO 12 | Pin 32 |

**Common Rail:** Ensure all Picos and the Raspberry Pi share a **Common Ground (GND)**.

## 3. Raspberry Pi Pico (Per Bay) Wiring

Each Pico is responsible for one bay. Refer to your `pico wiring.png` and `code.py` for these connections.

### Power & Control Input

* **VBUS/VSYS:** Connect to +5V (from Pi 4 or external power supply).

* **GND:** Common Ground rail.

* **Enable Signal (GP18):** Connect to the corresponding GPIO pin from the Master Pi 4 (see table above).

### OLED Display (I2C)

* **SDA:** GP0 (Pin 1)

* **SCL:** GP1 (Pin 2)

* **VCC:** 3.3V (Out from Pico)

* **GND:** GND

### LED Groups (PWM Controlled)

The LEDs are divided into "Tens of Minutes" and "Single Minutes" to act as a binary/incremental clock.

#### Tens of Minutes (GP2 - GP6)

| LED | Pico Pin | Role |
| ----- | ----- | ----- |
| LED 1 (10m) | GP2 | 10 Minutes |
| LED 2 (20m) | GP3 | 20 Minutes |
| LED 3 (30m) | GP4 | 30 Minutes |
| LED 4 (40m) | GP5 | 40 Minutes |
| LED 5 (50m) | GP6 | 50 Minutes |

#### Single Minutes (GP7 - GP10)

| LED | Pico Pin | Role |
| ----- | ----- | ----- |
| LED 1 (1m) | GP7 | 1 Minute (Bit 0) |
| LED 2 (2m) | GP8 | 2 Minutes (Bit 1) |
| LED 3 (4m) | GP9 | 4 Minutes (Bit 2) |
| LED 4 (8m) | GP10 | 8 Minutes (Bit 3) |

### Pico File Installation

To get the code running, your Pico's `CIRCUITPY` drive needs to look like this:

* `code.py` (The main script)
* `arc_reactor_2.bmp` (The image file)
* `lib/` (Folder containing the necessary libraries)
* `adafruit_displayio_ssd1306.mpy`
* `adafruit_imageload.mpy`
* `adafruit_bus_device/`

#### Overhead Lighting

* **Bay Light:** GP22 (Pin 29). This pin is set to `True` whenever the Pico is active.

## 4. Hardware Tips

### The "Cat 5" Trick

As noted in the materials list, using the twisted pairs from a **Cat 5 network cable** is an excellent way to keep wiring clean.

* Use one color (e.g., Orange/White-Orange) for I2C (SDA/SCL).

* Use Blue/White-Blue for Power and Ground.

* Keep the twists intact as long as possible to reduce signal interference over the distance of the diorama.

### Magnet Mounting

* The **3mm x 4mm magnets** should be glued into the feet of the Marvel Legends figures.

* The **Perforated Steel Sheet** should be painted and then used as the flooring. This allows the figures to snap into place securely while maintaining the "industrial" look of the Hall of Armor.

### Software Auto-Run

**Raspberry Pi 4:** Add `python3 /path/to/Suit_diag_master.py &` to your `/etc/rc.local` or create a systemd service to ensure the clock starts on boot.

**Picos:** Ensure the code is named `code.py`. CircuitPython automatically executes `code.py` whenever the board receives power or the `RUN` pin is toggled.

## 📂 Software & Setup

### Raspberry Pi 4 Auto-start To ensure the clock starts automatically on boot:

Ensure the shebang line #!/usr/bin/env python3 is at the top of Suit_diag_master.py.

Make the script executable: 
  ```bash sudo chmod +x suit_diag_master.py ```

Open the Cron file: 
  ```bash sudo crontab -e ```

Add the following line to the bottom (update the path to your script): 
  ```bash @reboot sudo /home/Path/To/Script/suit_diag_master.py 2>&1 | tee -a /home/Path/To/Script/fault ```
*This creates a fault file in your directory. If the script doesn't run at boot, check this file.*

#### Pico Setup Each Pico runs CircuitPython. The board will automatically execute code.py in its onboard memory upon receiving power or an enable signal. Please note that different boards require different versions of CircuitPython; refer to [circuitpython.org](https://www.google.com/search?q=https://circuitpython.org/) for the correct version.

## 📜 Credits & Attributions

* **3D Design:** Building the 3D STL files was done using [TinkerCad](http://www.tinkercad.com).
* Original design/dimensions: [WayGroovy's "Iron Man Hall of Armor"](https://www.google.com/search?q=https://www.tinkercad.com/things/l37zKctDpl7-iron-man-hall-of-armor).
* Honeycomb side pattern: Remixed from [ines.lopez's "panel"](https://www.google.com/search?q=https://www.tinkercad.com/things/dchcW7EJQ0m-panel).
* Front Panel: Elements from [ZDP189's "NASA Apollo Mission Control Panels"](https://www.google.com/search?q=https://www.tinkercad.com/things/6omLFvvjeiZ-nasa-apollo-mission-control-panels).
* **Code & Assets:** * OLED tutorials by [educ8s.tv](http://educ8s.tv).
* Arc Reactor Vector art via [OnlineResize.club](https://www.google.com/search?q=https://onlineresize.club/2021-club.html).

## 🏗️ Future Plans 
* Integration of a sound module to trigger specific audio cues on the hour. 
* Integration with smart home assistants (Google Assistant, etc.).

## ⚖️ License
This project is intended for the Maker community. I am happy for individuals to sell their custom builds or improve the design, but commercial use by large-scale manufacturers is not authorized without a separate agreement.

*Built for the 6" Marvel Legends scale.*
