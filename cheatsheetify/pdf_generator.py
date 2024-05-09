from fpdf import FPDF


def generate_pdf(pdf: FPDF, cheatsheet, palatte):
    # print(cheatsheet)

    # Add info about commands
    pdf.set_font(family="inter", style="", size=16)
    pdf.set_text_color(*palatte["foreground"])
    pdf.multi_cell(w=0, text=cheatsheet["info"]["command"], new_x="LEFT", new_y="NEXT")
    pdf.set_font(family="firacode", style="", size=12)
    pdf.multi_cell(
        w=0, text=cheatsheet["info"]["description"], new_x="LEFT", new_y="NEXT"
    )
    pdf.ln(10)

    return pdf
