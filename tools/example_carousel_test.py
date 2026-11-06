import os,sys
sys.path.insert(0,'/home/claude/elvira-turkce-media/tools');os.chdir('/home/claude/elvira-turkce-media/tools')
from lib import *
I_sun=ic2('<circle cx="50" cy="50" r="20" fill="#e2b04a"/><path d="M50 12v14M50 74v14M12 50h14M74 50h14M23 23l10 10M67 67l10 10M77 23L67 33M33 67L23 77" stroke="#d9202e" stroke-width="6" fill="none"/>')
I_ten=ic2('<circle cx="50" cy="50" r="38" fill="#fff7ec"/><text x="50" y="64" text-anchor="middle" font-family="Playfair Display" font-weight="800" font-size="40" fill="#d9202e" stroke="none">10</text>')
I_hi=ic2('<path d="M10 20h80a6 6 0 0 1 6 6v34a6 6 0 0 1-6 6H44L28 84V66H10a6 6 0 0 1-6-6V26a6 6 0 0 1 6-6z" fill="#fff7ec"/><text x="50" y="52" text-anchor="middle" font-family="Playfair Display" font-weight="800" font-size="34" fill="#d9202e" stroke="none">?</text>')
def q(n,title,sub,icon,opts):
    L='ABC'
    oc=''.join(f'<div style="display:flex;align-items:center;gap:28px;background:#fff;border:3px solid rgba(226,176,74,.55);border-radius:44px;padding:36px 36px;margin-bottom:40px;box-shadow:0 8px 0 rgba(18,40,76,.07)"><div style="flex:none;width:76px;height:76px;border-radius:50%;background:var(--navy);color:#fff;font-weight:800;font-size:40px;display:flex;align-items:center;justify-content:center">{L[i]}</div><div class="pf" style="font-size:50px;font-weight:700;color:var(--navy);line-height:1.1">{o}</div></div>' for i,o in enumerate(opts))
    return f'''<section class="s" id="s{n}">{tag(n)}
<div style="position:absolute;left:78px;top:150px;background:var(--red);color:#fff;font-weight:800;font-size:30px;padding:8px 28px 10px;border-radius:40px">Вопрос {n-1} из 5</div>
<h1 style="position:absolute;left:78px;top:240px;width:650px;font-size:64px;line-height:1.06">{title}</h1>
<div style="position:absolute;left:78px;top:470px;width:650px;font-weight:600;font-size:30px;color:var(--ink);line-height:1.35">{sub}</div>
<div style="position:absolute;right:78px;top:170px;width:240px;height:240px;border-radius:50%;background:#fff7ec;border:6px solid #fff;box-shadow:0 12px 30px rgba(18,40,76,.18);padding:36px">{icon}</div>
<div style="position:absolute;left:78px;right:78px;top:640px">{oc}</div>
{tulips()}{ft(n)}</section>'''
s1=f'''<section class="s" id="s1">{tag(1)}
<div style="position:absolute;left:78px;top:170px;background:var(--red);color:#fff;font-weight:800;font-size:32px;padding:8px 30px 10px;border-radius:40px">Уровень A1</div>
<h1 style="position:absolute;left:78px;top:270px;font-size:128px;line-height:1.0;width:930px">Тест:<br><span style="color:var(--red)">проверь себя</span></h1>
<div style="position:absolute;left:78px;top:620px;width:860px;font-size:40px;font-weight:600;color:var(--ink);line-height:1.35">5 вопросов по турецкому.<br>Сколько ответов угадаешь?</div>
<div style="position:absolute;left:240px;top:830px;width:600px;height:330px;display:flex;gap:26px;justify-content:center">
{''.join(f'<div style="width:100px;height:100px;border-radius:50%;background:{c};color:#fff;font-family:Playfair Display;font-weight:800;font-size:54px;display:flex;align-items:center;justify-content:center;box-shadow:0 10px 24px rgba(18,40,76,.2);margin-top:{m}px">{i+1}</div>' for i,(c,m) in enumerate([('#12284c',60),('#d9202e',0),('#e2b04a',60),('#d9202e',0),('#12284c',60)]))}</div>
<div style="position:absolute;left:78px;right:78px;top:1090px;text-align:center;font-weight:800;font-size:34px;color:var(--navy)">Ответы — в подписи под постом 👇</div>
{tulips()}{ft(1)}</section>'''
s2=q(2,'Как сказать «доброе утро»?','Выбери правильный вариант',I_sun,['Günaydın','İyi geceler','Hoş geldin'])
s3=q(3,'Как будет «вода»?','Выбери правильное слово',I_glass,['süt','su','çay'])
s4=q(4,'Какое число — «десять»?','Выбери правильное число',I_ten,['dokuz','yirmi','on'])
s5=q(5,'«У меня есть сестра»','Как это сказать по-турецки?',I_heart,['Kız kardeşim yok.','Kız kardeşim var.','Kız kardeşim değil.'])
s6=q(6,'Как спросить «Как дела?»','Выбери правильный вопрос',I_hi,['Nerelisin?','Kaç yaşındasın?','Nasılsın?'])
ph=ph64('assets/img0.jpg')
s7=f'''<section class="s" id="s7">{tag(7)}
<div style="position:absolute;left:350px;top:130px;width:380px;height:430px;border-radius:190px 190px 26px 26px;overflow:hidden;border:9px solid #fff;box-shadow:0 18px 44px rgba(18,40,76,.2)"><img src="data:image/jpeg;base64,{ph}" style="width:100%;height:100%;object-fit:cover;object-position:30% 20%"></div>
<h1 style="position:absolute;left:0;right:0;top:600px;text-align:center;font-size:58px;line-height:1.1">Ответы — в подписи.<br>Напиши свой результат!</h1>
<div style="position:absolute;left:70px;right:70px;top:800px;background:var(--navy);border-radius:36px;padding:38px 30px 40px;text-align:center;box-shadow:0 10px 0 var(--red)">
<div style="color:var(--gold);font-weight:800;font-size:30px;letter-spacing:2px;text-transform:uppercase">Турецкий с Эльвирой</div>
<div style="font-family:'Playfair Display',serif;font-weight:800;color:#fff;font-size:64px;line-height:1.08;margin:14px 0 18px">Запишись на бесплатный пробный урок</div>
<div style="display:inline-block;background:var(--red);color:#fff;font-weight:800;font-size:38px;padding:14px 40px 16px;border-radius:60px">Пиши мне в директ</div>
<div style="color:var(--cream);font-weight:800;font-size:40px;margin-top:20px">@elvira.turkce</div></div>
{tulips()}</section>'''
html=f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body>{defs}{s1}{s2}{s3}{s4}{s5}{s6}{s7}</body></html>'
open('/tmp/claude-0/-home-claude-elvira-turkce-media/6cd356a6-c820-5f83-a79a-19509734467b/scratchpad/test/carousel.html','w',encoding='utf-8').write(html)
