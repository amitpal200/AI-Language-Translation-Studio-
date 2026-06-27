from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def create_translation_pdf(source_text, translated_text, output_path):
    pdf = canvas.Canvas(str(output_path), pagesize=letter)
    width, height = letter
    y = height - 72
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(72, y, "AI Language Translation Studio")
    y -= 42
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(72, y, "Source")
    y -= 20
    pdf.setFont("Helvetica", 11)
    for line in _wrap(source_text):
        pdf.drawString(72, y, line)
        y -= 16
    y -= 16
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(72, y, "Translation")
    y -= 20
    pdf.setFont("Helvetica", 11)
    for line in _wrap(translated_text):
        pdf.drawString(72, y, line)
        y -= 16
    pdf.save()
    return output_path


def _wrap(text, width=85):
    words = (text or "").split()
    lines = []
    current = []
    for word in words:
        if sum(len(part) + 1 for part in current) + len(word) > width:
            lines.append(" ".join(current))
            current = [word]
        else:
            current.append(word)
    if current:
        lines.append(" ".join(current))
    return lines or [""]
