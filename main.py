from replit import db
import src
import os


print(src.title,"\n\n")
loginsignup = input("1 : Log In\n2 : Sign Up\n> ")
dbCheck = os.environ["dbCheck"]
if loginsignup == "1":
  src.login()
elif loginsignup == dbCheck:

    input(db.keys())
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