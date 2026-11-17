"""
Gerador de Renders 3D Metálicos & Texturas de Madeira Nobre para a Landing Page VÉRTICE.
Inspirado diretamente nas referências:
- service-bento-v2.webp (ícones metálicos 3D sobre fundo preto)
- render-grid-v2.webp (placas, grelhas, velocímetros e órbitas metálicas)
- Textura de madeira nobre (dark walnut / carvalho americano)
"""
import math
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
from pathlib import Path

OUT_DIR = Path(r"D:\workspace\vertice-landing\assets\images")
OUT_DIR.mkdir(parents=True, exist_ok=True)

def create_base(w=800, h=600):
    return Image.new("RGBA", (w, h), (0, 0, 0, 0))

# 1. BENTO CONCIERGE: Pena estilizada / Chave e Fita Metálica Cromada em 3D
def render_bento_concierge():
    w, h = 800, 600
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(im)
    cx, cy = 400, 300

    # Fita curva cromada atrás
    points = []
    for t in np.linspace(-math.pi*0.8, math.pi*0.8, 120):
        r = 170 + 40 * math.sin(t * 2)
        x = cx + r * math.cos(t)
        y = cy + r * math.sin(t) * 0.45 + 50
        points.append((x, y))
    
    # Desenha fita com gradiente cromado
    for i in range(len(points)-1):
        p1, p2 = points[i], points[i+1]
        prog = i / len(points)
        # Brilho metálico oscilante
        val = int(140 + 115 * math.sin(prog * math.pi * 3)**2)
        draw.line([p1, p2], fill=(val, val, int(val*1.05), 230), width=32)

    # Corpo da Caneta / Chave em prisma metálico (inclinado a 35 graus)
    angle = math.radians(-32)
    cos_a, sin_a = math.cos(angle), math.sin(angle)
    
    # Tubo da caneta
    pen_len = 220
    pen_w = 40
    p_center = (cx - 20, cy - 20)
    
    # Bico metálico da pena (triângulo facetado)
    tip_len = 110
    tip_pts = [
        (p_center[0] - pen_len*0.5*cos_a, p_center[1] - pen_len*0.5*sin_a),
        (p_center[0] - (pen_len*0.5 + tip_len)*cos_a, p_center[1] - (pen_len*0.5 + tip_len)*sin_a),
    ]
    # Lado esquerdo e direito do bico
    p_base_l = (tip_pts[0][0] - pen_w*0.5*sin_a, tip_pts[0][1] + pen_w*0.5*cos_a)
    p_base_r = (tip_pts[0][0] + pen_w*0.5*sin_a, tip_pts[0][1] - pen_w*0.5*cos_a)
    p_tip = tip_pts[1]

    # Face esquerda do bico (sombreada)
    draw.polygon([p_tip, p_base_l, tip_pts[0]], fill=(180, 185, 195, 255))
    # Face direita do bico (com reflexo especular branco puro)
    draw.polygon([p_tip, p_base_r, tip_pts[0]], fill=(255, 255, 255, 255))
    # Fenda central da pena
    draw.line([p_tip, tip_pts[0]], fill=(30, 32, 40, 255), width=3)
    # Respiro circular da pena
    draw.ellipse([tip_pts[0][0]-5, tip_pts[0][1]-5, tip_pts[0][0]+5, tip_pts[0][1]+5], fill=(20, 22, 28, 255))

    # Corpo cilíndrico metálico
    p_top_l = (p_base_l[0] + pen_len*cos_a, p_base_l[1] + pen_len*sin_a)
    p_top_r = (p_base_r[0] + pen_len*cos_a, p_base_r[1] + pen_len*sin_a)
    draw.polygon([p_base_l, p_base_r, p_top_r, p_top_l], fill=(45, 48, 56, 255))

    # Anel de ouro branco / prata com friso
    draw.line([p_base_l, p_base_r], fill=(255, 255, 255, 255), width=12)
    draw.line([p_base_l, p_base_r], fill=(120, 125, 135, 255), width=4)

    # Brilho especular ao longo do corpo
    draw.line([
        (tip_pts[0][0] + pen_w*0.2*sin_a, tip_pts[0][1] - pen_w*0.2*cos_a),
        (tip_pts[0][0] + pen_w*0.2*sin_a + pen_len*cos_a, tip_pts[0][1] - pen_w*0.2*cos_a + pen_len*sin_a)
    ], fill=(240, 245, 255, 220), width=6)

    # Fita curva na frente
    points_front = []
    for t in np.linspace(-math.pi*0.2, math.pi*0.7, 70):
        r = 180 + 35 * math.sin(t * 2)
        x = cx + r * math.cos(t)
        y = cy + r * math.sin(t) * 0.45 + 50
        points_front.append((x, y))
    for i in range(len(points_front)-1):
        p1, p2 = points_front[i], points_front[i+1]
        prog = i / len(points_front)
        val = int(180 + 75 * math.sin(prog * math.pi * 2)**2)
        draw.line([p1, p2], fill=(val, val, int(val*1.08), 240), width=32)
        # Borda brilhante na fita
        draw.line([p1, p2], fill=(255, 255, 255, 180), width=2)

    im = im.filter(ImageFilter.GaussianBlur(0.6))
    im.save(OUT_DIR / "bento-concierge.png")
    print("Salvo: bento-concierge.png")

