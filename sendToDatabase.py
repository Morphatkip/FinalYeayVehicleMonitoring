import pandas as pd
import firebase_admin
from firebase_admin import credentials, firestore

def sendToDatabase():
    cred = credentials.Certificate("roadmonitoring-d0a83-firebase-adminsdk-djmb8-2cba8a80ab.json")
    firebase_admin.initialize_app(cred)


    db = firestore.client()

    doc_ref = db.collection(u"cameraOne")
    # Import data
    df = pd.read_csv("output.csv")
    tmp = df.to_dict(orient="records")
    list(map(lambda x: doc_ref.add(x), tmp))

    # Export Data
    docs = doc_ref.stream()
    for doc in docs:
        print(f"{doc.id} => {doc.to_dict()}")
sendToDatabase()