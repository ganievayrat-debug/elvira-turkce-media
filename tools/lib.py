TOTAL=7
import base64,io,json
from PIL import Image,ImageEnhance
N='assets/'
defs=open(N+'defs.html',encoding='utf-8').read()
im=Image.open(N+'img0.jpg').convert('RGB')
im=ImageEnhance.Contrast(im).enhance(0.9);im=ImageEnhance.Color(im).enhance(0.95)
b=io.BytesIO();im.save(b,'JPEG',quality=90);ph=base64.b64encode(b.getvalue()).decode()
NAVY='#12284c';RED='#d9202e';GOLD='#e2b04a';CREAM='#fbf6ec'
css='''
:root{--navy:#12284c;--red:#d9202e;--gold:#e2b04a;--cream:#fbf6ec;--ink:#3a4a66}
*{box-sizing:border-box;margin:0;padding:0}
body{background:#888;font-family:Manrope,sans-serif}
.s{position:relative;width:1080px;height:1350px;background:var(--cream);overflow:hidden;margin-bottom:20px}
.s::before{content:"";position:absolute;inset:26px;border:3px solid rgba(18,40,76,.14);border-radius:34px;pointer-events:none}
.tag{position:absolute;left:78px;top:70px;font-weight:800;font-size:26px;color:var(--red);letter-spacing:.5px}
.tag small{display:block;font-weight:600;font-size:21px;color:#7b869b;margin-top:4px;letter-spacing:.3px}
.pg{position:absolute;right:78px;top:72px;font-weight:800;font-size:24px;color:var(--navy);background:#fff;border:2.5px solid var(--gold);border-radius:30px;padding:6px 18px}
.ft{position:absolute;left:78px;right:78px;bottom:104px;display:flex;justify-content:space-between;align-items:center;font-weight:700;font-size:24px;color:#7b869b}
.ft b{color:var(--red)}
.tul{position:absolute;left:0;right:0;bottom:0;height:86px}
h1{font-family:'Playfair Display',serif;font-weight:800;color:var(--navy)}
.hd{position:absolute;left:78px;top:176px;right:78px;display:flex;align-items:center;gap:30px}
.hd h1{font-size:92px;line-height:1}
.hd svg{width:130px;height:130px;flex:none}
.sub{position:absolute;left:78px;top:312px;font-size:34px;font-weight:600;color:var(--ink)}
.cards{position:absolute;left:78px;right:78px;top:396px;display:flex;flex-direction:column;gap:22px}
.c{background:#fff;border-radius:44px;padding:28px 40px 30px 70px;position:relative;box-shadow:0 8px 0 rgba(18,40,76,.07),0 14px 30px rgba(18,40,76,.07);border:2px solid rgba(226,176,74,.45)}
.c:nth-child(even){background:#fff7ec}
.c::before{content:"";position:absolute;left:34px;top:30px;bottom:30px;width:6px;border-radius:4px;background:var(--red)}
.tr{font-family:'Playfair Display',serif;font-weight:700;font-size:40px;color:var(--navy);line-height:1.15}
.ru{font-weight:700;font-size:28px;color:var(--red);margin-top:8px}
.n{position:absolute;right:30px;top:24px;width:46px;height:46px;border-radius:50%;background:var(--navy);color:#fff;font-weight:800;font-size:23px;display:flex;align-items:center;justify-content:center}
'''
def tulips():
    cols=[RED,GOLD,'#ffffff']
    s=''.join(f'<use href="#tu" x="{20+i*70}" y="{86-(54+(i%3)*12)}" width="{(54+(i%3)*12)*.6}" height="{54+(i%3)*12}" style="color:{cols[i%3]}"/>' for i in range(15))
    return f'<svg class="tul" viewBox="0 0 1080 86" preserveAspectRatio="none">{s}</svg>'
def ft(n):return f'<div class="ft"><span>@elvira.turkce</span><span>{"Листай →" if n<TOTAL else ""}</span></div>'
def tag(n):return f'<div class="tag">@elvira.turkce<small>турецкий для жизни</small></div><div class="pg">{n} / {TOTAL}</div>'
def ph64(f,box=None,w=700):
    im=Image.open(f).convert('RGB')
    if box:im=im.crop(box)
    im.thumbnail((w,w*2));b=io.BytesIO();im.save(b,'JPEG',quality=88);return base64.b64encode(b.getvalue()).decode()
