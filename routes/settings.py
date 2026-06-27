from flask import Blueprint, redirect, url_for


settings_bp = Blueprint("settings", __name__, url_prefix="/settings")


@settings_bp.get("/")
def settings():
    return redirect(url_for("home.index"))
