"""Mappa statica dell'officina: python sorgente/mappa.py
Compone una volta sola le tessere di OpenStreetMap (zoom 15) attorno a contenuti.GEO, disegna il segnaposto arancio
e salva docs/assets/img/mappa-officina.webp (1200x700) e -600.webp. Le pagine la mostrano come immagine del sito:
nessun contenuto esterno, quindi niente cookie. Va citata la fonte: © OpenStreetMap contributors (lo fa mappa() in sito.py).
Da rifare solo se cambiano le coordinate."""
import io, math, os, sys, time, urllib.request
from PIL import Image, ImageDraw
from contenuti import GEO
LAT, LON, Z = GEO[0], GEO[1], 15
DEST = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs", "assets", "img", "mappa-officina.webp")
L, A = 1200, 700        # larghezza e altezza finali
def pixel(lat, lon, z):
    n = 256 * 2 ** z
    x = (lon + 180) / 360 * n
    y = (1 - math.log(math.tan(math.radians(lat)) + 1 / math.cos(math.radians(lat))) / math.pi) / 2 * n
    return x, y
cx, cy = pixel(LAT, LON, Z)
x0, y0 = cx - L / 2, cy - A / 2
tela = Image.new("RGB", (L, A))
for tx in range(int(x0 // 256), int((x0 + L) // 256) + 1):
    for ty in range(int(y0 // 256), int((y0 + A) // 256) + 1):
        url = f"https://tile.openstreetmap.org/{Z}/{tx}/{ty}.png"
        dati = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "lmautoservizi-sito/1.0 (mappa statica, una tantum)"})).read()
        tela.paste(Image.open(io.BytesIO(dati)).convert("RGB"), (int(tx * 256 - x0), int(ty * 256 - y0)))
        time.sleep(0.3)
d = ImageDraw.Draw(tela)
px, py = L / 2, A / 2
# segnaposto arancio del sito: goccia con il cerchio bianco, la punta sul punto esatto
d.ellipse((px - 34, py - 98, px + 34, py - 30), fill=(255, 92, 43))
d.polygon([(px - 30, py - 52), (px + 30, py - 52), (px, py)], fill=(255, 92, 43))
d.ellipse((px - 13, py - 77, px + 13, py - 51), fill=(255, 255, 255))
tela.save(DEST, "WEBP", quality=80, method=6)
tela.resize((L // 2, A // 2), Image.LANCZOS).save(DEST.replace(".webp", "-600.webp"), "WEBP", quality=80, method=6)
print("ok")
