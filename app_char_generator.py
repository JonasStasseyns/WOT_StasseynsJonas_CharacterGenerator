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

ref = db.reference('/')
snapshot = ref.get()

# print(snapshot)

fetchedChar = []
newchar = []

for key, val in snapshot.items():
    print('///////////////////////// --- /////////////////////////')
    print('VAL OF: ' + str(key))
    print(val)
    print('')
    print('FETCHEDCHAR 1')
    fetchedChar += val
    print(fetchedChar)
    print('')

    for i in fetchedChar:
        if i == 0:
            newchar.append(nc)
        elif i == 1:
            newchar.append(c)
    fetchedChar = []
    print('NEWCHAR')
    print(newchar)
    print('')
    globalCharList.append(newchar)
    newchar = []


print('--------------- Sense ----------------')

for char in globalCharList:
    sense.clear()
    print('')
    print('')
    print(char)
    print(char.__len__())
    sense.set_pixels(char)
    sleep(2)

sense.clear()