SV='fill="none" stroke="#12284c" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"'
pan=f'<svg viewBox="0 0 130 130" {SV}><path d="M20 62h72v26a16 16 0 0 1-16 16H36a16 16 0 0 1-16-16z" fill="#fff"/><path d="M92 70h28" stroke-width="9"/><path d="M20 62h72" stroke="#d9202e" stroke-width="8"/><path d="M40 46c-6-8 6-12 0-22M60 46c-6-8 6-12 0-22M80 46c-6-8 6-12 0-22" stroke="#e2b04a"/></svg>'
heart=f'<svg viewBox="0 0 130 130" {SV}><path d="M65 108C18 76 16 38 40 30c12-4 22 2 25 13 3-11 13-17 25-13 24 8 22 46-25 78z" fill="#d9202e"/><path d="M100 18v16M92 26h16M24 96v12M18 102h12" stroke="#e2b04a"/></svg>'
def arch(k,l,t,w,h,rot=0):
    return f'<div style="position:absolute;left:{l}px;top:{t}px;width:{w}px;height:{h}px;border-radius:{w//2}px {w//2}px 28px 28px;overflow:hidden;border:9px solid #fff;box-shadow:0 18px 44px rgba(18,40,76,.2);transform:rotate({rot}deg)"><img src="data:image/jpeg;base64,{P[k]}" style="width:100%;height:100%;object-fit:cover;object-position:50% 18%"></div>'
def cards(rows,top=396,right=380):
    cs=''.join(f'<div class="c" style="padding:22px 24px 24px 60px"><div class="n" style="width:40px;height:40px;font-size:20px;right:18px;top:18px">{i+1}</div><div class="tr" style="font-size:38px">{t}</div><div class="ru" style="font-size:27px">{r}</div></div>' for i,(t,r) in enumerate(rows))
    return f'<div class="cards" style="top:{top}px;right:{right}px;gap:18px">{cs}</div>'
def hd(t,icon):return f'<div class="hd"><h1>{t}</h1>{icon}</div>'
def box(txt,ru,top=1040):
    return f'<div style="position:absolute;left:78px;right:78px;top:{top}px;background:var(--navy);border-radius:32px;padding:26px 36px 30px;box-shadow:0 8px 0 var(--red)"><div style="font-family:\'Playfair Display\',serif;font-weight:700;color:#fff;font-size:42px">{txt}</div><div style="color:var(--gold);font-weight:700;font-size:28px;margin-top:8px">{ru}</div></div>'