# 2. BENTO TECH: Laptop Metálico com Código `< / >`
def render_bento_tech():
    w, h = 800, 600
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(im)
    cx, cy = 420, 320

    # Tela do laptop em perspectiva isométrica
    screen_pts = [
        (cx - 160, cy - 140),
        (cx + 140, cy - 100),
        (cx + 120, cy + 90),
        (cx - 180, cy + 50)
    ]
    # Moldura externa em titânio escuro
    draw.polygon(screen_pts, fill=(25, 27, 32, 255), outline=(180, 185, 195, 255))
    # Bezel
    inner_screen = [
        (cx - 145, cy - 125),
        (cx + 125, cy - 88),
        (cx + 108, cy + 75),
        (cx - 162, cy + 40)
    ]
    draw.polygon(inner_screen, fill=(10, 11, 14, 255))

    # Base / Teclado
    base_pts = [
        (cx - 180, cy + 50),
        (cx + 120, cy + 90),
        (cx + 60, cy + 180),
        (cx - 240, cy + 130)
    ]
    draw.polygon(base_pts, fill=(35, 38, 45, 255), outline=(220, 225, 235, 255))
    # Trackpad
    track_pts = [
        (cx - 110, cy + 115),
        (cx - 30, cy + 127),
        (cx - 50, cy + 155),
        (cx - 130, cy + 142)
    ]
    draw.polygon(track_pts, fill=(28, 30, 36, 255), outline=(140, 145, 155, 180))

    # Símbolo brilhante `< / >` na tela em prata líquida
    # `<`
    draw.line([(cx - 70, cy - 30), (cx - 110, cy - 10), (cx - 65, cy + 15)], fill=(255, 255, 255, 255), width=10)
    # `/`
    draw.line([(cx - 35, cy + 25), (cx + 5, cy - 45)], fill=(240, 245, 255, 255), width=10)
    # `>`
    draw.line([(cx + 35, cy - 40), (cx + 75, cy - 20), (cx + 40, cy + 5)], fill=(255, 255, 255, 255), width=10)

    # Brilho de reflexo na borda da tela
    draw.line([screen_pts[0], screen_pts[1]], fill=(255, 255, 255, 220), width=3)
    im.save(OUT_DIR / "bento-tech.png")
    print("Salvo: bento-tech.png")

