from pathlib import Path
from collections import Counter
from datetime import datetime, timedelta
import csv, json, html
from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).parent
SOURCE = OUT.parent / 'dispatch-4.2-analysis'
roster = [
('Captain Vantage','Mr. Ambrose','Hillcrest'),('Cindermark','Farid Haddad','Mill District'),
('Corporal Ashgrove','Yusuf Demir','Northfield'),('Farlight','Linda Pruitt','Uptown'),
('Halfmoon','Simone Fischer','Westbury'),('Ironvale','Teresa Alvarez','Riverside'),
('Meteor Mite','Kip','Eastgate'),('Nightwell','Marjorie Sung','Midtown'),
('Sgt. Bulwark','Halloran','Foundry Row'),('Sgt. Falkirk','Owen Bramwell','Kingsbridge'),
('Stormwrack','Renata Kovač','Southport'),('The Drift','Beatrice Calloway','Greenway'),
('The Gale','Kip','Eastgate'),('The Longcast','Graham Petrov','Lakeshore'),
('The Undertow','Desmond Okafor','Harborside'),('Vesper','Aunt Dot','Old Town')]
start = datetime(2026,6,29)
end = datetime(2026,9,7)
release = datetime(2026,8,12)
pre_end = datetime(2026,8,10)
post_start = datetime(2026,8,17)
weeks = [start + timedelta(days=7*i) for i in range(10)]
colors = {'taken':'#15866f','turned down':'#d4982d','missed':'#d9546b'}
rows = list(csv.DictReader((SOURCE/'all-pings.csv').open()))
assert len(rows) == 1696
assert sum(r['outcome']=='taken' for r in rows) == 1222
assert set(r['outcome'] for r in rows) == set(colors)
assert len({tuple(r.values()) for r in rows}) == len(rows)
for r in rows:
    # The database column is local time without a timezone; do not convert it.
    r['at'] = datetime.fromisoformat(r['sent_at'].replace('Z',''))

def outcomes(events):
    c = Counter(r['outcome'] for r in events)
    return {k:c[k] for k in colors}

data=[]
for name,handler,area in roster:
    events = sorted((r for r in rows if r['responder']==name),key=lambda r:(r['at'],int(r['callout_number'])))
    assert len({r['at'] for r in events}) == len(events), 'Ordering needs a tie rule'
    weekly=[outcomes([r for r in events if w<=r['at']<w+timedelta(days=7)]) for w in weeks]
    pre=[r for r in events if r['at']<pre_end]
    post=[r for r in events if r['at']>=post_start]
    before,after=len(pre)/6,len(post)/3
    pct=(after/before-1)*100
    score=50; low=0; high=100
    path=[{'date':start.isoformat(),'score':.5,'low':0,'high':1}]
    pre_score=.5
    for r in events:
        delta=8 if r['outcome']=='taken' else -12
        score=max(0,min(100,score+delta));low=max(0,min(100,low+delta));high=max(0,min(100,high+delta))
        path.append({'date':r['at'].isoformat(),'score':score/100,'low':low/100,'high':high/100,'outcome':r['outcome'],'callout':r['callout_number']})
        if r['at']<pre_end: pre_score=score/100
    all_outcomes=outcomes(events)
    final_week=sum(weekly[-1].values())
    story=f'Offers per week {"fell" if pct<0 else "rose"} {abs(pct):.1f}%; final week: {final_week} offers, {weekly[-1]["taken"]} accepted.'
    data.append(dict(name=name,handler=handler,area=area,weekly=weekly,path=path,pre=outcomes(pre),post=outcomes(post),
        totals=all_outcomes,before=before,after=after,change=pct,pre_score=pre_score,end_score=score/100,end_low=low/100,end_high=high/100,story=story))

# Reconcile independently exported weekly counts, including the zero week.
observed={(r['responder'],r['week_start']):(int(r['pings']),int(r['taken'])) for r in csv.DictReader((SOURCE/'responder-week-rows.csv').open())}
for item in data:
    for w,c in zip(weeks,item['weekly']):
        assert observed[item['name'],w.date().isoformat()]==(sum(c.values()),c['taken'])
