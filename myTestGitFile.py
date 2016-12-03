# from flask import Flask
#
# app = Flask(__name__)
#
# @app.route("/lrs1/")
# def hello_1():
#     return "hi,lrs1! i am smart ET , you are fool @ yuan zhi ^_^^_^^_^"
#
# @app.route("/lrs2/")
# def hello_2():
#     return "hi,lrs2! i am smart ET , you are fool @ yuan zhi ^_^^_^^_^"
#
# if __name__ == "__main__":
#     app.run()

# from flask import Flask, render_template
# from flask_socketio import SocketIO, emit
# # from flask.ext.socketio import SocketIO
#
# app = Flask(__name__)
# # app.config['SECRET_KEY'] = 'secret'
# socketio = SocketIO(app)
#
# @app.route('/')
# def index():
#     return "i am ok,thank you !"
#
# @socketio.on('my event', namespace='/test')
# def handle_my_custom_event(message):
#     print 'receive'
#
# if __name__ == '__main__':
#     socketio.run(app)


from flask import Flask, render_template, request
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'so hard'
socketio = SocketIO(app)

stores = set()


@app.route('/')
def hello_world():
    print(request.headers)
    return 'hi i am here !!!'
    # return render_template('index.html')


@socketio.on('connect')
def connect():
    stores.add(request)
    print 'ccccc'
    print(request.headers)
    print('clinet', len(stores))


@socketio.on('message')
def handle_message(message):
    print('recive message:', message)
    print 'eeeee'

if __name__ == '__main__':
    app.debug = False
    socketio.run(app, host='0.0.0.0',port=8000)


# import socket
#
# def main():
#     s = socket.socket()
#     host = socket.gethostname()
#     # host = ''
#     port = 8000
#     s.bind((host,port))
#     s.listen(5)
#     while True:
#         c, addr = s.accept()
#         print 'connet_addr:', addr
#         server_send = "welcome learn net programming"
#         c.send(server_send)
#
#         server_recv = c.recv(1024)
#         print "server_recv:", server_recv
#
#         if server_recv == "close":
#             c.close()
#             break
#         else:
#             c.send(server_recv)
#
# if __name__ == '__main__':
#     main()




