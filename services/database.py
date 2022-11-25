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
            doc_ref = firestore.client().collection('users').document(username.lower()).collection("favourites").document(user_map['user']['screen_name']).collection('posts').document(user_map['id_str'])
            doc_ref.set(user_map)
            print("Favourite Sucessfully Sent")
        except Exception as e:
            print("Favourite not Sent")
            print(e)
            print(f"Tweet id: {user_map['id']}")
    
    def retrieveStatusInfo(username: str):
        docs = firestore.client().collection('users').document(username.lower()).collection('favourites').stream()
        for doc in docs:
            print()