/**
 * ONCARA — Press-On Nails de Lujo & Almas Salvajes
 * Main JavaScript Interactions
 */

document.addEventListener('DOMContentLoaded', () => {
  initHeader();
  initMobileMenu();
  initCartDrawer();
  initSearchModal();
  initCollectionFilter();
  initPersonalizadosForm();
  initMedidasSelector();
  initQuiz();
});

// Quiz "Descubrí tu set salvaje" (index). Set data is read from the collection cards on the page.
function initQuiz() {
  const stage = document.querySelector('.quiz-stage');
  if (!stage) return;

  const titles = { salvaje: 'SALVAJE', oraculo: 'ORÁCULO', ocaso: 'OCASO', hechizo: 'HECHIZO' };
  const questions = [
    {
      q: '¿Cuál es tu vibe?',
      options: [
        ['Audaz y magnética', 'salvaje'],
        ['Mística y soñadora', 'oraculo'],
        ['Intensa y sofisticada', 'ocaso'],
        ['Romántica y delicada', 'hechizo'],
      ],
    },
    {
      q: '¿Qué colores predominan en tu placard?',
      options: [
        ['Animal print y tonos tierra', 'salvaje'],
        ['Negro, verde oliva y dorado', 'oraculo'],
        ['Bordó, vino y tonos profundos', 'ocaso'],
        ['Nude, blanco y perla', 'hechizo'],
      ],
    },
    {
      q: '¿Para qué ocasión las querés?',
      options: [
        ['Una salida para robar miradas', 'salvaje'],
        ['Un ritual o una fecha con significado', 'oraculo'],
        ['Una cena o evento elegante de noche', 'ocaso'],
        ['Una boda, un cumple o un evento de día', 'hechizo'],
      ],
    },
  ];

  let answers = [];

  function setData(key) {
    const card = Array.from(document.querySelectorAll('.collection-card'))
      .find(c => c.querySelector('.card-title')?.textContent.trim() === titles[key]);
    if (!card) return null;
    return {
      name: 'Set ' + titles[key].charAt(0) + titles[key].slice(1).toLowerCase(),
      img: card.querySelector('img').getAttribute('src'),
      desc: card.querySelector('.card-desc').textContent.trim(),
      price: card.querySelector('.card-price').textContent.trim(),
    };
  }

  function focusHeading() {
    const heading = stage.querySelector('[tabindex="-1"]');
    if (heading) heading.focus({ preventScroll: true });
  }

  function renderQuestion(i) {
    const { q, options } = questions[i];
    stage.innerHTML = `
      <p class="quiz-progress">PREGUNTA ${i + 1} DE ${questions.length}</p>
      <h3 class="quiz-question" tabindex="-1">${q}</h3>
      <div class="quiz-options">
        ${options.map(([label, key]) => `<button type="button" class="quiz-option" data-key="${key}">${label}</button>`).join('')}
      </div>`;
    stage.querySelectorAll('.quiz-option').forEach(btn => btn.addEventListener('click', () => {
      answers.push(btn.dataset.key);
      if (answers.length < questions.length) renderQuestion(answers.length);
      else renderResult();
      focusHeading();
    }));
  }

  function renderResult() {
    const scores = {};
    answers.forEach(k => { scores[k] = (scores[k] || 0) + 1; });
    const best = Math.max(...Object.values(scores));
    // On a tie, the occasion (last answer) decides
    const key = scores[answers[answers.length - 1]] === best
      ? answers[answers.length - 1]
      : Object.keys(scores).find(k => scores[k] === best);
    const set = setData(key);
    if (!set) return;

    stage.innerHTML = `
      <div class="quiz-result">
        <img src="${set.img}" alt="${set.name}" width="1024" height="1024">
        <div class="quiz-result-info">
          <p class="quiz-progress">TU SET ES</p>
          <h3 class="quiz-question" tabindex="-1">${set.name.toUpperCase()}</h3>
          <p class="quiz-result-desc">${set.desc}</p>
          <p class="quiz-result-price">${set.price}</p>
          <div class="quiz-result-actions">
            <button type="button" class="btn btn-gold quiz-add">AGREGAR A MI BOLSA</button>
            <button type="button" class="btn btn-outline-gold quiz-restart">VOLVER A EMPEZAR</button>
          </div>
        </div>
      </div>`;
    stage.querySelector('.quiz-add').addEventListener('click', () => addToCart(set.name, set.price, set.img));
    stage.querySelector('.quiz-restart').addEventListener('click', () => {
      answers = [];
      renderQuestion(0);
      focusHeading();
    });
  }

  renderQuestion(0);
}