(OUT/'journeys-data.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
with (OUT/'responder-summary.csv').open('w') as f:
    writer=csv.writer(f)
    writer.writerow(['responder','handler','usual_area','pings_per_week_before','pings_per_week_after','change_percent','pre_taken','pre_turned_down','pre_missed','post_taken','post_turned_down','post_missed','MODEL_score_Aug9','MODEL_score_Sep6','MODEL_end_start0','MODEL_end_start1'])
    for a in data:writer.writerow([a['name'],a['handler'],a['area'],a['before'],a['after'],a['change'],*a['pre'].values(),*a['post'].values(),a['pre_score'],a['end_score'],a['end_low'],a['end_high']])

# Export four readable sheets, four responders each. Every chart uses the same axes.
groups=[['Farlight','Meteor Mite','The Undertow','Vesper'],['The Gale','Nightwell','Stormwrack','Captain Vantage'],
        ['Sgt. Falkirk','Cindermark','Ironvale','Sgt. Bulwark'],['Corporal Ashgrove','Halfmoon','The Drift','The Longcast']]
titles=['The four largest drops in offers','More offers: four responder journeys','More offers: four more journeys','Two smaller declines and two increases']

def font(n):return ImageFont.load_default(size=n)
for group_num,(names,title) in enumerate(zip(groups,titles),1):
    im=Image.new('RGB',(1800,2050),'#f1f5fa');d=ImageDraw.Draw(im)
    def text(x,y,s,n=25,c='#20314a'):d.text((x,y),str(s),font=font(n),fill=c)
    text(50,30,title,43)
    text(50,90,'Actual pings: 29 Jun-6 Sep 2026 | Blue score lines are a model, not recorded scores.',25)
    text(50,135,'Weekly bars: green = accepted  |  gold = declined  |  pink = missed  |  grey = release week',24)
    for i,name in enumerate(names):
        a=next(a for a in data if a['name']==name)
        x=40+(i%2)*880;y=200+(i//2)*880
        d.rounded_rectangle((x,y,x+840,y+850),radius=20,fill='white',outline='#cfdae8',width=2)
        text(x+25,y+20,a['name'],37)
        text(x+25,y+70,f"{a['handler']} | {a['area']}",23,'#596d86')
        text(x+25,y+112,f"Offers/week: {a['before']:.1f} to {a['after']:.1f} ({a['change']:+.1f}%)",26)
        text(x+25,y+155,'ACTUAL weekly offers',23)
        bx=x+65;by=y+212;bw=730;bh=205;slot=bw/10
        d.rectangle((bx+6*slot,by-10,bx+7*slot,by+bh+3),fill='#e7ebf0')
        for tick in (0,5,10,15,20,25):
            yy=by+bh-bh*tick/25
            d.line((bx,yy,bx+bw,yy),fill='#e3e9f0');text(bx-35,yy-10,tick,18,'#65768c')
        for j,c in enumerate(a['weekly']):
            bottom=by+bh;xx=bx+j*slot+13
            for outcome,color in colors.items():
                height=bh*c[outcome]/25
                if height:d.rectangle((xx,bottom-height,xx+slot-26,bottom),fill=color)
                bottom-=height
            text(xx,by+bh+9,sum(c.values()),19)
        text(bx,by+bh+40,'29 Jun',18);text(bx+6*slot-15,by+bh+40,'10 Aug*',18);text(bx+9*slot-5,by+bh+40,'31 Aug',18)
        text(x+25,y+505,'MODEL history score: starts at 0.50 on 29 Jun',23,'#285ca8')
        sx=x+65;sy=y+557;sw=730;sh=130
        def px(date):return sx+(datetime.fromisoformat(date)-start).total_seconds()/(end-start).total_seconds()*sw
        def py(score):return sy+(1-score)*sh
        for tick in (0,.5,1):
            d.line((sx,py(tick),sx+sw,py(tick)),fill='#e3e9f0');text(sx-45,py(tick)-10,f'{tick:.1f}',18,'#65768c')
        rx=px(release.isoformat());d.line((rx,sy,rx,sy+sh),fill='#7e8da2',width=2)
        points=[(sx,py(.5))]
        previous=.5
        for event in a['path'][1:]:
            xx=px(event['date']);points.extend([(xx,py(previous)),(xx,py(event['score']))]);previous=event['score']
        points.append((sx+sw,py(previous)));d.line(points,fill='#2863b4',width=3)
        text(sx,sy+sh+8,'29 Jun',18);text(rx-25,sy+sh+8,'12 Aug',18);text(sx+sw-53,sy+sh+8,'6 Sep',18)
        text(x+25,y+735,f"Model score: 9 Aug {a['pre_score']:.2f} to 6 Sep {a['end_score']:.2f}",25,'#285ca8')
        total=a['totals'];text(x+25,y+779,f"All offers: {sum(total.values())} | Yes {total['taken']} | No {total['turned down']} | Missed {total['missed']}",23)
    text(50,1980,'Before: 6 complete weeks to 9 Aug. After: 3 complete weeks from 17 Aug. *10 Aug week spans release.',22)
    text(50,2012,'Score replay: +0.08 accepted; -0.12 declined/missed; limited to 0-1. Times approximate outcome order.',22)
    im.save(OUT/f'responders-{group_num}.png')

# Standalone interactive explorer with weekly and event-level inspection.
page='''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Every responder's ping journey</title><style>
*{box-sizing:border-box}body{margin:0;background:#f1f5fa;color:#20314a;font:16px system-ui,sans-serif}main{max-width:1240px;margin:auto;padding:32px}h1{font-size:36px;margin:0 0 12px}h2{margin:0 0 8px}p{line-height:1.6}a{color:#285ca8}.note{background:#e5edf9;border-left:5px solid #2863b4;padding:16px;border-radius:8px}.controls{display:flex;gap:12px;flex-wrap:wrap;align-items:center;margin:20px 0}select,input{font:inherit;padding:9px;border:1px solid #bac9dd;border-radius:6px}article{background:white;border:1px solid #d0dbea;border-radius:15px;padding:24px;margin:24px 0}.stats{display:flex;gap:30px;flex-wrap:wrap}.stats b{font-size:28px;display:block}.muted{color:#5f7189}.legend{display:flex;gap:18px;flex-wrap:wrap;font-size:14px}.key{display:inline-block;width:12px;height:12px;margin-right:5px}svg{width:100%;height:auto;display:block;margin:16px 0}table{border-collapse:collapse;width:100%;font-size:14px}td,th{text-align:right;padding:9px;border-bottom:1px solid #e0e7f0}td:first-child,th:first-child{text-align:left}.scroll{overflow:auto;max-height:440px}summary{cursor:pointer;color:#285ca8;margin:15px 0}.jump{display:flex;gap:8px;flex-wrap:wrap}.jump a{padding:5px 9px;border:1px solid #cbd7e7;border-radius:20px;text-decoration:none}button{padding:8px 12px;cursor:pointer}footer{margin:30px 0}.warn{color:#953f52} @media print{.controls,.jump{display:none}article{break-inside:avoid}}
</style><main><h1>Every responder's ping journey</h1><p>16 responders · 1,696 actual pings · 29 June-6 September 2026. Bars show offers, not confirmed phone delivery.</p>
<div class="note"><b>The blue score line is a reconstruction, not an observed score.</b> It starts everyone at 0.50 on 29 June, applies +0.08 for accepting and -0.12 for declining or missing, and limits scores to 0-1. Starting scores, actual rankings, historical availability and outcome times are absent. Events are replayed in sent-time order; the score change is drawn at send time as an approximation. No waiting-time recovery is added. This is the history component only, not the complete job-specific ranking score.</div>
<p>Volume comparison: six full weeks, 29 June-9 August, versus three full weeks, 17 August-6 September. The mixed week of 10-16 August is shown but excluded from the before/after averages. The vertical line marks 12 August; grey bars mark the mixed week.</p>
<div class="controls"><label>Responder <select id="who"><option value="all">All 16 responders</option></select></label><label>Assumed starting score <input id="initial" type="number" min="0" max="1" step="0.01" value="0.50"></label><button id="reset">Reset to 0.50</button></div><nav class="jump" id="jump"></nav><div id="cards"></div>
<footer><p><b>How to read this:</b> Green = accepted, gold = declined, pink = missed. Hover over bars or the blue line for numbers. Expand the tables for exact weekly counts and every recorded offer.</p><p>Sources: Rook database responders and pings; saved all-pings.csv; dispatch-routing/history.py, offer.py and config.py. Coverage was checked against the database. No score table exists among its five tables. Scores in this model cannot establish why offers changed or prove deployed behavior matches the supplied code.</p></footer></main><script>const data=__DATA__;
const palette={'taken':'#15866f','turned down':'#d4982d','missed':'#d9546b'},keys=Object.keys(palette);
const weeks=['29 Jun','6 Jul','13 Jul','20 Jul','27 Jul','3 Aug','10 Aug','17 Aug','24 Aug','31 Aug'];
const begin=Date.parse('2026-06-29T00:00:00Z'),finish=Date.parse('2026-09-07T00:00:00Z');
const sum=o=>Object.values(o).reduce((a,b)=>a+b,0);const date=s=>Date.parse(s+'Z');
const escape=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const slug=s=>s.toLowerCase().replace(/[^a-z]+/g,'-');
function bars(a){let s='<svg viewBox="0 0 1000 290" role="img" aria-label="Actual weekly offers for '+escape(a.name)+'">';
 const x0=50,y0=225,h=185,w=910,slot=w/10;s+=`<rect x="${x0+6*slot}" y="20" width="${slot}" height="210" fill="#e7ebf0"/>`;
 for(let t=0;t<=25;t+=5){let y=y0-t/25*h;s+=`<line x1="50" x2="960" y1="${y}" y2="${y}" stroke="#dce5ef"/><text x="20" y="${y+5}" font-size="14">${t}</text>`}
 a.weekly.forEach((c,i)=>{let bottom=y0;keys.forEach(k=>{let bh=c[k]/25*h;bottom-=bh;s+=`<rect x="${x0+i*slot+14}" y="${bottom}" width="${slot-28}" height="${bh}" fill="${palette[k]}"><title>${weeks[i]}: ${k} ${c[k]}; total ${sum(c)}</title></rect>`});s+=`<text x="${x0+i*slot+slot/2}" y="${y0-sum(c)/25*h-8}" text-anchor="middle" font-size="15">${sum(c)}</text><text x="${x0+i*slot+slot/2}" y="252" text-anchor="middle" font-size="13">${weeks[i]}</text>`});return s+'</svg>'}
function replay(a,initial){let v=initial;return [{date:'2026-06-29T00:00:00',score:v},...a.path.slice(1).map(p=>{v=Math.max(0,Math.min(1,Math.round((v+(p.outcome==='taken'?.08:-.12))*10000)/10000));return {...p,score:v}})]}
function line(path){const x=s=>50+(date(s)-begin)/(finish-begin)*910,y=v=>170-v*140;let s='<svg viewBox="0 0 1000 225" role="img" aria-label="Modeled history score, not recorded score">';[0,.5,1].forEach(t=>s+=`<line x1="50" x2="960" y1="${y(t)}" y2="${y(t)}" stroke="#dce5ef"/><text x="12" y="${y(t)+5}" font-size="14">${t.toFixed(1)}</text>`);let rx=x('2026-08-12T00:00:00');s+=`<line x1="${rx}" x2="${rx}" y1="20" y2="175" stroke="#7e8da2" stroke-dasharray="5 5"/>`;let points=`50,${y(path[0].score)}`,last=path[0].score;path.slice(1).forEach(p=>{points+=` ${x(p.date)},${y(last)} ${x(p.date)},${y(p.score)}`;last=p.score});points+=` 960,${y(last)}`;s+=`<polyline points="${points}" fill="none" stroke="#2863b4" stroke-width="2.3"/>`;path.slice(1).forEach(p=>s+=`<circle cx="${x(p.date)}" cy="${y(p.score)}" r="4" fill="transparent"><title>${escape(p.date.replace('T',' '))}: ${p.outcome}; model ${p.score.toFixed(2)}</title></circle>`);s+=`<text x="50" y="204" font-size="14">29 Jun</text><text x="${rx-20}" y="204" font-size="14">12 Aug</text><text x="920" y="204" font-size="14">6 Sep</text>`;return s+'</svg>'}
function render(){const sel=document.querySelector('#who').value;let n=Number(document.querySelector('#initial').value);if(!Number.isFinite(n))n=.5;n=Math.max(0,Math.min(1,n));document.querySelector('#cards').innerHTML=data.filter(a=>sel==='all'||sel===a.name).map(a=>{let path=replay(a,n),last=path.at(-1).score,pre=path.filter(p=>date(p.date)<Date.parse('2026-08-10T00:00:00Z')).at(-1).score;let p=a.post;return `<article id="${slug(a.name)}"><h2>${escape(a.name)}</h2><p class="muted">Handler: ${escape(a.handler)} · Usual area: ${escape(a.area)}</p><p>${a.story}</p><div class="stats"><div><b>${a.before.toFixed(1)} → ${a.after.toFixed(1)}</b>actual offers per week</div><div><b>${a.change.toFixed(1)}%</b>change in offers per week</div><div><b>${pre.toFixed(2)} → ${last.toFixed(2)}</b>MODEL score: 9 Aug to 6 Sep</div></div><h3>Actual offers and outcomes each week</h3><div class="legend">${keys.map(k=>`<span><i class="key" style="background:${palette[k]}"></i>${k==='taken'?'accepted':k==='turned down'?'declined':'missed'}</span>`).join('')}</div>${bars(a)}<p>Full post-release weeks: <b>${sum(p)}</b> offers — ${p.taken} accepted, ${p['turned down']} declined, ${p.missed} missed. Accepted ${(100*p.taken/sum(p)).toFixed(1)}% of offers received.</p><h3>Modeled history score</h3>${line(path)}<p class="muted">Assumed starting score ${n.toFixed(2)}. No offer means no score change. Under this replay, starting at either 0 or 1 gives an ending score range of ${a.end_low.toFixed(2)}-${a.end_high.toFixed(2)}; this sensitivity check does not validate real production scores.</p><details><summary>Exact weekly counts</summary><div class="scroll"><table><tr><th>Week starting</th><th>Offers</th><th>Accepted</th><th>Declined</th><th>Missed</th></tr>${a.weekly.map((w,i)=>`<tr><td>${weeks[i]}${i===6?' (mixed)':''}</td><td>${sum(w)}</td><td>${w.taken}</td><td>${w['turned down']}</td><td>${w.missed}</td></tr>`).join('')}</table></div></details><details><summary>Every offer and the modeled score after its outcome</summary><p class="muted">Timestamp shown is when the offer was sent, not when the answer or timeout occurred.</p><div class="scroll"><table><tr><th>Sent (database local time)</th><th>Callout</th><th>Outcome</th><th>Modeled score</th></tr>${path.slice(1).map(p=>`<tr><td>${p.date.replace('T',' ')}</td><td>${p.callout}</td><td>${p.outcome}</td><td>${p.score.toFixed(2)}</td></tr>`).join('')}</table></div></details></article>`}).join('')}
data.forEach(a=>{let op=document.createElement('option');op.value=a.name;op.textContent=a.name;document.querySelector('#who').append(op)});document.querySelector('#jump').innerHTML=data.map(a=>`<a href="#${slug(a.name)}">${escape(a.name)}</a>`).join('');document.querySelector('#who').addEventListener('change',render);document.querySelector('#initial').addEventListener('input',render);document.querySelector('#reset').onclick=()=>{document.querySelector('#initial').value='.50';render()};render();</script></html>'''
(OUT/'responder-journeys.html').write_text(page.replace('__DATA__',json.dumps(data,ensure_ascii=False)))

lines=['# All responder journeys: actual pings and modeled history scores','',
'Coverage: 29 June-6 September 2026; 1,696 pings, 1,222 taken, 16 responders. Database coverage and roster checked during this analysis.',
'','Actual weekly counts match all 160 saved responder-week rows. Six complete pre-release weeks are compared with three complete post-release weeks; 10-16 August is excluded from averages.',
'','Scores are simulations, not observed database values. No recorded history score, rank, availability or outcome timestamp exists in the retrieved tables. Start at 0.50 on 29 June; apply code rules in sent-time order, immediately after each modeled outcome. Clamp every event to 0-1. These are not full ranking scores and cannot establish causation or production deployment. Lines use send time as an approximation; actual score updates happen after answers/timeouts. No timezone conversion is applied.',
'','Starting-value sensitivity: replay separately from 0 and 1 and report the ending interval. Convergence only removes this particular starting-value uncertainty under the model; it does not validate production behavior.',
'','| Responder | Pings/week before | After | Change | Model score 9 Aug | Model 6 Sep | Post offers: accepted / declined / missed |',
'|---|---:|---:|---:|---:|---:|---|']
for a in data:lines.append(f"| {a['name']} | {a['before']:.1f} | {a['after']:.1f} | {a['change']:+.1f}% | {a['pre_score']:.2f} | {a['end_score']:.2f} | {a['post']['taken']} / {a['post']['turned down']} / {a['post']['missed']} |")
lines+=['','Source files: ../dispatch-4.2-analysis/all-pings.csv and responder-week-rows.csv; ../../00-rook/code/dispatch-routing/{history,config,offer,routing}.py. Roster: SELECT name, handler, area FROM rook.responders ORDER BY name. Coverage: SELECT COUNT(*), MIN(sent_at), MAX(sent_at) FROM rook.pings.']
(OUT/'method-and-findings.md').write_text('\n'.join(lines)+'\n')
print('\n'.join(lines[-19:-1]))
print('Written: four PNG sheets, standalone HTML explorer, JSON, CSV and methodology. All 160 weekly rows reconciled.')
