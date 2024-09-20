# Iron-Man-HoA

File collection for a Marvel Legends scaled Iron Man Hall of Armor.

Designed to hold 12 Iron Man figures, with a replica H.O.M.E.R. panel and Elevator/Launch tube.

Project is designed to be 3D printed easily.

Main control is a Raspberry Pi, with each bay controlled by a separate Raspberry Pi Pico.
The main Raspberry Pi functions as a clock, enabling a different pico every hour.
The pico turns on and off lights on the front of the bay to imitate the bay running diagnostics on the suit inside.
An OLED screen is also ran, showing a rotating image.
The image does not rotate smoothly, imitating the diagnostic system as lagging while processing.

Plans are to also include a sound module to run on every hour.


To make the Raspberry Pi code autostart on boot:
At the top of the Python code meant to run on the pi, there is this shebang line

  #!/usr/bin/env python

Then, from the pi's terminal, enter the following to change the file attributes:

  sudo chmod +x suit_diag_master.py

Next, pull up the Cron file

  sudo crontab -e

And enter the following to run at boot.

  @reboot sudo /home/Path/To/Script/suit_diag_master.py 2>&1 | tee -a /home/Path/To/Script/fault

This will also create a fault file that can be opened in nano or another text editor.  If the script doesn't run at boot, check this file.


The Pico boards will automatically run code.py in its onboard memory when it powers up. 
