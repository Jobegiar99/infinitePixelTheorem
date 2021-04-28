import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from userInfo import UserInfo

user = UserInfo()
cred = credentials.Certificate(user.firebasejsonPath)
default_app = firebase_admin.initialize_app(cred, {
	'databaseURL': user.dbUrl
	})
ref = db.reference("/")



def checkIfImageExists(imageColors):
    data , result= ref.get("Generated_Images/")
    if imageColors in data["Generated_Images"]:
        return True

    data["Generated_Images"].append(imageColors)
    ref.set(data)
    return False



