from replit import db
import src

f = "svm1.py"
src.clear()
src.zone("Sun Valley Meadows River")
print("PICKUP a flower\nFISH in the river\n")
print("Walk To The WOOD\nWalk To The TOWN")

choice = input("\n> ")
if choice == "PICKUP":
    src.pickup("Poppy", 0.25, "svm1.py")
    src.exe(f)
elif choice == "FISH":
    src.fish("Salmon", 1, "svm1.py")
    src.exe(f)
elif choice == "WOOD":
  src.exe("svm2.py")
elif choice == "TOWN":
  src.exe("svm3.py")
elif choice == "quit" or "Quit" or "save" or "Save" or "SAVE":
  src.save(f)
elif choice == "give" or "Give" or "GIVE":
  pass
elif choice == "drop" or "Drop" or "DROP":
  src.drop(input("Item > "), input("Username > "), input("Password > "), "svm1.py")