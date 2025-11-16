import os
import sys

from jinja2 import FileSystemLoader, Environment


def evaluate(playlist: str):
    from google import genai

    # Configure your API key. It's recommended to store this as an environment variable (e.g., GEMINI_API_KEY)
    # and let the client automatically pick it up, rather than hardcoding it.
    # genai.configure(api_key='YOUR_API_KEY') # Uncomment and replace with your actual API key if not using environment variables

    # Initialize the Gemini client
    api_key = os.environ.get('GEMINI_API_KEY')
    client = genai.Client(api_key=api_key)

    # Specify the model you want to use
    # Examples include "gemini-2.5-flash", "gemini-2.0-flash", "gemini-1.5-pro", etc.
    model_name = "gemini-2.5-flash"

    # Define the content to send to the model
    file_loader = FileSystemLoader('templates') # 'templates' is the directory name
    env = Environment(loader=file_loader)
    template = env.get_template('prompt.template')
    data = {"playlist": playlist}
    prompt_text = template.render(data)
    print(prompt_text)

    # Generate content using the specified model and prompt
    response = client.models.generate_content(
        model=model_name,
        contents=prompt_text
    )

    # Print the generated text
    print(response.text)

    return response.text


if __name__ == '__main__':
    playlist = '["1. Api by Odiseo","2. Is by Vlasta Marek","3. All I Want by LCD Soundsystem","4. Endpoints by Glenn Horiuchi","5. You Are So Beautiful by Zucchero"]'
    evaluate(playlist)
