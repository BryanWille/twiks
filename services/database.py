import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials

class Database:
    
    def __init__(self, user_name):
        self.username = user_name
        self.cred = credentials.Certificate("keys/firebase-key.json")
        self.app = firebase_admin.initialize_app(self.cred)
        self.db = firestore.client()

    def createUserInfo(user_map):
        doc_ref = firestore.client().collection('users').document(user_map['screen_name'].lower()).collection("user_info").document(user_map['id_str'])
        doc_ref.set(user_map)
        print("User Sucessfully Sent")

    def createStatusInfo(self, user_map):
        try:
            doc_ref = firestore.client().collection('users').document(self.username.lower()).collection("favourites").document(user_map['id_str'])
            doc_ref.set(user_map)
            print("Favourite Sucessfully Sent")
        except Exception as e:
            print("Favourite not Sent")
            print(e)
            print(f"Tweet id: {user_map['id']}")
            
    def createRetweetInfo(self, user_map: map):
        print()
    
    
    def retrieveStatusInfo(self):
        db = firestore.client()            
        docs = db.collection(u'users').document(self.username).collection('favourites').stream()
        
        fav_list = []
        for doc in docs:
            fav_list.append(doc.to_dict())
            
        return fav_list

