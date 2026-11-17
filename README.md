# VÉRTICE — Private Concierge Residencial

> **"Concierge de serviços para a sua casa."**  
> Uma experiência editorial, minimalista e sofisticada concebida para moradores de condomínios de alto padrão.

---

## 🏛️ Sobre o Projeto

A landing page da **VÉRTICE Private** foi projetada com foco em exclusividade, elegância e conversão direta para clientes/moradores. O design equilibra:
- **Estética High-Contrast Noir:** Fundo preto obsidiana profundo (`#08090A`), superfícies de vidro escuro fosco (*matte glassmorphism*) e tipografia prata platina com acentos em branco puro.
- **Madeira Nobre (Dark Walnut):** Banner executivo com textura flutuante e acabamento de carvalho/nogueira escura, trazendo calor e autenticidade ao minimalismo digital.
- **Renders 3D Metálicos & Bento Grid:** Grid assimétrico inspirado no layout de alta relojoaria e design editorial suíço, com ícones e objetos cromados em perspectiva.
- **Hero Interativo (Cartão Black Físico):** Simulação 3D com efeito *tilt* interativo de giroscópio/cursor do mouse e brilho especular dinâmico no acabamento platina do cartão físico da Vértice.
- **Conversão sem Fricção:** Checklist interativo e formulário flutuante integrado ao WhatsApp oficial `+55 (48) 98477-7489`, gerando mensagens pré-formatadas prontas para envio.

---

## 📁 Estrutura de Arquivos

```text
vertice-landing/
├── index.html                   # Estrutura semântica principal (5 seções)
├── css/
│   └── style.css                # Design tokens, tipografia, glassmorphism e animações
├── js/
│   └── main.js                  # Tilt 3D, spec glint, scroll reveals e WhatsApp bridge
├── assets/
│   ├── images/                  # 12 Renders 3D cromados e textura nobre de madeira
│   │   ├── bento-concierge.png
│   │   ├── bento-tech.png
│   │   ├── bento-cubes.png
│   │   ├── bento-palette.png
│   │   ├── bento-road.png
│   │   ├── bento-lens.png
│   │   ├── feature-card1.png ... feature-card5.png
│   │   └── wood-texture.jpg
│   └── logos/                   # Identidade oficial Vértice (PNG e SVG vetorial)
│       ├── vertice-whatsapp-icone.png
│       ├── vertice-whatsapp-completo.png
│       ├── vertice-whatsapp-icone-transparente.png
│       └── vertice-whatsapp-icone.svg
├── generate_3d_assets.py        # Script gerador/renderizador dos assets 3D
├── .gitignore
└── README.md
```

---

## 🚀 Como Visualizar Localmente

Basta iniciar qualquer servidor estático HTTP dentro da pasta do projeto:

```bash
# Opção 1: Python
python -m http.server 8000

# Opção 2: Node.js (npx serve)
npx serve .
```

Abra seu navegador em: [`http://localhost:8000`](http://localhost:8000) ou dê duplo clique em `index.html`.

---

## 📤 Publicação no GitHub (`stocaline/vertice-landing`)

Para enviar este repositório para a sua conta pessoal no GitHub:

1. **Crie um novo repositório vazio no seu GitHub:**  
   Acesse [github.com/new](https://github.com/new) e dê o nome `vertice-landing` (deixe desmarcada a opção de adicionar README).

2. **No terminal dentro da pasta `D:\workspace\vertice-landing`, execute:**
   ```bash
   git branch -M main
   git remote add origin https://github.com/stocaline/vertice-landing.git
   git push -u origin main
   ```

3. **Deploy no GitHub Pages (Opcional):**
   - No GitHub do repositório, vá em **Settings** > **Pages**.
   - Em *Source*, selecione `Deploy from a branch` e escolha a branch `main` (pasta `/root`).
   - A página ficará instantaneamente acessível online no endereço:  
     `https://stocaline.github.io/vertice-landing/`

---

## 🎨 Design Tokens & Tipografia

- **Cinzel / Playfair Display:** Serifas editoriais clássicas para títulos de alto impacto.
- **Plus Jakarta Sans:** Tipografia moderna de legibilidade máxima para corpo e interfaces.
- **JetBrains Mono:** Numerais e tags técnicas em estilo estúdio suíço.
- **Paleta:** Obsidian `#08090A` / `#0D0E12`, Platinum `#E4E7EC`, Crisp White `#FFFFFF`, Muted Silver `#8F94A0`, Walnut Warmth `#20140D`.
