from flask import Flask, render_template, request, send_from_directory
import os
from dotenv import load_dotenv


load_dotenv()
from services.ai_service import generate_script
from services.tts_service import generate_audio
from services.logging_service import log_request

app = Flask(__name__)

AUDIO_FOLDER = "generated_audio"
os.makedirs(AUDIO_FOLDER, exist_ok=True)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():

    form_data = {
        "age_range": request.form.get("age_range"),
        "mood": request.form.get("mood"),
        "context": request.form.get("context"),
        "style": request.form.get("style"),
        "length": request.form.get("length")
    }

    script = generate_script(form_data)

    audio_filename = generate_audio(script)

    log_request(form_data, audio_filename)

    return render_template(
        "result.html",
        script=script,
        audio_file=audio_filename
    )


@app.route("/audio/<filename>")
def get_audio(filename):
    return send_from_directory(AUDIO_FOLDER, filename)


if __name__ == "__main__":
    app.run(debug=True)