from replit import db
import src
import os

src.clear()
print(src.title,"\n\n")
loginsignup = input("1 : Log In\n2 : Sign Up\n> ")
dbCheck = os.environ["dbCheck"]
if loginsignup == "1":
  src.login()
elif loginsignup == dbCheck:
    input(db.keys())
elif loginsignup == os.environ["svm1Cheat"]:
    src.exe("svm1.py")
elif loginsignup == os.environ["delAccount"]:
    p = input("Player: ")
    del db["PSE_"+ p]
    del db["PAS_"+ p]
    del db["INV_"+ p]
    del db["POS_"+ p]
    input(p + "'s account have been deleted.")
elif loginsignup == os.environ["playersList"]:
    plyrs = db.prefix("PSE_")
    print(plyrs)
    
elif loginsignup == os.environ["delAccount"]:
    p = input("Player:")
elif loginsignup == os.environ["checkPplInv"]:
    p = input("Player: ")
    input(db["INV_" + p])
elif loginsignup == os.environ["cmd"]:
    exit()
elif loginsignup == "2":
  src.clear()
  try:
    username = input("Username : ")
    if ("PSE_" + username) in db:
      input("Username already taken !")
      src.clear()
      src.exe("main.py")
    password = input("Password : ")
    db["PAS_" + username] = password
    db["POS_" + username] = "svm1.py"
    db["INV_" + username] = ""
    db["PSE_" + username] = username
  except:
    print("Sign up failed")
else :
  src.clear()
  src.exe("main.py")