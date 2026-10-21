import os
import streamlit as st
import json
from pathlib import Path
from dotenv import load_dotenv
from google import genai
from pydantic import BaseModel

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Customer Review Analyzer",
    page_icon="✨",
    layout="centered",
)

# ── Load environment & initialise client ─────────────────────────────────────
# Walk up to find .env (it lives in the parent directory)
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

if not os.getenv("GOOGLE_API_KEY") and not os.getenv("GEMINI_API_KEY"):
    st.error("⚠️ No API key found. Please set `GOOGLE_API_KEY` in your `.env` file.")
    st.stop()

@st.cache_resource
def get_client():
    return genai.Client()

client = get_client()

# ── Pydantic schema ──────────────────────────────────────────────────────────
class ReviewAnalysis(BaseModel):
    sentiment: str
    rating: int
    pros: list[str]
    cons: list[str]
    recommended_action: str

# ── Custom CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
/* ── Import premium font ───────────────────────────────────────────── */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

/* ── Global overrides ──────────────────────────────────────────────── */
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* Hide default Streamlit branding */
#MainMenu, footer, header {visibility: hidden;}

/* ── Animated gradient background ──────────────────────────────────── */
.stApp {
    background: linear-gradient(135deg, #0f0c29 0%, #1a1a40 40%, #24243e 100%);
}

/* ── Hero header ───────────────────────────────────────────────────── */
.hero-container {
    text-align: center;
    padding: 2.5rem 1rem 1.5rem;
}
.hero-title {
    font-size: 2.6rem;
    font-weight: 800;
    background: linear-gradient(135deg, #a78bfa 0%, #818cf8 30%, #6366f1 60%, #c084fc 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    letter-spacing: -0.5px;
    margin-bottom: 0.35rem;
}
.hero-subtitle {
    font-size: 1.05rem;
    color: #94a3b8;
    font-weight: 400;
    letter-spacing: 0.2px;
}

/* ── Glass card ────────────────────────────────────────────────────── */
.glass-card {
    background: rgba(255, 255, 255, 0.04);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 16px;
    padding: 1.8rem;
    margin-bottom: 1.2rem;
    transition: transform 0.25s ease, box-shadow 0.25s ease;
}
.glass-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 32px rgba(99, 102, 241, 0.12);
}

/* ── Section titles ────────────────────────────────────────────────── */
.section-title {
    font-size: 0.82rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1.4px;
    color: #818cf8;
    margin-bottom: 0.9rem;
}

/* ── Sentiment badge ───────────────────────────────────────────────── */
.sentiment-badge {
    display: inline-block;
    padding: 0.35rem 1.1rem;
    border-radius: 50px;
    font-weight: 600;
    font-size: 0.92rem;
    letter-spacing: 0.4px;
    text-transform: capitalize;
}
.sentiment-positive {
    background: linear-gradient(135deg, rgba(34,197,94,0.18), rgba(16,185,129,0.10));
    color: #4ade80;
    border: 1px solid rgba(34,197,94,0.3);
}
.sentiment-negative {
    background: linear-gradient(135deg, rgba(239,68,68,0.18), rgba(244,63,94,0.10));
    color: #f87171;
    border: 1px solid rgba(239,68,68,0.3);
}
.sentiment-mixed {
    background: linear-gradient(135deg, rgba(251,191,36,0.18), rgba(245,158,11,0.10));
    color: #fbbf24;
    border: 1px solid rgba(251,191,36,0.3);
}
.sentiment-neutral {
    background: linear-gradient(135deg, rgba(148,163,184,0.18), rgba(100,116,139,0.10));
    color: #94a3b8;
    border: 1px solid rgba(148,163,184,0.3);
}

/* ── Star rating ───────────────────────────────────────────────────── */
.star-rating {
    font-size: 1.6rem;
    letter-spacing: 3px;
}

/* ── Pros / Cons pills ─────────────────────────────────────────────── */
.pill-list {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
}
.pill {
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
    padding: 0.4rem 0.9rem;
    border-radius: 10px;
    font-size: 0.88rem;
    font-weight: 500;
}
.pill-pro {
    background: rgba(34, 197, 94, 0.10);
    color: #86efac;
    border: 1px solid rgba(34, 197, 94, 0.20);
}
.pill-con {
    background: rgba(239, 68, 68, 0.10);
    color: #fca5a5;
    border: 1px solid rgba(239, 68, 68, 0.20);
}

/* ── Recommendation box ────────────────────────────────────────────── */
.recommendation-box {
    background: linear-gradient(135deg, rgba(99,102,241,0.08), rgba(168,85,247,0.06));
    border-left: 3px solid #818cf8;
    border-radius: 0 12px 12px 0;
    padding: 1rem 1.2rem;
    color: #c7d2fe;
    font-size: 0.95rem;
    line-height: 1.65;
}

/* ── Streamlit text-area customisation ─────────────────────────────── */
.stTextArea textarea {
    background: rgba(255, 255, 255, 0.04) !important;
    border: 1px solid rgba(255, 255, 255, 0.10) !important;
    border-radius: 12px !important;
    color: #e2e8f0 !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.95rem !important;
    padding: 1rem !important;
    transition: border-color 0.3s ease !important;
}
.stTextArea textarea:focus {
    border-color: #818cf8 !important;
    box-shadow: 0 0 0 2px rgba(129, 140, 248, 0.15) !important;
}

/* ── Button styling ────────────────────────────────────────────────── */
.stButton > button {
    width: 100%;
    background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 0.7rem 2rem !important;
    font-family: 'Inter', sans-serif !important;
    font-weight: 600 !important;
    font-size: 1rem !important;
    letter-spacing: 0.3px !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 4px 15px rgba(99, 102, 241, 0.3) !important;
}
.stButton > button:hover {
    transform: translateY(-1px) !important;
    box-shadow: 0 6px 25px rgba(99, 102, 241, 0.45) !important;
}
.stButton > button:active {
    transform: translateY(0) !important;
}

/* ── Divider ───────────────────────────────────────────────────────── */
.subtle-divider {
    border: none;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.08), transparent);
    margin: 1.2rem 0;
}

