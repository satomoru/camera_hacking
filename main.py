# satomoru
from flask import Flask
from flask import request
from flask import render_template
import base64
import cv2
import numpy as np
import threading

app = Flask(__name__)

def update(frame):
  cv2.imshow('satomoru', frame)
  cv2.waitKey()

@app.route('/stream', methods=['POST'])
def stalk():
  img_str = request.form.get('frame').split('data:image/png;base64,')[-1]
  
  img_byt = base64.b64decode(img_str)
  
  image = np.fromstring(img_byt, np.uint8)
  
  frame = cv2.imdecode(image, cv2.IMREAD_COLOR)
  
  display_thread = threading.Thread(target=update, args=(frame,))
  display_thread.start()
  
  return ''

@app.route('/')
def index():
  return render_template_string()

if __name__ == '__main__':
 
  app.run(debug=True, threaded=True)