from replit import db
import src


src.clear()
print("Zone : Sun Valley Meadows\n")
print("1 : Pick up a flower\n2 : Fish in the river\n")
print("3 : Walk North\n4 : Walk East")

choice = input("\n> ")
if choice == "1":
    src.pickup("Poppy", 0.25)
if choice == "2":
    src.fish("Salmon", 1)