# import the necessary packages
import json
import os
import random

import cv2 as cv
import keras.backend as K
import numpy as np
import scipy.io

from utils import load_model

car_model = None

def load_model(model_path):
    car_model = load_model(model_path)
    car_model.load_weights(model_path)
    cars_meta = scipy.io.loadmat('devkit/cars_meta')
    class_names = cars_meta['class_names']  # shape=(1, 196)
    class_names = np.transpose(class_names)

def recognize_vehicle(img_path):
    # process image and predict model
    img_width, img_height = 224, 224
    bgr_img = cv.imread(img_path)
    bgr_img = cv.resize(bgr_img, (img_width, img_height), cv.INTER_CUBIC)
    rgb_img = cv.cvtColor(bgr_img, cv.COLOR_BGR2RGB)
    rgb_img = np.expand_dims(rgb_img, 0)
    preds = car_model.predict(rgb_img)
    prob = np.max(preds)
    class_id = np.argmax(preds)
    text = ('Predict: {}, prob: {}'.format(class_names[class_id][0][0], prob))
    return class_names[class_id][0][0]

def clear_session():
    K.clear_session()


load_model('model.96-0.89.hdf5')
recognize_vehicle('car2.jpeg')
clear_session()