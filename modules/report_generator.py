from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf(report_data, filename="report.pdf"):
    doc = SimpleDocTemplate(f"reports/{filename}")
    styles = getSampleStyleSheet()

    elements = []

    elements.append(Paragraph("Digital Forensics Report", styles["Title"]))
    elements.append(Spacer(1, 12))

    # Add basic info
    for key, value in report_data.items():
        if key != "Timeline":
            elements.append(Paragraph(f"<b>{key}:</b> {value}", styles["Normal"]))
            elements.append(Spacer(1, 8))

    # Add Timeline
    if "Timeline" in report_data:
        elements.append(Spacer(1, 12))
        elements.append(Paragraph("Event Timeline", styles["Heading2"]))
        elements.append(Spacer(1, 8))

        for item in report_data["Timeline"]:
            elements.append(Paragraph(f"{item['time']} → {item['event']}", styles["Normal"]))
            elements.append(Spacer(1, 6))

    doc.build(elements)

    return filename