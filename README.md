# Smart Farm Monitoring System

## Overview
The Smart Farm Monitoring System is an IoT project designed to monitor environmental conditions such as temperature and humidity on a farm. Using Azure IoT Hub, Azure Stream Analytics, and other Azure services, this system collects and processes real-time data from IoT sensors. It includes cybersecurity features to secure device communication and data integrity, ensuring reliable and secure monitoring.

## Features
- **Real-time Data Collection**: Monitors temperature and humidity via simulated IoT sensors.
- **Data Processing**: Uses Azure Stream Analytics to process and store data in real-time.
- **Data Storage**: Saves data to Azure Blob Storage for historical tracking.
- **Alerts and Notifications**: Triggers alerts for specific conditions (e.g., high temperature or low humidity).
- **Security**: Implements secure device communication, role-based access control, and Azure Sentinel for threat detection.

## Prerequisites
- **Azure Subscription**: Set up a [Microsoft Azure account](https://azure.microsoft.com/en-us/free/) if you don’t already have one.
- **Python**: Ensure Python is installed for running the sensor simulation script.
- **Azure IoT Device SDK**: Install via pip to simulate IoT devices.

## Setup

### 1. Create an Azure IoT Hub
1. Log into [Azure Portal](https://portal.azure.com/).
2. Go to **Create a resource** > **IoT Hub** and configure your IoT Hub.
3. After creation, navigate to the IoT Hub and copy the **IoT Hub Connection String**.

### 2. Register IoT Devices
1. In the IoT Hub, go to **Devices** > **+ New**.
2. Create a new device (e.g., `FarmSensor01`), select **Symmetric Key** for authentication, and save it.
3. Copy the **Primary Connection String** for this device. You’ll need it to connect the device simulation.

### 3. Set Up the Device Simulation
1. **Install the Azure IoT Device SDK**:
   ```bash
   pip install azure-iot-device
