import os, time
from replit import db
from random import randint as rnd
title = "Open World RPG Game"

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
    cmd = input("PRESS ENTER TO ENTER IN THE GAME.\n> ")
    """if cmd == "give":
        player = input("Player name: ")
        item = input("Item: ")

        give(Username, player, item)"""
    exe(db["POS_" + Username])
  else:
    input("Wrong password")
    clear()
    exe("main.py")

def save(file):
  Username = input("Username > ")
  if ("PAS_" + Username) in db:
    pass
  else:
    input("This account does not exist")
    clear()
    exe(file)
  loginPassword = input("Password > ")
  passwordUsername = "PAS_" + Username
  if db[passwordUsername] == loginPassword:
    del passwordUsername
    db["POS_" + Username] = file
    input("Save successfull")
    input("You can now leave the game")
    exe("main.py")
  else:
    input("Wrong password")
    clear()
    exe(file)

def pickup(plant, TIME, file):
  print("You pick up a ", plant, "...")
  wait(TIME)
  print("You picked up a ", plant)
  Username = input("Type the username of the person who will have this " + plant + " > ")
  db["INV_" + Username] += (" " + plant)
  exe(file)

def fish(fish, TIME, file):
  print("You fish some ", fish, "...")
  wait(TIME)
  print("You fished some ", fish)
  Username = input("Type the username of the person who will have this " + fish + " > ")
  db["INV_" + Username] += (" " + fish)
  exe(file)

def chop(loot, TIME):
    print("You chop some ", fish, "...")
    wait(TIME)
    print("You got some ", loot)
    Username = input("Type the username of the person who will have this " + loot + "> ")
    db["INV_" + Username] += (" " + loot)
    print("") 
  
def zone(zone):
  print("Zone : ", zone,"\n")

"""def give(playerwhogives, playerwhowillhavetheitem, item):
    if " " + item in db["INV_" + playerwhogives]:
        db["INV_" + playerwhowillhavetheitem] += (" " + item)
        regive = db["INV_" + playerwhogives].count(item) - 1
        db["INV_" + playerwhogives].replace(" " + item, " ")
        db["INV_" + playerwhogives] += regive * (" " + item)
    
    if " " + item not in db["INV_" + playerwhogives]:
        input("Nope. You don't have this item.")
    
    if "PSE_" + playerwhowillhavetheitem not in db.keys():
        input("This player doesn't exist.")"""

def drop(item, pse, pas, file):
  if "PAS_" + pse in db:
    if db["PAS_" + pse] == pas:
      if item in db["INV_" + pse]:
        regive = db["INV_" + pse].count(item) - 1
        db["INV_" + pse].replace(" " + item, " ")
        db["INV_" + pse] += regive * (" " + item)
        input("you dropped ", item)
        exe(file)
      else:
        exe(file)
    else:
      exe(file)
  else:
    exe(file)