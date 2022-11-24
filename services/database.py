import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials

class Database:

    def createUserInfo(user_map):
        cred = credentials.Certificate("keys/firebase-key.json")
        app = firebase_admin.initialize_app(cred)
        db = firestore.client()
        doc_ref = db.collection('users').document(user_map['screen_name'])
        doc_ref.set(user_map)
        print("sent sucessfully")