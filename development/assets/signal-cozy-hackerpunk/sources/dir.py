def col(name,sub,bg,panel,rule,ink,mut,acc,acc2,extra,notes,chosen=False):
    return f'''<section style="background:{bg};color:{ink}">
<header><div class=eyebrow style="color:{mut}">{sub}</div><h2 class=cond>{name}{' <em>ELEGIDA</em>' if chosen else ''}</h2></header>
<div class=scene style="border-color:{rule}">
<div class=bar style="background:{panel};border-color:{rule}"><b style="color:{acc};border:1px solid {acc};padding:0 6px">1</b><span class=mono style="color:{mut}">2 3 4</span><span style="flex:1"></span><span class=cond style="font-size:17px">21:47</span><span style="flex:1"></span><span class="eyebrow" style="color:{acc}">● EN VIVO</span></div>
<div class=card style="background:{panel};border-color:{rule};{extra}"><div class=eyebrow style="color:{mut}">01 · AUDIO</div>
<div style="display:flex;gap:4px;margin:14px 0">{"".join(f'<i style="width:9px;height:20px;background:{acc if k<9 else rule}"></i>' for k in range(18))}<span class=mono style="margin-left:10px">64</span></div>
<div style="display:flex;gap:4px">{"".join(f'<i style="width:9px;height:10px;background:{acc2 if k<6 else rule}"></i>' for k in range(18))}</div></div>
<div class=card style="background:{panel};border-color:{rule};margin-top:14px;{extra}"><div class=big2 class=cond>Pasá, sentate.</div><div class=mono style="color:{mut};font-size:12px;margin-top:6px">tres paletas, una sola lámpara</div></div>
</div><ul style="color:{ink}">{notes}</ul></section>'''
A=col("A · Bezel Cálido","LÁMPARA SOBRE EL BANCO","radial-gradient(500px 300px at 20% 10%,#4a2c1c,#14100F 70%)","#201A19","#3A302C","#F1E6D2","#C2B4A3","#F29A4A","#74C6E8","box-shadow:inset 0 1px 0 rgba(255,214,170,.1)","<li>Signal Bezel, luz cálida como instrumento</li><li>Costo: casi nulo (alphas + 1 textura)</li><li>Riesgo: parecer solo oscuro marrón</li>",True)
B=col("B · Taller","RADIOAFICIONADO / CHAPA PINTADA","linear-gradient(#2b2a22,#1e211c)","#2f3128","#55573f","#EADFC2","#BDB596","#E0A33A","#9DC27A","border-radius:2px;box-shadow:0 0 0 3px #1e211c,0 0 0 4px #55573f","<li>Chapa verde oliva, etiquetas papel, tornillos</li><li>Costo: texturas por superficie, más ruido</li><li>Riesgo: skeuomorfismo, fatiga en días largos</li>")
C=col("C · Noche Norteña","ELECTRO-FOLK / NEÓN VIOLETA","linear-gradient(160deg,#1b1030,#0f0a1d 60%,#07131c)","#1b1330","#3b2a63","#F2E8FF","#BBA9E0","#FF5CAB","#43E0E8","box-shadow:0 0 18px rgba(255,92,171,.25)","<li>Magenta/cian saturados, glow como lenguaje</li><li>Costo: blur en todo, GlowBudget roto</li><li>Riesgo: negro+neón genérico, choca con Signal</li>")
html=f'''<!doctype html><meta charset=utf-8><link rel=stylesheet href=common.css><style>
body{{background:#0b0908;display:grid;grid-template-columns:repeat(3,640px);color:#eee}}
section{{padding:36px 40px;height:1080px;position:relative}}
h2{{font-size:36px;font-weight:500;margin:6px 0 24px}}h2 em{{font:600 11px "IBM Plex Mono";letter-spacing:.12em;border:1px solid currentColor;padding:2px 8px;vertical-align:middle;margin-left:10px}}
.scene{{border:1px solid;padding:16px;height:560px}}.bar{{display:flex;gap:12px;align-items:center;padding:6px 12px;border:1px solid;margin-bottom:16px}}
.card{{border:1px solid;padding:16px}}.big2{{font:300 40px "IBM Plex Sans Condensed"}}ul{{margin-top:28px;font-size:15px;line-height:1.9;padding-left:20px}}
.concept{{bottom:16px}}</style><body>{A}{B}{C}<div class=concept style="color:#C2B4A3">CONCEPT RENDER · TRES DIRECCIONES</div></body>'''
open('dir.html','w').write(html)
