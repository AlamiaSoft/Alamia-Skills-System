/**
 * Fluid Engine — Optional viewport diagnostics and development inspector.
 * Responsive layout behavior belongs in CSS; this module is not required.
 */
export class FluidEngine {
  constructor(options = {}) {
    this.options = { enableInspector: false, updateHeroTelemetry: false, ...options };
    this.metrics = { width: 0, height: 0, dpr: 1, category: 'unknown', orientation: 'unknown' };
    this.badgeEl = null;
    this.initialized = false;
    this.onViewportChange = () => this.updateMetrics();
  }

  init() {
    if (this.initialized || typeof window === 'undefined' || typeof document === 'undefined') return this;
    this.initialized = true;
    this.updateMetrics();
    window.addEventListener('resize', this.onViewportChange, { passive: true });
    window.addEventListener('orientationchange', this.onViewportChange, { passive: true });
    window.visualViewport?.addEventListener('resize', this.onViewportChange, { passive: true });
    if (this.options.enableInspector) this.mountInspector();
    return this;
  }

  updateMetrics() {
    if (typeof window === 'undefined' || typeof document === 'undefined') return;
    const root = document.documentElement;
    const viewport = window.visualViewport;
    const width = Math.round(root.clientWidth || window.innerWidth);
    const height = Math.round(viewport?.height || window.innerHeight);
    this.metrics.width = width;
    this.metrics.height = height;
    this.metrics.dpr = window.devicePixelRatio || 1;
    this.metrics.orientation = width > height ? 'landscape' : 'portrait';

    if (width < 480) this.metrics.category = 'compact-mobile (< 480px)';
    else if (width < 768) this.metrics.category = 'mobile (480px - 767px)';
    else if (width < 1024) this.metrics.category = 'tablet (768px - 1023px)';
    else if (width < 1440) this.metrics.category = 'laptop / desktop (1024px - 1439px)';
    else if (width < 2160) this.metrics.category = 'large desktop (1440px - 2159px)';
    else this.metrics.category = 'ultrawide / 4K+ (≥ 2160px)';

    root.style.setProperty('--fluid-vw', `${width}px`);
    root.style.setProperty('--fluid-vh', `${height}px`);
    this.updateInspectorBadge();
    if (this.options.updateHeroTelemetry) this.updateHeroTelemetry();
  }

  updateHeroTelemetry() {
    const { width, height, category, orientation, dpr } = this.metrics;
    const setText = (id, value) => {
      const el = document.getElementById(id);
      if (el) el.textContent = value;
    };
    setText('live-hero-dimensions', `${width} × ${height}`);
    setText('live-hero-category', `Active Band: ${category}`);
    setText('live-orientation-pill', orientation.toUpperCase());
    setText('live-hero-dpr', `${dpr.toFixed(1)}x`);
    const bar = document.getElementById('live-spectrum-bar');
    if (bar) {
      const pct = Math.min(100, Math.max(10, ((width - 280) / (3840 - 280)) * 100));
      bar.style.width = `${pct.toFixed(0)}%`;
    }
  }

  mountInspector() {
    if (this.badgeEl || !document.body) return;
    const badge = document.createElement('output');
    badge.id = 'fluid-metrics-badge';
    badge.setAttribute('aria-label', 'Viewport diagnostics');
    badge.style.cssText = [
      'position:fixed','bottom:max(16px, env(safe-area-inset-bottom, 16px))',
      'right:max(16px, env(safe-area-inset-right, 16px))','z-index:99999',
      'background:rgba(15, 23, 42, .9)','color:#f8fafc',
      'font:11px/1.4 ui-monospace, monospace','padding:6px 12px',
      'border-radius:999px','backdrop-filter:blur(8px)',
      'box-shadow:0 4px 12px rgba(0,0,0,.25)',
      'border:1px solid rgba(255,255,255,.15)',
      'pointer-events:none','user-select:none'
    ].join(';');
    document.body.appendChild(badge);
    this.badgeEl = badge;
    this.updateInspectorBadge();
  }

  updateInspectorBadge() {
    if (!this.badgeEl) return;
    const { width, height, category, dpr } = this.metrics;
    this.badgeEl.textContent = `${width}×${height} • ${category} • @${dpr.toFixed(1)}x`;
  }

  toggleTheme() {
    if (typeof document === 'undefined') return null;
    const root = document.documentElement;
    const target = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
    root.setAttribute('data-theme', target);
    try {
      if (typeof localStorage !== 'undefined') localStorage.setItem('fluid-theme', target);
    } catch {
      // Storage may be unavailable in restricted browsing contexts.
    }
    return target;
  }

  destroy() {
    if (!this.initialized || typeof window === 'undefined') return;
    window.removeEventListener('resize', this.onViewportChange);
    window.removeEventListener('orientationchange', this.onViewportChange);
    window.visualViewport?.removeEventListener('resize', this.onViewportChange);
    this.badgeEl?.remove();
    this.badgeEl = null;
    this.initialized = false;
  }
}
