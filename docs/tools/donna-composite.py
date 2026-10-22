# Rebuilds crestwood/img/team/donna.jpg: Donna's LinkedIn headshot cut out (tools/cutout.swift, Apple Vision
# person segmentation) and placed on a forest plate stretched from the clear band above Teresa's head in the
# Basecamp team shoot, scaled and positioned so her face matches the team average (tools/faces.swift):
# centre x 376, centre y 319, face height 196 in a 720x900 card. Usage: python3 donna-composite.py RAW_DIR OUT
import sys
from PIL import Image, ImageFilter
import numpy as np
raw, out = sys.argv[1], sys.argv[2]   # raw: folder with teresa.webp and donna-cut.png
band = Image.open(f'{raw}/teresa.webp').convert('RGB').crop((0, 0, 1080, 195))
plate = band.resize((1080, 1620), Image.BICUBIC)
plate = Image.blend(plate.filter(ImageFilter.GaussianBlur(22)), plate.filter(ImageFilter.BoxBlur(30)).filter(ImageFilter.GaussianBlur(10)), 0.5)
arr = np.asarray(plate).astype(np.float32) * np.linspace(1.05, 0.8, 1620)[:, None, None]
arr += np.random.default_rng(5).normal(0, 2.2, (1620, 1080, 1))
plate = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8)).crop((0, 40, 1080, 1390)).resize((720, 900), Image.LANCZOS)
cut = Image.open(f'{raw}/donna-cut.png').convert('RGBA')
a = cut.getchannel('A').filter(ImageFilter.MinFilter(3))
rgb = np.asarray(cut.convert('RGB')).astype(np.float32)
edge = (np.asarray(cut.getchannel('A')).astype(np.float32) - np.asarray(a.filter(ImageFilter.MinFilter(5))).astype(np.float32)).clip(0, 255) / 255
rgb *= (1 - 0.35 * edge)[..., None]; rgb[..., 0] *= 1.05; rgb[..., 2] *= 0.94
cut = Image.fromarray(np.clip(rgb * 1.02, 0, 255).astype(np.uint8)); cut.putalpha(a)
s = 196 / 156; cx, cy = 396, 235
cut = cut.resize((round(cut.width * s), round(cut.height * s)), Image.LANCZOS)
cut.putalpha(cut.getchannel('A').filter(ImageFilter.GaussianBlur(0.9)))
x, y = round(376 - cx * s), round(319 - cy * s)
comp = plate.convert('RGBA'); comp.alpha_composite(cut, (max(x, 0), max(y, 0)), (max(-x, 0), max(-y, 0)))
comp.convert('RGB').save(out, quality=80, optimize=True, progressive=True)
