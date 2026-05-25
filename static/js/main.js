/**
 * main.js — Segun Banji Data Science Portfolio
 * Single responsibility: stat count-up animation on home page.
 * IntersectionObserver triggers when #stats-section enters viewport.
 */
(function () {
  "use strict";

  function animateCounter(el, target, suffix, duration) {
    const start = performance.now();
    function step(now) {
      const progress = Math.min((now - start) / duration, 1);
      const eased = 1 - Math.pow(1 - progress, 3); // ease-out cubic
      el.textContent = Math.floor(eased * target) + suffix;
      if (progress < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }

  function initCounters() {
    document.querySelectorAll("[data-count-target]").forEach(function (el) {
      const target = parseInt(el.dataset.countTarget, 10);
      const suffix = el.dataset.countSuffix || "";
      animateCounter(el, target, suffix, 1500);
    });
  }

  const section = document.getElementById("stats-section");
  if (!section) return;

  const observer = new IntersectionObserver(
    function (entries) {
      if (entries[0].isIntersecting) {
        initCounters();
        observer.disconnect();
      }
    },
    { threshold: 0.25 }
  );
  observer.observe(section);
})();