S2='fill="#fff" stroke="#12284c" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"'
def ic(body):return f'<svg viewBox="0 0 100 100" style="width:100%;height:100%" {S2}>{body}</svg>'
I_pan=ic('<path d="M16 52h60v24a14 14 0 0 1-14 14H30a14 14 0 0 1-14-14z"/><path d="M76 60h20" stroke-width="8"/><path d="M16 52h60" stroke="#d9202e" stroke-width="7"/><path d="M32 40c-5-7 5-10 0-18M46 40c-5-7 5-10 0-18M60 40c-5-7 5-10 0-18" stroke="#e2b04a" fill="none"/>')
I_book=ic('<rect x="22" y="14" width="52" height="72" rx="6"/><path d="M22 28h52" stroke="#d9202e" stroke-width="6"/><path d="M32 44h32M32 56h32M32 68h20" fill="none"/><g transform="rotate(35 70 60)"><rect x="64" y="34" width="12" height="44" rx="3" fill="#e2b04a"/><path d="M64 78l6 12 6-12z" fill="#d9202e"/></g>')
I_dumb=ic('<rect x="6" y="34" width="14" height="32" rx="5" fill="#d9202e"/><rect x="20" y="42" width="10" height="16" rx="3" fill="#e2b04a"/><rect x="30" y="47" width="40" height="6" rx="3" fill="#12284c"/><rect x="70" y="42" width="10" height="16" rx="3" fill="#e2b04a"/><rect x="80" y="34" width="14" height="32" rx="5" fill="#d9202e"/>')
I_bag=ic('<path d="M36 38v-8a14 14 0 0 1 28 0v8" fill="none"/><path d="M22 38h56l4 48H18z" fill="#d9202e"/><path d="M40 56c3 5 17 5 20 0" stroke="#fff" fill="none"/>')
I_buoy=ic('<circle cx="50" cy="50" r="38"/><circle cx="50" cy="50" r="15" fill="#fbf6ec"/><path d="M23 23l16 16M77 23L61 39M23 77l16-16M77 77L61 61" stroke="#d9202e" stroke-width="14" fill="none"/><circle cx="50" cy="50" r="38" fill="none"/><circle cx="50" cy="50" r="15" fill="none"/>')
I_tul=f'<svg viewBox="0 0 100 100" style="width:100%;height:100%"><use href="#tu" x="22" y="2" width="56" height="94" style="color:#d9202e"/></svg>'
I_please=ic('<path d="M10 20h80a6 6 0 0 1 6 6v34a6 6 0 0 1-6 6H44L28 84V66H10a6 6 0 0 1-6-6V26a6 6 0 0 1 6-6z" fill="#fff7ec"/><text x="50" y="50" text-anchor="middle" font-family="Manrope" font-weight="800" font-size="19" fill="#d9202e" stroke="none">lütfen</text>')
I_think=ic('<path d="M26 60c-14 0-18-20-4-24 0-16 22-20 30-8 8-8 28-2 26 14 14 2 12 22-4 20z" fill="#fff7ec"/><circle cx="30" cy="76" r="6"/><circle cx="20" cy="88" r="3.5"/><text x="50" y="54" text-anchor="middle" font-family="Playfair Display" font-weight="800" font-size="38" fill="#d9202e" stroke="none">?</text>')
I_clock=ic('<circle cx="50" cy="50" r="38"/><circle cx="50" cy="50" r="31" fill="#fff7ec" stroke="#e2b04a"/><path d="M50 26v26l16 10" stroke="#d9202e" stroke-width="6" fill="none"/><circle cx="50" cy="50" r="4" fill="#12284c"/>')
I_check=ic('<rect x="16" y="16" width="68" height="68" rx="14" fill="#fff7ec"/><path d="M30 52l14 14 28-30" stroke="#d9202e" stroke-width="9" fill="none"/>')
def iarch(l,t,w,h,icons,pad=26,bg='#f6e3b4'):
    n=len(icons);g=(h-2*pad)/n
    sz=min(w-60,g-14)
    items=''.join(f'<div style="position:absolute;left:{(w-sz)/2}px;top:{pad+i*g+(g-sz)/2}px;width:{sz}px;height:{sz}px">{x}</div>' for i,x in enumerate(icons))
    dots='radial-gradient(rgba(18,40,76,.12) 2px,transparent 2.5px) 0 0/22px 22px'
    return f'<div style="position:absolute;left:{l}px;top:{t}px;width:{w}px;height:{h}px;border-radius:{w//2}px {w//2}px 28px 28px;overflow:hidden;border:9px solid #fff;box-shadow:0 18px 44px rgba(18,40,76,.2);background:{dots},{bg}">{items}</div>'
def cover():
    return f'''<div style="position:absolute;left:240px;top:620px;width:600px;height:560px;border-radius:300px 300px 30px 30px;overflow:hidden;border:9px solid #fff;box-shadow:0 18px 44px rgba(18,40,76,.2);display:flex">
<div style="flex:1;background:radial-gradient(rgba(18,40,76,.12) 2px,transparent 2.5px) 0 0/22px 22px,#f6e3b4;position:relative"><div style="position:absolute;left:30px;top:130px;width:240px;height:240px">{I_pan}</div><div style="position:absolute;left:0;right:0;top:400px;text-align:center"><span style="background:var(--navy);color:#fff;font-weight:800;font-size:34px;padding:8px 28px 10px;border-radius:40px">yapmak</span></div></div>
<div style="flex:1;background:radial-gradient(rgba(255,255,255,.14) 2px,transparent 2.5px) 0 0/22px 22px,#12284c;position:relative"><div style="position:absolute;left:30px;top:130px;width:240px;height:240px">{I_heart}</div><div style="position:absolute;left:0;right:0;top:400px;text-align:center"><span style="background:var(--red);color:#fff;font-weight:800;font-size:34px;padding:8px 28px 10px;border-radius:40px">etmek</span></div></div>
<div style="position:absolute;left:250px;top:210px;width:100px;height:100px;border-radius:50%;background:#fff;border:5px solid var(--gold);display:flex;align-items:center;justify-content:center;font-family:'Playfair Display',serif;font-weight:800;font-size:44px;color:var(--navy)">≠</div></div>'''
I_heart=ic('<path d="M50 88C12 62 10 30 30 24c10-3 17 2 20 10 3-8 10-13 20-10 20 6 18 38-20 64z" fill="#d9202e" stroke="#fff"/><path d="M80 10v14M73 17h14M16 74v10M11 79h10" stroke="#e2b04a" stroke-width="5"/>')

chip=lambda t,c:f'<span style="display:inline-block;background:{c};color:#fff;border-radius:40px;padding:8px 26px 10px;font-size:30px;font-weight:800;margin:0 10px 10px 0">{t}</span>'


