from flask import Flask , render_template, request

import carprice as cp

app = Flask(__name__)

@app.route("/", methods = ['GET','POST'])
def price():
    global mp
    mp = []
    if request.method == "POST":
        lent = request.form['len']
        wid = request.form['wid']
        hrp = request.form['hrp']
        cuw = request.form['cuw']
        eng = request.form['eng']
        hiw = request.form['hiw']
        mp = cp.price_predict([lent,wid,hrp,cuw,eng,hiw])
    else:
        print(0)
    return render_template("index.html", my_price = mp)

if __name__ == "__main__":
    app.run(debug=True)
