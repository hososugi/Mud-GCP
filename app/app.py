

from __future__    import print_function
from flask         import Flask, render_template
from flask_sockets import Sockets


class CustomFlask(Flask):
    def run(self, host=None, port=None, debug=None, load_dotenv=True, **options):
        with self.app_context():
            load_data()

        super(CustomFlask, self).run(host=host, port=port, debug=debug, load_dotenv=load_dotenv, **options)


app = CustomFlask(__name__)
app.config['DEBUG'] = True
sockets = Sockets(app)


def load_data():
    print("INFO: Loading data.")


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


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    print("""
This can not be run directly because the Flask development server does not
support web sockets. Instead, use gunicorn:

gunicorn -b 127.0.0.1:8080 -k flask_sockets.worker main:app

""")
