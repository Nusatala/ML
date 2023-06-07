from werkzeug.utils import secure_filename
from flask import Flask, request, jsonify
import numpy as np
import os
import tensorflow as tf
from tensorflow import keras
# from tensorflow.keras.preprocessing import image
from PIL import Image


UPLOAD_FOLDER = os.environ['APP_HOME']

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)

model = keras.models.load_model("./nusatala.h5", compile=False)


def prediksi_gambar(image_upload, model=model):
    im = image_upload
    im = np.asarray(im)
    im = im*(1/225)
    im_input = tf.reshape(im, shape=[1, 256, 256, 3])

    Y_pred = sorted(model.predict(im_input)[0])[2]
    y_pred = np.argmax(model.predict(im_input))

    if y_pred == 0:
        label = 'Bonang'
    elif y_pred == 1:
        label = 'Kolintang'
    elif y_pred == 2:
        label = 'Rebab'
    elif y_pred == 3:
        label = 'Saluang'
    elif y_pred == 4:
        label = 'Sape'
    elif y_pred == 5:
        label = 'Sasando'
    else:
        label = 'Tifa'

    return label


app = Flask(__name__)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files.get("file")
        if file is None or file.filename == "":
            return jsonify({"error": "no file"})
        try:
            if allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(UPLOAD_FOLDER, filename))
                filepath = os.path.join(UPLOAD_FOLDER, filename)
                img = tf.keras.utils.load_img(
                    filepath, target_size=(256, 256))
                label = prediksi_gambar(img)
                return jsonify({"prediksi": label})
        except Exception as e:
            return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(debug=True)
