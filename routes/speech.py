from datetime import datetime

from flask import Blueprint, current_app, flash, redirect, request, send_file, url_for

from services.speech_service import create_speech_file


speech_bp = Blueprint("speech", __name__, url_prefix="/speech")


@speech_bp.post("/")
def speech():
    text = request.form.get("text", "")
    language = request.form.get("language", "en")
    filename = f"speech-{datetime.utcnow().strftime('%Y%m%d%H%M%S')}.mp3"
    output_path = current_app.config["DOWNLOAD_FOLDER"] / filename
    try:
        create_speech_file(text, language, output_path)
    except Exception as exc:
        flash(str(exc), "error")
        return redirect(url_for("home.index"))
    return send_file(output_path, as_attachment=True, download_name=filename)
