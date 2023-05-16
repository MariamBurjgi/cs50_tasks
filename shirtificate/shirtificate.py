from fpdf import FPDF

class MyPDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.cell(80)
        self.cell(30, 10, 'CS50 Shirtificate', 0, 0, 'C')
        self.ln(20)

pdf = MyPDF(orientation='P', unit='mm', format='A4')
pdf.add_page()
pdf.set_auto_page_break(False)

pdf.image('shirtificate.png', x=55, y=40, w=100)

pdf.set_font('Arial', 'B', 32)
pdf.set_text_color(255, 255, 255)
pdf.cell(0, -60, 'John Doe', 0, 0, 'C', fill=True)

pdf.output('shirtificate.pdf')
