from flask import Blueprint, flash, redirect, render_template, request, url_for

from services.history_service import add_history, recent_history
from services.language_detector import guess_language
from services.translator_service import LANGUAGES, TranslationError, translate_text


translate_bp = Blueprint("translate", __name__)


@translate_bp.post("/translate")
def translate():
    source_text = request.form.get("source_text", "")
    source_language = request.form.get("source_language") or "auto"
    target_language = request.form.get("target_language") or "hi"
    if source_language == "auto":
        source_language = guess_language(source_text)

    try:
        translated = translate_text(source_text, target_language, source_language)
        add_history(source_text.strip(), translated, source_language, target_language)
        result = translated
    except TranslationError as exc:
        flash(str(exc), "error")
        result = None

    return render_template(
        "index.html",
        languages=LANGUAGES,
        history=recent_history(10),
        result=result,
        source_text=source_text,
        source_language=source_language,
        target_language=target_language,
    )


@translate_bp.get("/translate")
def translate_get():
    return redirect(url_for("home.index"))