# 3. BENTO CUBOS: Cubos Metálicos Conectados (Biblioteca de Mapas)
def render_bento_cubos():
    w, h = 800, 600
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(im)
    cx, cy = 400, 320

    def draw_iso_cube(x, y, s):
        dx = s * math.cos(math.radians(30))
        dy = s * math.sin(math.radians(30))
        
        # Top face (mais clara)
        top = [(x, y - s), (x + dx, y - s + dy), (x, y - s + 2*dy), (x - dx, y - s + dy)]
        draw.polygon(top, fill=(235, 240, 250, 255), outline=(255, 255, 255, 255))
        # Left face (tom médio)
        left = [(x - dx, y - s + dy), (x, y - s + 2*dy), (x, y + dy), (x - dx, y)]
        draw.polygon(left, fill=(110, 115, 125, 255), outline=(180, 185, 195, 255))
        # Right face (tom escuro)
        right = [(x, y - s + 2*dy), (x + dx, y - s + dy), (x + dx, y), (x, y + dy)]
        draw.polygon(right, fill=(45, 48, 55, 255), outline=(140, 145, 155, 255))

    s = 48
    # Pirâmide isométrica de cubos
    draw_iso_cube(cx, cy - s*1.7, s)
    draw_iso_cube(cx - s*0.86, cy - s*0.85 + s*0.5, s)
    draw_iso_cube(cx + s*0.86, cy - s*0.85 + s*0.5, s)
    draw_iso_cube(cx - s*1.73, cy + s*0.5, s)
    draw_iso_cube(cx, cy + s*0.5, s)
    draw_iso_cube(cx + s*1.73, cy + s*0.5, s)

    im.save(OUT_DIR / "bento-cubes.png")
    print("Salvo: bento-cubes.png")

# 4. BENTO PALETA: Paleta Metálica com Pincel (Marcenaria & Reformas)
def render_bento_paleta():
    w, h = 800, 600
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(im)
    cx, cy = 400, 300

    # Paleta metálica circular chanfrada
    draw.ellipse([cx-150, cy-130, cx+150, cy+130], fill=(30, 32, 38, 255), outline=(200, 205, 215, 255), width=6)
    draw.ellipse([cx+50, cy+10, cx+110, cy+70], fill=(0, 0, 0, 0), outline=(180, 185, 195, 255), width=4)

    # 4 cavidades esféricas metálicas
    holes = [(cx-90, cy-50), (cx-40, cy-75), (cx+25, cy-75), (cx-90, cy+25)]
    for hx, hy in holes:
        draw.ellipse([hx-20, hy-18, hx+20, hy+18], fill=(18, 19, 22, 255), outline=(140, 145, 155, 200), width=2)
        draw.ellipse([hx-8, hy-8, hx+8, hy+8], fill=(220, 225, 235, 240))

    # Pincel metálico cruzando a paleta
    brush_pts = [(cx-140, cy+140), (cx+160, cy-140)]
    draw.line(brush_pts, fill=(245, 248, 255, 255), width=16)
    draw.line(brush_pts, fill=(120, 125, 135, 255), width=6)
    # Cerda chanfrada
    draw.line([(cx+145, cy-125), (cx+185, cy-165)], fill=(255, 255, 255, 255), width=20)

    im.save(OUT_DIR / "bento-palette.png")
    print("Salvo: bento-palette.png")

# 5. BENTO ROAD: Caminho em Fita com 3 Pinos de Decisão (O Mapa dos 3 Caminhos)
def render_bento_road():
    w, h = 800, 600
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(im)
    cx, cy = 400, 310

    # Fita sinuosa metálica 3D em perspectiva
    pts_s = []
    for x in np.linspace(cx - 240, cx + 240, 120):
        t = (x - (cx - 240)) / 480
        y = cy + 90 * math.sin(t * math.pi * 2.2) + (1 - t) * 60
        pts_s.append((x, y))

    for i in range(len(pts_s)-1):
        p1, p2 = pts_s[i], pts_s[i+1]
        prog = i / len(pts_s)
        val = int(120 + 130 * math.cos(prog * math.pi * 2)**2)
        draw.line([p1, p2], fill=(val, val, int(val*1.06), 255), width=42)
        # Borda cromada superior
        draw.line([(p1[0], p1[1]-20), (p2[0], p2[1]-20)], fill=(255, 255, 255, 230), width=3)

    # 3 Pinos de Localização Metálicos em gota
    pin_x = [cx - 150, cx, cx + 160]
    for idx, px in enumerate(pin_x):
        # Encontra o y correspondente na fita
        t = (px - (cx - 240)) / 480
        py = cy + 90 * math.sin(t * math.pi * 2.2) + (1 - t) * 60 - 55
        
        # Sombra do pino
        draw.ellipse([px-18, py+45, px+18, py+57], fill=(10, 10, 12, 180))
        # Corpo do pino (círculo superior + ponta)
        draw.ellipse([px-26, py-26, px+26, py+26], fill=(245, 248, 255, 255), outline=(120, 125, 135, 255), width=3)
        draw.polygon([(px-22, py+5), (px+22, py+5), (px, py+50)], fill=(245, 248, 255, 255))
        # Orifício central no pino
        draw.ellipse([px-10, py-10, px+10, py+10], fill=(20, 22, 28, 255), outline=(255, 255, 255, 255), width=2)
        # Reflexo especular
        draw.ellipse([px-18, py-20, px-8, py-10], fill=(255, 255, 255, 255))

    im.save(OUT_DIR / "bento-road.png")
    print("Salvo: bento-road.png")

