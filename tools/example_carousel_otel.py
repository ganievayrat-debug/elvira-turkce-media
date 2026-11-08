import os,sys
sys.path.insert(0,'/home/claude/elvira-turkce-media/tools');os.chdir('/home/claude/elvira-turkce-media/tools')
from lib import *
I_key=ic2('<circle cx="34" cy="40" r="20" fill="#e2b04a"/><circle cx="34" cy="40" r="7" fill="#fff7ec"/><path d="M50 52l34 34M70 70l10-10M78 78l10-10" fill="none" stroke-width="7"/>')
I_bed=ic2('<path d="M8 30v54M92 56v28M8 70h84V56a10 10 0 0 0-10-10H34v24" fill="#fff7ec"/><rect x="16" y="44" width="22" height="16" rx="7" fill="#d9202e"/>')
I_case=ic2('<rect x="16" y="32" width="68" height="52" rx="10" fill="#d9202e"/><path d="M38 32v-8a6 6 0 0 1 6-6h12a6 6 0 0 1 6 6v8" fill="none"/><path d="M16 56h68" stroke="#e2b04a" stroke-width="6"/>')
I_bell=ic2('<path d="M20 70a30 30 0 0 1 60 0z" fill="#e2b04a"/><path d="M12 76h76v8H12z" fill="#fff7ec"/><path d="M50 40v-8M44 32h12" fill="none"/>')
I_bub=ic2('<path d="M10 20h80a6 6 0 0 1 6 6v34a6 6 0 0 1-6 6H44L28 84V66H10a6 6 0 0 1-6-6V26a6 6 0 0 1 6-6z" fill="#fff7ec"/><path d="M24 38h52M24 50h34" stroke="#d9202e" stroke-width="5" fill="none"/>')
I_smile=ic2('<circle cx="50" cy="50" r="38" fill="#fff7ec"/><path d="M32 56c6 14 30 14 36 0" stroke="#d9202e" stroke-width="6" fill="none"/><circle cx="37" cy="40" r="4" fill="#12284c"/><circle cx="63" cy="40" r="4" fill="#12284c"/>')
def row(t,r,p=''):
    return f'<div style="background:#fff;border:2px solid rgba(226,176,74,.45);border-radius:34px;padding:14px 34px 16px;margin-bottom:16px;box-shadow:0 6px 0 rgba(18,40,76,.06)"><div class="pf" style="font-size:38px;font-weight:700;color:var(--navy);line-height:1.12">{t}</div><div style="font-weight:800;font-size:27px;color:var(--red);margin-top:4px">{r}</div></div>'
def lst(n,badge,title,sub,icon,rows,note,tsz=64):
    rs=''.join(row(*x) for x in rows)
    return f'''<section class="s" id="s{n}">{tag(n)}
<div style="position:absolute;left:78px;top:150px;background:var(--red);color:#fff;font-weight:800;font-size:30px;padding:8px 28px 10px;border-radius:40px">{badge}</div>
<h1 style="position:absolute;left:78px;top:225px;width:680px;font-size:{tsz}px;line-height:1.05">{title}</h1>
<div style="position:absolute;left:78px;top:395px;width:660px;font-weight:600;font-size:29px;color:var(--ink);line-height:1.35">{sub}</div>
<div style="position:absolute;right:78px;top:150px;width:230px;height:230px;border-radius:50%;background:#fff7ec;border:6px solid #fff;box-shadow:0 12px 30px rgba(18,40,76,.18);padding:34px">{icon}</div>
<div style="position:absolute;left:78px;right:78px;top:465px">{rs}</div>
<div style="position:absolute;left:78px;right:78px;top:1150px;font-weight:700;font-size:25px;color:var(--ink);line-height:1.35">{note}</div>
{tulips()}{ft(n)}</section>'''
s1=f'''<section class="s" id="s1">{tag(1)}
<div style="position:absolute;left:78px;top:170px;background:var(--red);color:#fff;font-weight:800;font-size:32px;padding:8px 30px 10px;border-radius:40px">Как это по-турецки</div>
<h1 style="position:absolute;left:78px;top:270px;font-size:112px;line-height:1.0;width:930px">15 фраз<br><span style="color:var(--red)">для отеля</span></h1>
<div style="position:absolute;left:78px;top:600px;width:860px;font-size:38px;font-weight:600;color:var(--ink);line-height:1.35">Заселиться, попросить, пожаловаться<br>и выехать без стресса</div>
<div style="position:absolute;left:150px;top:800px;width:780px;height:300px;display:flex;gap:22px;justify-content:center">
{''.join(f'<div style="width:140px;height:140px;border-radius:50%;background:#fff7ec;border:6px solid #fff;box-shadow:0 12px 26px rgba(18,40,76,.18);padding:26px;margin-top:{m}px">{ic_}</div>' for ic_,m in [(I_key,70),(I_bed,0),(I_bell,70),(I_case,0),(I_bub,70)])}</div>
<div style="position:absolute;left:78px;right:78px;top:1070px;text-align:center;font-weight:800;font-size:32px;color:var(--navy)">Сохрани, пригодится в поездке 👇</div>
{tulips()}{ft(1)}</section>'''
s2=lst(2,'Заселение','Приехали в отель','Первые фразы на ресепшене',I_key,[
 ('Rezervasyonum var.','У меня есть бронь.'),
 ('Oda anahtarı lütfen.','Ключ от номера, пожалуйста.'),
 ('Kahvaltı saat kaçta?','Во сколько завтрак?'),
 ('Wi-Fi şifresi nedir?','Какой пароль от Wi-Fi?'),
 ('Asansör nerede?','Где лифт?')],'Lütfen — «пожалуйста»: добавляй к любой просьбе.')
