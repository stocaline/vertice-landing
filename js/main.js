/**
 * VÉRTICE PRIVATE CONCIERGE · INTERACTION & MOTION CONTROLLER
 * Animações: Preloader SVG, Ambient Cursor, 3D Tilt, Envelope Interativo & WhatsApp Bridge
 */

document.addEventListener('DOMContentLoaded', () => {
  // 1. Preloader com Logotipo se formando
  const preloader = document.getElementById('preloader');
  const minPreloaderTime = 1600; // 1.6 segundos para contemplar o desenho do monograma
  const startTime = Date.now();

  const hidePreloader = () => {
    const elapsed = Date.now() - startTime;
    const remaining = Math.max(0, minPreloaderTime - elapsed);

    setTimeout(() => {
      if (preloader) {
        preloader.classList.add('is-loaded');
        // Remover do fluxo após a transição para liberar performance
        setTimeout(() => {
          preloader.style.display = 'none';
        }, 800);
      }
    }, remaining);
  };

  if (document.readyState === 'complete') {
    hidePreloader();
  } else {
    window.addEventListener('load', hidePreloader);
  }

  // 2. Cursor Ambient Spotlight
  const spotlight = document.querySelector('.cursor-spotlight');
  if (spotlight && window.matchMedia('(pointer: fine)').matches) {
    let mouseX = window.innerWidth / 2;
    let mouseY = window.innerHeight / 2;
    let currentX = mouseX;
    let currentY = mouseY;

    window.addEventListener('pointermove', (e) => {
      mouseX = e.clientX;
      mouseY = e.clientY;
    });

    const animateSpotlight = () => {
      currentX += (mouseX - currentX) * 0.12;
      currentY += (mouseY - currentY) * 0.12;
      spotlight.style.transform = `translate(${currentX}px, ${currentY}px) translate(-50%, -50%)`;
      requestAnimationFrame(animateSpotlight);
    };
    animateSpotlight();
  }

  // 3. Navbar Scrolled State
  const navbar = document.querySelector('.navbar');
  const handleScroll = () => {
    if (window.scrollY > 40) {
      navbar?.classList.add('scrolled');
    } else {
      navbar?.classList.remove('scrolled');
    }
  };
  window.addEventListener('scroll', handleScroll, { passive: true });

  // 4. Bento Grid & Feature Cards Mouse Sheen
  const cards = document.querySelectorAll('.bento-card, .feature-card');
  cards.forEach((card) => {
    card.addEventListener('pointermove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      card.style.setProperty('--mouse-x', `${x}px`);
      card.style.setProperty('--mouse-y', `${y}px`);
    });
  });

  // 5. Envelope de Luxo 3D Interativo
  const envelopeWrapper = document.getElementById('envelopeWrapper');
  const envelopeSeal = document.getElementById('envelopeSeal');
  const letterInputs = document.querySelectorAll('.letter-input, .letter-textarea');
  const letterForm = document.getElementById('letterForm');

  const openEnvelope = () => {
    if (envelopeWrapper && !envelopeWrapper.classList.contains('is-open')) {
      envelopeWrapper.classList.add('is-open');
    }
  };

  if (envelopeSeal) {
    envelopeSeal.addEventListener('click', openEnvelope);
  }

  letterInputs.forEach((input) => {
    input.addEventListener('focus', openEnvelope);
  });

  // Auto-abrir com IntersectionObserver ao rolar até o contato
  const contactSection = document.getElementById('contato');
  if (contactSection && 'IntersectionObserver' in window) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          setTimeout(openEnvelope, 400);
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.35 });

    observer.observe(contactSection);
  }

  // 6. Envio da Carta via WhatsApp
  if (letterForm) {
    letterForm.addEventListener('submit', (e) => {
      e.preventDefault();

      const name = document.getElementById('letterName')?.value.trim() || 'Não informado';
      const location = document.getElementById('letterLocation')?.value.trim() || 'Florianópolis / Região';
      const demand = document.getElementById('letterDemand')?.value.trim();

      if (!demand) {
        alert('Por favor, descreva em poucas palavras o que você gostaria de resolver na sua casa.');
        return;
      }

      const whatsappNumber = '5548984777489';
      const text = [
        'Olá, equipe VÉRTICE Private Concierge.',
        '',
        `Meu nome é: ${name}`,
        `Localização: ${location}`,
        '',
        'Em casa, eu gostaria de:',
        `"${demand}"`,
        '',
        'Gostaria de agendar uma conversa confidencial para entender como podemos conduzir essa demanda.'
      ].join('\n');

      const encodedText = encodeURIComponent(text);
      const url = `https://wa.me/${whatsappNumber}?text=${encodedText}`;

      window.open(url, '_blank', 'noopener,noreferrer');
    });
  }

  // 7. Smooth Scroll para links internos
  document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener('click', function (e) {
      const targetId = this.getAttribute('href');
      if (targetId && targetId !== '#') {
        const targetElement = document.querySelector(targetId);
        if (targetElement) {
          e.preventDefault();
          targetElement.scrollIntoView({ behavior: 'smooth' });
        }
      }
    });
  });
});