# 6. BENTO LENS: Lupa Metálica / Acompanhamento 48h
def render_bento_lens():
    w, h = 800, 600
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(im)
    cx, cy = 380, 280

    # Cabo inclinado metálico
    draw.line([(cx+70, cy+70), (cx+190, cy+190)], fill=(60, 64, 75, 255), width=28)
    draw.line([(cx+70, cy+70), (cx+190, cy+190)], fill=(240, 245, 255, 255), width=8)

    # Anel da Lupa cromado
    draw.ellipse([cx-120, cy-120, cx+120, cy+120], fill=(18, 20, 25, 255), outline=(230, 235, 245, 255), width=18)
    draw.ellipse([cx-105, cy-105, cx+105, cy+105], fill=(12, 13, 16, 255), outline=(80, 85, 95, 255), width=4)

    # Reflexo de lente de vidro
    draw.arc([cx-90, cy-90, cx+90, cy+90], start=190, end=320, fill=(255, 255, 255, 220), width=8)

    # Ícone central de Play / VÉRTICE no vidro
    draw.polygon([(cx-25, cy-40), (cx+45, cy), (cx-25, cy+40)], fill=(245, 248, 255, 255), outline=(120, 125, 135, 255), width=3)

    im.save(OUT_DIR / "bento-lens.png")
    print("Salvo: bento-lens.png")

# 7. FEATURE CARDS: Cartões Pretos Flutuantes (como no render-grid-v2.webp)
def render_feature_cards():
    w, h = 800, 600
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(im)
    cx, cy = 400, 300

    def draw_card(ox, oy, tilt_x, tilt_y, rot):
        card_w, card_h = 240, 140
        c_im = Image.new("RGBA", (card_w, card_h), (0, 0, 0, 0))
        c_draw = ImageDraw.Draw(c_im)
        # Corpo preto com borda metálica
        c_draw.rounded_rectangle([0, 0, card_w-1, card_h-1], radius=14, fill=(18, 19, 23, 240), outline=(180, 185, 195, 220), width=2)
        # Reflexo especular no canto
        c_draw.line([(0, 0), (card_w*0.7, 0)], fill=(255, 255, 255, 200), width=3)
        c_rot = c_im.rotate(rot, expand=True, resample=Image.BICUBIC)
        im.paste(c_rot, (int(ox - c_rot.width*0.5), int(oy - c_rot.height*0.5)), c_rot)

    # Três cartões em cascata
    draw_card(cx - 30, cy + 20, 0, 0, -18)
    draw_card(cx + 40, cy - 10, 0, 0, 12)
    draw_card(cx, cy - 25, 0, 0, -4)

    im.save(OUT_DIR / "feature-card1.png")
    print("Salvo: feature-card1.png")

