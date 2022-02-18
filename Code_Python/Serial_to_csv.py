import serial
import sys
import datetime
import time
import csv
import signal

ser = serial.Serial('COM5',9600)
time_sta = time.perf_counter()

try:
    while(1):
        value = int(ser.readline().decode('utf-8').rstrip('\n'))
        date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        time_end = time.perf_counter()
        tim = time_end - time_sta
        print(date,tim,value)
        with open('test.csv', 'a') as f:
            print('{},{},{}'.format(date,tim,value),file=f)
except KeyboardInterrupt:
    print("saved")
