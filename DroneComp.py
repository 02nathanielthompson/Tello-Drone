'''I wasn't able to actually fly the drone at all because of me being forced to quarantine for a month before the school continued to shut down for another few weeks so I'm sorry about not having this in'''
def firstHoop():


  #Drone mission throughthe second Hula Hoop
def secondHoop():
  

  #Drone mission through the thrd Hula Hoop with a yaw
def thirdHoopYaw():
  


  #Drones mission thourhg the first hula hoop
def fourthHoop():
  
print('\nNathan Thompson')
print('Porgram Name: Drone Flying School')
print("Date: 11.6.2020")
print('\n****CHECK YOUR TELLO WIFI ADDRESS****')
print('\n****CHECKSURROUNDING AREA BEFORE FLIGHT****')
ready = input('\nAre you ready to take flight?')


try:
  if ready.lower == 'yes':
    print('\nStarting Drone!\n')
    sendmsg('command')
    sendmsg('takeoff,8
        
     #Calling Function wth some being commented out for testing purposes
    firstHoop
    sendmsg('land')

    print('\nGreat Flight!!!')

  else:
    print('\nMake sure you check WIFI, surroudnings, co-pilor is ready, and re-run the program')
  except KeyboardInterrupt:
      sendmsg('emergency')
      
  breakr = True
  sock.close()