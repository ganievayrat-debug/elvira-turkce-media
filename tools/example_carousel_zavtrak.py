import os,sys
sys.path.insert(0,'/home/claude/elvira-turkce-media/tools');os.chdir('/home/claude/elvira-turkce-media/tools')
from lib import *
I_egg=ic2('<path d="M50 12C32 12 22 44 22 62a28 28 0 0 0 56 0C78 44 68 12 50 12z" fill="#fff7ec"/><circle cx="50" cy="64" r="14" fill="#e2b04a"/>')
I_cheese=ic2('<path d="M10 62L60 22l30 18v34H10z" fill="#f4d36b"/><path d="M10 62h80" /><circle cx="34" cy="74" r="5" fill="#fff7ec"/><circle cx="64" cy="70" r="6" fill="#fff7ec"/><circle cx="62" cy="46" r="4" fill="#fff7ec"/>')
I_bread=ic2('<path d="M14 62c-8-24 16-40 36-40s44 16 36 40z" fill="#e8b46a"/><path d="M14 62h72v14H14z" fill="#d9a05a"/><path d="M36 36l6 12M54 32l6 14M72 38l4 10" stroke="#fff7ec" fill="none"/>')
I_jar=ic2('<rect x="26" y="26" width="48" height="58" rx="12" fill="#e2b04a"/><rect x="30" y="14" width="40" height="14" rx="5" fill="#d9202e"/><rect x="36" y="44" width="28" height="22" rx="6" fill="#fff7ec"/>')
I_olive=ic2('<ellipse cx="42" cy="56" rx="24" ry="30" fill="#6a8a3a" transform="rotate(25 42 56)"/><circle cx="36" cy="64" r="7" fill="#d9202e"/><path d="M60 24c10-8 22-6 28 2" fill="none" stroke="#2e9a4f" stroke-width="5"/>')
I_smile=ic2('<circle cx="50" cy="50" r="38" fill="#fff7ec"/><path d="M32 56c6 14 30 14 36 0" stroke="#d9202e" stroke-width="6" fill="none"/><circle cx="37" cy="40" r="4" fill="#12284c"/><circle cx="63" cy="40" r="4" fill="#12284c"/>')
I_bubble=ic2('<path d="M10 20h80a6 6 0 0 1 6 6v34a6 6 0 0 1-6 6H44L28 84V66H10a6 6 0 0 1-6-6V26a6 6 0 0 1 6-6z" fill="#fff7ec"/><path d="M24 38h52M24 50h34" stroke="#d9202e" stroke-width="5" fill="none"/>')
def listslide(n,badge,title,sub,icon,rows,note,rowpad=16):
    rs=''.join(f'<div style="display:flex;align-items:center;justify-content:space-between;gap:20px;background:#fff;border:2px solid rgba(226,176,74,.45);border-radius:34px;padding:{rowpad}px 34px {rowpad+2}px;margin-bottom:16px;box-shadow:0 6px 0 rgba(18,40,76,.06)"><div><div class="pf" style="font-size:{fs}px;font-weight:700;color:var(--navy);line-height:1.12">{t}</div><div style="font-weight:700;font-size:23px;color:#7b869b;margin-top:2px">{p}</div></div><div style="font-weight:800;font-size:{rs_}px;color:var(--red);text-align:right;max-width:{mw}px;line-height:1.2">{r}</div></div>' for t,p,r,fs,rs_,mw in rows)
    return f'''<section class="s" id="s{n}">{tag(n)}
<div style="position:absolute;left:78px;top:150px;background:var(--red);color:#fff;font-weight:800;font-size:30px;padding:8px 28px 10px;border-radius:40px">{badge}</div>
<h1 style="position:absolute;left:78px;top:225px;width:680px;font-size:64px;line-height:1.05">{title}</h1>
<div style="position:absolute;left:78px;top:395px;width:660px;font-weight:600;font-size:29px;color:var(--ink);line-height:1.35">{sub}</div>
<div style="position:absolute;right:78px;top:150px;width:230px;height:230px;border-radius:50%;background:#fff7ec;border:6px solid #fff;box-shadow:0 12px 30px rgba(18,40,76,.18);padding:34px">{icon}</div>
<div style="position:absolute;left:78px;right:78px;top:470px">{rs}</div>
<div style="position:absolute;left:78px;right:78px;top:1138px;font-weight:700;font-size:25px;color:var(--ink);line-height:1.35">{note}</div>
{tulips()}{ft(n)}</section>'''
def W(t,p,r):return (t,p,r,42,32,330)
NOTE='Транскрипция приблизительная: ориентир для чтения, а не точное произношение.'
s1=f'''<section class="s" id="s1">{tag(1)}
<div style="position:absolute;left:78px;top:170px;background:var(--red);color:#fff;font-weight:800;font-size:32px;padding:8px 30px 10px;border-radius:40px">Слова и фразы</div>
<h1 style="position:absolute;left:78px;top:270px;font-size:118px;line-height:1.0;width:930px">Турецкий<br><span style="color:var(--red)">завтрак</span></h1>
<div style="position:absolute;left:78px;top:600px;width:860px;font-size:38px;font-weight:600;color:var(--ink);line-height:1.35">Что на столе и как заказать —<br>на турецком, с переводом</div>
<div style="position:absolute;left:150px;top:800px;width:780px;height:300px;display:flex;gap:22px;justify-content:center">
{''.join(f'<div style="width:140px;height:140px;border-radius:50%;background:#fff7ec;border:6px solid #fff;box-shadow:0 12px 26px rgba(18,40,76,.18);padding:26px;margin-top:{m}px">{ic_}</div>' for ic_,m in [(I_egg,70),(I_cheese,0),(I_glass,70),(I_bread,0),(I_jar,70)])}</div>
<div style="position:absolute;left:78px;right:78px;top:1070px;text-align:center;font-weight:800;font-size:32px;color:var(--navy)">Kahvaltı = завтрак. Сохрани себе 👇</div>
{tulips()}{ft(1)}</section>'''
s2=listslide(2,'Слова №1','Что на столе','Основные продукты',I_cheese,[
 W('ekmek','«экмек»','хлеб'),W('peynir','«пейнир»','сыр'),W('zeytin','«зейтин»','оливки'),W('yumurta','«юмурта»','яйцо'),W('domates','«доматес»','помидор')],NOTE,16)
