#!/usr/bin/env python3

import sendData as send
import read_sensors as readSenors
import systemControl as sysCtrl
import time

while True:

    try:
        print('Reading I2C sensors...')
        readSenors.read_I2C_sensors()
        print('Finished reading I2C sensors')
    except:
        print('Failed to read I2C sensors')

    try:
        print('Sending cabin sensor data...')
        send.send_cabin_data()
        print('Finished sending cabin sensor data')
    except:
        print('Failed to send cabin sensor data')

    try:
        print('Leyendo sensores de nivel de agua...')
        readSenors.read_water_level()
        print('Sensores nivel de agua leidos')
    except:
        print('Failed to read water level sensors')

    try:
        print('Enviando los valores del entorno...')
        send.send_system_values()
        print('Datos del entorno enviados')
    except:
        print('Failed to send system sensor data')
    
    try:
        print('Ventilation control')
        sysCtrl.ventilationControl()
        print('Ventilation control done')
    except:
        print('Failed to do Ventilation control')

    try:
        print('Lighting control')
        sysCtrl.lightingControl()
        print('Lighting control done')
    except:
        print('Failed to do Lighting control')

    time.sleep(120)
