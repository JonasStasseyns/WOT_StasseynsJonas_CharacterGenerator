const firebaseConfig = {
    apiKey: "AIzaSyBFxCC7ALGXsA4WAaKbvx9MDxOmWVFDiC0",
    authDomain: "chargen-13eae.firebaseapp.com",
    databaseURL: "https://chargen-13eae.firebaseio.com",
    projectId: "chargen-13eae",
    storageBucket: "chargen-13eae.appspot.com",
    messagingSenderId: "453800657527",
    appId: "1:453800657527:web:058ccd2bcc692730f0bc72"
};
firebase.initializeApp(firebaseConfig);

document.querySelector('.gen').addEventListener('click', saveToFirebase)
const matrix = document.querySelector('.matrix');

let char = new Array(64).fill(0);
let key = ''
let realtimeMode = true

function loadCanvas() {
    // console.log(char)
    matrix.innerHTML = ''
    for (let i = 0; i < char.length; i++) {
        const pixel = document.createElement('div')
        pixel.classList.add((char[i] === 0) ? 'no-pix' : 'pix')
        pixel.id = i.toString();
        pixel.addEventListener('click', (evt) => {
            const id = evt.currentTarget.id;
            char[id] = (char[id] === 0) ? 1 : 0;
            loadCanvas()
        })
        matrix.appendChild(pixel)
    }
    // console.log(char)
    if(realtimeMode){
        updateFirebase()
    }
}

function updateFirebase() {
    if (key === '') {
        console.log('emptykey')
        key = saveToFirebase()
    }else{
        console.log(key)
        firebase.database().ref(`/${key}`).update(char)
    }
}

function saveToFirebase() {
    return firebase.database().ref('/').push(char).getKey()
}

loadCanvas()