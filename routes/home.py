from flask import Blueprint, render_template

from services.history_service import recent_history
from services.translator_service import LANGUAGES


home_bp = Blueprint("home", __name__)


@home_bp.get("/")
def index():
    return render_template(
        "index.html",
        languages=LANGUAGES,
        history=recent_history(10),
        result=None,
        source_text="",
        source_language="auto",
        target_language="hi",
    )
