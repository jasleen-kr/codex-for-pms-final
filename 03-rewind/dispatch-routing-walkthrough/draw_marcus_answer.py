from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import math

OUT=Path(__file__).parent
im=Image.new('RGB',(1600,1550),'#f2f6fb')
d=ImageDraw.Draw(im)
def f(n):return ImageFont.load_default(size=n)
def text(x,y,s,n=27,c='#20324b'):
    for line in s.split('\n'):
        d.text((x,y),line,font=f(n),fill=c);y+=n+11
def box(x,y,w,h,heading,body,fill='#ffffff',border='#ccd8e7',hc='#20324b'):
    d.rounded_rectangle((x,y,x+w,y+h),radius=22,fill=fill,outline=border,width=2)
    text(x+25,y+20,heading,32,hc)
    text(x+25,y+75,body,26)
def arrow(points):
    d.line(points,fill='#637b99',width=4,joint='curve')
    a,b=points[-2:];t=math.atan2(b[1]-a[1],b[0]-a[0])
    d.polygon([b,(b[0]-17*math.cos(t-.5),b[1]-17*math.sin(t-.5)),(b[0]-17*math.cos(t+.5),b[1]-17*math.sin(t+.5))],fill='#637b99')

text(60,35,"Answering Marcus's question about 4.2",46)
text(60,100,'14 August 2026 | Release-page comment + supplied routing code',25,'#5a6f89')
box(60,160,1480,155,'Marcus asked two things:',
    'Does the ranking change also apply to people who have been declining jobs?\nWas that a deliberate decision, or did it just happen that way?',fill='#e7eef9',border='#aabfdd')
arrow([(450,315),(450,355)]);arrow([(1170,315),(1170,355)])
box(60,355,760,210,'HOW IT WORKS: YES',
    'Everyone returned as available uses the same rules.\nPrevious decliners are included.\nThere is no separate ranking setting for that group.',
    fill='#e7f4ed',border='#90c6a7',hc='#216b4c')
box(860,355,680,210,'WAS IT DELIBERATE? UNKNOWN',
    'The code shows behavior, not the decision.\nThe release-page comments contain no\nrecorded answer to that part of his question.',
    fill='#fff2db',border='#d6b770',hc='#82570d')
text(65,600,'The existing rules create a possible cycle',34)
box(60,660,700,145,'Declines an offer',
    'Subtract 0.12 from the history score.\nhistory.py:35  +  config.py:19')
box(840,660,700,145,'Misses an offer',
    'Subtract the same 0.12 from history.\noffer.py:30  +  history.py:35')
arrow([(410,805),(410,832),(800,832),(800,860)])
arrow([(1190,805),(1190,832),(800,832)])
box(250,860,1100,145,'May appear later in the asking order for future jobs',
    'Travel time and matching abilities still matter too.\nrouting.py:38',fill='#eaf0fc',border='#9bb4dd')
arrow([(800,1005),(800,1040)])
box(250,1040,1100,145,'If someone earlier accepts, this person gets no offer',
    'No offer means no chance to earn acceptance points on that job.\noffer.py:25  |  Time alone does not restore the score: history.py:30')
box(60,1230,1480,185,'What 4.2 actually changed',
    'Answer window: 90 to 60 seconds  |  Travel-time weight: 0.45 to 0.60\nHistory weight: 0.40 to 0.25. The history penalty was not newly introduced or increased.\nconfig.py:9-19',fill='#e7eef9',border='#aabfdd')
text(60,1430,'The mechanism is supported by the code. Actual ranking records are needed to confirm',26)
text(60,1470,'it caused the observed quiet phones; Product needs to establish whether it was intended.',26)
im.save(OUT/'marcus-question-explained.png')
