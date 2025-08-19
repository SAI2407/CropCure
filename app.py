from flask import Flask, render_template, request
from predict import predict
import os
from Transformation import transformation

app = Flask(__name__)
# Path of uploads folder
UPLOAD_FOLDER = os.path.join("static", "uploads")
# Makes upload folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["image"]
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filepath)
        # Call prediction function here
        img_model = transformation(filepath , device = "cpu")
        result = predict(img_model)

        return render_template("index.html", prediction=result, image=file.filename)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug= False , host = "0.0.0.0" , port = 7860)



