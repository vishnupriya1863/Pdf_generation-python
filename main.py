from fpdf import FPDF
import pandas as pd

pdf =FPDF(orientation="P", unit="mm", format ="A4")
pdf.set_auto_page_break(auto=False,margin=0)

df = pd.read_csv("topics.csv")

for index,row in df.iterrows():
    pdf.add_page()
    # set the header
    pdf.set_font(family="Times",style="B",size=25)
    pdf.set_text_color(250,0,0)
    pdf.cell(w=0,h=16,txt=row["Topic"],align="L",ln=1)
    for i in range(20,298,10):
        pdf.line(10,i,200,i)
    pdf.line(10,21,200,21)
    #set the footer
    pdf.ln(258)
    pdf.set_font(family="Times",style="B",size=10)
    pdf.set_text_color(250,0,0)
    pdf.cell(w=0,h=18,txt=row["Topic"],align="L",ln=1)
    for i in range(row["Pages"] - 1):
        pdf.add_page()

        # set the footer
        pdf.ln(270)
        pdf.set_font(family="Times", style="B", size=10)
        pdf.set_text_color(250, 0, 0)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R", ln=1)

pdf.output("output.pdf")


