from lib import *
s1=f'''<section class="s" id="s1">{tag(1)}
<h1 style="position:absolute;left:78px;top:180px;font-size:112px;line-height:1.02;width:930px">5 ошибок<br>русскоговорящих<br><span style="color:var(--red)">в турецком</span></h1>
<div style="position:absolute;left:78px;top:610px;width:800px;font-size:36px;font-weight:600;color:var(--ink);line-height:1.35">Проверь, не делаешь ли ты их</div>
<div style="position:absolute;left:150px;top:720px;width:640px;background:#fff;border-radius:50px 50px 50px 12px;padding:30px 40px;box-shadow:0 14px 34px rgba(18,40,76,.14);border:3px solid rgba(226,176,74,.5)"><div style="font-weight:800;font-size:26px;color:var(--red)">✗ Так читают</div><div class="pf" style="font-size:54px;font-weight:700;color:var(--navy);text-decoration:line-through;text-decoration-color:var(--red);text-decoration-thickness:4px">sıcak = «сиджак»</div></div>
<div style="position:absolute;left:150px;top:960px;width:640px;background:var(--navy);border-radius:50px 50px 12px 50px;padding:30px 40px;box-shadow:0 14px 34px rgba(18,40,76,.2)"><div style="font-weight:800;font-size:26px;color:var(--gold)">✓ Так правильно</div><div class="pf" style="font-size:54px;font-weight:700;color:#fff">sıcak = «сыджак»</div></div>
<div style="position:absolute;left:820px;top:790px;width:190px;transform:rotate(8deg)">{I_therm.replace('style="width:100%;height:100%"','style="width:100%"')}</div>
{tulips()}{ft(1)}</section>'''
s2=errslide(2,1,I_therm,'ı — не «и», а «ы»','Без точки — другой звук. С точкой i = «и», без точки ı = «ы».','sıcak = «сиджак»','sıcak = «сыджак»',[('sıcak','«сыджак»','горячий'),('kırmızı','«кырмызы»','красный'),('kız','«кыз»','девочка')],'Точка меняет звук и часто смысл слова.')
s3=errslide(3,2,I_glass,'c — это «дж», а не «ц» и не «к»','Латинская c в турецком читается как русская «дж».','cam = «цам»','cam = «джам»',[('cam','«джам»','стекло'),('cadde','«джадде»','улица'),('cuma','«джума»','пятница')],'Звук «ч» передаёт другая буква: ç (çay = «чай»).')
s4=errslide(4,3,I_mount,'Ğ почти не читается','Это «мягкая г»: она не произносится, а удлиняет гласную перед ней.','dağ = «даг»','dağ = «даа»',[('dağ','«даа»','гора'),('yağmur','«яамур»','дождь'),('öğretmen','«ёретмен»','учитель')],'Не говори «г», просто протяни гласный звук.')
s5=errslide(5,4,I_order,'Глагол стоит в конце','В турецком предложении сказуемое идёт последним, а не вторым, как в русском.','Ben içiyorum çay.','Ben çay içiyorum.',[('Ben her gün Türkçe öğreniyorum.','','Я каждый день учу турецкий'),('Anne yemek yapıyor.','','Мама готовит еду'),('Ahmet kitap okuyor.','','Ахмет читает книгу')],'Схема: кто → что → глагол в конце.')
s6=errslide(6,5,I_neq,'Yok или değil?','Оба значат «нет», но используются в разных случаях.','Su değil. («воды нет»)','Su yok.',[('Su yok.','','Воды нет (чего-то нет)'),('Bu su değil.','','Это не вода (это другое)'),('Zamanım yok.','','У меня нет времени')],'Yok: чего-то нет. Değil: «это не то».')
s6=s6.replace('Su değil. («воды нет»)','Su değil.')
ph=ph64('assets/img0.jpg')
s7=f'''<section class="s" id="s7">{tag(7)}
<div style="position:absolute;left:350px;top:130px;width:380px;height:430px;border-radius:190px 190px 26px 26px;overflow:hidden;border:9px solid #fff;box-shadow:0 18px 44px rgba(18,40,76,.2)"><img src="data:image/jpeg;base64,{ph}" style="width:100%;height:100%;object-fit:cover;object-position:30% 20%"></div>
<h1 style="position:absolute;left:0;right:0;top:600px;text-align:center;font-size:58px;line-height:1.1">Сохрани, чтобы<br>не повторять эти ошибки</h1>
<div style="position:absolute;left:70px;right:70px;top:800px;background:var(--navy);border-radius:36px;padding:38px 30px 40px;text-align:center;box-shadow:0 10px 0 var(--red)">
<div style="color:var(--gold);font-weight:800;font-size:30px;letter-spacing:2px;text-transform:uppercase">Турецкий с Эльвирой</div>
<div style="font-family:'Playfair Display',serif;font-weight:800;color:#fff;font-size:64px;line-height:1.08;margin:14px 0 18px">Запишись на бесплатный пробный урок</div>
<div style="display:inline-block;background:var(--red);color:#fff;font-weight:800;font-size:38px;padding:14px 40px 16px;border-radius:60px">Пиши мне в директ</div>
<div style="color:var(--cream);font-weight:800;font-size:40px;margin-top:20px">@elvira.turkce</div></div>
{tulips()}</section>'''
html=f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body>{defs}{s1}{s2}{s3}{s4}{s5}{s6}{s7}</body></html>'
open('carousel.html','w',encoding='utf-8').write(html)
