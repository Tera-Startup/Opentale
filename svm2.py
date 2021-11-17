from replit import db
import src

f = "svm2.py"
src.clear()
src.zone("Sun Valley Meadows Wood")
print("CHOP Some oak\n\nWalk to the RIVER\nWalk to the TOWN\nWalk to the MOUNTAINS")
choice = input("> ")
if choice == "CHOP":
  src.chop("Oak", 1.5)
elif choice == "RIVER":
  src.exe("svm1.py")
elif choice == "TOWN":
  src.exe("svm3.py")
elif choice == "MOUNTAINS":
  print("This place is not disponible yet !")