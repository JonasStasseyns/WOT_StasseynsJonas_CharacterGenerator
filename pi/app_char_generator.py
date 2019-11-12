import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.set_rotation(180)

globalCharList = []

c = [50, 50, 50]
nc = [0, 0, 0]

# Fetch the service account key JSON file contents
cred = credentials.Certificate('keys.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://chargen-13eae.firebaseio.com'
})


def listener(event):
    data = db.reference('/').get()
    for key, val in data.items():
        print('VAL OF: ' + str(key))
        print(val)
        print('')
        val = val.split(',')
        char = []
        for pix in val:
            if pix == '0':
                char.append(nc)
            elif pix == '1':
                char.append(c)
        sense.set_pixels(char)
        sleep(2)
    sense.clear()

db.reference('/').listen(listener)

