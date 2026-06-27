from deep_translator import GoogleTranslator


LANGUAGES = {
    "auto": "Auto detect",
    "en": "English",
    "es": "Spanish",
    "fr": "French",
    "de": "German",
    "hi": "Hindi",
    "it": "Italian",
    "ja": "Japanese",
    "ko": "Korean",
    "pt": "Portuguese",
    "ru": "Russian",
    "zh-CN": "Chinese (Simplified)",
}


OFFLINE_TRANSLATIONS = {
    ("hello", "hi"): "\u0928\u092e\u0938\u094d\u0924\u0947",
    ("hello", "es"): "hola",
    ("hello", "fr"): "bonjour",
    ("hello", "de"): "hallo",
    ("thank you", "hi"): "\u0927\u0928\u094d\u092f\u0935\u093e\u0926",
    ("thank you", "es"): "gracias",
    ("good morning", "hi"): "\u0938\u0941\u092a\u094d\u0930\u092d\u093e\u0924",
}


class TranslationError(RuntimeError):
    pass


def translate_text(text, target_language, source_language="auto"):
    cleaned = (text or "").strip()
    if not cleaned:
        raise TranslationError("Enter text to translate.")
    if target_language not in LANGUAGES or target_language == "auto":
        raise TranslationError("Choose a valid target language.")

    key = (cleaned.lower(), target_language)
    if key in OFFLINE_TRANSLATIONS:
        return OFFLINE_TRANSLATIONS[key]

    source = source_language if source_language in LANGUAGES else "auto"
    try:
        return GoogleTranslator(source=source, target=target_language).translate(cleaned)
    except Exception as exc:
        raise TranslationError(
            "Translation service is unavailable. Check your internet connection or try a shorter phrase."
        ) from exc
