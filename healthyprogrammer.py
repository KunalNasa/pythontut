# time
# datetime
# pygame
# mixer.init()
# file = "/Users/akashnasa/Desktop/prog.mp3"
# mixer.music.load(file)
# mixer.music.set_volume(10.0)
# mixer.music.play()
# time.sleep(20)


import datetime
import time
from pygame import mixer

def today():
  return datetime.datetime.now()
i = 1
while i < 6:

  def water():
    mixer.init()
    file = "/Users/akashnasa/Desktop/prog.mp3"
    mixer.music.load(file)
    mixer.music.set_volume(10.0)
    mixer.music.play()
    x = input("press p for pause")
    if x == "p":
        mixer.music.pause()
    with open("kannu.txt", "a") as logging:
        a = input("enter amount of water in ml \n")
        logging.write(str([str(today())]) + "water : " + a + "\n")


  def eyes():
    mixer.init()
    file = "/Users/akashnasa/Desktop/prog.mp3"
    mixer.music.load(file)
    mixer.music.set_volume(10.0)
    mixer.music.play()
    x = input("write p if you have started your eyes exercise")
    if x == "p":
      mixer.music.pause()
    mixer.music.pause()
    with open("kannu.txt", "a") as logging:
        a = input("enter done for eyes exercise \n")
        logging.write(str([str(today())]) + "eyes exercise : " + a + "\n")

  def physical():
    mixer.init()
    file = "/Users/akashnasa/Desktop/prog.mp3"
    mixer.music.load(file)
    mixer.music.set_volume(10.0)
    mixer.music.play()
    x = input("write p if you have started your physical activity")
    if x == "p":
      mixer.music.pause()
    mixer.music.pause()
    with open("kannu.txt", "a") as logging:
        a = input("enter done for physical activity \n")
        logging.write(str([str(today())]) + "physical activity : " + a + "\n")


  water()
  time.sleep(1)
  eyes()
  time.sleep(1)
  physical()
  time.sleep(7200)



  i += 1

