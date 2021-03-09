import time
import io
import serial

ser = serial.Serial('/dev/ttyACM0', timeout=1, baudrate=115200)
sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))

print('Ohjelma ohjaa lednauhan väriä. Anna haluamasi väri.')
try:
    while True:
        answer = input('r = red , g = green, b = blue, a = animation\n')
        if answer == 'r':
            ser.write(b'r')
            print('Lähetetttiin vastaus: ',answer)
        elif answer == 'g':
            ser.write(b'g')
            print('Lähetetttiin vastaus: ',answer)
        elif answer == 'b':
            ser.write(b'b')
            print('Lähetetttiin vastaus: ',answer)
        elif answer == 'a':
            ser.write(b'a')
            print('Lähetetttiin vastaus: ',answer)
        time.sleep(0.5)

except KeyboardInterrupt:
    ser.close()
    print('Ohjelman suoritus paattyy.')