// Toast notification
function showToast(message) {
  let toast = document.querySelector('.toast-notice');
  if (!toast) {
    toast = document.createElement('div');
    toast.className = 'toast-notice';
    document.body.appendChild(toast);
  }
  toast.textContent = message;
  toast.classList.add('show');
  setTimeout(() => {
    toast.classList.remove('show');
  }, 3200);
}

// Sticky Header
function initHeader() {
  const header = document.querySelector('.main-header');
  if (!header) return;

  const backToTop = document.createElement('button');
  backToTop.className = 'back-to-top';
  backToTop.setAttribute('aria-label', 'Volver arriba');
  backToTop.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M12 19V5M5 12l7-7 7 7"/></svg>';
  backToTop.addEventListener('click', () => window.scrollTo({ top: 0 }));
  document.body.appendChild(backToTop);

  // On the home page the logo scrolls back up instead of reloading
  const logo = document.querySelector('.brand-center-badge');
  const onHome = /(\/|index\.html)$/.test(location.pathname);
  if (logo && onHome) {
    logo.addEventListener('click', (e) => {
      e.preventDefault();
      window.scrollTo({ top: 0 });
    });
  }

  window.addEventListener('scroll', () => {
    header.classList.toggle('scrolled', window.scrollY > 40);
    backToTop.classList.toggle('visible', window.scrollY > 600);
  });
}

// Mobile Menu Drawer
function initMobileMenu() {
  const menuBtn = document.querySelector('.mobile-menu-btn');
  const closeBtn = document.querySelector('.mobile-nav-close');
  const mobileNav = document.querySelector('.mobile-nav');
  const backdrop = document.querySelector('.mobile-nav-backdrop');

  if (!menuBtn || !mobileNav) return;

  function openMenu() {
    mobileNav.classList.add('open');
    if (backdrop) backdrop.classList.add('open');
    document.body.style.overflow = 'hidden';
  }

  function closeMenu() {
    mobileNav.classList.remove('open');
    if (backdrop) backdrop.classList.remove('open');
    document.body.style.overflow = '';
  }

  menuBtn.addEventListener('click', openMenu);
  if (closeBtn) closeBtn.addEventListener('click', closeMenu);
  if (backdrop) backdrop.addEventListener('click', closeMenu);
}

// Cart / Order Drawer
let cart = JSON.parse(localStorage.getItem('oncara_cart') || '[]');

function updateCartUI() {
  const badgeCounts = document.querySelectorAll('.badge-count');
  const itemsContainer = document.querySelector('.cart-items-body');
  const subtotalElem = document.querySelector('.cart-subtotal-val');

  badgeCounts.forEach(el => {
    el.textContent = cart.length;
    el.style.display = cart.length > 0 ? 'flex' : 'none';
  });

  if (!itemsContainer) return;

  if (cart.length === 0) {
    itemsContainer.innerHTML = '<div class="cart-empty-message">Tu selección de joyas está vacía.<br>Elegí tus sets favoritos de la colección.</div>';
    if (subtotalElem) subtotalElem.textContent = '$0';
    return;
  }

  let total = 0;
  itemsContainer.innerHTML = cart.map((item, index) => {
    const numPrice = parseInt(item.price.replace(/[^0-9]/g, '')) || 0;
    total += numPrice;
    return `
      <div class="cart-item">
        <img src="${item.img}" alt="${item.name}" class="cart-item-img">
        <div class="cart-item-details">
          <div class="cart-item-title">${item.name}</div>
          <div class="cart-item-price">${item.price}</div>
        </div>
        <button class="icon-btn remove-cart-btn" onclick="removeFromCart(${index})" style="color:#C2A06B; font-size:1.2rem;">&times;</button>
      </div>
    `;
  }).join('');

  if (subtotalElem) {
    subtotalElem.textContent = `$${total.toLocaleString('es-AR')}`;
  }
}

