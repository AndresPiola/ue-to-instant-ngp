import json
import socket
import threading
import sys
from PIL import Image
import io

import cv2
import numpy as np

json_obj = {
    "fov": 90, "camera_origin": [0.5, 0.5, 0.5],  "direction": [0.154, -0.219, -0.964], "nerf_scale": 2}

# Wait for incoming data from server
# .decode is used to turn the message in bytes to a string


def receive(socket, signal):
    while signal:
        try:
            data = socket.recv(32)
            print(str(data.decode("utf-8")))
        except:
            print("You have been disconnected from the server")
            signal = False
            break


server_address = ('localhost', 27015)
# Attempt connection to server
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(server_address)
except:
    print("Could not make a connection to the server")
    input("Press enter to quit")
    sys.exit(0)

# Create new thread to wait for data
receiveThread = threading.Thread(target=receive, args=(sock, True))
receiveThread.start()
json_data = json.dumps(json_obj, sort_keys=False, indent=2)

sock.sendall(json_data.encode())
while True:
    data = sock.recv(512)
    if (len(data) < 1):
        break
    image = np.asarray(data, dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    cv2.imwrite("image.png", image)
    print('Received', repr(data))
