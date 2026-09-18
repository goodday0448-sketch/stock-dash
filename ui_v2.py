from __future__ import annotations

import html
import streamlit as st


NAV_ITEMS = [
    ("홈", "⌂"),
    ("시장 현황", "▥"),
    ("종목 분석", "◫"),
    ("공시 분석", "▤"),
    ("테마 & 섹터", "◇"),
    ("포트폴리오", "▣"),
    ("관심 종목", "☆"),
    ("AI 인사이트", "✦"),
    ("데이터 연결 관리", "⚙"),
]


def apply_theme():
    st.markdown(
        """
<style>
:root{
  --bg:#FFFFFF;
  --bg2:#F7F9FC;
  --panel:#FFFFFF;
  --panel2:#F4F7FB;
  --line:#E2E8F0;
  --line2:#CBD5E1;
  --text:#172033;
  --muted:#64748B;
  --blue:#1677FF;
  --blue2:#2D8CFF;
  --up:#FF4565;
  --down:#3B82F6;
  --green:#18C98A;
}
html,body,[class*="css"]{
  font-family:Pretendard,"Noto Sans KR","Apple SD Gothic Neo",sans-serif;
}
.stApp{
  background:#FFFFFF !important;
  color:var(--text);
}
.block-container{
  max-width:1540px !important;
  padding:1.15rem 1.25rem 3.5rem !important;
}
header[data-testid="stHeader"]{
  background:rgba(255,255,255,.94);
  backdrop-filter:blur(14px);
}
section[data-testid="stSidebar"]{
  background:#FFFFFF !important;
  border-right:1px solid #E2E8F0 !important;
}
section[data-testid="stSidebar"] > div{padding-top:.9rem}
[data-testid="stSidebar"] .stRadio > label{display:none}
[data-testid="stSidebar"] .stRadio div[role="radiogroup"]{gap:.2rem}
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label{
  color:#475569;
  border-radius:10px;
  padding:.62rem .7rem;
  transition:.15s ease;
}
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:hover{
  background:#F1F5F9;
  color:#172033;
}
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:has(input:checked){
  background:linear-gradient(90deg,#176FF0,#155FCB);
  color:#FFFFFF;
  font-weight:800;
  box-shadow:0 6px 18px rgba(22,119,255,.2);
}
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label p{font-size:13px}
[data-testid="stSidebar"] [data-testid="stCaptionContainer"]{color:#708AA5}
[data-testid="stSidebar"] hr{border-color:#E2E8F0 !important}
h1,h2,h3,h4,h5{color:var(--text);letter-spacing:-.035em}
h1{font-weight:800}
h2,h3{font-weight:750}
p,li{line-height:1.55}
[data-testid="stCaptionContainer"]{color:var(--muted)}
[data-testid="stMetric"]{
  background:#FFFFFF;
  border:1px solid var(--line);
  border-radius:14px;
  padding:15px 17px;
  box-shadow:0 6px 18px rgba(15,23,42,.06);
}
[data-testid="stMetricLabel"]{color:#64748B}
[data-testid="stMetricValue"]{color:#172033;font-weight:800}
[data-testid="stMetricDelta"] svg{display:none}
[data-testid="stVerticalBlockBorderWrapper"]{
  border-color:var(--line) !important;
  border-radius:14px !important;
  background:#FFFFFF !important;
  box-shadow:0 6px 18px rgba(15,23,42,.06);
}
.stButton > button,.stFormSubmitButton > button{
  border-radius:10px;
  min-height:2.65rem;
  font-weight:750;
  border-color:#CBD5E1;
  background:#FFFFFF;
  color:#334155;
}
.stButton > button:hover,.stFormSubmitButton > button:hover{
  border-color:#1677FF;
  color:#FFFFFF;
}
.stButton > button[kind="primary"],.stFormSubmitButton > button[kind="primary"]{
  background:linear-gradient(135deg,#1677FF,#1262D5);
  border-color:#1677FF;
  color:#FFFFFF;
}
.stTextInput input,.stTextArea textarea,.stSelectbox div[data-baseweb="select"] > div{
  background:#FFFFFF !important;
  color:#172033 !important;
  border:1px solid #CBD5E1 !important;
  border-radius:10px !important;
}
.stTextInput input::placeholder,.stTextArea textarea::placeholder{color:#64748B}
.stTabs [data-baseweb="tab-list"]{gap:7px;border-bottom:1px solid var(--line)}
.stTabs [data-baseweb="tab"]{
  color:#64748B;
  border-radius:9px 9px 0 0;
  padding:8px 12px;
}
.stTabs [aria-selected="true"]{color:#172033 !important;background:#EAF2FF;border-bottom:2px solid #1677FF}
.stDataFrame{border:1px solid var(--line);border-radius:12px;overflow:hidden}
hr{border-color:#E2E8F0 !important}

/* StockDash brand */
.planx-brand{
  display:flex;
  align-items:center;
  gap:10px;
  margin:4px 0 20px;
  padding:2px 3px 16px;
  border-bottom:1px solid #E2E8F0;
}
.planx-brand:before{
  content:"↗";
  width:38px;height:38px;border-radius:11px;
  display:flex;align-items:center;justify-content:center;
  background:linear-gradient(145deg,#1677FF,#1BC7A0);
  color:#fff;font-size:22px;font-weight:900;
  box-shadow:0 8px 20px rgba(22,119,255,.22);
}
.planx-brand-title{
  color:#172033;
  font-size:21px;
  line-height:1.1;
  font-weight:850;
  letter-spacing:-.045em;
}
.planx-brand-sub{
  color:#64748B;
  font-size:9px;
  letter-spacing:.16em;
  margin-top:4px;
}

/* Hero / KPI cards */
.planx-hero{
  background:#F8FAFC;
  border:1px solid #E2E8F0;
  border-radius:17px;
  padding:22px 24px;
  margin-bottom:16px;
  box-shadow:0 14px 36px rgba(0,0,0,.2);
}
.planx-eyebrow{
  color:#1677FF;
  font-size:10px;
  font-weight:850;
  letter-spacing:.13em;
  margin-bottom:7px;
}
.planx-hero h1{margin:0;font-size:30px;line-height:1.18}
.planx-hero p{margin:8px 0 0;color:#64748B;font-size:13px}
.planx-card{
  background:#FFFFFF;
  border:1px solid #E2E8F0;
  border-radius:14px;
  padding:16px 17px;
  min-height:108px;
  box-shadow:0 9px 24px rgba(0,0,0,.14);
}
.planx-card-title{font-size:11px;color:#64748B;margin-bottom:7px;font-weight:700}
.planx-card-value{font-size:22px;color:#172033;font-weight:850;letter-spacing:-.035em}
.planx-card-note{margin-top:6px;font-size:10px;color:#64748B}
.planx-empty{
  background:#F8FAFC;
  border:1px dashed #2A557E;
  border-radius:13px;
  padding:20px;
  color:#64748B;
}
.planx-source{
  display:inline-flex;
  align-items:center;
  gap:5px;
  color:#91A8C0;
  background:#F8FAFC;
  border:1px solid #CBD5E1;
  padding:4px 8px;
  border-radius:999px;
  font-size:9px;
}
.planx-status-ok{color:#087F5B;background:#ECFDF5;border-color:#A7F3D0}
.planx-status-wait{color:#9A6700;background:#FFFBEB;border-color:#FDE68A}
.planx-status-bad{color:#C6284A;background:#FFF1F2;border-color:#FECDD3}

/* Shared dashboard helpers */
.px-market-strip{
  display:grid;
  grid-template-columns:repeat(5,1fr);
  gap:8px;
  margin-bottom:14px;
}
.px-market-item{
  background:#FFFFFF;
  border:1px solid #173A5F;
  border-radius:11px;
  padding:9px 12px;
}
.px-market-item span{display:block;color:#64748B;font-size:9px}
.px-market-item strong{display:block;color:#172033;font-size:15px;margin-top:3px}
.px-up{color:var(--up) !important}.px-down{color:var(--down) !important}.px-green{color:var(--green) !important}

@media(max-width:900px){
  .block-container{padding-left:1rem!important;padding-right:1rem!important}
  .planx-hero{padding:20px}
  .planx-hero h1{font-size:27px}
  .px-market-strip{grid-template-columns:repeat(2,1fr)}
}
@media(max-width:640px){
  .planx-card{min-height:94px;padding:13px}
  .planx-card-value{font-size:20px}
  .px-market-strip{grid-template-columns:1fr 1fr}
}
</style>
""",
        unsafe_allow_html=True,
    )


