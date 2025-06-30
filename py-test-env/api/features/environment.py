import threading
import time
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import app

SERVER_THREAD = None

def before_all(context):
    global SERVER_THREAD
    SERVER_THREAD = threading.Thread(target=lambda: app.run(host='0.0.0.0', port=1666))
    SERVER_THREAD.daemon = True
    SERVER_THREAD.start()
    time.sleep(1)

def after_all(context):
    pass
