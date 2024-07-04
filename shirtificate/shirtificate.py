from fpdf import FPDF

class PDF(FPDF):
    def __init__(self):
        super().image("./shirtificate.png", 10, 70, 190)

def main():
    name = input("Name: ")
    shirt(name)


def shirt(s):
    try:
        pdf = PDF()
        pdf.add_page()
        pdf.set_font("helvetica", size=24)
        pdf.set_text_color(255,255,255)
        pdf.cell(0, 213, f"{s} took CS50", align="C")
        pdf.output("shirtificate.pdf")
    except RuntimeError as e:
        print(e)


if __name__ == "__main__":
    main()
