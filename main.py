import time
import requests
import os
import io
from dotenv import load_dotenv, find_dotenv
from PIL import Image
import streamlit as st

# Load environment variables
load_dotenv(find_dotenv())
HUGGINGFACE_API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")

# Function to generate image from text using Hugging Face API
def text2image(prompt: str, model: str):
    if model == "FLUX.1":
        API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-dev"
    elif model == "Stable-Diffusion":
        API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
    elif model == "RealVisXL":
        API_URL = "https://api-inference.huggingface.co/models/SG161222/RealVisXL_V4.0"
    else:
        st.error("Invalid model selected.")
        return None

    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"}
    payload = {
        "inputs": prompt,
    }

    retries = 5  # Number of retries
    delay = 50   # Delay in seconds between retries

    for attempt in range(retries):
        response = requests.post(API_URL, headers=headers, json=payload)

        if response.status_code == 200:
            # Image generated successfully
            image_bytes = response.content
            image = Image.open(io.BytesIO(image_bytes))
            return image
        elif response.status_code == 503:
            # Model is still loading, wait and retry
            st.write(f"Attempt {attempt+1}/{retries}: Model is still loading, retrying in {delay} seconds...")
            time.sleep(delay)
        else:
            # Handle other errors
            st.error(f"Error: {response.status_code}, {response.text}")
            return None

    st.error("Failed to generate image after several attempts.")
    return None

# Streamlit App Interface
st.set_page_config(page_title="Text-to-Image Generator", page_icon=":art:", layout="wide")  # Set app icon with emoji

# Sidebar for model selection
st.sidebar.title("Settings")
model_choice = st.sidebar.selectbox(
    "Select the model to generate images:",
    ("FLUX.1", "Stable-Diffusion", "RealVisXL")
)

# Markdown instructions
st.markdown("""
    # Welcome to the **Text-to-Image Generator**!
    This app allows you to generate images from text using advanced AI models.

    ## How to use:
    1. Choose a model from the **Settings** sidebar.
    2. Enter a text prompt.
    3. Press **Enter** or click the button below to generate the image.

    _Note: Please be patient while the image is being generated._
""")

# Input prompt from the user
prompt = st.text_input("Enter a text prompt:", placeholder="A smiley face...")

# Progress bar
progress_bar = st.empty()

if prompt.strip():
    st.write("Generating image...")
    # Start progress bar
    with progress_bar:
        progress = st.progress(0)
        for i in range(100):
            time.sleep(5)  # Simulate some delay for the progress bar
            progress.progress(i + 1)
    
    # Generate image once progress bar finishes
    generated_image = text2image(prompt, model_choice)
    if generated_image:
        # Display the generated image
        st.image(generated_image, caption="Generated Image", use_container_width=True)

        # Save the image to a BytesIO object for download
        img_byte_arr = io.BytesIO()
        generated_image.save(img_byte_arr, format="PNG")
        img_byte_arr.seek(0)

        # Add the download button
        st.download_button(
            label="Download Image",
            data=img_byte_arr,
            file_name="generated_image.png",
            mime="image/png"
        )

    else:
        st.write("Failed to generate the image. Please try again later.")
else:
    st.warning("Please enter a valid text prompt.")

# Footer Section
st.markdown("---")
st.markdown("""
    <footer style="text-align:center; padding: 10px;">
        <p>Created with ❤️ by Amrit, Powered by Streamlit and Hugging Face.</p>
        <p><a href="https://huggingface.co">Visit Hugging Face for more models</a></p>
    </footer>
""", unsafe_allow_html=True)
