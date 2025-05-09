#!/usr/bin/python
# -*- encoding: utf-8 -*-
# File    :   Joule_calculator.py
# Time    :   2025/05/05 20:43:16
# Author  :   Hsu, Liang-Yi 
# Email:   yi75798@gmail.com
# Description : Airsoft Joule Calculator

from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__, static_url_path="/")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calculate", methods=['GET'])
def cal_J():
  # Get values from user
  mm = float(request.args.get('mm'))
  weight = float(request.args.get('weight'))
  velocity = float(request.args.get('velocity'))
  cm2 = (((mm * 0.1)/2)**2)*3.1416
  
  # Calculate Joule
  res_J = round(weight*0.001 * ((velocity**2)/2), 3)
  
  # Calculate Joule/cm2
  try:
    res_Jcm2 = round(res_J/cm2, 3)
  except ZeroDivisionError:
    res_Jcm2 = "Infinity"

  # Calculate FPS
  res_fps = round(velocity * 3.280839895, 3)

  # Calculate diff V to J
  # V = (2J / 0.001w)^0.5
  res_2 = round(((2 * res_J)/(0.001 * 0.2))**0.5, 1)
  res_25 = round(((2 * res_J)/(0.001 * 0.25))**0.5, 1)
  res_3 = round(((2 * res_J)/(0.001 * 0.3))**0.5, 1)
  res_36 = round(((2 * res_J)/(0.001 * 0.36))**0.5, 1)
  res_4 = round(((2 * res_J)/(0.001 * 0.4))**0.5, 1)

  return render_template('index.html', res_J=res_J,
                         res_Jcm2=res_Jcm2,
                         res_fps=res_fps,
                         res_2=res_2,
                         res_25=res_25,
                         res_3=res_3,
                         res_36=res_36,
                         res_4=res_4,
                         mm = request.args.get('mm', 0, type=float),
                         weight = request.args.get('weight', 0, type=float),
                         velocity = request.args.get('velocity', 0, type=float))

app.run(host="0.0.0.0", port=10000)
