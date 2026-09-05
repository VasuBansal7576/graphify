import json
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
root=Path(__file__).resolve().parent
receipt=json.loads((root/'receipt.json').read_text())
font=lambda n:ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf',n)
im=Image.new('RGB',(1500,860),'#f5f7fa');d=ImageDraw.Draw(im)
d.text((50,35),'Explicit export forwarding: raw graph evidence',font=font(36),fill='#152b49')
d.text((50,94),'Offline audit rendered from actual CLI graph.json. Not a Graphify viewer screenshot.',font=font(23),fill='#52647d')
d.text((50,145),'base.ts defines VALUE. bridge.ts imports VALUE and exports that local binding.',font=font(24),fill='#152b49')
d.text((50,185),'api.ts re-exports VALUE from bridge.ts.',font=font(24),fill='#152b49')
for i,stage in enumerate(['before','after']):
 x=50+i*725;r=receipt['results'][stage];g=json.loads((root/f'{stage}.json').read_text());edge=next(e for e in g['edges'] if e['source']=='api' and e['relation']=='re_exports' and e['context']=='re-export')
 d.rounded_rectangle((x,245,x+675,620),radius=12,fill='white',outline='#d7deea',width=2)
 d.text((x+25,267),stage.title(),font=font(32),fill='#152b49')
 d.text((x+25,326),f"{r['nodes']} nodes | {r['edges']} edge records",font=font(26),fill='#152b49')
 d.text((x+25,384),'api --re_exports--> '+edge['target'],font=font(24),fill='#152b49')
 d.text((x+25,445),'Missing targets: '+str(len(r['missing_target_edges'])),font=font(27),fill='#ad3232' if stage=='before' else '#18764b')
 d.text((x+25,515),'Source site: api.ts, L1',font=font(24),fill='#52647d')
 d.text((x+25,561),'All edge records retained.',font=font(23),fill='#52647d')
d.text((50,653),'Before: bridge_value has no node. After: base_value is the existing definition.',font=font(23),fill='#152b49')
for i,stage in enumerate(['before','after']):d.text((50,709+i*40),stage+' SHA-256: '+receipt['results'][stage]['sha256'],font=font(18),fill='#52647d')
im.save(root/'raw-graph-audit.png')
