import reflex as rx

_COUNT_UP_JS = """
(function () {
  function easeOutCubic(t) {
    return 1 - Math.pow(1 - t, 3);
  }
  function formatVal(v, mode) {
    var n = Math.round(v);
    if (mode === "k" || mode === "int") return n.toLocaleString("en-US");
    return String(n);
  }
  function animateEl(el) {
    var raw = el.getAttribute("data-ptg-count");
    if (raw == null || raw === "") return;
    var target = parseFloat(raw);
    if (isNaN(target)) return;
    var mode = el.getAttribute("data-ptg-mode") || "int";
    var dur = 1400;
    var start = performance.now();
    function tick(now) {
      var p = Math.min(1, (now - start) / dur);
      var v = target * easeOutCubic(p);
      el.textContent = formatVal(v, mode);
      if (p < 1) requestAnimationFrame(tick);
    }
    el.textContent = formatVal(0, mode);
    requestAnimationFrame(tick);
  }
  function run() {
    document.querySelectorAll(".ptg-count-up").forEach(animateEl);
  }
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", run);
  } else {
    run();
  }
  setTimeout(run, 120);
  setTimeout(run, 600);
})();
"""


def count_up_script() -> rx.Component:
    return rx.script(_COUNT_UP_JS, defer=True)
