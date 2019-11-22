

from __future__    import print_function

# [START gae_flex_websockets_app]
import google.api_core.exceptions

from flask         import Flask, render_template
from flask_sockets import Sockets
#from google.cloud  import firestore


app = Flask(__name__)
app.config['DEBUG'] = True
sockets = Sockets(app)


@sockets.route('/chat')
def chat_socket(ws):
    while not ws.closed:
        message = ws.receive()
        if message is None:  # message is "None" if the client has closed.
            continue
        # Send the message to all clients connected to this webserver
        # process. (To support multiple processes or instances, an
        # extra-instance storage or messaging system would be required.)
        clients = ws.handler.server.clients.values()
        for client in clients:
            client.ws.send(message)
# [END gae_flex_websockets_app]


@app.route('/')
def index():
    return render_template('index.html')


def quickstart_new_instance():
    # [START quickstart_new_instance]
    # Project ID is determined by the GCLOUD_PROJECT environment variable
    db = firestore.Client()
    # [END quickstart_new_instance]

    return db


def quickstart_add_data_one():
    db = firestore.Client()
    # [START quickstart_add_data_one]
    doc_ref = db.collection(u'users').document(u'alovelace')
    doc_ref.set({
        u'user_id': 0,
        u'nickname':  u'Hosoi',
        u'room':  0
    })
    # [END quickstart_add_data_one]


if __name__ == '__main__':
    print("""
This can not be run directly because the Flask development server does not
support web sockets. Instead, use gunicorn:

gunicorn -b 127.0.0.1:8080 -k flask_sockets.worker main:app

""")
