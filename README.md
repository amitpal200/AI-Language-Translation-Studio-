# AI Language Translation Studio

A fast Flask-based multilingual translation workspace that helps users translate text, keep translation history, export results, and generate speech output from translated content.

## Preview

### Translation workspace

![AI Language Translation Studio workspace](docs/Screenshots/translation-workspace.png)

### English to Hindi output

![Translated Hindi output with source text](docs/Screenshots/translated-output.png)

## Highlights

- Translate text between multiple languages with an easy two-panel workspace.
- Detect source language and translate into the selected target language.
- Copy translated text or download it as a TXT file.
- Generate downloadable speech audio from translated text.
- Keep recent translation history for quick review.
- Extract and translate text from images with OCR upload support.
- Extract and translate text from PDF documents.
- Use speech-to-text translation from uploaded audio.
- Use a grammar correction helper for cleaner writing.
- Export saved translation history as CSV.

## Tech Stack

- Python
- Flask
- Deep Translator
- gTTS and SpeechRecognition
- Tesseract OCR through pytesseract
- HTML, CSS, and JavaScript
- SQLite

## Project Structure

```text
AI-Language-Translation-Studio/
├── app.py
├── run.py
├── config.py
├── database/
├── docs/
│   └── Screenshots/
├── routes/
├── services/
├── static/
├── templates/
├── tests/
└── requirements.txt
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/amitpal200/AI-Language-Translation-Studio-.git
cd AI-Language-Translation-Studio-
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
```

Windows:

```powershell
venv\Scripts\activate
```

macOS/Linux:

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
python run.py
```

Open the app in your browser:

```text
http://127.0.0.1:5000
```

The extra tools page is available at:

```text
http://127.0.0.1:5000/tools/
```

## API Usage

Translate text:

```powershell
Invoke-RestMethod -Method Post -Uri http://127.0.0.1:5000/api/translate -ContentType "application/json" -Body '{"text":"hello","target_language":"hi"}'
```

List supported languages:

```powershell
Invoke-RestMethod http://127.0.0.1:5000/api/languages
```

## Notes

- Most translations use `deep-translator`, so internet access is required for full translation support.
- Speech recognition and text-to-speech features also use online services.
- Image OCR uses `pytesseract`, so the Tesseract OCR engine must be installed on your system.
- A few small offline examples are included so the app can still be smoke-tested without network access.

## Author

Built by [Amit Pal](https://github.com/amitpal200).