s3=listslide(3,'Слова №2','Сладкое и напитки','К чаю и не только',I_jar,[
 W('çay','«чай»','чай'),W('süt','«сют»','молоко'),W('bal','«бал»','мёд'),W('reçel','«речел»','варенье'),W('tereyağı','«терейаы»','сливочное масло')],NOTE,16)
s4=listslide(4,'Блюда','Любимые блюда','Их заказывают чаще всего',I_egg,[
 ('menemen','«менемен»','яйца с помидорами и перцем',42,27,380),('sucuklu yumurta','«суджуклу юмурта»','яичница с колбасой суджук',42,27,380),('simit','«симит»','бублик с кунжутом',42,27,380),('börek','«бёрек»','слоёная выпечка с начинкой',42,27,380),('kahvaltı tabağı','«кахвалты табаа»','тарелка-ассорти для завтрака',40,27,380)],NOTE,16)
s5=listslide(5,'Фразы','Как попросить и поблагодарить','Пригодится в кафе и в гостях',I_bubble,[
 ('Bir çay lütfen.','','Чай, пожалуйста.',38,27,330),('Çay alır mısınız?','','Будете чай?',38,27,330),('Biraz daha ekmek alabilir miyim?','','Можно ещё хлеба?',34,27,300),('Afiyet olsun!','«афиет олсун»','Приятного аппетита!',38,27,330),('Elinize sağlık.','','Спасибо за еду (хозяйке)',38,27,330)],NOTE,16)
