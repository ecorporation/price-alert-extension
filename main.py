from flask import Flask, redirect, url_for, render_template, request
import MetaTrader5 as mt5
import time

app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def index():
    if(request.method == "POST"):
        symbol = request.form["symbol"]
        price = request.form["price"]
        try:
            cp = mt5.symbol_info_tick(symbol)._asdict()['ask']
            alert()
            return render_template("index.html", symbol=symbol, cp=cp)
        except:
            print(f"Error downloading data for {symbol}...")
        return render_template("index.html", symbol=symbol, cp="N/A")
    else:
        mt5.initialize()
        return render_template("index.html")

async def alert():
    while(True):
        '''
            NOT IMPLEMENTED YET
        '''
        time.sleep(10)
        
if __name__ == '__main__':
    app.run(debug=True, port=80)