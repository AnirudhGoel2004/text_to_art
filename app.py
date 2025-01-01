from flask import Flask, render_template, request, send_from_directory
import os
from generator import generate_image

app = Flask(__name__)
UPLOAD_FOLDER = 'static'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        prompt = request.form["prompt"]
        image = generate_image(prompt)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], "generated_image.png")
        image.save(filepath)
        return render_template("index.html", image_path=filepath)
    return render_template("index.html", image_path=None)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

