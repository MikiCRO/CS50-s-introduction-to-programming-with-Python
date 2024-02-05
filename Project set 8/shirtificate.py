from fpdf import FPDF

name=input("What is your name? ")

pdf = FPDF(format="A4")
pdf.add_page("P")
pdf.image("shirtificate.png", x=10, y=70, w=190, keep_aspect_ratio=True)
pdf.set_font("helvetica", "B", 40)
pdf.cell(40)
pdf.cell(h=40,text="CS50 Shirtificate",  align="C")


pdf.set_text_color(255,255, 255)
pdf.set_font("helvetica","",36)
pdf.cell(-120,245,text=name+" took CS50", align="C")


pdf.set_auto_page_break(0)
pdf.output("shirtificate.pdf")