window.addToCart = function(name, price, img) {
  cart.push({ name, price, img });
  localStorage.setItem('oncara_cart', JSON.stringify(cart));
  updateCartUI();
  openCart();
};

window.removeFromCart = function(index) {
  cart.splice(index, 1);
  localStorage.setItem('oncara_cart', JSON.stringify(cart));
  updateCartUI();
};

function openCart() {
  const drawer = document.querySelector('.cart-drawer');
  const backdrop = document.querySelector('.cart-drawer-backdrop');
  if (drawer) drawer.classList.add('open');
  if (backdrop) backdrop.classList.add('open');
  document.body.style.overflow = 'hidden';
}

function closeCart() {
  const drawer = document.querySelector('.cart-drawer');
  const backdrop = document.querySelector('.cart-drawer-backdrop');
  if (drawer) drawer.classList.remove('open');
  if (backdrop) backdrop.classList.remove('open');
  document.body.style.overflow = '';
}

function initCartDrawer() {
  const cartBtns = document.querySelectorAll('.cart-toggle-btn');
  const closeBtn = document.querySelector('.cart-close-btn');
  const backdrop = document.querySelector('.cart-drawer-backdrop');
  const checkoutBtn = document.querySelector('.cart-checkout-btn');

  cartBtns.forEach(btn => btn.addEventListener('click', openCart));
  if (closeBtn) closeBtn.addEventListener('click', closeCart);
  if (backdrop) backdrop.addEventListener('click', closeCart);

  if (checkoutBtn) {
    checkoutBtn.addEventListener('click', () => {
      if (cart.length === 0) {
        showToast('Tu carrito está vacío');
        return;
      }
      let itemsList = cart.map(i => `• ${i.name} (${i.price})`).join('%0A');
      let msg = `Hola! Quiero encargar los siguientes sets Oncara:%0A%0A${itemsList}%0A%0APor favor, confirmame disponibilidad y tiempos de confección. Gracias!`;
      window.open(`https://wa.me/5491165464483?text=${msg}`, '_blank');
    });
  }

  updateCartUI();
}

// Search Modal
function initSearchModal() {
  const searchBtns = document.querySelectorAll('.search-toggle-btn');
  const searchModal = document.querySelector('.search-modal');
  const modalBackdrop = document.querySelector('.modal-backdrop');
  const searchClose = document.querySelector('.search-close-btn');
  const searchInput = document.querySelector('#searchInput');
  const searchResults = document.querySelector('.search-results-list');

  if (!searchModal) return;

  const catalog = [
    { title: 'Set Salvaje', url: 'tienda.html#salvaje', desc: 'Diseño leopardo icónico, audaz y sensual' },
    { title: 'Set Oráculo', url: 'tienda.html#oraculo', desc: 'Líneas astrales y misticismo en oro sobre obsidiana' },
    { title: 'Set Ocaso', url: 'tienda.html#ocaso', desc: 'Mármol bordó y destellos de oro líquido' },
    { title: 'Set Hechizo', url: 'tienda.html#hechizo', desc: 'Aura celestial nude con microperlas doradas' },
    { title: 'Pedidos Personalizados', url: 'personalizados.html', desc: 'Creá tu diseño exclusivo a tu medida' },
    { title: 'Guía de Cuidados', url: 'cuidados.html', desc: 'Cómo colocar, proteger y retirar tus Oncara' },
    { title: 'Sobre Oncara', url: 'sobre-oncara.html', desc: 'Nuestra historia, actitud y manifiesto' }
  ];

  function openSearch() {
    searchModal.classList.add('open');
    if (modalBackdrop) modalBackdrop.classList.add('open');
    if (searchInput) {
      searchInput.focus();
      renderResults(catalog);
    }
  }

  function closeSearch() {
    searchModal.classList.remove('open');
    if (modalBackdrop) modalBackdrop.classList.remove('open');
    if (searchInput) searchInput.value = '';
  }

  function renderResults(items) {
    if (!searchResults) return;
    if (items.length === 0) {
      searchResults.innerHTML = '<li style="padding:15px; color:#A6A092; text-align:center;">No encontramos resultados para tu búsqueda.</li>';
      return;
    }
    searchResults.innerHTML = items.map(i => `
      <li style="border-bottom:1px solid rgba(194, 160, 107, 0.15); padding:10px 0;">
        <a href="${i.url}" style="display:block;">
          <strong style="color:#C2A06B; font-family:'Cinzel', serif; font-size:0.95rem;">${i.title}</strong>
          <p style="color:#CFC9BC; font-size:0.85rem; margin-top:2px;">${i.desc}</p>
        </a>
      </li>
    `).join('');
  }

  searchBtns.forEach(btn => btn.addEventListener('click', openSearch));
  if (searchClose) searchClose.addEventListener('click', closeSearch);
  if (modalBackdrop) modalBackdrop.addEventListener('click', closeSearch);

  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      const q = e.target.value.toLowerCase().trim();
      if (!q) {
        renderResults(catalog);
        return;
      }
      const filtered = catalog.filter(i => 
        i.title.toLowerCase().includes(q) || i.desc.toLowerCase().includes(q)
      );
      renderResults(filtered);
    });
  }
}

