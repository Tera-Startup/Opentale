from replit import db
import src

f = "svm1.py"
src.clear()
src.zone("Sun Valley Meadows River")
print("1 : Pick up a flower\n2 : Fish in the river\n")
print("3 : Walk To The Wood\n4 : Walk To The Town")

choice = input("\n> ")
if choice == "1":
    src.pickup("Poppy", 0.25, "svm1.py")
    src.exe(f)
elif choice == "2":
    src.fish("Salmon", 1, "svm1.py")
    src.exe(f)
elif choice == "3":
  src.exe("svm2.py")
elif choice == "4":
  src.exe("svm3.py")
elif choice == "quit" or "Quit" or "save" or "Save":
  src.save(f)
elif choice == "give" or "Give":
  pass
elif choice == "drop" or "Drop":
  src.drop(input("Item > "), input("Username > "), input("Password > "), "svm1.py")