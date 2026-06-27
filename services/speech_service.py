from gtts import gTTS


def create_speech_file(text, language, output_path):
    if not text or not text.strip():
        raise ValueError("Enter text before creating speech.")
    tts = gTTS(text=text.strip(), lang=(language or "en").split("-")[0])
    tts.save(str(output_path))
    return output_path
