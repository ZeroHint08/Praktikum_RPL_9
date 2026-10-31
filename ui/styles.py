"""Gaya tampilan (CSS) untuk View Layer. Dipisah agar app.py tetap singkat."""

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="st-"], .stApp { font-family: Inter, ui-sans-serif, system-ui, sans-serif; }
.stApp { background: #f6f8f7; color: #020617; }
.block-container { max-width: 1152px; padding-top: 2rem; padding-bottom: 2rem; }
#MainMenu, footer { visibility: hidden; }
header[data-testid="stHeader"] { background: transparent; }

/* ---------- Header ---------- */
.kp-header { display: flex; flex-wrap: wrap; gap: 1.5rem; justify-content: space-between;
  align-items: flex-end; border-bottom: 1px solid #e2e8f0; padding-bottom: 2rem; margin-bottom: 2rem; }
.kp-brand { display: flex; align-items: center; gap: .75rem; margin-bottom: 1.25rem; }
.kp-logo { width: 2.25rem; height: 2.25rem; border-radius: .75rem; background: #0f766e; color: #fff;
  display: grid; place-items: center; font-weight: 900; font-size: .875rem; }
.kp-brand-name { font-size: .875rem; font-weight: 700; color: #1e293b; }
.kp-sep { width: 1px; height: 1rem; background: #cbd5e1; }
.kp-brand-sub { font-size: .75rem; font-weight: 500; color: #94a3b8; }
.kp-eyebrow { font-size: .75rem; font-weight: 700; letter-spacing: .2em; text-transform: uppercase; color: #0f766e; margin: 0; }
.kp-title { margin: .75rem 0 0; font-size: 3rem; font-weight: 600; line-height: 1.05; letter-spacing: -.05em; color: #020617; }
.kp-subtitle { margin: 1rem 0 0; max-width: 40rem; font-size: 1rem; line-height: 1.75; color: #64748b; }
.kp-stats { display: flex; gap: .75rem; }
.kp-stat { border: 1px solid #e2e8f0; background: #fff; border-radius: 1rem; padding: .75rem 1.25rem; box-shadow: 0 1px 2px rgba(15,23,42,.05); }
.kp-stat.teal { border-color: #ccfbf1; background: #f0fdfa; }
.kp-stat-num { margin: 0; font-size: 1.5rem; font-weight: 600; letter-spacing: -.02em; color: #020617; }
.kp-stat.teal .kp-stat-num { color: #115e59; }
.kp-stat-label { margin: 0; font-size: .75rem; color: #94a3b8; }
.kp-stat.teal .kp-stat-label { color: rgba(15,118,110,.7); }

/* ---------- Kartu form ---------- */
div[data-testid="stForm"] { background: #fff; border: 1px solid rgba(226,232,240,.8); border-radius: 28px;
  padding: 2rem; box-shadow: 0 20px 60px -32px rgba(15,23,42,.24); }
.kp-card-head { display: flex; justify-content: space-between; gap: 1rem; align-items: flex-start; margin-bottom: .75rem; }
.kp-card-title { margin: .5rem 0 0; font-size: 1.5rem; font-weight: 600; letter-spacing: -.03em; color: #020617; }
.kp-card-desc { margin: .5rem 0 0; font-size: .875rem; line-height: 1.5; color: #64748b; max-width: 32rem; }
.kp-icon { width: 2.75rem; height: 2.75rem; flex-shrink: 0; border-radius: 1rem; background: #f0fdfa; color: #0f766e;
  display: grid; place-items: center; font-size: 1.25rem; }

div[data-testid="stForm"] label p { font-weight: 600; color: #334155; font-size: .875rem; }
div[data-baseweb="input"], div[data-baseweb="base-input"] { border-radius: 12px !important; background: #f8fafc !important; }
div[data-baseweb="input"] { border: 1px solid #e2e8f0 !important; }
div[data-baseweb="input"]:focus-within { border-color: #0d9488 !important; box-shadow: 0 0 0 4px rgba(13,148,136,.12) !important; }
div[data-baseweb="input"] input { font-size: .875rem; }
.kp-hint { margin: -.5rem 0 .75rem; font-size: .75rem; color: #94a3b8; }
.kp-hint.err { color: #e11d48; font-weight: 500; }
.kp-alert { border: 1px solid #ffe4e6; background: #fff1f2; color: #be123c; border-radius: 12px;
  padding: .75rem 1rem; font-size: .875rem; font-weight: 500; margin-bottom: .75rem; }
div[data-testid="stFormSubmitButton"] button { width: 100%; height: 3rem; border-radius: 12px; background: #020617;
  border: none; transition: background .15s; }
div[data-testid="stFormSubmitButton"] button p { color: #fff; font-weight: 700; font-size: .875rem; }
div[data-testid="stFormSubmitButton"] button:hover { background: #115e59; }

/* ---------- Panel hasil ---------- */
.kp-result { position: relative; overflow: hidden; border-radius: 28px; padding: 2rem; color: #fff;
  box-shadow: 0 24px 70px -36px rgba(15,118,110,.7); min-height: 31rem; display: flex; flex-direction: column; background: #020617; }
.kp-result.lulus { background: #115e59; }
.kp-result.tidak { background: #1e293b; }
.kp-result::before { content: ""; position: absolute; right: -4rem; top: -4rem; width: 11rem; height: 11rem;
  border-radius: 50%; border: 1px solid rgba(255,255,255,.1); }
.kp-result-top { display: flex; justify-content: space-between; align-items: center; position: relative; }
.kp-result-eyebrow { margin: 0; font-size: .75rem; font-weight: 700; letter-spacing: .18em; text-transform: uppercase; color: #99f6e4; }
.kp-result-badge { width: 2.5rem; height: 2.5rem; border-radius: 50%; background: rgba(255,255,255,.1); display: grid; place-items: center; }
.kp-result-body { margin: auto 0; padding: 2.5rem 0; position: relative; }
.kp-muted { margin: 0; font-size: .875rem; color: rgba(255,255,255,.6); }
.kp-result-name { margin: .25rem 0 0; font-size: 1.5rem; font-weight: 600; letter-spacing: -.02em; }
.kp-divider { height: 1px; background: rgba(255,255,255,.1); margin: 1.5rem 0; }
.kp-result-status { margin: 0; font-size: 1.875rem; font-weight: 600; line-height: 1.2; letter-spacing: -.04em; }
.kp-result-text { margin: 1rem 0 0; font-size: .875rem; line-height: 1.6; color: rgba(255,255,255,.65); max-width: 24rem; }
.kp-limits { display: grid; grid-template-columns: 1fr 1fr; gap: .75rem; position: relative; }
.kp-limit { border: 1px solid rgba(255,255,255,.1); background: rgba(255,255,255,.06); border-radius: 1rem; padding: 1rem; }
.kp-limit-num { margin: 0; font-size: 1.5rem; font-weight: 600; }
.kp-limit-label { margin: .25rem 0 0; font-size: .75rem; color: rgba(255,255,255,.5); }

/* ---------- Tabel riwayat ---------- */
.kp-section { margin-top: 2rem; overflow: hidden; border: 1px solid rgba(226,232,240,.8); background: #fff;
  border-radius: 28px; box-shadow: 0 20px 60px -38px rgba(15,23,42,.22); }
.kp-section-head { display: flex; flex-wrap: wrap; gap: .75rem; justify-content: space-between; align-items: center;
  border-bottom: 1px solid #f1f5f9; padding: 1.5rem 2rem; }
.kp-pill-count { border-radius: 999px; background: #f1f5f9; color: #64748b; font-size: .75rem; font-weight: 600; padding: .375rem .75rem; }
.kp-table-wrap { overflow-x: auto; }
.kp-table { width: 100%; min-width: 720px; border-collapse: collapse; text-align: left; }
.kp-table th { background: rgba(248,250,252,.7); border-bottom: 1px solid #f1f5f9; font-size: .75rem; font-weight: 700;
  letter-spacing: .06em; text-transform: uppercase; color: #94a3b8; padding: 1rem 1.25rem; }
.kp-table td { border-bottom: 1px solid #f1f5f9; font-size: .875rem; padding: 1.25rem; color: #475569; }
.kp-table tr:last-child td { border-bottom: none; }
.kp-table tr:hover td { background: rgba(248,250,252,.5); }
.kp-table th:first-child, .kp-table td:first-child { padding-left: 2rem; }
.kp-table th:last-child, .kp-table td:last-child { padding-right: 2rem; text-align: right; }
.kp-student { display: flex; align-items: center; gap: .75rem; }
.kp-avatar { width: 2.25rem; height: 2.25rem; border-radius: 50%; background: #f1f5f9; color: #475569;
  display: grid; place-items: center; font-size: .75rem; font-weight: 700; flex-shrink: 0; }
.kp-student-name { font-weight: 600; color: #1e293b; }
.kp-num { font-weight: 600; color: #334155; font-variant-numeric: tabular-nums; }
.kp-status { display: inline-flex; align-items: center; gap: .5rem; border-radius: 999px; font-size: .75rem; font-weight: 700; padding: .375rem .75rem; }
.kp-status.lulus { background: #f0fdfa; color: #0f766e; }
.kp-status.tidak { background: #fffbeb; color: #b45309; }
.kp-dot { width: .375rem; height: .375rem; border-radius: 50%; }
.kp-status.lulus .kp-dot { background: #14b8a6; }
.kp-status.tidak .kp-dot { background: #f59e0b; }
.kp-date { color: #94a3b8; }
.kp-empty { text-align: center; padding: 4rem 1.5rem; }
.kp-empty-icon { width: 3rem; height: 3rem; margin: 0 auto; border-radius: 1rem; background: #f1f5f9; color: #94a3b8;
  display: grid; place-items: center; font-size: 1.25rem; font-weight: 700; }
.kp-empty h3 { margin: 1rem 0 0; font-size: 1rem; font-weight: 600; color: #1e293b; }
.kp-empty p { margin: .5rem auto 0; max-width: 24rem; font-size: .875rem; color: #94a3b8; }
.kp-footer { display: flex; flex-wrap: wrap; justify-content: space-between; gap: .5rem; padding: 2rem .5rem 1rem; font-size: .75rem; color: #94a3b8; }
.kp-footer p { margin: 0; }

@media (max-width: 640px) { .kp-title { font-size: 2.25rem; } }
</style>
"""
