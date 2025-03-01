#!/bin/bash

echo "Checking for running RTL-SDR processes..."

# Get the process IDs of any RTL-SDR-related processes (excluding this script)
processes=$(sudo lsof | grep rtl | awk '{print $2}' | grep -v $$)

if [ -n "$processes" ]; then
    echo "Found active RTL-SDR processes. Terminating them..."
    sudo kill -9 $processes
    sleep 2
else
    echo "No active RTL-SDR processes found."
fi

# Unbind and rebind the RTL-SDR device
echo "Resetting RTL-SDR device..."
sudo rmmod dvb_usb_rtl28xxu rtl2832 > /dev/null 2>&1
sudo modprobe rtl2832 > /dev/null 2>&1

echo "RTL-SDR device reset complete. Now running rtl_sdr..."

# Run your RTL-SDR command
rtl_sdr -f 491000000 -s 2e6 -g 20 -p 70 output.iq

