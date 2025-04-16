import os
from dotenv import load_dotenv  # <-- Load environment variables from .env
import google.generativeai as genai

# Load .env file from project root
load_dotenv()

# Configure Gemini with the API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_readme_from_file_list(file_list, repo_url):
    prompt = f"""
    Generate a professional README.md for a public GitHub repository. 
    The repository is located at: {repo_url}

    The file structure is as follows:
    {chr(10).join(f'- {file}' for file in file_list)}

    Include project description, features, setup instructions (if possible), and usage examples.
    """

    model = genai.GenerativeModel('gemini-1.5-pro-latest')
    response = model.generate_content(prompt)
    with open('README.md', 'w') as file:
        file.write(response.text)

    return response.text