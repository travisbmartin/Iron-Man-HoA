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
