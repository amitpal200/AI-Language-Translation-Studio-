from flask import Blueprint, Response, redirect, render_template, request, url_for

from services.export_service import history_to_csv
from services.history_service import clear_history, recent_history


history_bp = Blueprint("history", __name__, url_prefix="/history")


@history_bp.get("/")
def history():
    return render_template("history.html", history=recent_history(100))


@history_bp.post("/clear")
def clear():
    clear_history()
    return redirect(url_for("history.history"))


@history_bp.get("/export.csv")
def export_csv():
    csv_data = history_to_csv(recent_history(1000))
    return Response(
        csv_data,
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment; filename=translation-history.csv"},
    )


@history_bp.post("/export.txt")
def export_txt():
    source_text = request.form.get("source_text", "").strip()
    translated_text = request.form.get("translated_text", "").strip()
    content = f"Source:\n{source_text}\n\nTranslation:\n{translated_text}\n"
    return Response(
        content,
        mimetype="text/plain",
        headers={"Content-Disposition": "attachment; filename=translation.txt"},
    )
