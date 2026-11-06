from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import math

OUT = Path(__file__).parent
im = Image.new('RGB', (1600, 2160), '#f4f7fb')
d = ImageDraw.Draw(im)

def font(size):
    return ImageFont.load_default(size=size)

def label(x, y, lines, size=27, color='#20324b', spacing=10):
    for line in lines.split('\n'):
        d.text((x, y), line, font=font(size), fill=color)
        y += size + spacing

def card(x, y, w, h, title, body, source, fill='#ffffff', border='#cdd8e6'):
    d.rounded_rectangle((x,y,x+w,y+h), radius=22, fill=fill, outline=border, width=2)
    label(x+26,y+20,title,31)
    label(x+26,y+68,body,25,spacing=9)
    label(x+26,y+h-39,source,21,'#566d8a')

def arrow(points, color='#657b96', width=4):
    d.line(points,fill=color,width=width,joint='curve')
    a,b=points[-2:]
    theta=math.atan2(b[1]-a[1],b[0]-a[0])
    tip=[b,(b[0]-17*math.cos(theta-.48),b[1]-17*math.sin(theta-.48)),
           (b[0]-17*math.cos(theta+.48),b[1]-17*math.sin(theta+.48))]
    d.polygon(tip,fill=color)

label(70,48,'How a job reaches a responder',49)
label(70,115,'Dispatch asks one person at a time. The first yes ends the search.',28)

card(250,190,1100,145,'1  A request for help arrives',
     'Includes the place, time, area and abilities needed.',
     'offer.py:19  |  Creating the request happens outside this folder.')
arrow([(800,335),(800,370)])
card(250,370,1100,145,'2  Find people marked available',
     'Use availability set by the responder or their handler.',
     'availability.py:12  |  No available people means nobody can be asked.')
arrow([(800,515),(800,550)])
card(250,550,1100,180,'3  Give each person a score for this job',
     'Travel time: 60%   |   Past acceptance: 25%   |   Abilities: 15%\nShorter travel time, higher history and more matching abilities add points.',
     'routing.py:30  +  availability.py:21  +  history.py:20  +  config.py:13')
arrow([(800,730),(800,765)])
card(250,765,1100,145,'4  Put the highest score first',
     'Make the order once for this job. A place in line does not guarantee an offer.',
     'routing.py:18')
arrow([(800,910),(800,945)])
card(250,945,1100,150,'5  Send the next person an offer; start the 60-second clock',
     'Their phone should buzz. Actual delivery is not shown in these files.',
     'offer.py:34, 51  +  config.py:9',fill='#e9f0ff',border='#8aa8e4')

arrow([(800,1095),(800,1130),(290,1130),(290,1170)])
arrow([(800,1130),(800,1170)])
arrow([(800,1130),(1310,1130),(1310,1170)])
card(60,1170,460,195,'6A  Accepts',
     'Add 0.08 to their history score.\nReturn who accepted the job.',
     'offer.py:27  +  history.py:25',fill='#e7f4ed',border='#92c6ab')
card(570,1170,460,195,'6B  Turns it down',
     'Subtract 0.12 from their\nhistory score.',
     'offer.py:30  +  history.py:35',fill='#fff3de',border='#dabb7a')
card(1080,1170,460,195,'6C  Does not answer',
     'At 60 seconds, remove offer.\nSubtract 0.12 from history.',
     'offer.py:47  +  history.py:35',fill='#fdebed',border='#d8a1a8')
arrow([(290,1365),(290,1410)],color='#3f8a64')
card(60,1410,460,145,'STOP asking for this job',
     'People later in line get no offer.',
     'offer.py:29',fill='#e7f4ed',border='#92c6ab')
arrow([(800,1365),(800,1410)])
arrow([(1310,1365),(1310,1390),(1040,1390),(1040,1410)])
card(570,1410,970,145,'Ask the next person in the existing order',
     'If the list is exhausted, return “nobody accepted.”',
     'offer.py:25-31')
arrow([(1540,1480),(1570,1480),(1570,1020),(1350,1020)])

d.rounded_rectangle((60,1620,1540,2050),radius=25,fill='#e9edf5')
label(90,1650,'What repeated missed offers can mean for future jobs',33)
label(90,1710,'Starting at 0.50, five consecutive misses lower the history score to zero:',26)
label(130,1770,'0.50   >   0.38   >   0.26   >   0.14   >   0.02   >   0.00',34,'#9b3e4b')
label(90,1840,'Lower history > may be later in line > others may accept before they are asked.',27)
label(90,1890,'Time alone does not restore the score. Accepting an offer adds 0.08.',27)
label(90,1940,'Travel time and abilities still count. No offer received means no new penalty.',27)
label(90,1995,'history.py:15-43  +  routing.py:30  |  Scores stay between 0 and 1.',22,'#566d8a')
label(60,2090,'Source folder: 00-rook/code/dispatch-routing/  |  Diagram describes the supplied files.',23,'#566d8a')
im.save(OUT/'dispatch-routing-explained.png')
