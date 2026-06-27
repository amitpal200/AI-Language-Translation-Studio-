import tempfile
import unittest
from pathlib import Path

from app import create_app
from database.database import db
from services.translator_service import TranslationError, translate_text


class TranslatorServiceTests(unittest.TestCase):
    def test_offline_hindi_translations_render_correctly(self):
        self.assertEqual(translate_text("hello", "hi"), "\u0928\u092e\u0938\u094d\u0924\u0947")
        self.assertEqual(
            translate_text("thank you", "hi"),
            "\u0927\u0928\u094d\u092f\u0935\u093e\u0926",
        )
        self.assertEqual(
            translate_text("good morning", "hi"),
            "\u0938\u0941\u092a\u094d\u0930\u092d\u093e\u0924",
        )

    def test_offline_lookup_ignores_case_and_surrounding_whitespace(self):
        self.assertEqual(translate_text("  HELLO  ", "es"), "hola")

    def test_empty_text_is_rejected(self):
        with self.assertRaisesRegex(TranslationError, "Enter text"):
            translate_text("   ", "hi")

    def test_auto_is_not_a_valid_target_language(self):
        with self.assertRaisesRegex(TranslationError, "valid target"):
            translate_text("hello", "auto")


class TranslationApiTests(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.TemporaryDirectory()

        class TestConfig:
            TESTING = True
            SECRET_KEY = "test-secret"
            SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
            SQLALCHEMY_TRACK_MODIFICATIONS = False
            DOWNLOAD_FOLDER = Path(self.tempdir.name)

        self.app = create_app(TestConfig)
        self.client = self.app.test_client()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()
        self.tempdir.cleanup()

    def test_translate_api_returns_translation_and_persists_history(self):
        response = self.client.post(
            "/api/translate",
            json={"text": "hello", "target_language": "hi"},
        )

        self.assertEqual(response.status_code, 200)
        payload = response.get_json()
        self.assertEqual(payload["translation"], "\u0928\u092e\u0938\u094d\u0924\u0947")
        self.assertEqual(payload["target_language"], "hi")
        self.assertIsInstance(payload["history_id"], int)

        history_response = self.client.get("/api/history")

        self.assertEqual(history_response.status_code, 200)
        history = history_response.get_json()
        self.assertEqual(len(history), 1)
        self.assertEqual(history[0]["source_text"], "hello")
        self.assertEqual(history[0]["translated_text"], "\u0928\u092e\u0938\u094d\u0924\u0947")


if __name__ == "__main__":
    unittest.main()
