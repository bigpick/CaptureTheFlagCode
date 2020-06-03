#!/usr/bin/env python3

# Generated via:
# tshark -r interrupts.pcapng -T fields -e usb.capdata > usb_captured_data
with open('usb_captured_data', 'r') as infile:
    interupt_data = infile.readlines()
    interupt_data = [x.strip() for x in interupt_data if x.strip() != ""]

for x in interupt_data:
    print(x)