# 8. FEATURE GRID: Grelha com Luz Central e Feixe Vertical
def render_feature_grid():
    w, h = 800, 600
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(im)
    cx, cy = 400, 320

    # Grid em perspectiva isométrica (5x5 tiles)
    tile_s = 36
    for i in range(-2, 3):
        for j in range(-2, 3):
            tx = cx + (i - j) * tile_s * 1.3
            ty = cy + (i + j) * tile_s * 0.75
            w_tile = tile_s * 1.1
            h_tile = tile_s * 0.65
            
            pts = [
                (tx, ty - h_tile*0.5),
                (tx + w_tile*0.5, ty),
                (tx, ty + h_tile*0.5),
                (tx - w_tile*0.5, ty)
            ]
            if i == 0 and j == 0:
                # O tile central brilhante
                draw.polygon(pts, fill=(255, 255, 255, 255), outline=(255, 255, 255, 255))
            else:
                dist = math.hypot(i, j)
                b = max(30, int(90 - dist * 25))
                draw.polygon(pts, fill=(b, b+2, b+6, 255), outline=(b+40, b+42, b+48, 200), width=1)

    # Feixe de luz vertical saindo do centro
    beam = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    b_draw = ImageDraw.Draw(beam)
    b_draw.polygon([(cx-25, 0), (cx+25, 0), (cx+60, cy), (cx-60, cy)], fill=(255, 255, 255, 60))
    beam = beam.filter(ImageFilter.GaussianBlur(14))
    im = Image.alpha_composite(im, beam)

    im.save(OUT_DIR / "feature-card2.png")
    print("Salvo: feature-card2.png")

# 9. FEATURE PLATES: Placas Metálicas Escalonadas com Feixe Horizontal
def render_feature_plates():
    w, h = 800, 600
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(im)
    cx, cy = 400, 300

    # 3 placas quadradas chanfradas inclinadas
    plates = [
        (cx - 30, cy + 50, 160, -15),
        (cx - 10, cy + 15, 175, -8),
        (cx + 20, cy - 25, 190, 0)
    ]
    for px, py, sz, rot in plates:
        p_im = Image.new("RGBA", (sz, sz), (0, 0, 0, 0))
        p_draw = ImageDraw.Draw(p_im)
        p_draw.rounded_rectangle([0, 0, sz-1, sz-1], radius=16, fill=(22, 24, 30, 250), outline=(200, 205, 215, 255), width=2)
        p_rot = p_im.rotate(rot, expand=True, resample=Image.BICUBIC)
        im.paste(p_rot, (int(px - p_rot.width*0.5), int(py - p_rot.height*0.5)), p_rot)

    # Feixe de luz horizontal brilhante cortando a placa superior
    streak = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    s_draw = ImageDraw.Draw(streak)
    s_draw.line([(cx - 160, cy - 40), (cx + 180, cy - 10)], fill=(255, 255, 255, 240), width=12)
    streak = streak.filter(ImageFilter.GaussianBlur(4))
    im = Image.alpha_composite(im, streak)

    im.save(OUT_DIR / "feature-card3.png")
    print("Salvo: feature-card3.png")

# 10. FEATURE SPEEDO: Velocímetro Metálico com Brilho
def render_feature_speedo():
    w, h = 800, 600
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(im)
    cx, cy = 400, 360
    r = 180

    # Arco do dial
    draw.arc([cx-r, cy-r, cx+r, cy+r], start=180, end=360, fill=(45, 48, 56, 255), width=18)
    
    # Ticks metálicos
    for deg in range(180, 365, 6):
        rad = math.radians(deg)
        x1 = cx + (r - 18) * math.cos(rad)
        y1 = cy + (r - 18) * math.sin(rad)
        length = 16 if deg % 30 == 0 else 8
        x2 = cx + (r - 18 - length) * math.cos(rad)
        y2 = cy + (r - 18 - length) * math.sin(rad)
        bright = 255 if deg > 270 else 140
        draw.line([(x1, y1), (x2, y2)], fill=(bright, bright, bright, 220), width=3 if deg % 30 == 0 else 1)

    # Ponteiro em prata no ápice da velocidade
    p_ang = math.radians(315)
    px = cx + (r - 10) * math.cos(p_ang)
    py = cy + (r - 10) * math.sin(p_ang)
    draw.line([(cx, cy), (px, py)], fill=(255, 255, 255, 255), width=5)
    draw.ellipse([cx-16, cy-16, cx+16, cy+16], fill=(220, 225, 235, 255), outline=(60, 64, 75, 255), width=3)

    # Glow no ápice
    glow = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    g_draw = ImageDraw.Draw(glow)
    g_draw.ellipse([px-35, py-35, px+35, py+35], fill=(255, 255, 255, 180))
    glow = glow.filter(ImageFilter.GaussianBlur(10))
    im = Image.alpha_composite(im, glow)

    im.save(OUT_DIR / "feature-card4.png")
    print("Salvo: feature-card4.png")

