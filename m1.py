#------------------------------------------------------------- Start of Library
#to connect to pins on raspberry pi zero board
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#to connect to accelerometer  gy-521
#from mpu6050 import mpu6050

#import the libraries to create threads
import os

#to connect to the gps -gy-gps6mv1
from gps import *
from time import *
import time
import threading
#------------------------------------------------------------- End of Library

#bringing the global variable in.
gpsd = None #seting the global variable

#---prepping terminal---------
#clear the terminal (optional)
#os.system('clear')
#NOT FUNCTIONING

class GpsPoller(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    global gpsd #bring it in scope
    gpsd = gps(mode=WATCH_ENABLE) #starting the stream of info
    self.current_value = None
    self.running = True #setting the thread running to true

  def run(self):
    global gpsd
    while gpsp.running:
      gpsd.next() #this will continue to loop and grab EACH set of gpsd info to clear the buffer

#--------------------------------------- Initiate launch
# Define a function for the thread
def Parachute_Init():
    while True:
        #this sets delay as a parameter the sleep timer
        print ("Initiating Function: launch_Init seconds: 2")

    

      #-------------------------------Settings for the pin-------------------------

        print ("Parachute initiated -- NANI??")

    #Setting up the pin
    #establishing output
        time.sleep(20)
        GPIO.setup(12, GPIO.OUT)
    # Turning on power to pin 12.
        GPIO.output(12, GPIO.HIGH)
        time.sleep(2)
        print ("Launch has occured/LED should be on")
        GPIO.output(12, GPIO.LOW)
        #GPIO.cleanup()
        print ("Launch has occured/LED should be off")

#--------------------------------------- End of thread creation   -------------


#-----------------------------Initalize Accelerometer
# Define a function for the thread
#def accel_Init():

#      #this sets delay as a parameter the sleep timer
#      time.sleep(2)
#      print ("Initiating Function: accel_Init seconds: 2")
#      sensor = mpu6050(0x68)
#      accelerometer_data = sensor.get_accel_data()
#      print (accelerometer_data)

#------------------------- end of Accelerometer



#-------------------------------Intialize to GPS
# Define a function for the thread
def gps_Init():
      #this sets delay as a parameter the sleep timer
        time.sleep(2)

        print ("Initiating Function: gps_Init seconds: 2")

     #starting the stream of info
        gpsd = GpsPoller()

    # gps_Init.next() #this will continue to loop and grab EACH set of gpsd info to clear the buffer
        gpsd.start()
        #It may take a second or two to get good data
        #print gpsd.fix.latitude,', ',gpsd.fix.longitude,'  Time: ',gpsd.utc

    #os.system('clear')
        print (' GPS reading')
        print ('----------------------------------------')
        print ('latitude    ' , gpsd.fix.latitude)
        print ('longitude   ' , gpsd.fix.longitude)
        print ('time utc    ' , gpsd.utc,' + ', gpsd.fix.time)
        print ('altitude (m)' , gpsd.fix.altitude)
        print ('eps         ' , gpsd.fix.eps)
        print ('epx         ' , gpsd.fix.epx)
        print ('epv         ' , gpsd.fix.epv)
        print ('ept         ' , gpsd.fix.ept)
        print ('speed (m/s) ' , gpsd.fix.speed)
        print ('climb       ' , gpsd.fix.climb)
        print ('track       ' , gpsd.fix.track)
        print ('mode        ' , gpsd.fix.mode)
        print ('sats        ' , gpsd.satellites)
        time.sleep(2) #set to whatever
          # except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
          #  print "\nKilling Thread..."
          #  gpsp.running = False
          #  gpsp.join() # wait for the thread to finish what it's doing
          #  print "Done.\nExiting."
          #----------------------------- End of thread creation   -------------

# Creating three threads
try:
 #           x = threading.Thread(accel_Init)
 #           x.start()
            print("Accel_Init started successfully")
            x2 = threading.Thread(target=Parachute_Init)
            x2.start()
            print("Launch_Init started successfully")
            #x3 = threading.Thread(target=gps_Init)
            #x3.start()
            #print("gps_Init started successfully")
except: 
            print("Failure")