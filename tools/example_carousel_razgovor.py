import os,sys
sys.path.insert(0,'/home/claude/elvira-turkce-media/tools');os.chdir('/home/claude/elvira-turkce-media/tools')
from lib import *
I_wow=ic2('<circle cx="50" cy="50" r="38" fill="#fff7ec"/><ellipse cx="50" cy="66" rx="9" ry="11" fill="#d9202e"/><circle cx="37" cy="40" r="5" fill="#12284c"/><circle cx="63" cy="40" r="5" fill="#12284c"/><path d="M28 30q8-8 16-2M72 30q-8-8-16-2" stroke="#12284c" stroke-width="4" fill="none"/>')
I_chill=ic2('<path d="M22 70c-10 0-14-16-3-19 0-13 18-16 24-6 7-7 22-2 21 11 11 2 10 16-3 14z" fill="#cfeaf7"/><circle cx="76" cy="26" r="12" fill="#e2b04a"/>')
I_talk=ic2('<path d="M8 18h56a6 6 0 0 1 6 6v26a6 6 0 0 1-6 6H34L20 70V56H8a6 6 0 0 1-6-6V24a6 6 0 0 1 6-6z" fill="#fff7ec"/><path d="M42 62h42a6 6 0 0 1 6 6v14a6 6 0 0 1-6 6H80v10L66 88H42a6 6 0 0 1-6-6V68a6 6 0 0 1 6-6z" fill="#e2b04a"/><path d="M16 32h40M16 42h24" stroke="#d9202e" stroke-width="5" fill="none"/>')
I_smile=ic2('<circle cx="50" cy="50" r="38" fill="#fff7ec"/><path d="M32 56c6 14 30 14 36 0" stroke="#d9202e" stroke-width="6" fill="none"/><circle cx="37" cy="40" r="4" fill="#12284c"/><circle cx="63" cy="40" r="4" fill="#12284c"/>')
def row(t,r,p=''):
    return f'<div style="background:#fff;border:2px solid rgba(226,176,74,.45);border-radius:34px;padding:16px 34px 18px;margin-bottom:18px;box-shadow:0 6px 0 rgba(18,40,76,.06)"><div class="pf" style="font-size:44px;font-weight:700;color:var(--navy);line-height:1.12">{t}</div><div style="font-weight:800;font-size:27px;color:var(--red);margin-top:4px">{r}</div></div>'
def lst(n,badge,title,sub,icon,rows,note,tsz=64):
    rs=''.join(row(*x) for x in rows)
    return f'''<section class="s" id="s{n}">{tag(n)}
<div style="position:absolute;left:78px;top:150px;background:var(--red);color:#fff;font-weight:800;font-size:30px;padding:8px 28px 10px;border-radius:40px">{badge}</div>
<h1 style="position:absolute;left:78px;top:225px;width:680px;font-size:{tsz}px;line-height:1.05">{title}</h1>
<div style="position:absolute;left:78px;top:395px;width:660px;font-weight:600;font-size:29px;color:var(--ink);line-height:1.35">{sub}</div>
<div style="position:absolute;right:78px;top:150px;width:230px;height:230px;border-radius:50%;background:#fff7ec;border:6px solid #fff;box-shadow:0 12px 30px rgba(18,40,76,.18);padding:34px">{icon}</div>
<div style="position:absolute;left:78px;right:78px;top:470px">{rs}</div>
<div style="position:absolute;left:78px;right:78px;top:1150px;font-weight:700;font-size:25px;color:var(--ink);line-height:1.35">{note}</div>
{tulips()}{ft(n)}</section>'''
s1=f'''<section class="s" id="s1">{tag(1)}
<div style="position:absolute;left:78px;top:170px;background:var(--red);color:#fff;font-weight:800;font-size:32px;padding:8px 30px 10px;border-radius:40px">Как это по-турецки</div>
<h1 style="position:absolute;left:78px;top:270px;font-size:104px;line-height:1.0;width:930px">12 живых фраз,<br><span style="color:var(--red)">как говорят турки</span></h1>
<div style="position:absolute;left:78px;top:600px;width:860px;font-size:38px;font-weight:600;color:var(--ink);line-height:1.35">«Забей», «да ладно», «ничего себе» —<br>разговорный турецкий для A1–B1</div>
<div style="position:absolute;left:150px;top:800px;width:780px;height:300px;display:flex;gap:22px;justify-content:center">
{''.join(f'<div style="width:140px;height:140px;border-radius:50%;background:#fff7ec;border:6px solid #fff;box-shadow:0 12px 26px rgba(18,40,76,.18);padding:26px;margin-top:{m}px">{i}</div>' for i,m in [(I_wow,70),(I_chill,0),(I_talk,70),(I_smile,0),(I_check,70)])}</div>
<div style="position:absolute;left:78px;right:78px;top:1070px;text-align:center;font-weight:800;font-size:32px;color:var(--navy)">Сохрани и проверь себя в конце 👇</div>
{tulips()}{ft(1)}</section>'''
s2=lst(2,'Реакции','Эмоции','Что сказать, когда удивлён или рад',I_wow,[
 ('Hadi ya!','Да ладно! / Не может быть!'),
 ('Vay canına!','Ничего себе!'),
 ('Yazık!','Как жаль! / Жалко!'),
 ('Aferin!','Молодец! / Браво!')],'Это неформальные фразы: для друзей и знакомых.',72)
