from database.database import db
from database.models import TranslationHistory


def add_history(source_text, translated_text, source_language, target_language):
    item = TranslationHistory(
        source_text=source_text,
        translated_text=translated_text,
        source_language=source_language or "auto",
        target_language=target_language,
    )
    db.session.add(item)
    db.session.commit()
    return item


def recent_history(limit=25):
    return (
        TranslationHistory.query.order_by(TranslationHistory.created_at.desc())
        .limit(limit)
        .all()
    )


def clear_history():
    TranslationHistory.query.delete()
    db.session.commit()