s3=lst(3,'Просьбы и проблемы','Что-то не так','Как сказать об этом вежливо',I_bed,[
 ('Havlu alabilir miyim?','Можно полотенце?'),
 ('Klima çalışmıyor.','Кондиционер не работает.'),
 ('Sıcak su yok.','Нет горячей воды.'),
 ('Oda çok gürültülü.','В номере очень шумно.'),
 ('Odayı değiştirebilir miyim?','Можно поменять номер?')],'Alabilir miyim? — «Можно мне взять?» Очень полезная конструкция.',58)
s4=lst(4,'Выезд','Пора домой','Фразы на выезде',I_case,[
 ('Çıkış saat kaçta?','Во сколько выезд?'),
 ('Hesabı alabilir miyim?','Можно счёт?'),
 ('Bavulumu bırakabilir miyim?','Можно оставить чемодан?'),
 ('Taksi çağırabilir misiniz?','Вы можете вызвать такси?'),
 ('Her şey için teşekkürler.','Спасибо за всё.')],'Çıkış — выход/выезд, giriş — вход/заселение.',64)
words=[('oda','«ода»','номер, комната'),('anahtar','«анахтар»','ключ'),('havlu','«хавлу»','полотенце'),('bavul','«бавул»','чемодан'),('asansör','«асансёр»','лифт')]
rs=''.join(f'<div style="display:flex;align-items:center;justify-content:space-between;background:#fff;border:2px solid rgba(226,176,74,.45);border-radius:34px;padding:16px 34px 18px;margin-bottom:16px;box-shadow:0 6px 0 rgba(18,40,76,.06)"><div><div class="pf" style="font-size:44px;font-weight:700;color:var(--navy)">{t}</div><div style="font-weight:700;font-size:23px;color:#7b869b">{p}</div></div><div style="font-weight:800;font-size:32px;color:var(--red)">{r}</div></div>' for t,p,r in words)
s5=f'''<section class="s" id="s5">{tag(5)}
<div style="position:absolute;left:78px;top:150px;background:var(--red);color:#fff;font-weight:800;font-size:30px;padding:8px 28px 10px;border-radius:40px">Слова</div>
<h1 style="position:absolute;left:78px;top:225px;width:680px;font-size:64px;line-height:1.05">5 слов для отеля</h1>
<div style="position:absolute;left:78px;top:330px;width:660px;font-weight:600;font-size:29px;color:var(--ink);line-height:1.35">Выучи сегодня</div>
<div style="position:absolute;right:78px;top:150px;width:230px;height:230px;border-radius:50%;background:#fff7ec;border:6px solid #fff;box-shadow:0 12px 30px rgba(18,40,76,.18);padding:34px">{I_bed}</div>
<div style="position:absolute;left:78px;right:78px;top:465px">{rs}</div>
<div style="position:absolute;left:78px;right:78px;top:1150px;font-weight:700;font-size:25px;color:var(--ink);line-height:1.35">Транскрипция приблизительная, как ориентир для чтения.</div>
{tulips()}{ft(5)}</section>'''
def bub(who,tr,ru,left,col):
    return f'<div style="margin-left:{left}px;margin-right:{80-left}px;margin-bottom:26px;background:#fff;border-radius:44px;padding:24px 34px 26px;border:3px solid {col};box-shadow:0 8px 0 rgba(18,40,76,.07)"><div style="font-weight:800;font-size:24px;color:{col}">{who}</div><div class="pf" style="font-size:40px;font-weight:700;color:var(--navy);margin-top:4px;line-height:1.15">{tr}</div><div style="font-weight:700;font-size:26px;color:var(--ink);margin-top:6px">{ru}</div></div>'
