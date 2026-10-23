# Image Caption Generator Using BLIP and LSTM

## Project Description

The **Image Caption Generator** is a deep learning-based web application that automatically generates meaningful textual descriptions of images. It combines computer vision and natural language processing (NLP) to help computers understand visual content and describe it in human-readable language.

The application is developed using **Python, Flask, HTML, CSS, and JavaScript**. Users can upload an image through an interactive web interface and receive an automatically generated caption. The Flask backend processes the image using a pretrained BLIP model, and the generated description is displayed dynamically on the webpage.

The project explores **BLIP (Bootstrapping Language-Image Pre-training)** and **LSTM (Long Short-Term Memory)** concepts. BLIP is a pretrained vision-language model used for image caption generation, while LSTM is a recurrent neural network architecture that can generate text sequences word by word. The initial implementation uses BLIP for caption generation, with LSTM intended as an additional training component.

The **Flickr8k dataset**, available through Kaggle, provides images and human-written captions for training and evaluation experiments. A small subset can be selected to simplify experimentation and reduce computational requirements.

## Technologies Used

- Frontend: HTML, CSS, JavaScript
- Backend: Python and Flask
- Deep Learning: PyTorch and Hugging Face Transformers
- Models: BLIP and LSTM
- Dataset: Flickr8k
- Tools: VS Code, Git, and GitHub

## Project Setup

**1. Clone the repository**

```bash
git clone <your-repository-url>
cd image_caption_generator
```

**2. Create a virtual environment**

```bash
python -m venv venv
venv\Scripts\activate
```

**3. Install dependencies**

Create a `requirements.txt` file containing Flask, Pillow, torch, and `transformers==4.44.2`, then run:

```bash
python -m pip install -r requirements.txt
```

**4. Download the dataset**

Download Flickr8k from Kaggle and optionally select a small subset of images and captions for experiments.

**5. Run the application**

```bash
python app.py
```

Open `http://127.0.0.1:5000` in your browser. The pretrained BLIP model downloads automatically when first loaded, requiring an internet connection.

## Key Features

- Image upload and preview.
- Automatic caption generation using BLIP.
- Interactive web interface.
- Flask-based backend integration.
- Support for future LSTM training and evaluation.

## Applications

The system can support accessibility for visually impaired users, automated image descriptions, image indexing, digital content management, and educational applications.

This project demonstrates the practical integration of deep learning and web development to build an intelligent image captioning system, with scope for future improvements in caption quality and custom LSTM integration.

**Note:** The current implementation uses pretrained BLIP. LSTM must be implemented and trained separately before it can be described as a working component.