def bub(who,tr,ru,left,col):
    return f'<div style="margin-left:{left}px;margin-right:{80-left}px;margin-bottom:26px;background:#fff;border-radius:44px;padding:24px 34px 26px;border:3px solid {col};box-shadow:0 8px 0 rgba(18,40,76,.07)"><div style="font-weight:800;font-size:24px;color:{col}">{who}</div><div class="pf" style="font-size:42px;font-weight:700;color:var(--navy);margin-top:4px;line-height:1.15">{tr}</div><div style="font-weight:700;font-size:26px;color:var(--ink);margin-top:6px">{ru}</div></div>'
s6=f'''<section class="s" id="s6">{tag(6)}
<div style="position:absolute;left:78px;top:150px;background:var(--red);color:#fff;font-weight:800;font-size:30px;padding:8px 28px 10px;border-radius:40px">Мини-диалог</div>
<h1 style="position:absolute;left:78px;top:225px;width:660px;font-size:64px;line-height:1.05">Заказываем завтрак</h1>
<div style="position:absolute;right:78px;top:150px;width:210px;height:210px;border-radius:50%;background:#fff7ec;border:6px solid #fff;box-shadow:0 12px 30px rgba(18,40,76,.18);padding:30px">{I_smile}</div>
<div style="position:absolute;left:78px;right:0;top:340px;width:924px">
{bub('Официант','Kahvaltı için ne istersiniz?','Что желаете на завтрак?',0,'#12284c')}
{bub('Ты','Peynir, zeytin ve bir çay lütfen.','Сыр, оливки и чай, пожалуйста.',60,'#d9202e')}
{bub('Официант','Başka bir şey ister misiniz?','Желаете что-нибудь ещё?',0,'#12284c')}
{bub('Ты','Hayır, teşekkürler.','Нет, спасибо.',60,'#d9202e')}</div>
<div style="position:absolute;left:78px;right:78px;top:1135px;font-weight:700;font-size:25px;color:var(--ink);line-height:1.35">💡 Kahvaltı — дословно «перед кофе» (kahve + altı).</div>
{tulips()}{ft(6)}</section>'''
ph=ph64('assets/img0.jpg')
s7=f'''<section class="s" id="s7">{tag(7)}
<div style="position:absolute;left:350px;top:130px;width:380px;height:430px;border-radius:190px 190px 26px 26px;overflow:hidden;border:9px solid #fff;box-shadow:0 18px 44px rgba(18,40,76,.2)"><img src="data:image/jpeg;base64,{ph}" style="width:100%;height:100%;object-fit:cover;object-position:30% 20%"></div>
<h1 style="position:absolute;left:0;right:0;top:600px;text-align:center;font-size:58px;line-height:1.1">Сохрани, чтобы не забыть<br>слова для завтрака</h1>
<div style="position:absolute;left:70px;right:70px;top:800px;background:var(--navy);border-radius:36px;padding:38px 30px 40px;text-align:center;box-shadow:0 10px 0 var(--red)">
<div style="color:var(--gold);font-weight:800;font-size:30px;letter-spacing:2px;text-transform:uppercase">Турецкий с Эльвирой</div>
<div style="font-family:'Playfair Display',serif;font-weight:800;color:#fff;font-size:64px;line-height:1.08;margin:14px 0 18px">Запишись на бесплатный пробный урок</div>
<div style="display:inline-block;background:var(--red);color:#fff;font-weight:800;font-size:38px;padding:14px 40px 16px;border-radius:60px">Пиши мне в директ</div>
<div style="color:var(--cream);font-weight:800;font-size:40px;margin-top:20px">@elvira.turkce</div></div>
{tulips()}</section>'''
html=f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body>{defs}{s1}{s2}{s3}{s4}{s5}{s6}{s7}</body></html>'
open('carousel.html','w',encoding='utf-8').write(html)
