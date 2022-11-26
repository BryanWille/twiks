import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials

class Database:
    cred = credentials.Certificate("keys/firebase-key.json")
    app = firebase_admin.initialize_app(cred)
    
    def doesUserExist(user_name: str, user_id: str):
        db = firestore.client().collection('users')
        return db.document(user_name).collection("user_info").document(user_id).get().exists

    def createUserInfo(user_map, user_name: str):
        doc_ref = firestore.client().collection('users').document(user_name.lower()).collection("user_info").document(user_map['id_str'])
        doc_ref.set(user_map)
        print("User Sucessfully Sent")

    def createStatusInfo(user_map, user_name: str):
        try:
            doc_ref = firestore.client().collection('users').document(user_name.lower()).collection("favourites").document(user_map['id_str'])
            doc_ref.set(user_map)
            print("Favourite Sucessfully Sent")
        except Exception as e:
            print(e)
    
    def createPostsInfo(user_map: map, user_name: str):
        try:
            doc_ref = firestore.client().collection('users').document(user_name.lower()).collection("posts").document(user_map['id_Str'])
            doc_ref.set(user_map)
            print("Post Sucessfuly Saved")
        except Exception as e:
            print(e)
    
    def retrieveUserInfo( user_name: str):
        docs = firestore.client().collection('users').document(user_name.lower()).collection('user_info').stream()
        fav_list = []
        for doc in docs:
            fav_list.append(doc.to_dict())
        return fav_list
    
    def retrieveStatusInfo( user_name: str):
        docs = firestore.client().collection('users').document(user_name.lower()).collection('favourites').stream()
        fav_list = []
        for doc in docs:
            fav_list.append(doc.to_dict())
        return fav_list

    
    def retrievePostsInfo( user_name: str):
        docs = firestore.client().collection('users').document(user_name.lower()).collection('posts').stream()
        post_list = []
        for doc in docs:
            post_list.append(doc.to_dict())
        return post_list