import string

from evdev import InputDevice
from select import select

keyid = ""
keys = "X^1234567890XXXXqwertzuiopXXXXasdfghjklXXXXXyxcvbnmXXXXXXXXXXXXXXXXXXXXXXX"
#dev = InputDevice('/dev/input/by-id/usb-Sycreader_RFID_Technology_Co.__Ltd_SYC_ID_IC_USB_Reader_08FF20140315-event-kbd')
dev = InputDevice('/dev/input/event0')
print "Galamb Tracker V1.0"
while True:
   r,w,x = select([dev], [], [])
   for event in dev.read():
        if event.type==1 and event.value==1:
                char = ( keys[ event.code ] )
                if char.find("X") == -1:
                        keyid = keyid + char
                else:
                        print "ID jott : %s " % keyid
                        keyid = ""
