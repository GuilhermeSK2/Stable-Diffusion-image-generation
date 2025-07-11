!pip install hf_xet

from diffusers import StableDiffusionXLPipeline
import torch
import matplotlib.pyplot as plt

pretrained_model = "stabilityai/stable-diffusion-xl-base-1.0"
prompt = "Sketch drawing of a 90s Formula 1 car"
negative_prompt = "blurry, low quality, graystyle, monochrome, dull, dark"
num_inference_steps = 50
guidence_scale = 7.5
height = 768
width = 768
seed = 42

generator = torch.manual_seed(seed)
pipeline = StableDiffusionXLPipeline.from_pretrained(
    pretrained_model,
    torch_dtype=torch.float16,
    use_safetensor=True
).to("cuda")

image = pipeline(
    prompt = prompt,
    negative_prompt = negative_prompt,
    height = height,
    width = width,
    num_inference_steps = num_inference_steps,
    guidence_scale = guidence_scale,
    generator = generator
).images[0]

plt.imshow(image)
plt.axis("off")
plt.show
