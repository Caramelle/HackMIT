from firebase import Firebase
from firebase_token_generator import create_token
from key import key

auth_payload = {"uid": "1"}
token = create_token(key, auth_payload)

fire = Firebase('https://hackmit-58edf.firebaseio.com/movies',auth_token=token)
