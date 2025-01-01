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
**Generated Output**: 
Whisper of the Horizon

The sun descends, a gilded crown,
Adorning waves in amber gown.
The ocean sighs, its breath so deep,
A tranquil song that bids the day to sleep.

Clouds blush soft in twilight's glow,
As winds embrace the ebb and flow.
Each ripple hums a secret tune,
While sky and sea merge under the moon.

Golden paths on waters glide,
Drawing hearts to the horizon's side.
A moment held in fleeting grace,
The endless ocean, time's embrace.

Whisper now, oh gentle night,
Guard this peace 'til morning light.
For in this sunset's gentle gleam,
The world finds solace, and dares to dream.
