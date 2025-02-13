from flask import Flask, render_template, request
import openai
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


def get_jungian_analysis(dream_text):
    try:
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "developer", "content": """You are an expert Jungian analyst specializing in dream interpretation. 
                Analyze dreams in these sections:
                1. Key Symbols & Their Meanings
                2. Present Archetypes (Shadow, Anima/Animus, Self, etc.)
                3. Message from the Unconscious
                4. Suggested Actions

                Keep the analysis clear and insightful."""},
                {"role": "user", "content": f"Analyze this dream:\n{dream_text}"}
            ],
            temperature=1.2,
            max_tokens=800
        )

        # Generate DALL-E image prompt based on dream
        image_prompt_response = openai.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system",
                 "content": "Create a surreal, artistic DALL-E prompt based on the dream's key elements. Make it vivid and dreamlike."},
                {"role": "user", "content": f"Create an artistic image prompt for this dream:\n{dream_text}"}
            ],
            temperature=0.9,
            max_tokens=200
        )

        image_prompt = image_prompt_response.choices[0].message.content

        # Generate image using DALL-E
        image_response = openai.images.generate(
            prompt=image_prompt,
            n=1,
            size="1024x1024",
            quality="standard"
        )

        return {
            "analysis": response.choices[0].message.content,
            "image_url": image_response.data[0].url
        }
    except Exception as e:
        return {
            "analysis": f"Analysis error: {str(e)}",
            "image_url": None
        }


@app.route("/", methods=["GET", "POST"])
def index():
    analysis = None
    image_url = None
    dream_text = None

    if request.method == "POST":
        dream_text = request.form.get("dream_text", "")
        result = get_jungian_analysis(dream_text)
        analysis = result["analysis"]
        image_url = result["image_url"]

    return render_template("index.html",
                           analysis=analysis,
                           image_url=image_url,
                           dream_text=dream_text)


if __name__ == "__main__":
    app.run(debug=True)