# AI Language Translation Studio

A Flask-based AI Language Translation Studio for translating text, saving translation history, exporting results, and generating speech audio.

## Run locally

```powershell
venv\Scripts\python.exe run.py
```

Open http://127.0.0.1:5000 in your browser.

## API

Translate text:

```powershell
Invoke-RestMethod -Method Post -Uri http://127.0.0.1:5000/api/translate -ContentType "application/json" -Body '{"text":"hello","target_language":"hi"}'
```

List supported languages:

```powershell
Invoke-RestMethod http://127.0.0.1:5000/api/languages
```

## Notes

Most translations use `deep-translator`, so they need internet access. A few tiny offline examples are included so the app can still be smoke-tested without network access.
