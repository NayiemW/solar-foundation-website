/* Solar Foundation static site — interactivity + live chain data
   Self-contained, no dependencies. */
(function () {
  "use strict";

  /* ---------- hover (replaces dc-runtime style-hover) ---------- */
  document.querySelectorAll("[data-h]").forEach(function (el) {
    var hov = el.getAttribute("data-h");
    var base = el.getAttribute("style") || "";
    el.addEventListener("mouseenter", function () {
      el.setAttribute("style", base + ";" + hov);
    });
    el.addEventListener("mouseleave", function () {
      el.setAttribute("style", base);
    });
  });

  /* ---------- accordion (homepage history) ---------- */
  document.querySelectorAll("[data-acc]").forEach(function (head) {
    head.addEventListener("click", function () {
      var panel = head.nextElementSibling;
      if (!panel) return;
      var icon = head.querySelector(":scope > span");
      var open = panel.style.display !== "none";
      panel.style.display = open ? "none" : "block";
      if (icon) icon.style.transform = open ? "rotate(0deg)" : "rotate(45deg)";
    });
  });

  /* ---------- unified navbar: dropdowns + mobile toggle ---------- */
  document.querySelectorAll(".snav-ddbtn").forEach(function (btn) {
    btn.addEventListener("click", function (e) {
      e.stopPropagation();
      var dd = btn.parentElement;
      var isOpen = dd.classList.contains("open");
      document.querySelectorAll(".snav-dd.open").forEach(function (o) { o.classList.remove("open"); });
      if (!isOpen) dd.classList.add("open");
    });
  });
  document.addEventListener("click", function () {
    document.querySelectorAll(".snav-dd.open").forEach(function (o) { o.classList.remove("open"); });
  });
  var navTg = document.querySelector(".snav-tg");
  if (navTg) navTg.addEventListener("click", function (e) {
    e.stopPropagation();
    var h = document.querySelector(".snav");
    if (h) h.classList.toggle("open");
  });

  /* ---------- FAQ accordion: only one <details> open at a time ---------- */
  var allDetails = document.querySelectorAll("details");
  if (allDetails.length > 1) {
    allDetails.forEach(function (d) {
      d.addEventListener("toggle", function () {
        if (d.open) {
          allDetails.forEach(function (o) {
            if (o !== d) o.open = false;
          });
        }
      });
    });
  }

  /* ---------- archive filter (search + tag pills) ---------- */
  var search = document.getElementById("arcSearch");
  var pills = document.querySelectorAll(".pill");
  if (search || pills.length) {
    var curTag = "All";
    function applyFilter() {
      var q = (search && search.value || "").toLowerCase().trim();
      var anyVisible = false;
      document.querySelectorAll(".arc-group").forEach(function (group) {
        var shown = 0;
        group.querySelectorAll(".arc-card").forEach(function (card) {
          var okTag = curTag === "All" || card.getAttribute("data-tag") === curTag;
          var okQ = !q || (card.getAttribute("data-text") || "").indexOf(q) !== -1;
          var vis = okTag && okQ;
          card.style.display = vis ? "block" : "none";
          if (vis) shown++;
        });
        var count = group.querySelector(".arc-count");
        if (count) count.textContent = shown + (shown === 1 ? " post" : " posts");
        group.style.display = shown ? "block" : "none";
        if (shown) anyVisible = true;
      });
      var empty = document.getElementById("arcEmpty");
      if (empty) empty.style.display = anyVisible ? "none" : "block";
    }
    pills.forEach(function (pill) {
      pill.addEventListener("click", function () {
        curTag = pill.getAttribute("data-tag");
        pills.forEach(function (p) {
          var active = p === pill;
          p.style.border = "1px solid " + (active ? "#3a3942" : "#1c1b21");
          p.style.color = active ? "#f4f3f6" : "#8b8a93";
          p.style.background = active ? "rgba(255,255,255,.05)" : "transparent";
        });
        applyFilter();
      });
    });
    if (search) search.addEventListener("input", applyFilter);
  }

  /* ---------- evidence page: expand a row to show the screenshot inline ---------- */
  document.querySelectorAll(".ev-shot").forEach(function (b) {
    b.addEventListener("click", function () {
      var box = b.nextElementSibling;
      if (!box) return;
      if (box.getAttribute("data-loaded") !== "1") {
        var im = document.createElement("img");
        im.src = b.getAttribute("data-img");
        im.loading = "lazy";
        im.alt = "Exhibit screenshot";
        im.style.cssText = "width:100%;max-width:780px;display:block;border:1px solid #1c1b21;border-radius:10px;background:#fff;";
        box.appendChild(im);
        box.setAttribute("data-loaded", "1");
      }
      var open = box.style.display !== "none";
      box.style.display = open ? "none" : "block";
      b.innerHTML = open ? "View screenshot ▼" : "Hide screenshot ▲";
    });
  });

  /* ---------- live chain data from api.solar.org ---------- */
  var SOLAR_EPOCH = Date.UTC(2022, 2, 28, 18, 0, 0); // 2022-03-28T18:00:00Z
  function fmt(n) { return Number(n).toLocaleString("en-US"); }

  function setChainState(word, color) {
    document.querySelectorAll('[data-live="chainstate"]').forEach(function (cs) {
      cs.style.color = color;
      var dot = cs.querySelector('[data-live="chaindot"]');
      if (dot) dot.style.background = color;
      // replace trailing text node(s) after the dot
      Array.prototype.slice.call(cs.childNodes).forEach(function (n) {
        if (n.nodeType === 3) cs.removeChild(n);
      });
      cs.appendChild(document.createTextNode(word));
    });
  }
  function setLive(key, val) {
    document.querySelectorAll('[data-live="' + key + '"]').forEach(function (el) {
      el.textContent = val;
    });
  }

  function loadChain() {
    if (!document.querySelector('[data-live]')) return;
    fetch("https://api.solar.org/api/blocks?limit=1&orderBy=height:desc", { cache: "no-store" })
      .then(function (r) { return r.ok ? r.json() : Promise.reject(r.status); })
      .then(function (j) {
        var b = j.data && j.data[0];
        if (!b) throw "no block";
        setLive("height", fmt(b.height));
        var ts = (b.timestamp && (b.timestamp.epoch != null ? b.timestamp.epoch : b.timestamp)) || 0;
        var blockMs = SOLAR_EPOCH + ts * 1000;
        var age = Math.max(0, Math.round((Date.now() - blockMs) / 1000));
        setLive("ago", age);
        if (age <= 60) setChainState(" advancing", "#46d39a");
        else if (age <= 600) setChainState(" delayed (" + age + "s)", "#f6a623");
        else setChainState(" stalled", "#f76a6a");
      })
      .catch(function () {
        // honest fallback: don't fake liveness
        setChainState(" status unknown", "#8b8a93");
      });
    fetch("https://api.solar.org/api/blockchain", { cache: "no-store" })
      .then(function (r) { return r.ok ? r.json() : Promise.reject(r.status); })
      .then(function (j) {
        var sup = j.data && j.data.supply;
        if (sup) setLive("supply", Math.round(Number(sup) / 1e8 / 1e6)); // -> millions
      })
      .catch(function () {});
  }

  loadChain();
  setInterval(loadChain, 30000);
})();
