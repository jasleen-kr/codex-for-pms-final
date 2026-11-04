from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import html

OUT = Path(__file__).parent
W, H = 1800, 3850
im = Image.new('RGB', (W, H), '#0b1124')
d = ImageDraw.Draw(im)
INK, MUTED, GOLD = '#f4f6ff', '#b9c5df', '#ffcf49'
def font(n): return ImageFont.load_default(size=n)
def text(x,y,s,n=25,c=INK): d.text((x,y),s,font=font(n),fill=c)
def wrap(s,width,n):
    lines=[]; line=''
    for word in s.split():
        trial=(line+' '+word).strip()
        if d.textlength(trial,font=font(n))>width and line:
            lines.append(line); line=word
        else: line=trial
    return lines+[line]
def para(x,y,s,width,n=25,c=MUTED):
    for line in wrap(s,width,n): text(x,y,line,n,c); y+=n+9
    return y
def box(x,y,w,h,fill='#17233e',outline='#354568'):
    d.rounded_rectangle((x,y,x+w,y+h),radius=20,fill=fill,outline=outline,width=2)
def title(y,k,s):
    text(60,y,k,22,GOLD); text(60,y+34,s,42)
def card(x,y,w,h,heading,body,color=GOLD):
    box(x,y,w,h); text(x+25,y+21,heading,30,color)
    para(x+25,y+70,body,w-50)
def hero(x,y,color,mark):
    # Concept costumes: deliberately generic masked silhouettes.
    cx=x+140
    d.ellipse((cx-95,y,cx+95,y+190),fill='#243451')
    d.polygon([(cx-40,y+90),(cx+40,y+90),(cx+86,y+213),(cx-86,y+213)],fill=color)
    d.rounded_rectangle((cx-41,y+84,cx+41,y+184),radius=18,fill='#101a30')
    d.ellipse((cx-32,y+22,cx+32,y+87),fill='#c1cce3')
    d.rounded_rectangle((cx-34,y+42,cx+34,y+63),radius=6,fill='#101a30')
    d.line((cx-23,y+52,cx-10,y+52),fill=GOLD,width=4)
    d.line((cx+10,y+52,cx+23,y+52),fill=GOLD,width=4)
    text(cx-12,y+117,mark,32,color)

# Masthead
d.polygon([(0,0),(1800,0),(1800,250),(0,315)],fill='#1b3156')
text(60,38,'ROOK INDUSTRIES  /  FIELD GUIDE',24,GOLD)
text(60,86,'THE RESPONDER UNIVERSE',66)
para(60,173,'Independent heroes. Human handlers. Software that connects the mission.',1600,30)
text(60,264,'FICTIONAL COURSE SCENARIO  |  Evidence: June-September 2026  |  Concept artwork',22,GOLD)

title(335,'01 / THE HERO ROSTER','Five responders. Four handler perspectives.')
roster=[
 ('VESPER','Aunt Dot','Offers vanish before reaching the phone; also quiet stretches.','Powers not specified.','#9b83ff','V'),
 ('CAPTAIN VANTAGE','Mr. Ambrose','Offers move on while getting ready. Saved filters sometimes reset.','Tags: flight, structural-entry.','#55c6ef','C'),
 ('SGT. BULWARK','Halloran','Cracked vest plate approval delayed 11 days; one fast-moving offer.','Powers not specified.','#ffbb54','B'),
 ('METEOR MITE','Kip','Unusually quiet phone and little incoming work.','Powers not specified.','#ef7c91','M'),
 ('THE GALE','Kip','Heavy workload while Meteor Mite is quiet in the same city.','Powers not specified.','#58d4b6','G')]
for i,(name,handler,body,powers,color,mark) in enumerate(roster):
    x=60+i*340; box(x,445,320,545)
    hero(x+20,461,color,mark)
    text(x+18,686,name,25,color)
    text(x+18,727,'Handler: '+handler,21)
    yy=para(x+18,772,body,284,23)
    para(x+18,yy+15,powers,284,21,GOLD)
text(60,1008,'Costumes are invented illustrations. Names do not establish powers, appearance or legal identities.',22,MUTED)

title(1070,'02 / MISSION CONTROL','Rook sells software; responders work independently.')
card(60,1175,820,230,'DISPATCH / COORDINATE','Handler web console + responder phone app. Incident > rank available responders > ping > taken assigns the incident. Turned down or missed advances to the next responder.','#55c6ef')
card(910,1175,830,230,'SUPPLY / EQUIP','Requisition > quartermaster approval > fulfillment > maintenance. Field failure reports can bring maintenance forward. Handlers manage readiness; quartermasters own equipment and approvals.','#58d4b6')
box(60,1425,1680,100,'#243451')
para(85,1444,'SHARED DEPENDENCY: Dispatch writes the Responder Availability Record. Supply reads it for maintenance scheduling, so Dispatch changes can affect equipment readiness.',1620,26)
text(60,1546,'Founded 2014  |  241 employees  |  Subscription per active responder  |  Monthly 4.x release train',24,GOLD)

title(1610,'03 / THE SIGNALS','More reports after 4.2. Cause still unconfirmed.')
for x,num,label in [(60,'147','tickets reviewed'),(490,'0.9 > 4.0','tickets per day'),(920,'~4.4x','daily report rate'),(1350,'44 / 105','post-release symptom tickets')]:
    box(x,1715,390,130); text(x+22,1732,num,43,GOLD); text(x+22,1794,label,21)
