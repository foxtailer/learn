from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.colors import pink, black, red, blue, green


c = canvas.Canvas('myfile.pdf')

#c.scale(0.75,0.5)

c.setStrokeColor(pink)
c.grid([inch, 2*inch, 3*inch, 4*inch], [0.5*inch, inch, 1.5*inch, 2*inch, 2.5*inch])
c.setStrokeColor(black)
c.setFont("Times-Roman", 20)
c.drawString(0,0, "(0,0) the Origin")
c.drawString(2.5*inch, inch, "(2.5,1) in inches")
c.drawString(4*inch, 2.5*inch, "(4, 2.5)")
c.setFillColor(red)
c.rect(0,2*inch,0.2*inch,0.3*inch, fill=1)
c.setFillColor(green)
c.circle(4.5*inch, 0.4*inch, 0.2*inch, fill=1)

c.saveState()

c.translate(2*inch, 8*inch)
c.scale(1.0, -1.0)

c.setStrokeColor(pink)
c.grid([inch, 2*inch, 3*inch, 4*inch], [0.5*inch, inch, 1.5*inch, 2*inch, 2.5*inch])
c.setStrokeColor(black)
c.setFont("Times-Roman", 20)
c.drawString(0,0, "(0,0) the Origin")
c.drawString(2.5*inch, inch, "(2.5,1) in inches")
c.drawString(4*inch, 2.5*inch, "(4, 2.5)")
c.setFillColor(red)
c.rect(0,2*inch,0.2*inch,0.3*inch, fill=1)
c.setFillColor(green)
c.circle(4.5*inch, 0.4*inch, 0.2*inch, fill=1)

c.restoreState()
c.drawString(5*inch, inch, "(5,1) in inches[restored]")

#c.showPage()
c.save()

