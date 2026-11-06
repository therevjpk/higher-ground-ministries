/* Renders books and songs from data/catalog.json into any element with
   data-books="full|short|all|teaser" or data-songs="featured|list|teaser". */
(function () {
  var esc = function (s) {
    return String(s || '').replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  };

  function cover(item, square, label, mini) {
    var cls = 'cover' + (square ? ' square' : '');
    if (!item.cover && mini) {
      var initial = item.title.replace(/^(The|A|An|I’ve|I)\s+/i, '').charAt(0);
      return '<div class="' + cls + '" aria-hidden="true"><div class="titlecard mono"><b>' + esc(initial) + '</b></div></div>';
    }
    if (item.cover) {
      return '<div class="' + cls + '"><img src="' + esc(item.cover) + '" alt="Cover of ' + esc(item.title) +
        '" loading="lazy" decoding="async" width="480" height="' + (square ? 480 : 720) + '"></div>';
    }
    return '<div class="' + cls + '" role="img" aria-label="' + esc(item.title) + '"><div class="titlecard">' +
      '<small>' + esc(label) + '</small><b>' + esc(item.title) + '</b><small>John P. Kennon</small></div></div>';
  }

  function book(b) {
    var actions = '';
    if (b.sample) actions += '<a href="' + esc(b.sample) + '" target="_blank" rel="noopener">Read a sample</a>';
    if (b.purchase_url) actions += '<a href="' + esc(b.purchase_url) + '" target="_blank" rel="noopener">Buy</a>';
    return '<article class="book">' + cover(b, false, b.kind) +
      '<div><p class="kind">' + esc(b.kind) + '</p><h3>' + esc(b.title) + '</h3>' +
      (b.subtitle ? '<p class="subtitle">' + esc(b.subtitle) + '</p>' : '') + '</div>' +
      (b.description ? '<p class="desc">' + esc(b.description) + '</p>' : '') +
      (actions ? '<div class="actions">' + actions + '</div>' : '') + '</article>';
  }

  function player(s) {
    if (!s.preview) return '';
    return '<audio controls preload="none" src="' + esc(s.preview) + '" aria-label="Preview of ' + esc(s.title) + '"></audio>' +
      '<p class="preview-note">60-second preview</p>';
  }

  function song(s) {
    return '<li class="song">' + cover(s, true, 'Song', true) +
      '<div><h3>' + esc(s.title) + '</h3>' +
      (s.credit ? '<p class="credit">' + esc(s.credit) + '</p>' : '') +
      (s.description ? '<p class="desc">' + esc(s.description) + '</p>' : '') + '</div>' +
      '<div class="player">' + player(s) + '</div></li>';
  }

  function featured(s) {
    return '<div class="featured">' + cover(s, true, 'Featured song') +
      '<div><p class="label">Featured song</p><h3>' + esc(s.title) + '</h3>' +
      (s.description ? '<p class="desc">' + esc(s.description) + '</p>' : '') + player(s) + '</div></div>';
  }

  function render(data) {
    document.querySelectorAll('[data-books]').forEach(function (el) {
      var mode = el.getAttribute('data-books');
      var list = data.books.filter(function (b) {
        return mode === 'all' || mode === 'teaser' || b.group === mode;
      });
      if (mode === 'teaser') list = list.filter(function (b) { return b.cover; }).slice(0, 6);
      el.innerHTML = list.map(book).join('');
    });
    document.querySelectorAll('[data-songs]').forEach(function (el) {
      var mode = el.getAttribute('data-songs');
      if (mode === 'featured') {
        var f = data.songs.filter(function (s) { return s.featured; })[0];
        el.innerHTML = f ? featured(f) : '';
        return;
      }
      var list = data.songs.filter(function (s) { return !s.featured; });
      if (mode === 'teaser') list = list.slice(0, 5);
      el.innerHTML = list.map(song).join('');
    });
    // Only one preview plays at a time.
    document.addEventListener('play', function (e) {
      document.querySelectorAll('audio').forEach(function (a) { if (a !== e.target) a.pause(); });
    }, true);
  }

  if (document.querySelector('[data-books],[data-songs]')) {
    fetch('data/catalog.json').then(function (r) { return r.json(); }).then(render).catch(function () {
      document.querySelectorAll('[data-books],[data-songs]').forEach(function (el) {
        el.innerHTML = '<p>The catalog could not load. Please refresh the page.</p>';
      });
    });
  }

  // Contact form: FormSubmit returns here with ?sent=1
  if (/[?&]sent=1/.test(location.search)) {
    var t = document.getElementById('thanks'), f = document.getElementById('contact-form');
    if (t && f) { t.hidden = false; f.hidden = true; }
  }
})();
