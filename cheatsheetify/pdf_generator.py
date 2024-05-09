from fpdf import FPDF


def generate_pdf(pdf: FPDF, cheatsheet, palatte):
    # print(cheatsheet)

    # Add info about commands
    # Add heading
    pdf.set_font(family="firacode", style="", size=16)
    pdf.set_text_color(*palatte["foreground"])
    pdf.set_fill_color(*palatte["background_secondary"])
    pdf.multi_cell(
        w=0,
        text=cheatsheet["info"]["command"],
        new_x="LEFT",
        new_y="NEXT",
        fill=True,
        padding=2,
    )
    pdf.ln(2)

    # Add description
    pdf.set_font(family="inter", style="", size=12)
    pdf.set_text_color(*palatte["foreground_secondary"])
    pdf.multi_cell(
        w=0, text=cheatsheet["info"]["description"], new_x="LEFT", new_y="NEXT"
    )
    pdf.ln(2)

    # Add link
    pdf.set_font(family="firacode", style="", size=10)
    pdf.set_text_color(*palatte["blue"])
    pdf.multi_cell(w=0, text=cheatsheet["info"]["homepage"], new_x="LEFT", new_y="NEXT")
    pdf.ln(5)

    # Add comamnds and their explaination
    for key, value in cheatsheet["commands"].items():
        pdf.set_font(family="firacode", style="", size=12)
        pdf.set_text_color(*palatte["red"])
        pdf.set_fill_color(*palatte["background_secondary"])
        pdf.multi_cell(w=0, text=f"\u2022{key}", new_x="LEFT", new_y="NEXT")
        pdf.ln(2)

        pdf.set_font(family="inter", style="I", size=12)
        pdf.set_text_color(*palatte["foreground"])
        pdf.set_fill_color(*palatte["background_secondary"])
        pdf.multi_cell(
            w=0, text=f"{value}", new_x="LEFT", new_y="NEXT", padding=(0, 0, 0, 3)
        )
        pdf.ln(4)
    pdf.ln(7)

    return pdf
