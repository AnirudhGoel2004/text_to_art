import torch
from diffusers import StableDiffusionPipeline

# Initialize the Stable Diffusion pipeline
def load_pipeline():
    pipeline = StableDiffusionPipeline.from_pretrained(
        "runwayml/stable-diffusion-v1-5",
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
    )
    device = "cuda" if torch.cuda.is_available() else "cpu"
    pipeline = pipeline.to(device)
    return pipeline

# Generate an image based on text input
def generate_image(prompt):
    pipeline = load_pipeline()
    image = pipeline(prompt).images[0]
    return image