// Tienda Catalog Filter
function initCollectionFilter() {
  const filterBtns = document.querySelectorAll('.filter-btn');
  const items = document.querySelectorAll('.tienda-item-card');

  if (!filterBtns.length || !items.length) return;

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const filterVal = btn.getAttribute('data-filter');

      items.forEach(item => {
        const itemCat = item.getAttribute('data-category');
        if (filterVal === 'all' || itemCat === filterVal) {
          item.style.display = 'flex';
          item.style.opacity = '1';
        } else {
          item.style.display = 'none';
          item.style.opacity = '0';
        }
      });
    });
  });
}

// Personalizados: Interactive Sizer & Length Selector
function initMedidasSelector() {
  // Table row select
  const tableRows = document.querySelectorAll('.talles-table tbody tr');
  const talleSelect = document.querySelector('#talleSelect');

  tableRows.forEach(row => {
    row.addEventListener('click', () => {
      tableRows.forEach(r => r.classList.remove('selected'));
      row.classList.add('selected');
      const talleVal = row.getAttribute('data-talle');
      if (talleSelect && talleVal) {
        talleSelect.value = talleVal;
      }
    });
  });

  if (talleSelect) {
    talleSelect.addEventListener('change', () => {
      const val = talleSelect.value;
      tableRows.forEach(row => {
        if (row.getAttribute('data-talle') === val) {
          row.classList.add('selected');
        } else {
          row.classList.remove('selected');
        }
      });
    });
  }

  // Largos visual selector
  const largoItems = document.querySelectorAll('.largo-item');
  const largoSelect = document.querySelector('#largoSelect');

  largoItems.forEach(item => {
    item.addEventListener('click', () => {
      largoItems.forEach(l => l.classList.remove('active'));
      item.classList.add('active');
      const val = item.getAttribute('data-largo');
      if (largoSelect && val) {
        largoSelect.value = val;
      }
    });
  });

  if (largoSelect) {
    largoSelect.addEventListener('change', () => {
      const val = largoSelect.value;
      largoItems.forEach(item => {
        if (item.getAttribute('data-largo') === val) {
          item.classList.add('active');
        } else {
          item.classList.remove('active');
        }
      });
    });
  }
}

