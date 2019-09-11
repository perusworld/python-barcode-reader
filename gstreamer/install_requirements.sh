#!/bin/bash

if grep -s -q "MX8MQ" /sys/firmware/devicetree/base/model; then
  echo "Installing DevBoard specific dependencies"
  sudo apt-get install python3-pip
  sudo pip3 install svgwrite
  sudo pip3 install python-periphery 
  sudo pip3 install pyzbar
else
  # Install gstreamer 
  sudo apt-get install -y gstreamer1.0-plugins-bad gstreamer1.0-plugins-good python3-gst-1.0 python3-gi
  pip3 install svgwrite
  pip3 install pyzbar

  if grep -s -q "Raspberry Pi" /sys/firmware/devicetree/base/model; then
    echo "Installing Raspberry Pi specific dependencies"
    sudo apt-get install python3-rpi.gpio
    # Add v4l2 video module to kernel
    if ! grep -q "bcm2835-v4l2" /etc/modules; then
      echo bcm2835-v4l2 | sudo tee -a /etc/modules
    fi
    sudo modprobe bcm2835-v4l2 
  fi
fi
