import json
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
root=Path(__file__).resolve().parent
receipt=json.loads((root/'receipt.json').read_text())
font=lambda size:ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf',size)
for label,r in receipt['results'].items():
 image=Image.new('RGB',(1440,800),'#f5f7fa');draw=ImageDraw.Draw(image)
 draw.text((50,35),f'{label.title()}: declaration ownership guard',font=font(36),fill='#152b49')
 draw.text((50,92),'Offline-rendered raw-graph audit report. Not a Graphify viewer screenshot.',font=font(22),fill='#52647d')
 for i,(n,title) in enumerate([(r['nodes'],'nodes'),(r['edges'],'edge records'),(len(r['missing_source_edges']),'missing source endpoints')]):
  x=50+i*435;draw.rounded_rectangle((x,145,x+400,265),radius=12,fill='white',outline='#d7deea',width=2)
  draw.text((x+25,160),str(n),font=font(46),fill='#152b49');draw.text((x+25,219),title,font=font(22),fill='#52647d')
 draw.text((50,300),'All inheritance and type-reference records',font=font(26),fill='#152b49')
 g=json.loads((root/label/'graph.json').read_text());ids={n['id'] for n in g['nodes']}
 columns=[50,590,790,1120]
 for x,title in zip(columns,['Source','Relation','Target','Source node']):draw.text((x,355),title,font=font(22),fill='#52647d')
 y=401
 for e in g['edges']:
  if e['relation'] not in ('inherits','references'):continue
  draw.line((50,y-9,1380,y-9),fill='#d7deea',width=1)
  for x,text in zip(columns,[e['source'],e['relation'],e['target'],'present' if e['source'] in ids else 'MISSING']):draw.text((x,y),text,font=font(23),fill='#152b49' if text!='MISSING' else '#b63232')
  y+=47
 draw.text((50,640),'Visible.method -> Result remains present. Hidden and Hidden.method have no extracted nodes.',font=font(22),fill='#152b49')
 draw.text((50,698),'Base: '+receipt['base_revision'],font=font(18),fill='#52647d')
 draw.text((50,730),'Graph SHA-256: '+r['sha256'],font=font(18),fill='#52647d')
 image.save(root/f'{label}.png')