s3=lst(3,'Успокоить','Не переживай','Фразы, чтобы поддержать и сбавить градус',I_chill,[
 ('Boş ver.','Забей. / Не бери в голову.'),
 ('Önemli değil.','Неважно. / Ничего страшного.'),
 ('Merak etme.','Не волнуйся.'),
 ('Neyse.','Ладно, проехали.')],'Boş ver — буквально «оставь пустое».',64)
s4=lst(4,'В разговоре','Болтаем','Короткие слова, без которых не обойтись',I_talk,[
 ('Ne haber?','Как дела? (букв. «какие новости?»)'),
 ('Aynen.','Вот именно. / Точно.'),
 ('Efendim?','Простите, что? / Да?'),
 ('Ne alaka?','Причём тут это?')],'Ne haber? — со своими. Efendim? — вежливое «что, простите?».',72)
def bub(who,tr,ru,left,col):
    return f'<div style="margin-left:{left}px;margin-right:{80-left}px;margin-bottom:26px;background:#fff;border-radius:44px;padding:24px 34px 26px;border:3px solid {col};box-shadow:0 8px 0 rgba(18,40,76,.07)"><div style="font-weight:800;font-size:24px;color:{col}">{who}</div><div class="pf" style="font-size:40px;font-weight:700;color:var(--navy);margin-top:4px;line-height:1.15">{tr}</div><div style="font-weight:700;font-size:26px;color:var(--ink);margin-top:6px">{ru}</div></div>'