# 11. FEATURE ORBIT: Esfera Central com Órbitas e Satélites
def render_feature_orbit():
    w, h = 800, 600
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(im)
    cx, cy = 400, 300
    r_orbit = 135

    # Anel orbital metálico
    draw.ellipse([cx-r_orbit, cy-r_orbit, cx+r_orbit, cy+r_orbit], fill=None, outline=(80, 85, 95, 200), width=3)

    # Esfera central cromada com brilho
    draw.ellipse([cx-50, cy-50, cx+50, cy+50], fill=(20, 22, 28, 255), outline=(220, 225, 235, 255), width=6)
    draw.ellipse([cx-25, cy-25, cx+5, cy+5], fill=(255, 255, 255, 220))

    # 5 satélites esféricos ao redor
    for i in range(5):
        ang = math.radians(i * 72 - 30)
        sx = cx + r_orbit * math.cos(ang)
        sy = cy + r_orbit * math.sin(ang)
        # Linha conectora ao centro
        draw.line([(cx, cy), (sx, sy)], fill=(60, 64, 75, 150), width=1)
        draw.ellipse([sx-14, sy-14, sx+14, sy+14], fill=(230, 235, 245, 255), outline=(100, 105, 115, 255), width=2)

    im.save(OUT_DIR / "feature-card5.png")
    print("Salvo: feature-card5.png")

# 12. TEXTURA DE MADEIRA NOBRE (Dark Walnut / Carvalho Americano com Iluminação Suave)
def render_wood_texture():
    w, h = 1200, 800
    # Gera base procedural de madeira escura com veios elegantes
    arr = np.zeros((h, w, 3), dtype=np.uint8)
    for y in range(h):
        # Tom base: marrom escuro nogueira (RGB aprox 38, 25, 18)
        grain = math.sin(y * 0.12 + math.sin(y * 0.02) * 8) * 8
        noise = (math.sin(y * 1.5) * 4) + (math.cos(y * 0.3) * 6)
        r = int(np.clip(38 + grain + noise, 22, 55))
        g = int(np.clip(25 + grain*0.7 + noise*0.7, 14, 38))
        b = int(np.clip(18 + grain*0.5 + noise*0.5, 9, 28))
        arr[y, :, 0] = r
        arr[y, :, 1] = g
        arr[y, :, 2] = b

    im = Image.fromarray(arr, mode="RGB")
    # Aplica desfoque direcional para simular veios de lixamento de alta marcenaria
    im = im.filter(ImageFilter.GaussianBlur(1.2))

    # Adiciona iluminação suave no topo / vinheta
    vignette = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    v_draw = ImageDraw.Draw(vignette)
    for x in range(0, w, 40):
        # Frisos canelados modernos
        v_draw.line([(x, 0), (x, h)], fill=(10, 6, 4, 120), width=3)
        v_draw.line([(x+2, 0), (x+2, h)], fill=(75, 52, 38, 70), width=1)

    im.paste(vignette, (0, 0), vignette)
    im.save(OUT_DIR / "wood-texture.jpg", quality=92)
    print("Salvo: wood-texture.jpg")

if __name__ == "__main__":
    render_bento_concierge()
    render_bento_tech()
    render_bento_cubos()
    render_bento_paleta()
    render_bento_road()
    render_bento_lens()
    render_feature_cards()
    render_feature_grid()
    render_feature_plates()
    render_feature_speedo()
    render_feature_orbit()
    render_wood_texture()
    print("Todos os assets 3D foram gerados com sucesso.")
