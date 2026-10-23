
from flask import Flask, render_template, request, jsonify
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import torch
import os

app = Flask(__name__)

# Upload configuration
UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Load pretrained BLIP model
processor = BlipProcessor.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate_caption():
    if "image" not in request.files:
        return jsonify({"error": "Please upload an image"}), 400

    file = request.files["image"]

    if file.filename == "":
        return jsonify({"error": "No image selected"}), 400

    try:
        image = Image.open(file.stream).convert("RGB")

        # Generate caption
        inputs = processor(images=image, return_tensors="pt")
        inputs = {key: value.to(device)
                  for key, value in inputs.items()}

        with torch.no_grad():
            output = model.generate(**inputs, max_new_tokens=40)

        caption = processor.decode(
            output[0], skip_special_tokens=True
        )

        return jsonify({"caption": caption})

    except Exception as error:
        return jsonify({"error": str(error)}), 500


if __name__ == "__main__":
    app.run(debug=True)
