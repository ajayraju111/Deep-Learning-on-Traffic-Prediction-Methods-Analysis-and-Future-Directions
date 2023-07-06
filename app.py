from keras.models import load_model
from flask import Flask, render_template, request


app=Flask(__name__)

model = load_model('AAR_model.h5')

@app.route("/")
def predict():
    return render_template("index.html")


@app.route("/output", methods=[ "GET" ] )
def dia():
    x1 = request.args.get("1")
    x2 = request.args.get("2")
    x3 = request.args.get("3")
    x4 = request.args.get("4")
    x5 = request.args.get("5")
    x6 = request.args.get("6")
    x7 = request.args.get("7")
   
    output = model.predict([[ int(x1), int(x2), int(x3), int(x4), int(x5), int(x6), int(x7) ]])
    final = (round(output[0][0]))
    if final == 0:
        result = 'The Traffic is Busy!'
        return render_template("result.html", pred = result)
    elif final == 1:
        result = 'The Traffic is Heavy!'
        return render_template("result.html", pred = result)
    elif final == 2:
        result = 'The Traffic is Moving On/Move ON !'
        return render_template("result.html", pred = result)
    elif final == 3:
        result = 'The Traffic is Normal!'
        return render_template("result.html", pred = result)
    elif final == 4:
        result = 'The Traffic is Worst!'
        return render_template("result.html", pred = result)
        
    else:
        result = 'Invaild Data!'
        return render_template("result.html", pred = result)


if __name__ == "__main__":
    app.run(debug=True)
