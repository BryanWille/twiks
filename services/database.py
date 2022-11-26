import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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
        user_names = []
        
        for doc in docs:
            fav_list.append(doc.to_dict())
            user_names.append(doc.to_dict()['user']['screen_name'])
            
        names = user_names
        
        for c in range(0, len(user_names)):
            if user_names.count(user_names[c%len(user_names)]) < 3:
                names.pop(c%len(user_names))
        
        likes = pd.value_counts(np.array(user_names))
        
        likes.plot.pie(x="Quantidade_de_likes", y='Usuários', figsize=(5, 5))
        
        plt.title(f"Usuários que {username} mais curtiu!")
        plt.show()

Database.retrieveStatusInfo("monark")