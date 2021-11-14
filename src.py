import os, time
from replit import db
from random import randint as rnd
title = "My Incredible Game"

def exe(file):
  exec(open(file).read())
def wait(Time):
  time.sleep(Time)
def clear():
  os.system("clear")

def login():
  Username = input("Username > ")
  if ("PAS_" + Username) in db:
    pass
  else:
    input("This account does not exist")
    clear()
    exe("main.py")
  loginPassword = input("Password > ")
  passwordUsername = "PAS_" + Username
  if db[passwordUsername] == loginPassword:
    print("Connection successfull")
    del passwordUsername
    exe(db["POS_" + Username])
  else:
    input("Wrong password")
    clear()
    exe("main.py")
def pickup(plant, TIME):
  print("You pick up a ", plant, "...")
  wait(TIME)
  print("You picked up a ", plant)
  Username = input("Type the username of the person who will have this " + plant + " > ")
  db["INV_" + Username] += (" " + plant)

def fish(fish, TIME):
  print("You fish some ", fish, "...")
  wait(TIME)
  print("You fished some ", fish)
  Username = input("Type the username of the personx who will have this " + fish + " > ")
  db["INV_" + Username] += (" " + fish)
  print("")

def zone(zone):
  print("Zone : ", zone,"\n")