// Personalizados Form & Image Dropzone
function initPersonalizadosForm() {
  const form = document.querySelector('#customOrderForm');
  const radioCustomYes = document.querySelector('#medidasYes');
  const radioCustomNo = document.querySelector('#medidasNo');
  const customFields = document.querySelector('.custom-mm-fields');
  const dropzone = document.querySelector('#dropzone');
  const fileInput = document.querySelector('#fileInput');
  const previewsContainer = document.querySelector('.dropzone-previews');

  // Toggle custom mm inputs
  if (radioCustomYes && radioCustomNo && customFields) {
    radioCustomYes.addEventListener('change', () => {
      if (radioCustomYes.checked) customFields.classList.add('show');
    });
    radioCustomNo.addEventListener('change', () => {
      if (radioCustomNo.checked) customFields.classList.remove('show');
    });
  }

  // File Upload Handlers
  let uploadedFiles = [];

  if (dropzone && fileInput) {
    dropzone.addEventListener('click', () => fileInput.click());

    dropzone.addEventListener('dragover', (e) => {
      e.preventDefault();
      dropzone.classList.add('dragover');
    });

    dropzone.addEventListener('dragleave', () => {
      dropzone.classList.remove('dragover');
    });

    dropzone.addEventListener('drop', (e) => {
      e.preventDefault();
      dropzone.classList.remove('dragover');
      handleFiles(e.dataTransfer.files);
    });

    fileInput.addEventListener('change', (e) => {
      handleFiles(e.target.files);
    });
  }

  function handleFiles(files) {
    if (!files) return;
    Array.from(files).forEach(file => {
      if (!file.type.match('image.*')) {
        showToast('Solo se permiten imágenes (JPG, PNG, WEBP)');
        return;
      }
      if (uploadedFiles.length >= 10) {
        showToast('Máximo 10 imágenes');
        return;
      }
      uploadedFiles.push(file);
      renderPreviews();
    });
  }

  function renderPreviews() {
    if (!previewsContainer) return;
    previewsContainer.innerHTML = '';
    uploadedFiles.forEach((file, idx) => {
      const reader = new FileReader();
      reader.onload = (e) => {
        const thumb = document.createElement('div');
        thumb.className = 'preview-thumb';
        thumb.innerHTML = `
          <img src="${e.target.result}" alt="Ref ${idx+1}">
          <button type="button" class="preview-remove" data-idx="${idx}">&times;</button>
        `;
        thumb.querySelector('.preview-remove').addEventListener('click', (ev) => {
          ev.stopPropagation();
          uploadedFiles.splice(idx, 1);
          renderPreviews();
        });
        previewsContainer.appendChild(thumb);
      };
      reader.readAsDataURL(file);
    });
  }

  // Form Submission via WhatsApp
  if (form) {
    form.addEventListener('submit', (e) => {
      e.preventDefault();

      const nombre = document.querySelector('#nombreInput')?.value || '';
      const contacto = document.querySelector('#contactoInput')?.value || '';
      const talle = document.querySelector('#talleSelect')?.value || 'No especificado';
      const largo = document.querySelector('#largoSelect')?.value || 'No especificado';
      const esPersonalizado = radioCustomYes?.checked;
      const idea = document.querySelector('#ideaTextarea')?.value || '';

      let mmText = '';
      if (esPersonalizado) {
        const pulgar = document.querySelector('#mmPulgar')?.value || '-';
        const indice = document.querySelector('#mmIndice')?.value || '-';
        const medio = document.querySelector('#mmMedio')?.value || '-';
        const anular = document.querySelector('#mmAnular')?.value || '-';
        const menique = document.querySelector('#mmMenique')?.value || '-';
        mmText = `%0A• Medidas exactas (mm): P:${pulgar} | I:${indice} | M:${medio} | A:${anular} | Me:${menique}`;
      }

      const filesCount = uploadedFiles.length > 0 ? `%0A• Adjunto ${uploadedFiles.length} foto(s) de referencia por este chat.` : '';

      const waMsg = `¡Hola Oncara! Quiero consultar por un pedido PERSONALIZADO:%0A%0A` +
        `• Nombre: ${encodeURIComponent(nombre)}%0A` +
        `• Contacto/IG: ${encodeURIComponent(contacto)}%0A` +
        `• Talle: ${encodeURIComponent(talle)}%0A` +
        `• Largo deseado: ${encodeURIComponent(largo)}` +
        mmText + `%0A` +
        `• Mi idea: ${encodeURIComponent(idea)}` +
        filesCount + `%0A%0A` +
        `Quedo a la espera de confirmación y presupuesto. ¡Muchas gracias!`;

      showToast('✦ Redirigiendo a WhatsApp...');
      setTimeout(() => {
        window.open(`https://wa.me/5491165464483?text=${waMsg}`, '_blank');
      }, 700);
    });
  }
}
