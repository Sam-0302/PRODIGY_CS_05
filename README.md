# Network Packet Analyzer

## Overview

The **Network Packet Analyzer** is a Python-based tool designed to capture and analyze network traffic in real-time. It extracts and displays relevant information such as source and destination IP addresses, protocols, ports, and payload data, allowing users to inspect network packets.

## Features

- **Real-time packet capture**: Captures network packets live.
- **IP and Protocol analysis**: Displays source and destination IP addresses, and identifies protocols (TCP/UDP).
- **Port information**: Shows source and destination port numbers for TCP and UDP traffic.
- **Payload inspection**: Extracts and displays the packet payload data when available.

## Requirements

- Python 3.x
- `scapy` library

- 
## Installation

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/Sam-0302/PRODIGY_CS_05.git
    ```

2. Navigate to the project directory:
    ```bash
    cd PRODIGY_CS_05
    ```

3. Install the required Python dependencies:
    ```bash
    pip install scapy
    ```

## Usage

1. Run the script using Python with administrative privileges:
    ```bash
    sudo python packet_analyzer.py
    ```

2. The tool will capture packets and display relevant details such as IP addresses, protocols, and payload data in real-time.

3. Press `CTRL+C` to stop the packet capture.

> **Note**: Administrative or root privileges may be required depending on your system.

## Ethical Use

This tool is intended for educational purposes only. Ensure that you have the necessary permissions to monitor network traffic on any network you use this tool on. Unauthorized packet sniffing is illegal and unethical.

