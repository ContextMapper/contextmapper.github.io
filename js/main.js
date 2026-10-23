// Context Mapper website: theme toggle, mobile menu, docs menu and search (no dependencies)
(function () {
  'use strict';

  var root = document.documentElement;

  // theme toggle: stores the visitor's choice in localStorage (no cookies); without a choice the OS setting applies
  var darkQuery = window.matchMedia('(prefers-color-scheme: dark)');

  function currentTheme() {
    return root.getAttribute('data-theme') || (darkQuery.matches ? 'dark' : 'light');
  }

  var themeToggle = document.getElementById('theme-toggle');
  if (themeToggle) {
    themeToggle.addEventListener('click', function () {
      var theme = currentTheme() === 'dark' ? 'light' : 'dark';
      root.setAttribute('data-theme', theme);
      try {
        localStorage.setItem('theme', theme);
      } catch (e) {}
    });
  }

  // mobile menu
  var menuToggle = document.getElementById('menu-toggle');
  var siteNav = document.getElementById('site-nav');
  if (menuToggle && siteNav) {
    menuToggle.addEventListener('click', function () {
      var open = siteNav.classList.toggle('open');
      menuToggle.setAttribute('aria-expanded', String(open));
    });
  }

  // docs menu: collapsed on small screens
  var sidebar = document.getElementById('docs-sidebar');
  var sidebarToggle = sidebar && sidebar.querySelector('.sidebar-toggle');
  if (sidebarToggle) {
    var setCollapsed = function (collapsed) {
      sidebar.classList.toggle('collapsed', collapsed);
      sidebarToggle.setAttribute('aria-expanded', String(!collapsed));
    };
    setCollapsed(window.matchMedia('(max-width: 860px)').matches);
    sidebarToggle.addEventListener('click', function () {
      setCollapsed(!sidebar.classList.contains('collapsed'));
    });
  }

  // search over the page titles (search.json)
  var input = document.getElementById('search-input');
  var results = document.getElementById('search-results');
  if (!input || !results) return;

  var pages = null;
  var matches = [];
  var active = -1;

  function loadIndex() {
    if (pages) return Promise.resolve(pages);
    return fetch(input.getAttribute('data-index'))
      .then(function (response) { return response.json(); })
      .then(function (data) { pages = data; return pages; });
  }

  function close() {
    results.hidden = true;
    input.setAttribute('aria-expanded', 'false');
    input.removeAttribute('aria-activedescendant');
    active = -1;
  }

  function render() {
    results.textContent = '';
    if (matches.length === 0) {
      var empty = document.createElement('li');
      empty.className = 'search-empty';
      empty.textContent = 'No matching pages';
      results.appendChild(empty);
    }
    matches.forEach(function (page, index) {
      var li = document.createElement('li');
      li.setAttribute('role', 'option');
      li.id = 'search-result-' + index;
      var link = document.createElement('a');
      link.href = page.url;
      link.textContent = page.title;
      if (index === active) link.className = 'active';
      var section = document.createElement('span');
      section.className = 'search-section';
      section.textContent = page.section;
      link.appendChild(section);
      li.appendChild(link);
      results.appendChild(li);
    });
    results.hidden = false;
    input.setAttribute('aria-expanded', 'true');
    if (active >= 0) input.setAttribute('aria-activedescendant', 'search-result-' + active);
  }

  function search() {
    var terms = input.value.toLowerCase().split(/\s+/).filter(Boolean);
    if (terms.length === 0) {
      close();
      return;
    }
    loadIndex().then(function (data) {
      matches = data.filter(function (page) {
        var text = (page.title + ' ' + page.section).toLowerCase();
        return terms.every(function (term) { return text.indexOf(term) !== -1; });
      }).slice(0, 12);
      active = matches.length ? 0 : -1;
      render();
    });
  }

  input.addEventListener('input', search);
  input.addEventListener('focus', function () { loadIndex(); });

  input.addEventListener('keydown', function (event) {
    if (event.key === 'ArrowDown' || event.key === 'ArrowUp') {
      if (!matches.length) return;
      event.preventDefault();
      var step = event.key === 'ArrowDown' ? 1 : -1;
      active = (active + step + matches.length) % matches.length;
      render();
    } else if (event.key === 'Enter') {
      if (active >= 0 && matches[active]) {
        event.preventDefault();
        window.location.href = matches[active].url;
      }
    } else if (event.key === 'Escape') {
      close();
      input.blur();
    }
  });

  document.addEventListener('click', function (event) {
    if (!results.contains(event.target) && event.target !== input) close();
  });

  // "/" focuses the search field
  document.addEventListener('keydown', function (event) {
    var tag = (event.target.tagName || '').toLowerCase();
    if (event.key === '/' && tag !== 'input' && tag !== 'textarea' && !event.target.isContentEditable) {
      event.preventDefault();
      if (menuToggle && siteNav && getComputedStyle(menuToggle).display !== 'none' && !siteNav.classList.contains('open')) {
        menuToggle.click();
      }
      input.focus();
    }
  });
})();
