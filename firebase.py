from firebaseconfig import firebase
from Markov import registergame, logingame
import getpass 
import json

auth = firebase.auth()

db = firebase.database()

def login():

    email = input("Please Enter Your Email Address : \n")
    password = getpass("Please Enter Your Password : \n")
    login = auth.sign_in_with_email_and_password(email, password)
    print("You are logged in!")
    lst1 = []
    botlst1 = [] 
    useremail = email
    json_lst = db.child(useremail).child("lst").get().val()
    json_botlst = db.child(useremail).child("botlst").get().val()
    lst = list(json_lst.split(" ")) 
    botlst = list(json_botlst.split(" ")) 
    lst1, botlst1 = logingame(lst,botlst)

    json_lst1 = ' '.join([str(elem) for elem in lst1]) 
    json_botlst1 = ' '.join([str(elem) for elem in botlst1]) 
    
    json_lst + = json_lst1
    json_botlst + = json_lst1
    db.child(useremail).child("lst").update(json_lst)          #can be used to update data 
    db.child(useremail).child("botlst").update(json_botlst)

    
def register():
    email = input("Please Enter the Email Address with which you want to register : \n")
    password = getpass.getpass("Please Choose a Password : \n")
    user = auth.create_user_with_email_and_password(email, password)
    print("User is created successfully!")
    login = auth.sign_in_with_email_and_password(email, password) #logged in
    useremail = email                                             #logged in user email
    lst, botlst = registergame()                                  #function returns two lists
    
    json_lst = ' '.join([str(elem) for elem in lst]) 
    json_botlst = ' '.join([str(elem) for elem in botlst]) 
    db.child(useremail).child("lst").set(json_lst)             
    db.child(useremail).child("botlst").set(json_botlst)


l_r = """
Do you want to login or register?
"""
print(l_r)

logorreg = int(input("Press 1 for login and 2 for register!! \n"))

if(logorreg==1):
    login()
else:
    register()    



