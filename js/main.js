/**
 * VÉRTICE PRIVATE CONCIERGE · interação e movimento
 * Preloader, revelações, inversão de seções, paralaxe, envelope e ponte com o WhatsApp.
 */

document.addEventListener('DOMContentLoaded', () => {
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const hasIO = 'IntersectionObserver' in window;

  // 1. Preloader: só libera as revelações depois que ele sai
  const preloader = document.getElementById('preloader');
  const startTime = Date.now();
  const minPreloaderTime = reduceMotion ? 0 : 1600;

  const startReveals = () => {
    const targets = document.querySelectorAll('.reveal, .reveal-media');
    if (!hasIO || reduceMotion) {
      targets.forEach((el) => el.classList.add('is-in'));
      return;
    }
    const io = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-in');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.15, rootMargin: '0px 0px -6% 0px' });
    targets.forEach((el) => io.observe(el));
  };

  const hidePreloader = () => {
    const remaining = Math.max(0, minPreloaderTime - (Date.now() - startTime));
    setTimeout(() => {
      document.body.classList.add('is-ready');
      preloader?.classList.add('is-loaded');
      setTimeout(() => { if (preloader) preloader.style.display = 'none'; }, 900);
      startReveals();
    }, remaining);
  };

  if (document.readyState === 'complete') hidePreloader();
  else window.addEventListener('load', hidePreloader);

  // 2. Seções que se invertem para marfim ao ocupar o centro da tela
  const invertSections = document.querySelectorAll('[data-invert]');
  if (hasIO && !reduceMotion) {
    const invertIO = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-lit');
          invertIO.unobserve(entry.target);
        }
      });
    }, { rootMargin: '-38% 0px -38% 0px' });
    invertSections.forEach((s) => invertIO.observe(s));
  } else {
    invertSections.forEach((s) => s.classList.add('is-lit'));
  }

  // 3. Spotlight do cursor
  const spotlight = document.querySelector('.cursor-spotlight');
  if (spotlight && !reduceMotion && window.matchMedia('(pointer: fine)').matches) {
    let mouseX = window.innerWidth / 2;
    let mouseY = window.innerHeight / 2;
    let currentX = mouseX;
    let currentY = mouseY;
    window.addEventListener('pointermove', (e) => { mouseX = e.clientX; mouseY = e.clientY; });
    const animateSpotlight = () => {
      currentX += (mouseX - currentX) * 0.12;
      currentY += (mouseY - currentY) * 0.12;
      spotlight.style.transform = `translate(${currentX}px, ${currentY}px) translate(-50%, -50%)`;
      requestAnimationFrame(animateSpotlight);
    };
    animateSpotlight();
  }

  // 4. Navbar + paralaxe do interlúdio (um único listener de scroll)
  const navbar = document.querySelector('.navbar');
  const interlude = document.querySelector('.interlude-frame');
  let ticking = false;
  const onScroll = () => {
    navbar?.classList.toggle('scrolled', window.scrollY > 40);
    if (interlude && !reduceMotion) {
      const rect = interlude.getBoundingClientRect();
      const vh = window.innerHeight;
      if (rect.bottom > 0 && rect.top < vh) {
        // -1 (entrando por baixo) → 1 (saindo por cima)
        const progress = (vh / 2 - (rect.top + rect.height / 2)) / (vh / 2 + rect.height / 2);
        interlude.style.setProperty('--parallax', `${(progress * 7).toFixed(2)}%`);
      }
    }
    ticking = false;
  };
  window.addEventListener('scroll', () => {
    if (!ticking) { ticking = true; requestAnimationFrame(onScroll); }
  }, { passive: true });
  onScroll();

  // 5. Brilho que segue o cursor nos cartões
  document.querySelectorAll('.bento-card').forEach((card) => {
    card.addEventListener('pointermove', (e) => {
      const rect = card.getBoundingClientRect();
      card.style.setProperty('--mouse-x', `${e.clientX - rect.left}px`);
      card.style.setProperty('--mouse-y', `${e.clientY - rect.top}px`);
    });
  });

  // 6. Envelope: abre pelo lacre, pelo foco num campo ou ao entrar em cena
  const stage = document.getElementById('envelopeStage');
  const seal = document.getElementById('envelopeSeal');
  const openEnvelope = () => {
    if (!stage || stage.classList.contains('is-open')) return;
    stage.classList.add('is-open');
    seal?.setAttribute('tabindex', '-1');
    seal?.setAttribute('aria-hidden', 'true');
  };

  seal?.addEventListener('click', () => {
    openEnvelope();
    setTimeout(() => document.getElementById('letterName')?.focus({ preventScroll: true }), reduceMotion ? 0 : 1400);
  });
  document.querySelectorAll('.letter-input, .letter-textarea').forEach((el) => el.addEventListener('focus', openEnvelope));
  stage?.querySelector('.envelope')?.addEventListener('click', openEnvelope);

  if (stage && hasIO && !reduceMotion) {
    const envelopeIO = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          setTimeout(openEnvelope, 500);
          envelopeIO.unobserve(entry.target);
        }
      });
    }, { threshold: 0.45 });
    envelopeIO.observe(stage.querySelector('.envelope'));
  } else {
    openEnvelope();
  }

  // 7. Data por extenso e assinatura que acompanha o nome
  const dateEl = document.getElementById('letterDate');
  if (dateEl) {
    dateEl.textContent = new Date().toLocaleDateString('pt-BR', { day: 'numeric', month: 'long', year: 'numeric' });
  }

  const nameInput = document.getElementById('letterName');
  const signature = document.getElementById('letterSignature');
  const syncSignature = () => {
    if (!signature) return;
    const value = nameInput?.value.trim();
    signature.textContent = value || 'Sua assinatura';
    signature.classList.toggle('is-empty', !value);
  };
  nameInput?.addEventListener('input', syncSignature);
  syncSignature();

  // 8. Origem do acesso (ex: ?ref=cartao via QR Code do cartão físico) e envio via WhatsApp
  const params = new URLSearchParams(window.location.search);
  const refParam = (params.get('ref') || params.get('utm_source') || '').toLowerCase();
  const veioDoCartao = refParam.includes('cartao') || refParam.includes('card');

  if (veioDoCartao) {
    const msgDireta = encodeURIComponent(
      'Olá, equipe VÉRTICE Private Concierge. Acessei pelo QR Code do cartão e gostaria de conversar.'
    );
    document.querySelectorAll('a[href^="https://wa.me/5548984777489"]').forEach((link) => {
      link.setAttribute('href', `https://wa.me/5548984777489?text=${msgDireta}`);
    });
  }

  const letterForm = document.getElementById('letterForm');
  const demandInput = document.getElementById('letterDemand');
  const errorEl = document.getElementById('letterError');

  const setError = (show) => {
    if (!errorEl || !demandInput) return;
    errorEl.hidden = !show;
    demandInput.setAttribute('aria-invalid', show ? 'true' : 'false');
  };
  demandInput?.addEventListener('input', () => { if (demandInput.value.trim()) setError(false); });

  letterForm?.addEventListener('submit', (e) => {
    e.preventDefault();
    const name = nameInput?.value.trim() || 'Não informado';
    const location = document.getElementById('letterLocation')?.value.trim() || 'Não informado';
    const demand = demandInput?.value.trim();

    if (!demand) {
      setError(true);
      demandInput?.focus();
      return;
    }
    setError(false);

    const lines = [
      'Olá, equipe VÉRTICE Private Concierge.',
      ...(veioDoCartao ? ['[Origem: QR Code do Cartão VÉRTICE]'] : []),
      '',
      `Meu nome é: ${name}`,
      `Localização: ${location}`,
      '',
      'Gostaria de solicitar:',
      `"${demand}"`,
      '',
      'Gostaria de agendar uma conversa confidencial para entender como podemos conduzir essa demanda.'
    ];

    window.open(`https://wa.me/5548984777489?text=${encodeURIComponent(lines.join('\n'))}`, '_blank', 'noopener,noreferrer');
  });
});
