import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials

class Database:
    cred = credentials.Certificate("keys/firebase-key.json")
    app = firebase_admin.initialize_app(cred)

    def createUserInfo(user_map):
        doc_ref = firestore.client().collection('users').document(user_map['screen_name'].lower()).collection("user_info").document(user_map['id_str'])
        doc_ref.set(user_map)
        print("User Sucessfully Sent")

    def createStatusInfo(user_map, username: str):
        try:
            doc_ref = firestore.client().collection('users').document(username.lower()).collection("favourites").document(user_map['id_str'])
            doc_ref.set(user_map)
            print("Favourite Sucessfully Sent")
        except Exception as e:
            print("Favourite not Sent")
            print(e)
            print(f"Tweet id: {user_map['id']}")
    
    def retrieveStatusInfo(username: str):
        db = firestore.client()            
        docs = db.collection(u'users').document(username).collection('favourites').stream()
        
        fav_list = []
        for doc in docs:
            fav_list.append(doc.to_dict())
            
        return fav_list
