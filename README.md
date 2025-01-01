# AI Text-to-Art Generator

This project uses a generative AI model to create images from textual descriptions. It is built with Python, Flask, and the Stable Diffusion model. The application allows users to input a text prompt and generate corresponding artwork.

## Features

- Generate artwork from text prompts.
- Supports CPU-based inference for macOS and other systems without CUDA-enabled GPUs.
- Lightweight and easy to use.

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd text_to_art
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Download the Stable Diffusion model:
   The model is automatically downloaded when you first run the application.

## Usage

1. Run the Flask app:
   ```bash
   python3 app.py
   ```
2. Open the application in your browser:
   ```
   http://127.0.0.1:5000
   ```
3. Enter a text prompt and generate artwork.

## Dependencies

- Python 3.8+
- Flask
- PyTorch
- Diffusers
- PIL (Pillow)

## Notes

- The application defaults to CPU inference for macOS systems.
- For faster performance, use a system with a CUDA-enabled GPU.

## Example

**Prompt**: "A serene sunset over the ocean"  
**Generated Output**: ![Generated Image](static/example.png)

## License

This project is licensed under the MIT License.
