from flask import Flask
from firebase_admin import credentials, firestore, initialize_app

app = Flask(__name__)

#Initialising Firebase Database
credential = credentials.Certificate('key.json')# Public key
default_app = initialize_app(credential)
database = firestore.client()
todo_ref = ...