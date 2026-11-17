import sys
P=dict(ground="#14100F",sunken="#1A1514",base="#201A19",panel="#27201E",raised="#302826",lifted="#3B312E",ink="#F1E6D2",muted="#C2B4A3",faint="#867969",rule="#3A302C",rs="#8F8071",signal="#F29A4A",cue="#74C6E8",ph="#93D79B",alert="#F2705E",glow="#FFB070",pink="#D98FC0")
grain='<svg class="grain" width="1920" height="1080"><filter id="n"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2" stitchTiles="stitch"/><feColorMatrix values="0 0 0 0 .5 0 0 0 0 .5 0 0 0 0 .5 0 0 0 .9 0"/></filter><rect width="100%" height="100%" filter="url(#n)"/></svg>'
def seg(n,on,col,off):
    return '<span class="seg">'+''.join(f'<i style="background:{col if k<on else off}"></i>' for k in range(n))+'</span>'
def page(title,body,css,concept_col):
    return f'<!doctype html><meta charset=utf-8><title>{title}</title><link rel=stylesheet href=common.css><style>{css}</style><body>{body}{grain}<div class=concept style="color:{concept_col}">CONCEPT RENDER</div></body>'
# ---------- chosen: Dusk specimen
p=P
css=f'''body{{background:radial-gradient(1200px 700px at 30% 25%,#4a2c1c 0%,#2a1b17 38%,{p["ground"]} 80%);color:{p["ink"]}}}
.lamp{{position:absolute;left:-100px;top:-120px;width:900px;height:700px;background:radial-gradient(closest-side,rgba(255,176,112,.20),transparent);z-index:1}}
.rim{{position:absolute;right:-200px;bottom:-200px;width:900px;height:700px;background:radial-gradient(closest-side,rgba(116,198,232,.10),transparent)}}
.vig{{background:radial-gradient(ellipse at 50% 45%,transparent 55%,rgba(0,0,0,.45))}}
.top{{position:absolute;left:18px;right:18px;top:14px;height:34px;background:{p["base"]};border:1px solid {p["rule"]};border-radius:3px;display:flex;align-items:center;padding:0 12px;gap:22px;z-index:5;box-shadow:inset 0 1px 0 rgba(255,214,170,.07)}}
.bot{{position:absolute;left:0;right:0;bottom:0;height:28px;background:{p["base"]};border-top:1px solid {p["rule"]};display:flex;align-items:center;padding:0 16px;gap:26px;z-index:5;font-size:12px}}
.ws{{display:flex;gap:4px}}.ws b{{width:22px;height:20px;border:1px solid {p["rule"]};font:500 11px "IBM Plex Mono";display:grid;place-items:center;color:{p["muted"]}}}
.ws b.on{{border-color:{p["signal"]};color:{p["signal"]};box-shadow:0 1px 0 {p["signal"]},0 0 6px rgba(242,154,74,.35)}}
.led{{display:inline-block;width:7px;height:7px;border-radius:50%;margin-right:7px;vertical-align:1px}}
.panel{{position:absolute;background:{p["panel"]};border:1px solid {p["rule"]};border-radius:3px;z-index:4;box-shadow:inset 0 1px 0 rgba(255,214,170,.08),0 18px 40px rgba(0,0,0,.35)}}
.panel h3{{padding:10px 14px;border-bottom:1px solid {p["rule"]};color:{p["muted"]}}}
.well{{background:{p["sunken"]};border:1px solid {p["rule"]};border-radius:2px;padding:8px 10px}}
.row{{display:flex;justify-content:space-between;align-items:center;padding:7px 14px}}
.big{{font:300 120px/1 "IBM Plex Sans Condensed";letter-spacing:-.02em}}
.plate{{font:600 12px "IBM Plex Sans Condensed";letter-spacing:.14em;text-transform:uppercase;color:{p["ink"]};border:1px solid {p["rs"]};padding:2px 8px;border-radius:2px;background:{p["sunken"]}}}
.cream{{position:absolute;background:#E8DCC4;color:#2a1b17;font:500 12px "IBM Plex Mono";padding:6px 10px;transform:rotate(-1.2deg);z-index:6;border-radius:1px;box-shadow:0 2px 0 rgba(0,0,0,.35)}}
'''
body=f'''<div class=lamp></div><div class=rim></div><div class=vig></div>
<div class=top><span class="ws"><b class=on>1</b><b>2</b><b>3</b><b>4</b></span><span class=mono style="font-size:12px;color:{p["muted"]}">kitty — ~/taller</span><span style="flex:1"></span>
<span class=cond style="font-size:18px;font-weight:500">21:47</span><span style="flex:1"></span>
<span class=eyebrow style="color:{p["muted"]}"><span class=led style="background:{p["ph"]}"></span>NET</span><span class=eyebrow style="color:{p["muted"]}">VOL <span style="color:{p["ink"]}">64</span></span><span class=eyebrow style="color:{p["signal"]}"><span class=led style="background:{p["signal"]};box-shadow:0 0 6px {p["glow"]}"></span>EN VIVO</span></div>
<div class=panel style="left:90px;top:130px;width:520px;height:330px"><h3 class=eyebrow>01 · Taller</h3>
<div style="padding:20px 24px"><div class=big>21:47</div><div class=mono style="color:{p["muted"]};margin-top:10px;font-size:14px">MAR 17 NOV · BUENOS AIRES · 24°C</div>
<div style="margin-top:24px;display:flex;gap:10px"><span class=plate>Hornero</span><span class=plate style="color:{p["signal"]};border-color:{p["signal"]}">Dusk</span></div></div></div>
<div class=panel style="left:650px;top:130px;width:540px;height:370px"><h3 class=eyebrow>02 · Instrumentos</h3>
<div class=row><span class=eyebrow style="color:{p["muted"]}">CPU</span>{seg(20,7,p["signal"],p["raised"])}<span class=mono style="width:70px;white-space:nowrap;text-align:right">34 %</span></div>
<div class=row><span class=eyebrow style="color:{p["muted"]}">MEM</span>{seg(20,12,p["cue"],p["raised"])}<span class=mono style="width:70px;white-space:nowrap;text-align:right">8,4 G</span></div>
<div class=row><span class=eyebrow style="color:{p["muted"]}">DISCO</span>{seg(20,5,p["ph"],p["raised"])}<span class=mono style="width:70px;white-space:nowrap;text-align:right">212 G</span></div>
<div class=row><span class=eyebrow style="color:{p["muted"]}">TEMP</span>{seg(20,9,p["pink"],p["raised"])}<span class=mono style="width:70px;white-space:nowrap;text-align:right">58 °C</span></div>
<div style="padding:10px 14px"><div class=well><svg width="480" height="90" viewBox="0 0 480 90"><g stroke="{p["rule"]}" stroke-width="1">{"".join(f'<line x1="{x}" y1="0" x2="{x}" y2="90"/>' for x in range(0,481,40))}{"".join(f'<line x1="0" y1="{y}" x2="480" y2="{y}"/>' for y in range(0,91,30))}</g>
<polyline fill="none" stroke="{p["ph"]}" stroke-width="2" points="0,60 40,52 80,58 120,30 160,38 200,22 240,48 280,40 320,62 360,34 400,44 440,28 480,36"/></svg></div></div></div>
<div class=panel style="left:1230px;top:130px;width:360px;height:330px"><h3 class=eyebrow>03 · Estado</h3>
<div class=row><span>Red</span><span><span class=led style="background:{p["ph"]}"></span><span class=mono>Conectada</span></span></div>
<div class=row><span>Batería</span><span class=mono>82 %  ·  3 h 40</span></div>
<div class=row><span>Modo</span><span class=plate>Cotidiano</span></div>
<div class=row><span>Alerta</span><span><span class=led style="background:{p["alert"]}"></span><span class=mono>1 pendiente</span></span></div>
<div style="padding:10px 14px;color:{p["muted"]};font-size:13px;line-height:1.5">Ya está lista la mesa. Pasá, sentate.</div></div>
<div class=cream style="left:1250px;top:520px">// la luz de la lámpara es una señal, no un efecto</div>
<div class=panel style="left:90px;top:520px;width:1100px;height:330px;background:{p["base"]}"><h3 class=eyebrow>04 · Terminal</h3>
<pre class=mono style="padding:16px 20px;font-size:14px;line-height:1.7;color:{p["ink"]}"><span style="color:{p["ph"]}">javi@hornero</span> <span style="color:{p["cue"]}">~/taller</span> $ horneroctl appearance chromatic
<span style="color:{p["muted"]}">paleta derivada del fondo · 4 variantes · contraste AA ok</span>
<span style="color:{p["signal"]}">&gt;&gt;</span> aplicado: <span style="color:{p["pink"]}">dusk-rosa-vieja</span>
<span style="color:{p["ph"]}">javi@hornero</span> <span style="color:{p["cue"]}">~/taller</span> $ <span style="background:{p["signal"]};color:#1C1006"> </span></pre></div>
<div class=bot><span class=eyebrow style="color:{p["muted"]}">HORNERO · SIGNAL DUSK</span><span class=mono style="color:{p["muted"]}">↑ 1,2 MB/s</span><span class=mono style="color:{p["muted"]}">↓ 14,6 MB/s</span><span style="flex:1"></span><span class=eyebrow style="color:{p["muted"]}">lámpara 0,8 · grano 0,3 · viñeta 0,4</span></div>'''
open('dusk.html','w').write(page('dusk',body,css,p["muted"]))
