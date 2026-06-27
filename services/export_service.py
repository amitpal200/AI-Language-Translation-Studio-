import csv
import io


def history_to_csv(history_items):
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(
        ["created_at", "source_language", "target_language", "source_text", "translated_text"]
    )
    for item in history_items:
        writer.writerow(
            [
                item.created_at.isoformat(),
                item.source_language,
                item.target_language,
                item.source_text,
                item.translated_text,
            ]
        )
    return output.getvalue()