/* ── Metrics row ───────────────────────────────────────────────────── */
.metrics-row {
    display: flex;
    gap: 1rem;
    margin-bottom: 1rem;
}
.metric-card {
    flex: 1;
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.06);
    border-radius: 12px;
    padding: 1.1rem;
    text-align: center;
}
.metric-label {
    font-size: 0.72rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1.2px;
    color: #64748b;
    margin-bottom: 0.4rem;
}
.metric-value {
    font-size: 1.25rem;
    font-weight: 700;
    color: #e2e8f0;
}

/* ── Spinner ───────────────────────────────────────────────────────── */
.stSpinner > div {
    border-color: #818cf8 !important;
}
</style>
""", unsafe_allow_html=True)

# ── Hero header ──────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-container">
    <div class="hero-title">✨ Review Analyzer</div>
    <div class="hero-subtitle">AI-powered customer review insights in seconds</div>
</div>
""", unsafe_allow_html=True)

# ── Input area ───────────────────────────────────────────────────────────────
review_text = st.text_area(
    "Paste a customer review below",
    placeholder="e.g. I ordered the wireless earbuds last week. Sound quality is amazing and battery lasts all day, but the case feels cheap and it arrived two days late...",
    height=150,
    label_visibility="collapsed",
)

analyze_clicked = st.button("🔍  Analyze Review")

# ── Analysis logic ───────────────────────────────────────────────────────────
if analyze_clicked:
    if not review_text.strip():
        st.warning("Please paste a review before analyzing.")
        st.stop()

    with st.spinner("Analyzing review…"):
        try:
            interaction = client.interactions.create(
                model="gemini-3.5-flash-lite",
                input=review_text,
                response_format={
                    "type": "text",
                    "mime_type": "application/json",
                    "schema": ReviewAnalysis.model_json_schema(),
                },
            )
            result = ReviewAnalysis.model_validate_json(interaction.output_text)
        except Exception as e:
            st.error(f"Something went wrong: {e}")
            st.stop()

    # ── Helper functions ─────────────────────────────────────────────────────
    def sentiment_class(s: str) -> str:
        s_lower = s.lower()
        if s_lower in ("positive", "very positive"):
            return "sentiment-positive"
        if s_lower in ("negative", "very negative"):
            return "sentiment-negative"
        if s_lower == "mixed":
            return "sentiment-mixed"
        return "sentiment-neutral"

    def render_stars(rating: int, out_of: int = 5) -> str:
        filled = "★" * min(rating, out_of)
        empty = "☆" * (out_of - min(rating, out_of))
        return filled + empty

    # ── Metrics row ──────────────────────────────────────────────────────────
    st.markdown(f"""
    <div class="metrics-row">
        <div class="metric-card">
            <div class="metric-label">Sentiment</div>
            <div class="metric-value">
                <span class="sentiment-badge {sentiment_class(result.sentiment)}">{result.sentiment}</span>
            </div>
        </div>
        <div class="metric-card">
            <div class="metric-label">Rating</div>
            <div class="metric-value star-rating">{render_stars(result.rating)}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Pros ─────────────────────────────────────────────────────────────────
    pros_html = "".join(
        f'<span class="pill pill-pro">✓ {p}</span>' for p in result.pros
    )
    st.markdown(f"""
    <div class="glass-card">
        <div class="section-title">👍 Pros</div>
        <div class="pill-list">{pros_html}</div>
    </div>
    """, unsafe_allow_html=True)

    # ── Cons ─────────────────────────────────────────────────────────────────
    cons_html = "".join(
        f'<span class="pill pill-con">✗ {c}</span>' for c in result.cons
    )
    st.markdown(f"""
    <div class="glass-card">
        <div class="section-title">👎 Cons</div>
        <div class="pill-list">{cons_html}</div>
    </div>
    """, unsafe_allow_html=True)

    # ── Recommendation ───────────────────────────────────────────────────────
    st.markdown(f"""
    <div class="glass-card">
        <div class="section-title">💡 Recommended Action</div>
        <div class="recommendation-box">{result.recommended_action}</div>
    </div>
    """, unsafe_allow_html=True)

    # ── Raw JSON expander ────────────────────────────────────────────────────
    # with st.expander("📄 View raw JSON response"):
    #     st.json(result.model_dump())