para(60,1865,'Before 12 Aug: 40 tickets / 44 days. After 12 Aug: 105 / 26 days. Two release-day tickets kept separate. Counts are reports, not verified incidents or independent customers.',1680,24)
card(60,1965,820,210,'QUIET / FEWER PINGS: 32 REPORTS','From 4 handlers after release. Quiet phones do not prove notification failure. Validate whether responders were selected and whether pings were delivered.','#9b83ff')
card(910,1965,830,210,'DISAPPEARING OFFERS: 14 REPORTS','From 10 handlers after release. Two reports overlap with quiet-phone reports: 44 distinct tickets total, about 42% of the 105 post-release tickets.','#ef7c91')
para(60,2195,'Support estimated ~3x normal callout tickets in August; this differs in scope from the calculated ~4.4x rate across all reviewed tickets. Interviews echo disappearing offers (3/4) and quiet/uneven work (2/4).',1680,24)

title(2300,'04 / THE RELEASE STORY','Two routing changes shipped together.')
card(60,2405,530,245,'4.0 / 7 APR 2026','New console navigation, responder profile redesign, routing override audit log.')
card(615,2405,545,245,'4.1 / 16 JUN 2026','Travel-time proximity, bulk callout and phone push reliability.')
card(1185,2405,555,245,'4.2 / 12 AUG 2026','More weight on proximity; ping wait 90 > 60 seconds; persistent filters; three defect fixes.')
para(60,2670,'Ranking uses travel time, availability, capabilities and recent acceptance. Declined and missed offers lower the history component. Engineering questioned whether 4.2 behavior for responders declining jobs was intentional.',1680,24)
para(60,2760,'Seasonality and September recovery were Priya\'s hypotheses. No resolution is recorded in the reviewed discussion. Ambrose reports similar incidents earlier in the year; the release is not a proven starting point.',1680,24,GOLD)

title(2860,'05 / THE NEXT MISSIONS','Validate the mechanism and the commitments.')
card(60,2965,820,295,'CUSTOMER EXPERIENCE','Interviews: small text 2/4; handler alert awareness or identification 3/4; Kip alone explicitly describes overload beside inactivity. Tickets also surface profile/availability controls, sign-in and fulfillment. Filter requests: 2 before release; resets/usability: 11 after. Maintenance timing/visibility: 5 post-release tickets.','#55c6ef')
card(910,2965,830,295,'ROADMAP / LAST REVIEWED 30 JUN','4.2 committed: routing, timeout tuning, Availability Confidence. Confidence is absent from release notes; delivery needs confirmation. 4.3: requisition approval chains. Q4 exploration: handler phone app and shared cover (unsupported today). Commitments still list Priya as owner.','#58d4b6')
box(60,3285,1680,260)
text(85,3305,'THE SUPPORT TEAM',30,GOLD)
team=[('Helen Achebe','Product director; commitments'),('Marcus Oyelaran','Engineering manager; technical partner'),('Wen Li','Staff engineer; routing behavior'),('Ravi Menon','Analyst; weekly acceptance reporting'),('Nadia Hoffmann','Support lead; customer tickets'),('Sofia Marino','Designer; September interviews'),('Priya Raghunathan','Previous PM; left 21 Aug 2026')]
for i,(name,role) in enumerate(team):
    col=i%2; row=i//2; x=85+col*825; y=3360+row*42
    text(x,y,name,23); text(x+245,y,role,20,MUTED)
para(60,3570,'METRICS: Acceptance = taken / all pings. Time-to-accept = median seconds from ping to taken. Coverage gap = nobody available with the required capability tags; distinct from rejection.',1680,24)
para(60,3660,'NEXT: Ravi + Wen compare responder-level pings and timing around 12 Aug; Nadia validates reports; Helen confirms delivery and owners. Ask why changes shipped together, what justified 60 seconds and which promises were deferred.',1680,23)
text(60,3772,'Sources: Rook wiki + September interviews + supplied AGENTS.md research summary. Current outcomes unverified.',21,MUTED)
im.save(OUT/'rook-superhero-board.png')

links=[('Company overview','https://app.notion.com/p/About-Rook-3eac8516f50181afbc4de9d8ff334082'),('Customer interviews','https://app.notion.com/p/83a83da875364a1ab725d914482fad35'),('4.2 release discussion','https://app.notion.com/p/4-2-3eac8516f50181499fc4c5cf15c1ace7'),('Q3 roadmap','https://app.notion.com/p/950ebd7431764f11b6dc1cc13378dca2')]
page='''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Rook: The Responder Universe</title><style>body{margin:0;background:#0b1124;color:#f4f6ff;font:18px system-ui}main{max-width:1800px;margin:auto}img{width:100%;height:auto;display:block}nav{padding:24px;display:flex;gap:24px;flex-wrap:wrap}a{color:#ffcf49}</style><main><img src="rook-superhero-board.png" alt="Rook superhero field guide: five responders, products, ticket evidence, release history, roadmap and team. Illustrative costumes; fictional course scenario."><nav>'''
page+=''.join(f'<a href="{html.escape(url)}">{html.escape(label)}</a>' for label,url in links)
page+='</nav></main></html>'
(OUT/'rook-superhero-board.html').write_text(page)
print(OUT/'rook-superhero-board.png')
