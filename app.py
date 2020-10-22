from sense_hat import SenseHat
from datetime import datetime
from request import send
sense = SenseHat()

DEVICE_ID = "1111"


while True:
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']

    xg=round(x, 0)
    yg=round(y, 0)
    zg=round(z, 0)
    
    x = abs(x)
    y = abs(y)
    z = abs(z)
    
    print("x={0}, y={1}, z={2}".format(x, y, z))
    if xg == 1 and yg == 0 and zg ==0:
        temp = sense.get_temperature()
        if temp > 37:
            date = datetime.now()
            date_time = date.strftime("%m/%d/%y, %H:%M:%S")
            data = {
                "device_id" : DEVICE_ID,
                "temp":temp,
                "down":0,
                "date":date_time
            }
            print(data)
            #send(data)
            print("//// temputure")
            break
    else:
        temp = sense.get_temperature()
        if x > 1 or y > 1 or z > 1:
            temp = sense.get_temperature()
            date = datetime.now()
            date_time = date.strftime("%m/%d/%y, %H:%M:%S")
            data = {
                "device_id" : DEVICE_ID,
                "temp":temp,
                "down":1,
                "date":date_time
            }
            print(data)
#             send(data)
            print("----------------the man is in danger situation")
            break
        else:
            temp = sense.get_temperature()
            date = datetime.now()
            date_time = date.strftime("%m/%d/%y, %H:%M:%S")
            data = {
                "device_id" : DEVICE_ID,
                "temp":temp,
                "down":0,
                "date":date_time
            }
            send(data)
            print(data)
            print(">>>>>>>myby the man is in danger situation")
            break