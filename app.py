import json
import pandas as pd
import yfinance as yf
from flask import Flask, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config['CORS HEADERS'] = 'Content Type'

#homepage
@app.route("/")
def hello_world():
    return "<p>Stock Research API for ZeroBizz Research Console<br>Developed by Souvik Paul</p>"

#live ticker api
@app.route('/live', methods=['GET'])
@cross_origin()
def tickerlive():
    name = request.args.get('ticker')
    ticker = yf.Ticker(name)
    return ticker.info

#ticker history api
@app.route('/history', methods=['GET'])
@cross_origin()
def tickerhistory():
    name = request.args.get('ticker')
    duration = request.args.get('duration')
    
    ticker = yf.Ticker(name)
    history = ticker.history(period=duration)
    dataToJson = history.to_json(orient = 'table')
    
    return dataToJson

#ticker intraday api
@app.route('/intraday', methods=['GET'])
@cross_origin()
def tickerinterval():
    name = request.args.get('ticker')
    duration = request.args.get('duration')
    interval = request.args.get('interval')
    
    ticker = yf.Ticker(name)
    history = ticker.history(period=duration, interval=interval)
    dataToJson = history.to_json(orient = 'table')
    
    return dataToJson

#ticker balance sheet api
@app.route('/balance-sheet', methods=['GET'])
@cross_origin()
def tickerbalancesheet():
    name = request.args.get('ticker')
    
    ticker = yf.Ticker(name)
    balance_sheet = ticker.balance_sheet
    dataToJson = balance_sheet.to_json(orient = 'table')
    
    return dataToJson

if __name__ == "__main__":
	app.run(debug=True, port=5000)