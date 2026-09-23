from pathlib import Path
import math
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, Color
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import A4

HERE = Path(__file__).resolve().parent
OUT = HERE / 'authority_dictionary_visual_introduction.pdf'
for name, file in [('Body', 'calibri.ttf'), ('Bold', 'calibrib.ttf'), ('Italic', 'calibrii.ttf')]:
    pdfmetrics.registerFont(TTFont(name, 'C:/Windows/Fonts/' + file))
pdfmetrics.registerFontFamily('Body', normal='Body', bold='Bold', italic='Italic', boldItalic='Bold')
W, H = A4
c = canvas.Canvas(str(OUT), pagesize=A4)
c.setTitle('Authority Dictionary | A visual introduction')
c.setAuthor('VD Newton')
c.setSubject('An ordered list of entries, their headwords and definientia, and the definition formed by a shared headword.')
INK = '#20333D'; MUTED = '#617078'; TEAL = '#087E83'; PALE = '#EAF6F4'; LINE = '#CAD7DA'; GOLD = '#AD7324'

def box(x, y, w, h, fill='#FFFFFF', stroke=LINE, radius=6, lw=0.8):
    c.setFillColor(HexColor(fill)); c.setStrokeColor(HexColor(stroke)); c.setLineWidth(lw)
    c.roundRect(x, H-y-h, w, h, radius, fill=1, stroke=1)

def txt(x, y, text, size=11, font='Body', color=INK):
    c.setFillColor(HexColor(color)); c.setFont(font, size); c.drawString(x, H-y-size, text)

def para(x, y, w, text, size=11, leading=15, color=INK, font='Body'):
    s = ParagraphStyle('p', fontName=font, fontSize=size, leading=leading, textColor=HexColor(color))
    p = Paragraph(text, s); _, h = p.wrap(w, H)
    p.drawOn(c, x, H-y-h)
    return h

def line(points, color=MUTED, lw=1, arrow=False):
    c.setStrokeColor(HexColor(color)); c.setFillColor(HexColor(color)); c.setLineWidth(lw)
    p=c.beginPath(); p.moveTo(points[0][0], H-points[0][1])
    for x,y in points[1:]: p.lineTo(x,H-y)
    c.drawPath(p)
    if arrow:
        a,b=points[-2:]; angle=math.atan2(b[1]-a[1],b[0]-a[0]); r=5
        p=c.beginPath(); p.moveTo(b[0],H-b[1])
        for t in [angle+2.65,angle-2.65]: p.lineTo(b[0]+r*math.cos(t),H-(b[1]+r*math.sin(t)))
        p.close(); c.drawPath(p,fill=1,stroke=0)

# Editorial heading and the proposal as stated in the conversation.
txt(40, 34, 'VD  /  FOUNDATIONAL VOCABULARY', 9, 'Bold', TEAL)
txt(40, 57, 'Authority Dictionary', 32, 'Bold')
txt(40, 98, 'An ordered list. A shared vocabulary.', 15, 'Body', MUTED)
para(40, 136, 515,
     'An <b>Authority Dictionary (AD)</b> is an ordered list of entries. '
     'Each entry pairs a <b>headword</b>, the word being defined, with a '
     '<b>definiens</b>, the defining content supplied by that entry.', 12, 17)
para(40, 196, 515,
     'The <b>definition of a word</b> is the collection of all entries with that '
     'headword. A definition can therefore comprise several entries in the AD.', 12, 17)
line([(40,247),(555,247)], LINE, 0.8)
txt(40, 261, 'A SHORT EXAMPLE, WITH ITS PARTS LABELLED', 9, 'Bold', MUTED)

# Callout boxes above the two fields. Arrows land on the first entry's cells.
box(140, 287, 112, 49, '#F4F7F8')
txt(150,294,'Headword',12,'Bold')
txt(150,312,'The word being defined',8.5,color=MUTED)
box(312,287,238,49,'#F4F7F8')
txt(324,294,'Definiens',12,'Bold')
txt(324,312,'The defining content in this entry',9,color=MUTED)

# The outer box is the AD; each inner row is a complete entry.
box(120,358,430,234,'#FFFFFF',INK,8,1.2)
rows = [
    ('marker','An object used to identify a location.'),
    ('route','An ordered sequence of locations.'),
    ('marker','Each marker has a unique label.'),
    ('signal','A sign that conveys information.'),
]
for i,(word,content) in enumerate(rows):
    y=370+i*54
    selected=word=='marker'
    border=TEAL if selected else (GOLD if i==1 else LINE)
    box(140,y,400,46,PALE if selected else '#FFFFFF',border,4,1.1 if selected or i==1 else 0.7)
    line([(258,y),(258,y+46)],border,0.6)
    txt(154,y+13,word,13,'Bold',TEAL if selected else INK)
    para(271,y+9,252,content,11,14)
    txt(127,y+15,str(i+1),9,'Bold',MUTED)

line([(193,336),(193,370)],MUTED,1,True)
line([(431,336),(431,370)],MUTED,1,True)

box(40,350,70,65,'#F4F7F8')
txt(48,357,'AD',12,'Bold')
para(48,376,61,'The whole<br/>ordered list',9,12,color=MUTED)
line([(110,360),(120,360)],INK,1,True)
box(40,433,70,48,'#FCF6EA','#DFC69E')
txt(48,440,'Entry',12,'Bold',GOLD)
txt(48,460,'One whole row',8.5,color=MUTED)
line([(110,462),(140,462)],GOLD,1,True)
txt(40,550,'1, 2, 3, 4',9,'Bold',MUTED)
para(40,565,77,'Positions in<br/>the list',8.5,11,color=MUTED)

# Both highlighted entries converge on the definition box. The branches
# touch complete rows, making the collection of entries visually explicit.
line([(540,393),(565,393),(565,624),(525,624),(525,641)],TEAL,1.3,True)
line([(540,501),(565,501)],TEAL,1.3)
for y in [393,501]:
    c.setFillColor(HexColor(TEAL)); c.circle(540,H-y,2.4,fill=1,stroke=0)
txt(140,601,'The two highlighted entries share the headword "marker".',9,color=MUTED)
box(130,641,420,102,PALE,TEAL,8,1.1)
txt(146,653,'Definition of "marker"',17,'Bold',TEAL)
para(146,681,385,'<b>Entry 1 + Entry 3, taken together.</b><br/>'
     'Both complete entries make up this word\'s definition in the example AD.',11,15)

line([(40,772),(555,772)],LINE,0.7)
para(40,785,465,'Illustrative entries invented for this diagram. Based on the vocabulary proposed in this conversation, 8 September 2026.',8.5,11,color=MUTED)
txt(546,792,'1',9,color=MUTED)
c.showPage(); c.save()
print(OUT)
