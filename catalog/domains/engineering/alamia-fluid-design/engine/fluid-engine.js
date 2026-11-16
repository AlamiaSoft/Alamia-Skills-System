/**
 * Fluid Engine JS — Dynamic Viewport & Container Inspector + Tweaks
 * Inspired by OpenDesign parameterization
 */

export class FluidEngine {
  constructor(options = {}) {
    this.options = {
      enableInspector: options.enableInspector ?? true,
      enableTweaks: options.enableTweaks ?? true,
      ...options
    };

    this.metrics = {
      width: 0,
      height: 0,
      dpr: window.devicePixelRatio || 1,
      category: 'mobile',
      orientation: 'portrait'
    };

    this.init();
  }

  init() {
    this.updateMetrics();
    window.addEventListener('resize', () => this.updateMetrics(), { passive: true });
    window.addEventListener('orientationchange', () => this.updateMetrics(), { passive: true });

    if (this.options.enableInspector) {
      this.mountInspector();
    }
  }

  updateMetrics() {
    const w = window.innerWidth;
    const h = window.innerHeight;
    this.metrics.width = w;
    this.metrics.height = h;
    this.metrics.dpr = window.devicePixelRatio || 1;
    this.metrics.orientation = w > h ? 'landscape' : 'portrait';

    if (w < 480) {
      this.metrics.category = 'compact-mobile (< 480px)';
    } else if (w < 768) {
      this.metrics.category = 'mobile (480px - 767px)';
    } else if (w < 1024) {
      this.metrics.category = 'tablet (768px - 1023px)';
    } else if (w < 1440) {
      this.metrics.category = 'laptop / desktop (1024px - 1439px)';
    } else if (w < 2160) {
      this.metrics.category = 'large desktop (1440px - 2159px)';
    } else {
      this.metrics.category = 'ultrawide / 4K+ (≥ 2160px)';
    }

    // Set dynamic viewport units on root
    document.documentElement.style.setProperty('--fluid-vw', `${w}px`);
    document.documentElement.style.setProperty('--fluid-vh', `${h}px`);

    this.updateInspectorBadge();
    this.updateHeroTelemetry();
  }

  updateHeroTelemetry() {
    const dimEl = document.getElementById('live-hero-dimensions');
    const catEl = document.getElementById('live-hero-category');
    const oriEl = document.getElementById('live-orientation-pill');
    const dprEl = document.getElementById('live-hero-dpr');
    const barEl = document.getElementById('live-spectrum-bar');

    if (dimEl) dimEl.textContent = `${this.metrics.width} × ${this.metrics.height}`;
    if (catEl) catEl.textContent = `Active Band: ${this.metrics.category}`;
    if (oriEl) oriEl.textContent = this.metrics.orientation.toUpperCase();
    if (dprEl) dprEl.textContent = `${this.metrics.dpr.toFixed(1)}x`;

    if (barEl) {
      // Calculate percentage along 280px to 2560px spectrum
      const pct = Math.min(100, Math.max(10, ((this.metrics.width - 280) / (2560 - 280)) * 100));
      barEl.style.width = `${pct.toFixed(0)}%`;
    }
  }

  mountInspector() {
    if (document.getElementById('fluid-metrics-badge')) return;

    const badge = document.createElement('div');
    badge.id = 'fluid-metrics-badge';
    badge.style.cssText = `
      position: fixed;
      bottom: max(16px, env(safe-area-inset-bottom, 16px));
      right: max(16px, env(safe-area-inset-right, 16px));
      z-index: 99999;
      background: rgba(15, 23, 42, 0.88);
      color: #f8fafc;
      font-family: ui-monospace, monospace;
      font-size: 11px;
      line-height: 1.4;
      padding: 6px 12px;
      border-radius: 999px;
      backdrop-filter: blur(8px);
      box-shadow: 0 4px 12px rgba(0,0,0,0.25);
      border: 1px solid rgba(255,255,255,0.15);
      pointer-events: none;
      user-select: none;
      transition: opacity 0.2s;
    `;
    document.body.appendChild(badge);
    this.badgeEl = badge;
    this.updateInspectorBadge();
  }

  updateInspectorBadge() {
    if (!this.badgeEl) return;
    const { width, height, category, dpr } = this.metrics;
    this.badgeEl.innerHTML = `<span style="color: #38bdf8;">${width}×${height}</span> • ${category} • @${dpr.toFixed(1)}x`;
  }

  toggleTheme() {
    const current = document.documentElement.getAttribute('data-theme');
    const target = current === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', target);
    try {
      localStorage.setItem('fluid-theme', target);
    } catch (e) {}
    return target;
  }
}

// Auto-initialize when loaded
if (typeof window !== 'undefined') {
  window.fluidEngine = new FluidEngine();
}
