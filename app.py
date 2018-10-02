# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 09:59:43 2018

@author: WillRoyero
"""

from flask import Flask, jsonify, request
from sklearn.externals import joblib
import sklearn


app= Flask(__name__)

@app.route("/")
def home():
    return "La página está funcionando bien"

if __name__=='__main__':
    app.run()