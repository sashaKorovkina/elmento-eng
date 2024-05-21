import streamlit as st
import firebase_admin

from firebase_admin import credentials
from firebase_admin import auth
from firebase_admin import firestore

def initialize_firebase_app():
    try:
        firebase_admin.get_app()
    except ValueError:
        secrets = st.secrets["firebase-auth"]

        cred = credentials.Certificate({
            "type": secrets["type"],
            "project_id": secrets["project_id"],
            "private_key_id": secrets["private_key_id"],
            "private_key": secrets["private_key"],
            "client_email": secrets["client_email"],
            "client_id": secrets["client_id"],
            "auth_uri": secrets["auth_uri"],
            "token_uri": secrets["token_uri"],
            "auth_provider_x509_cert_url": secrets["auth_provider_x509_cert_url"],
            "client_x509_cert_url": secrets["client_x509_cert_url"],
        })

        # Initialize the Firebase app with the created credential
        firebase_admin.initialize_app(cred,
                                      {
                                          'storageBucket': 'gs://elmento-eng.appspot.com'
                                      }
                                      )

# Call the function to initialize the app
initialize_firebase_app()

st.title('Hi there, I am :blue[Elmento AI]!')

if 'username' not in st.session_state:
    st.session_state.username = ''

if 'useremail' not in st.session_state:
    st.session_state.useremail = ''

def f():
    try:
        user = auth.get_user_by_email(email)
        print(user.uid)

        st.success('Successfully logged in!')

        st.session_state.username = user.uid
        st.session_state.useremail = user.email

        st.session_state.signout = True
        st.session_state.signedout = True
        st.session_state['logged_in'] = True
    except:
        st.warning('Log in error')

# sign out function
def t():
    st.session_state.signout = False
    st.session_state.signedout = False
    st.session_state.username = ''

if 'signedout' not in st.session_state:
    st.session_state.signedout = False
if 'signout' not in st.session_state:
    st.session_state.signout = False

if not st.session_state['signedout']:
    db = firestore.client()
    st.session_state.db = db
    docs = db.collection('users').get()

    choice = st.selectbox('Login/Register', ['Login', 'Register'])

    if choice == 'Login':
        email = st.text_input('Email')
        password = st.text_input('Password', type='password')
        st.button('Login', on_click=f)

    else:
        email = st.text_input('Email')
        password = st.text_input('Password', type='password')

        username = st.text_input('Please enter your unqiue username.')

        if st.button('Create an account'):
            user = auth.create_user(email=email, password=password)

            doc_ref = db.collection('users').document(user.uid)
            doc_ref.set({
                'uid': user.uid,
                'email': email,
            })

            st.success('Account successfully created!')
            st.markdown('Please login or register to view this page.')
            st.balloons()

if 'logged_in' in st.session_state and st.session_state.logged_in:
    st.write(st.session_state.useremail)

