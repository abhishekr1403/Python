import streamlit as st
from dotenv import load_dotenv
from google import genai

# ── Init ──────────────────────────────────────────────────────────────
load_dotenv()
client = genai.Client()

st.set_page_config(
    page_title="RecipeAI",
    page_icon="🍳",
    layout="centered",
)

# ── CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

:root {
    --accent: #f97316;
    --bg: #0f172a;
    --card: rgba(30,41,59,0.6);
    --border: rgba(255,255,255,0.07);
    --text: #f1f5f9;
    --muted: #94a3b8;
}

html, body, [data-testid="stApp"] {
    font-family: 'Inter', sans-serif;
    color: var(--text);
}
[data-testid="stApp"] {
    background: linear-gradient(160deg, #0f172a, #1e293b);
}

/* Header */
.app-header {
    text-align: center;
    padding: 2.5rem 0 1.5rem;
}
.app-header h1 {
    font-size: 2.2rem;
    font-weight: 700;
    margin: 0;
    background: linear-gradient(135deg, #fff, #fdba74);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.app-header p {
    color: var(--muted);
    font-size: .95rem;
    margin: .3rem 0 0;
}

/* Tags */
.tag-wrap { display: flex; flex-wrap: wrap; gap: .4rem; margin: .5rem 0; }
.tag {
    background: rgba(249,115,22,0.15);
    border: 1px solid rgba(249,115,22,0.3);
    color: #fdba74;
    padding: .25rem .7rem;
    border-radius: 999px;
    font-size: .8rem;
    font-weight: 500;
}

/* Streamlit overrides */
.stTextInput > div > div > input {
    background: var(--card) !important;
    border: 1px solid var(--border) !important;
    color: var(--text) !important;
    border-radius: 10px !important;
}
.stTextInput > div > div > input:focus {
    border-color: var(--accent) !important;
    box-shadow: 0 0 0 2px rgba(249,115,22,0.2) !important;
}
.stSelectbox > div > div {
    background: var(--card) !important;
    border: 1px solid var(--border) !important;
    border-radius: 10px !important;
    color: var(--text) !important;
    transition: border-color .15s, box-shadow .15s;
}
.stSelectbox > div > div:focus-within,
.stSelectbox > div > div[aria-expanded="true"] {
    border-color: var(--accent) !important;
    box-shadow: 0 0 0 2px rgba(249,115,22,0.25) !important;
}
.stButton > button {
    width: 100%;
    background: linear-gradient(135deg, var(--accent), #ea580c) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 10px !important;
    padding: .7rem 1.2rem !important;
    font-weight: 600 !important;
    transition: transform .12s, box-shadow .12s !important;
}
.stButton > button:hover {
    transform: translateY(-1px) !important;
    box-shadow: 0 4px 16px rgba(249,115,22,0.4) !important;
}

/* Recipe result */
.recipe-box {
    background: var(--card);
    border: 1px solid rgba(249,115,22,0.15);
    border-radius: 14px;
    padding: 1.8rem;
    line-height: 1.7;
    color: var(--text);
    animation: fadeIn .35s ease;
}
.recipe-box h1, .recipe-box h2, .recipe-box h3,
.recipe-box strong { color: #fdba74; }
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to   { opacity: 1; transform: translateY(0); }
}

/* Footer */
.footer {
    text-align: center;
    color: var(--muted);
    font-size: .75rem;
    margin-top: 2.5rem;
    opacity: .6;
}

/* Hide chrome */
#MainMenu, footer, header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# ── Header ────────────────────────────────────────────────────────────
st.markdown("""
<div class="app-header">
    <h1>🍳 RecipeAI</h1>
    <p>Drop in your ingredients — get a recipe instantly.</p>
</div>
""", unsafe_allow_html=True)

# ── Ingredients ───────────────────────────────────────────────────────
ingredients = st.text_input(
    "Ingredients",
    placeholder="e.g. chicken, tomato, basil, garlic …",
    label_visibility="collapsed",
)

# ── Preferences ───────────────────────────────────────────────────────
c1, c2 = st.columns(2)
with c1:
    cuisine = st.selectbox("Cuisine", ["Any", "Indian", "Italian", "Mexican",
        "Chinese", "Japanese", "Thai", "French", "Mediterranean", "Korean"])
with c2:
    diet = st.selectbox("Diet", ["Any", "Vegetarian", "Vegan", "Non-Vegetarian",
        "Jain", "Keto", "Gluten-Free", "Pescatarian"])

# ── Generate ──────────────────────────────────────────────────────────
if st.button("✨ Generate Recipe", key="gen_btn", use_container_width=True):
    if not ingredients.strip():
        st.warning("Enter your ingredients first.")
    else:
        with st.spinner("Generating…"):
            try:
                prompt = f"""Generate one food recipe using: {ingredients.strip()}
Cuisine: {cuisine} | Diet: {diet}
Include: recipe name, prep/cook time, ingredients with quantities, numbered steps, a chef's tip.
Use markdown. Keep it under 200 words."""

                result = client.interactions.create(
                    model="gemini-3.5-flash-lite",
                    input=prompt,
                )
                st.markdown(
                    f'<div class="recipe-box">{result.output_text}</div>',
                    unsafe_allow_html=True,
                )
            except Exception as e:
                st.error(f"Something went wrong: {e}")

# ── Footer ────────────────────────────────────────────────────────────
st.markdown('<div class="footer">Powered by Gemini · Built with Streamlit</div>',
    unsafe_allow_html=True)
