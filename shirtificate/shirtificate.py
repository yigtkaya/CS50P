from fpdf import FPDF

def main():

    name = input("Name: ")
    pdf = FPDF(orientation="portrait", format="A4")
    pdf.add_page()
    pdf.set_auto_page_break(auto=False, margin=0)

    pdf.set_font("helvetica", "B", size=30)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 50, border=0, align="C", txt="CS50 Shirtificate")
    pdf.ln()

    pdf.image(
            "shirtificate.png",
            x=15,
            y=(297 / 4),
            w=180,
            alt_text=f"A Harvard shirt with the words: {name} took CS50",
        )

    pdf.set_font("helvetica", "B", size=20)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(0, 150, border=0, align="C", txt=f"{name} took CS50")

    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()