SVG2='fill="#fff" stroke="#12284c" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"'
def ic2(b):return f'<svg viewBox="0 0 100 100" style="width:100%;height:100%" {SVG2}>{b}</svg>'
I_therm=ic2('<rect x="40" y="10" width="20" height="56" rx="10"/><circle cx="50" cy="74" r="16" fill="#d9202e"/><rect x="46" y="34" width="8" height="40" fill="#d9202e" stroke="none"/><path d="M68 24h14M68 38h10M68 52h14" stroke="#e2b04a" stroke-width="5"/>')
I_glass=ic2('<path d="M26 14h48l-6 72H32z" fill="#cfeaf7"/><path d="M36 26l4 52" stroke="#fff" stroke-width="6" fill="none"/><path d="M30 44h40" stroke="#e2b04a" stroke-width="4" fill="none"/>')
I_mount=ic2('<circle cx="76" cy="24" r="12" fill="#e2b04a" stroke="#12284c"/><path d="M4 86L36 28l22 36 12-18 26 40z" fill="#8fb2d9"/><path d="M36 28l-9 16 9-6 8 6z" fill="#fff" stroke-width="3"/>')
I_order=ic2('<rect x="6" y="38" width="24" height="24" rx="6" fill="#e2b04a"/><rect x="38" y="38" width="24" height="24" rx="6" fill="#cfeaf7"/><rect x="70" y="38" width="24" height="24" rx="6" fill="#d9202e"/><path d="M14 80h72m-10-8l10 8-10 8" fill="none" stroke="#12284c"/>')
I_neq=ic2('<circle cx="50" cy="50" r="38" fill="#fff7ec"/><path d="M32 40h36M32 60h36" stroke="#12284c" stroke-width="7" fill="none"/><path d="M58 24L42 76" stroke="#d9202e" stroke-width="7" fill="none"/>')
def errslide(n,num,icon,title,sub,bad,good,rows,note):
    rs=''.join(f'<div style="display:flex;align-items:baseline;justify-content:space-between;gap:20px;background:#fff;border:2px solid rgba(226,176,74,.45);border-radius:30px;padding:12px 30px 14px;margin-bottom:12px"><div><div class="pf" style="font-size:40px;font-weight:700;color:var(--navy)">{t}</div><div style="font-weight:700;font-size:25px;color:var(--red);margin-top:2px">{r}</div></div><div style="font-weight:800;font-size:27px;color:#7b869b;white-space:nowrap">{p}</div></div>' for t,p,r in rows)
    return f'''<section class="s" id="s{n}">{tag(n)}
<div style="position:absolute;left:78px;top:150px;background:var(--red);color:#fff;font-weight:800;font-size:30px;padding:8px 28px 10px;border-radius:40px">Ошибка №{num}</div>
<h1 style="position:absolute;left:78px;top:230px;width:660px;font-size:60px;line-height:1.06">{title}</h1>
<div style="position:absolute;left:78px;top:400px;width:660px;font-weight:600;font-size:29px;color:var(--ink);line-height:1.35">{sub}</div>
<div style="position:absolute;right:78px;top:150px;width:230px;height:230px;border-radius:50%;background:#fff7ec;border:6px solid #fff;box-shadow:0 12px 30px rgba(18,40,76,.18);padding:34px">{icon}</div>
<div style="position:absolute;left:78px;right:78px;top:510px;display:flex;gap:20px">
<div style="flex:1;background:#fde5e7;border-radius:30px;padding:18px 26px 22px;border:3px solid var(--red)"><div style="font-weight:800;font-size:25px;color:var(--red)">✗ Так не надо</div><div class="pf" style="font-size:40px;font-weight:700;color:var(--navy);margin-top:6px;text-decoration:line-through;text-decoration-color:var(--red);text-decoration-thickness:3px">{bad}</div></div>
<div style="flex:1;background:#e3f4e6;border-radius:30px;padding:18px 26px 22px;border:3px solid #2e9a4f"><div style="font-weight:800;font-size:25px;color:#2e9a4f">✓ Правильно</div><div class="pf" style="font-size:40px;font-weight:700;color:var(--navy);margin-top:6px">{good}</div></div></div>
<div style="position:absolute;left:78px;right:78px;top:690px">{rs}</div>
<div style="position:absolute;left:78px;right:78px;top:1135px;font-weight:700;font-size:26px;color:var(--ink);line-height:1.35">💡 {note}</div>
{tulips()}{ft(n)}</section>'''