s6=f'''<section class="s" id="s6">{tag(6)}
<div style="position:absolute;left:78px;top:150px;background:var(--red);color:#fff;font-weight:800;font-size:30px;padding:8px 28px 10px;border-radius:40px">Мини-диалог</div>
<h1 style="position:absolute;left:78px;top:225px;width:660px;font-size:64px;line-height:1.05">На ресепшене</h1>
<div style="position:absolute;right:78px;top:150px;width:210px;height:210px;border-radius:50%;background:#fff7ec;border:6px solid #fff;box-shadow:0 12px 30px rgba(18,40,76,.18);padding:30px">{I_smile}</div>
<div style="position:absolute;left:78px;right:0;top:340px;width:924px">
{bub('Ресепшн','Hoş geldiniz! Rezervasyonunuz var mı?','Добро пожаловать! У вас есть бронь?',0,'#12284c')}
{bub('Ты','Evet, rezervasyonum var.','Да, у меня есть бронь.',60,'#d9202e')}
{bub('Ресепшн','Pasaportunuzu alabilir miyim?','Можно ваш паспорт?',0,'#12284c')}
{bub('Ты','Tabii, buyurun.','Конечно, вот, пожалуйста.',60,'#d9202e')}</div>
<div style="position:absolute;left:78px;right:78px;top:1150px;font-weight:700;font-size:25px;color:var(--ink);line-height:1.35">💡 Buyurun — «пожалуйста» в смысле «вот, возьмите».</div>
{tulips()}{ft(6)}</section>'''
ph=ph64('assets/img0.jpg')
s7=f'''<section class="s" id="s7">{tag(7)}
<div style="position:absolute;left:350px;top:130px;width:380px;height:430px;border-radius:190px 190px 26px 26px;overflow:hidden;border:9px solid #fff;box-shadow:0 18px 44px rgba(18,40,76,.2)"><img src="data:image/jpeg;base64,{ph}" style="width:100%;height:100%;object-fit:cover;object-position:30% 20%"></div>
<h1 style="position:absolute;left:0;right:0;top:600px;text-align:center;font-size:58px;line-height:1.1">Сохрани, чтобы не забыть<br>фразы для отеля</h1>
<div style="position:absolute;left:70px;right:70px;top:800px;background:var(--navy);border-radius:36px;padding:38px 30px 40px;text-align:center;box-shadow:0 10px 0 var(--red)">
<div style="color:var(--gold);font-weight:800;font-size:30px;letter-spacing:2px;text-transform:uppercase">Турецкий с Эльвирой</div>
<div style="font-family:'Playfair Display',serif;font-weight:800;color:#fff;font-size:64px;line-height:1.08;margin:14px 0 18px">Запишись на бесплатный пробный урок</div>
<div style="display:inline-block;background:var(--red);color:#fff;font-weight:800;font-size:38px;padding:14px 40px 16px;border-radius:60px">Пиши мне в директ</div>
<div style="color:var(--cream);font-weight:800;font-size:40px;margin-top:20px">@elvira.turkce</div></div>
{tulips()}</section>'''
html=f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body>{defs}{s1}{s2}{s3}{s4}{s5}{s6}{s7}</body></html>'
open('carousel_otel.html','w',encoding='utf-8').write(html)
