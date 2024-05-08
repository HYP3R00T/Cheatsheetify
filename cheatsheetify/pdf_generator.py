from reportlab.lib import colors
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from typing import Dict, List


def generate_pdf(data: Dict, elements: List = []):

    styles = getSampleStyleSheet()

    # Info Section
    info = data["info"]
    elements.append(
        Paragraph("<font><b>{}</b></font>".format(info["command"]), styles["Heading1"])
    )
    elements.append(
        Paragraph(
            "<font><b>{}</b></font>".format(info["description"]),
            styles["Heading2"],
        )
    )
    elements.append(
        Paragraph(
            "<font><b>{}</b></font>".format(info["homepage"]),
            styles["Heading4"],
        )
    )
    elements.append(Spacer(1, 12))

    # Commands Section
    commands = data["commands"]
    for command, description in commands.items():
        table_data = [
            [
                Paragraph(
                    f"<font face='Courier'>{command}</font>",
                    styles["Code"],
                ),
                Paragraph(description, styles["Normal"]),
            ]
        ]
        t = Table(table_data, colWidths=(150, 350))
        t.setStyle(
            TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, 0), colors.azure),
                    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                    ("ALIGN", (0, 0), (-1, -1), "LEFT"),
                    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                    ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
                    ("BACKGROUND", (0, 1), (-1, -1), colors.white),
                    ("GRID", (0, 0), (-1, -1), 1, colors.black),
                ]
            )
        )
        elements.append(t)
        elements.append(Spacer(1, 12))
