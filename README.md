# VÉRTICE — Private Concierge

> **"A vida que você deseja, conduzida com discrição."**  
> Uma experiência editorial de ultra-luxo e lifestyle management concebida para clientes de alto padrão.

---

## 🏛️ Sobre o Projeto

A landing page da **VÉRTICE Private** foi projetada com rigor estético, minimalismo noir e conversão discreta via WhatsApp. Principais diferenciais e arquitetura de design:

- **Preloader com Logotipo Vetorial se Formando:** Ao abrir o site, as arestas do monograma geométrico da VÉRTICE são desenhadas com traço de luz prateada (`stroke-dashoffset`), com pulsação suave no ponto de convergência central e revelação em tipografia *Cinzel*.
- **Posicionamento Concierge Integral (Lifestyle Management):**
  - **Viagens e Experiências:** Itinerários sob medida, hospedagens exclusivas e acessos raros.
  - **Mobilidade e Transporte:** Motoristas particulares de confiança e transfers discretos.
  - **Rotina e Tempo Pessoal:** Agenda, compromissos e prioridades conduzidos com leveza.
  - **Acessos e Gastronomia:** Mesas disputadas, eventos fechados e curadoria cultural.
  - **Rede de Contatos e Especialistas:** Médicos de referência e assessoria qualificada.
  - **Gestão de Residências & Imprevistos:** Da residência impecável a imprevistos solucionados em silêncio.
- **Seção de Contato estilo Carta / Envelope de Luxo 3D:** Envelope físico de papelaria nobre com lacre metálico. Ao rolar ou interagir, o envelope se abre em 3D (`rotateX(180deg)`) e a folha timbrada desliza suavemente para preenchimento e envio direto ao WhatsApp oficial `+55 (48) 98477-7489`.
- **Estética High-Contrast Noir & Madeira Nobre:** Preto obsidiana profundo (`#060709`), acentos em carvalho/nogueira (*dark walnut*), superfícies de vidro fosco (*matte glassmorphism*) e luz ambiente (*cursor spotlight*) dinâmica.
- **Copywriting Humanizado:** Redigido pelo Claude com pontuação cadenciada, elegância aristocrática e sem travessões.

---

## 📁 Estrutura de Arquivos

```text
vertice-landing/
├── index.html                   # Estrutura semântica principal
├── css/
│   └── style.css                # Design tokens, preloader animado, envelope 3D e motion
├── js/
│   └── main.js                  # Lógica do preloader, spotlight, envelope 3D e WhatsApp bridge
├── assets/
│   ├── images/                  # 12 Renders 3D cromados e textura nobre de carvalho
│   └── logos/                   # Identidade oficial VÉRTICE (PNG e SVG vetorial)
├── copywriting_lifestyle.md     # Documento mestre de redação editorial (Claude Opus 5.5)
├── generate_3d_assets.py        # Script gerador dos assets visuais
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

## 🌐 Deploy no GitHub Pages

Para ativar a visualização online no seu GitHub:
1. Acesse o repositório em: [github.com/stocaline/vertice-landing](https://github.com/stocaline/vertice-landing).
2. Vá em **Settings** > **Pages**.
3. Em *Build and deployment* > *Source*, selecione `Deploy from a branch`.
4. Escolha a branch `main` e a pasta `/ (root)`.
5. Em poucos instantes o site estará acessível no endereço:  
   👉 **`https://stocaline.github.io/vertice-landing/`**

---

## 🎨 Tipografia

- **Cinzel:** Logotipo e títulos com proporções epigráficas clássicas.
- **Plus Jakarta Sans:** Tipografia moderna de alta legibilidade para corpo e interface.
- **JetBrains Mono:** Tags técnicas e numerais de precisão.