s5=f'''<section class="s" id="s5">{tag(5)}
<div style="position:absolute;left:78px;top:150px;background:var(--red);color:#fff;font-weight:800;font-size:30px;padding:8px 28px 10px;border-radius:40px">Мини-диалог</div>
<h1 style="position:absolute;left:78px;top:225px;width:660px;font-size:64px;line-height:1.05">Разговор друзей</h1>
<div style="position:absolute;right:78px;top:150px;width:210px;height:210px;border-radius:50%;background:#fff7ec;border:6px solid #fff;box-shadow:0 12px 30px rgba(18,40,76,.18);padding:30px">{I_smile}</div>
<div style="position:absolute;left:78px;right:0;top:372px;width:924px">
{bub('Али','Ne haber?','Как дела?',0,'#12284c')}
{bub('Ты','İyiyim, ama sınavı geçemedim.','Хорошо, но я не сдал экзамен.',60,'#d9202e')}
{bub('Али','Yazık! Boş ver, bir dahaki sefere olur.','Жаль! Забей, в следующий раз получится.',0,'#12284c')}
{bub('Ты','Aynen, sağ ol!','Точно, спасибо!',60,'#d9202e')}</div>
{tulips()}{ft(5)}</section>'''
qs=['Забей!','Ничего себе!','Вот именно.','Как жаль!','Причём тут это?']
qr=''.join(f'<div style="display:flex;align-items:center;gap:26px;background:#fff;border:2px solid rgba(226,176,74,.45);border-radius:34px;padding:16px 34px;margin-bottom:18px;box-shadow:0 6px 0 rgba(18,40,76,.06)"><div style="flex:none;width:54px;height:54px;border-radius:50%;background:var(--navy);color:#fff;font-weight:800;font-size:28px;display:flex;align-items:center;justify-content:center">{i+1}</div><div style="font-weight:800;font-size:40px;color:var(--navy)">{q}</div><div style="margin-left:auto;font-family:\'Playfair Display\',serif;font-weight:800;font-size:44px;color:var(--red)">?</div></div>' for i,q in enumerate(qs))
s6=f'''<section class="s" id="s6">{tag(6)}
<div style="position:absolute;left:78px;top:150px;background:var(--red);color:#fff;font-weight:800;font-size:30px;padding:8px 28px 10px;border-radius:40px">Проверь себя</div>
<h1 style="position:absolute;left:78px;top:225px;width:680px;font-size:64px;line-height:1.05">Переведи за 5 секунд</h1>
<div style="position:absolute;left:78px;top:395px;width:660px;font-weight:600;font-size:29px;color:var(--ink);line-height:1.35">Как это по-турецки?</div>
<div style="position:absolute;right:78px;top:150px;width:230px;height:230px;border-radius:50%;background:#fff7ec;border:6px solid #fff;box-shadow:0 12px 30px rgba(18,40,76,.18);padding:34px">{I_clock}</div>
<div style="position:absolute;left:78px;right:78px;top:470px">{qr}</div>
<div style="position:absolute;left:78px;right:78px;top:1150px;font-weight:700;font-size:25px;color:var(--ink);line-height:1.35">💬 Пиши ответы в комментариях. Правильные — в подписи!</div>
{tulips()}{ft(6)}</section>'''
ph=ph64('assets/img0.jpg')
s7=f'''<section class="s" id="s7">{tag(7)}
<div style="position:absolute;left:350px;top:130px;width:380px;height:430px;border-radius:190px 190px 26px 26px;overflow:hidden;border:9px solid #fff;box-shadow:0 18px 44px rgba(18,40,76,.2)"><img src="data:image/jpeg;base64,{ph}" style="width:100%;height:100%;object-fit:cover;object-position:30% 20%"></div>
<h1 style="position:absolute;left:0;right:0;top:600px;text-align:center;font-size:58px;line-height:1.1">Хочешь говорить<br>как турки?</h1>
<div style="position:absolute;left:70px;right:70px;top:800px;background:var(--navy);border-radius:36px;padding:38px 30px 40px;text-align:center;box-shadow:0 10px 0 var(--red)">
<div style="color:var(--gold);font-weight:800;font-size:30px;letter-spacing:2px;text-transform:uppercase">Турецкий с Эльвирой</div>
<div style="font-family:'Playfair Display',serif;font-weight:800;color:#fff;font-size:64px;line-height:1.08;margin:14px 0 18px">Запишись на бесплатный пробный урок</div>
<div style="display:inline-block;background:var(--red);color:#fff;font-weight:800;font-size:38px;padding:14px 40px 16px;border-radius:60px">Пиши мне в директ</div>
<div style="color:var(--cream);font-weight:800;font-size:40px;margin-top:20px">@elvira.turkce</div></div>
{tulips()}</section>'''
html=f'<!doctype html><html><head><meta charset="utf-8"><style>{css}.pf{{font-family:\'Playfair Display\',serif}}</style></head><body>{defs}{s1}{s2}{s3}{s4}{s5}{s6}{s7}</body></html>'
open('carousel_razgovor.html','w',encoding='utf-8').write(html)
