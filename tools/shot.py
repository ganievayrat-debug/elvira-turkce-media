"""Рендер слайдов карусели: python3 shot.py carousel.html OUT_DIR N_SLIDES  -> OUT_DIR/slide-1.png ..."""
import sys,os
from playwright.sync_api import sync_playwright
html,out,n=sys.argv[1],sys.argv[2],int(sys.argv[3])
os.makedirs(out,exist_ok=True)
with sync_playwright() as p:
    br=p.chromium.launch();pg=br.new_page(viewport={'width':1080,'height':1350},device_scale_factor=1)
    pg.route('**/*',lambda r:r.abort() if r.request.url.startswith('http') else r.continue_())
    pg.goto('file://'+os.path.abspath(html));pg.wait_for_timeout(700)
    for i in range(1,n+1):pg.locator(f'#s{i}').screenshot(path=f'{out}/slide-{i}.png')
    br.close()
