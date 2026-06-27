from flask import Blueprint, jsonify, request

from services.history_service import add_history, recent_history
from services.language_detector import guess_language
from services.translator_service import LANGUAGES, TranslationError, translate_text


api_bp = Blueprint("api", __name__)


@api_bp.get("/languages")
def languages():
    return jsonify(LANGUAGES)


@api_bp.get("/history")
def history():
    return jsonify([item.to_dict() for item in recent_history(50)])


@api_bp.post("/translate")
def translate_api():
    payload = request.get_json(silent=True) or {}
    source_text = payload.get("text", "")
    source_language = payload.get("source_language") or "auto"
    target_language = payload.get("target_language") or "hi"
    if source_language == "auto":
        source_language = guess_language(source_text)

    try:
        translated = translate_text(source_text, target_language, source_language)
    except TranslationError as exc:
        return jsonify({"error": str(exc)}), 400

    item = add_history(source_text.strip(), translated, source_language, target_language)
    return jsonify(
        {
            "translation": translated,
            "source_language": source_language,
            "target_language": target_language,
            "history_id": item.id,
        }
    )