def brand():
    st.markdown(
        """
<div class="planx-brand">
  <div>
    <div class="planx-brand-title">StockDash</div>
    <div class="planx-brand-sub">STOCK INTELLIGENCE</div>
  </div>
</div>
""",
        unsafe_allow_html=True,
    )


def hero(title: str, subtitle: str, eyebrow: str = "STOCKDASH INVESTMENT OS"):
    st.markdown(
        f"""
<div class="planx-hero">
  <div class="planx-eyebrow">{html.escape(eyebrow)}</div>
  <h1>{html.escape(title)}</h1>
  <p>{html.escape(subtitle)}</p>
</div>
""",
        unsafe_allow_html=True,
    )


def card(title: str, value: str, note: str = "", status: str = ""):
    status_html = f'<div class="planx-card-note">{html.escape(status)}</div>' if status else ""
    st.markdown(
        f"""
<div class="planx-card">
  <div class="planx-card-title">{html.escape(title)}</div>
  <div class="planx-card-value">{html.escape(value)}</div>
  <div class="planx-card-note">{html.escape(note)}</div>
  {status_html}
</div>
""",
        unsafe_allow_html=True,
    )


def empty_state(title: str, message: str):
    st.markdown(
        f"""
<div class="planx-empty">
  <strong style="color:#172033">{html.escape(title)}</strong><br>
  <span>{html.escape(message)}</span>
</div>
""",
        unsafe_allow_html=True,
    )


def source_badge(label: str, state: str = "wait"):
    cls = {"ok": "planx-status-ok", "bad": "planx-status-bad"}.get(state, "planx-status-wait")
    st.markdown(
        f'<span class="planx-source {cls}">{html.escape(label)}</span>',
        unsafe_allow_html=True,
    )
