from firebaseconfig import firebaseConfig 
from Markov import registergame, logingame


auth = firebase.auth()

db = firebase.database()

l_r = """
Do you want to login or register?
"""
print(l_r)

logorreg = int(input("Press 1 for login and 2 for register!! \n"))

if(logorreg==1):
    login()
else:
    register()    

def login():

    email = input("Please Enter Your Email Address : \n")
    password = getpass("Please Enter Your Password : \n")
    login = auth.sign_in_with_email_and_password(email, password)
    print("You are logged in!")
    lst = []
    botlst = []
    useremail = firebase.auth().currentUser.email
    lst = db.child(useremail).child("lst").get().val()
    botlst = db.child(useremail).child("botlst").get().val()
    lst1, botlst1 = logingame(lst,botlst)
    db.child(useremail).child("lst").update(lst1)          #can be used to update data 
    db.child(useremail).child("botlst").update(botlst1)

    
def register():
    email = input("Please Enter the Email Address with which you want to register : \n")
    password = getpass("Please Choose a Password : \n")
    user = auth.create_user_with_email_and_password(email, password)
    print("User is created successfully!")
    login = auth.sign_in_with_email_and_password(email, password) #logged in
    useremail = firebase.auth().currentUser.email                 #logged in user email
    lst, botlst = registergame()                         #function returns two lists
    db.child(useremail).child("lst").set(lst)             #can be used to et data 
    db.child(useremail).child("botlst").set(botlst)

