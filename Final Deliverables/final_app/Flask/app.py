from flask import Flask, render_template, request, redirect
#
import numpy as np

#
# from tensorflow.k
from keras.saving.save import load_model

app = Flask(__name__,template_folder='template')


@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')


@app.route('/predict.html', methods=["POST", "GET"])
@app.route('/method', methods=["POST", "GET"])
def method():
    if request.method == "POST":
        string = request.form['val']
        string = string.split(',')
        temp_input = [eval(i) for i in string]

        x_input = np.zeros(shape=(1, 10))
        x_input.shape

        lst_output = []
        n_steps = 10
        i = 0
        while (i < 10):
            if (len(temp_input) > 10):
                x_input = np.array(temp_input[1:])
                x_input = x_input.reshape(1, -1)
                x_input = x_input.reshape((1, n_steps, 1))
                yhat = model.predict(x_input, verbose=0)
                temp_input.extend(yhat[0].tolist())
                temp_input = temp_input[1:]
                lst_output.extend(yhat.tolist())
                i = i + 1

            else:
                x_input = x_input.reshape((1, n_steps, 1))
                yhat = model.predict(x_input, verbose=0)
                temp_input.extend(yhat[0].tolist())
                lst_output.extend(yhat.tolist())
                i = i + 1
        val = lst_output[9]
        return render_template('predict.html', prediction=val)
    if request.method == "GET":
        return render_template('predict.html')


if __name__ == "__main__":
    model = load_model(r'C:\Users\akash\Desktop\IBM-python app\IBM-Project-8197-1664354492\Project Development Phase\Sprint 3\crude_oil.h5')
    app.run(debug=True)