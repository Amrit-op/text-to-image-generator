# Text-to-Image Generator
🚀 Project Overview

The Text-to-Image Generator is a web application built using Streamlit and the Hugging Face API. It allows users to generate stunning AI-generated images from textual descriptions using various pre-trained models.

## 🌟 Features
- **Model Selection**: Users can choose between multiple pre-trained models like FLUX.1, Stable Diffusion, and RealVisXL for image generation.

- **Interactive UI**: A responsive and user-friendly interface with real-time progress updates.

- **Download Feature**: Option to download the generated images for personal use.

- **Customizable Themes**: Includes a neon-inspired dark theme for an enhanced visual experience.

- **Markdown Formatting**: Instructions are clearly displayed using Markdown for better readability.

- **Footer Section**: A personalized footer with credits and useful links.

## 🛠️ Tech Stack
- **Streamlit**: For building the interactive web application.

- **Hugging Face API**: For text-to-image generation using pre-trained models.

- **Python**: Core programming language for functionality.

- **Pillow (PIL)**: For image handling and processing.

- **dotenv**: For securely managing API keys

## 📋 Setup Instructions

**1. Clone the Repository**

```
git clone https://github.com/your-username/text-to-image-generator.git  
cd text-to-image-generator  

```

**2. Install Required Packages**
```
pip install -r requirements.txt  
```

**3. Add Your Hugging Face API Key**
- Create a `.env` file in the root directory and add your Hugging Face API token:
```
HUGGINGFACE_API_TOKEN=your_api_token_here  
```

**4. Run the Application**
```
streamlit run app.py  
```



## 📂 Project Structure

```python
📦 text-to-image-generator  
 ┣ 📜 app.py          # Main application script  
 ┣ 📜 requirements.txt # Dependencies  
 ┣ 📜 .env.example     # Example environment file for API key  
 ┣ 📜 README.md        # Project documentation  
 ┗ 📂 images           # (Optional) For storing generated images  
```
## 📷 Models Integrated

[FLUX.1](black-forest-labs/FLUX.1-dev)

[Stable Diffusion](stabilityai/stable-diffusion-xl-base-1.0)

[RealVisXL](SG161222/RealVisXL_V4.0)

# 📝 Future Enhancements

- Integrate more models for diverse image generation.

- Add the ability to customize image resolution and other parameters.

- Implement user authentication for personalized usage.

# ❤️ Acknowledgements

- Streamlit: For the incredible framework.

- Hugging Face: For providing the models and API

## 📜 License
This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License
