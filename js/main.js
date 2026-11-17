/**
 * VÉRTICE PRIVATE CONCIERGE · INTERACTIVE MOTION & LOGIC
 * Efeitos: 3D Card Tilt, Magnetic Buttons, Scroll Reveal, WhatsApp Funnel
 */

document.addEventListener('DOMContentLoaded', () => {
  init3DCardTilt();
  initWhatsAppForm();
  initScrollAnimations();
  initSmoothScroll();
});

/* --------------------------------------------------------------------------
   1. INTERACTIVE 3D CARD TILT (Hero Black Card)
   -------------------------------------------------------------------------- */
function init3DCardTilt() {
  const cardStage = document.getElementById('heroCardStage');
  const card = document.getElementById('card3d');

  if (!cardStage || !card) return;

  let bounds;

  function rotateToMouse(e) {
    bounds = cardStage.getBoundingClientRect();
    const mouseX = e.clientX;
    const mouseY = e.clientY;
    const leftX = mouseX - bounds.x;
    const topY = mouseY - bounds.y;
    const center = {
      x: leftX - bounds.width / 2,
      y: topY - bounds.height / 2
    };
    const distance = Math.sqrt(center.x ** 2 + center.y ** 2);

    const maxTilt = 18;
    const tiltX = (center.y / (bounds.height / 2)) * -maxTilt;
    const tiltY = (center.x / (bounds.width / 2)) * maxTilt;

    card.style.transform = `
      rotateX(${tiltX.toFixed(2)}deg) 
      rotateY(${tiltY.toFixed(2)}deg)
      scale3d(1.04, 1.04, 1.04)
    `;

    // Efeito de brilho especular dinâmico
    const glintProg = Math.max(0.15, Math.min(0.85, (center.x / bounds.width) + 0.5));
    card.style.setProperty('--card-glint', glintProg.toFixed(2));
  }

  cardStage.addEventListener('mouseenter', () => {
    bounds = cardStage.getBoundingClientRect();
    document.addEventListener('mousemove', rotateToMouse);
  });

  cardStage.addEventListener('mouseleave', () => {
    document.removeEventListener('mousemove', rotateToMouse);
    card.style.transform = 'rotateX(0deg) rotateY(0deg) scale3d(1, 1, 1)';
    card.style.transition = 'transform 0.6s cubic-bezier(0.16, 1, 0.3, 1)';
    card.style.setProperty('--card-glint', '0.35');
  });
}

/* --------------------------------------------------------------------------
   2. ENQUIRY FORM -> DISPARO DIRETO PARA O WHATSAPP
   -------------------------------------------------------------------------- */
function initWhatsAppForm() {
  const form = document.getElementById('enquiryForm');
  if (!form) return;

  form.addEventListener('submit', (e) => {
    e.preventDefault();

    const nome = document.getElementById('clientName').value.trim();
    const local = document.getElementById('clientLocation').value.trim();
    const demanda = document.getElementById('clientDemand').value.trim();

    if (!demanda) {
      alert('Por favor, descreva brevemente qual serviço ou pendência você precisa resolver.');
      return;
    }

    // Monta mensagem natural e elegante para o WhatsApp do Concierge
    let texto = 'Olá! Gostaria de acionar a curadoria do Vértice Private Concierge.';
    if (nome) texto += `\nMeu nome é *${nome}*`;
    if (local) texto += ` (Condomínio / Bairro: *${local}*).`;
    else texto += '.';
    texto += `\n\nMinha pendência é: \n"${demanda}"`;
    texto += '\n\nAguardo as 3 opções checadas. Obrigado!';

    const encodedText = encodeURIComponent(texto);
    const waUrl = `https://wa.me/5548984777489?text=${encodedText}`;

    // Abre direto o WhatsApp em nova aba
    window.open(waUrl, '_blank', 'noopener,noreferrer');
  });
}

/* --------------------------------------------------------------------------
   3. SCROLL REVEAL ANIMATIONS (IntersectionObserver)
   -------------------------------------------------------------------------- */
function initScrollAnimations() {
  const elements = document.querySelectorAll('.reveal-on-scroll');
  if (!elements.length) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-revealed');
        observer.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.12,
    rootMargin: '0px 0px -40px 0px'
  });

  elements.forEach(el => observer.observe(el));
}

/* --------------------------------------------------------------------------
   4. SMOOTH SCROLL PARA ÂNCORAS
   -------------------------------------------------------------------------- */
function initSmoothScroll() {
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      const targetId = this.getAttribute('href');
      if (targetId === '#' || !targetId) return;

      const targetEl = document.querySelector(targetId);
      if (targetEl) {
        e.preventDefault();
        targetEl.scrollIntoView({
          behavior: 'smooth',
          block: 'start'
        });
      }
    });
  });
}
