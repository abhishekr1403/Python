import streamlit as st
from dotenv import load_dotenv
from google import genai
import time

# ── Load environment & initialise client ──────────────────────────────
load_dotenv()
client = genai.Client()

# ── Page config ───────────────────────────────────────────────────────
st.set_page_config(
    page_title="RecipeAI – Smart Recipe Generator",
    page_icon="🍳",
    layout="centered",
)

# ── Custom CSS ────────────────────────────────────────────────────────
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Playfair+Display:wght@700;800&display=swap');

    /* ── Global ───────────────────────────────── */
    :root {
        --accent: #f97316;
        --accent-dark: #ea580c;
        --bg-gradient-start: #0f172a;
        --bg-gradient-end: #1e293b;
        --card-bg: rgba(30, 41, 59, 0.65);
        --card-border: rgba(255, 255, 255, 0.08);
        --text-primary: #f1f5f9;
        --text-secondary: #94a3b8;
        --glass: rgba(255,255,255,0.04);
    }

    html, body, [data-testid="stApp"] {
        font-family: 'Inter', sans-serif;
        color: var(--text-primary);
    }

    [data-testid="stApp"] {
        background: linear-gradient(160deg, var(--bg-gradient-start) 0%, var(--bg-gradient-end) 100%);
    }

    /* ── Hero ─────────────────────────────────── */
    .hero-wrapper {
        position: relative;
        border-radius: 20px;
        overflow: hidden;
        margin-bottom: 2.2rem;
        box-shadow: 0 8px 32px rgba(0,0,0,0.45);
    }
    .hero-wrapper img {
        width: 100%;
        height: 260px;
        object-fit: cover;
        display: block;
        filter: brightness(0.55);
    }
    .hero-overlay {
        position: absolute;
        inset: 0;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        padding: 1rem;
        text-align: center;
        background: linear-gradient(180deg, rgba(15,23,42,0.1) 0%, rgba(15,23,42,0.75) 100%);
    }
    .hero-title {
        font-family: 'Playfair Display', serif;
        font-size: 2.6rem;
        font-weight: 800;
        color: #fff;
        margin: 0;
        text-shadow: 0 2px 12px rgba(0,0,0,0.5);
    }
    .hero-sub {
        font-size: 1.05rem;
        color: #cbd5e1;
        margin-top: .35rem;
        font-weight: 300;
        letter-spacing: .3px;
    }

    /* ── Glass card ───────────────────────────── */
    .glass-card {
        background: var(--card-bg);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid var(--card-border);
        border-radius: 16px;
        padding: 2rem 2rem 1.6rem;
        margin-bottom: 1.6rem;
        box-shadow: 0 4px 24px rgba(0,0,0,0.25);
    }
    .card-heading {
        font-size: 1.15rem;
        font-weight: 600;
        color: var(--text-primary);
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: .5rem;
    }

    /* ── Tags ─────────────────────────────────── */
    .tag-container {
        display: flex;
        flex-wrap: wrap;
        gap: .5rem;
        margin-top: .5rem;
    }
    .tag {
        display: inline-flex;
        align-items: center;
        gap: .35rem;
        background: linear-gradient(135deg, rgba(249,115,22,0.2), rgba(249,115,22,0.08));
        border: 1px solid rgba(249,115,22,0.35);
        color: #fdba74;
        padding: .3rem .75rem;
        border-radius: 999px;
        font-size: .82rem;
        font-weight: 500;
        letter-spacing: .2px;
        animation: fadeTag .3s ease;
    }
    @keyframes fadeTag {
        from { opacity: 0; transform: scale(0.85); }
        to   { opacity: 1; transform: scale(1); }
    }

    /* ── Streamlit overrides ──────────────────── */
    .stTextInput > div > div > input {
        background: var(--glass) !important;
        border: 1px solid var(--card-border) !important;
        color: var(--text-primary) !important;
        border-radius: 10px !important;
        padding: .65rem 1rem !important;
        font-size: .95rem !important;
    }
    .stTextInput > div > div > input:focus {
        border-color: var(--accent) !important;
        box-shadow: 0 0 0 2px rgba(249,115,22,0.25) !important;
    }
    .stSelectbox > div > div {
        background: var(--glass) !important;
        border: 1px solid var(--card-border) !important;
        border-radius: 10px !important;
        color: var(--text-primary) !important;
    }

    /* Button */
    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, var(--accent), var(--accent-dark)) !important;
        color: #fff !important;
        border: none !important;
        border-radius: 12px !important;
        padding: .75rem 1.4rem !important;
        font-size: 1.05rem !important;
        font-weight: 600 !important;
        letter-spacing: .3px;
        cursor: pointer;
        transition: transform .15s ease, box-shadow .15s ease !important;
    }
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(249,115,22,0.45) !important;
    }
    .stButton > button:active {
        transform: translateY(0) !important;
    }

    /* ── Recipe output ────────────────────────── */
    .recipe-output {
        background: linear-gradient(145deg, rgba(30,41,59,0.8), rgba(15,23,42,0.9));
        border: 1px solid rgba(249,115,22,0.2);
        border-radius: 16px;
        padding: 2rem;
        line-height: 1.75;
        color: var(--text-primary);
        box-shadow: 0 4px 24px rgba(0,0,0,0.3);
        animation: slideUp .45s ease;
    }
    .recipe-output h1, .recipe-output h2, .recipe-output h3,
    .recipe-output strong, .recipe-output b {
        color: #fdba74;
    }
    @keyframes slideUp {
        from { opacity: 0; transform: translateY(18px); }
        to   { opacity: 1; transform: translateY(0); }
    }

    /* ── Divider ──────────────────────────────── */
    .styled-divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(249,115,22,0.35), transparent);
        border: none;
        margin: 1.5rem 0;
    }

    /* ── Footer ───────────────────────────────── */
    .app-footer {
        text-align: center;
        color: var(--text-secondary);
        font-size: .78rem;
        margin-top: 2rem;
        padding-bottom: 1.5rem;
        opacity: .7;
    }

    /* Hide streamlit branding */
    #MainMenu, footer, header {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True,
)

# ── Hero banner ───────────────────────────────────────────────────────
hero_img_name = "recipe_hero_banner_1792521933932.png"
import os, base64, pathlib

# Try local directory first, then artifact directory as fallback
script_dir = pathlib.Path(__file__).resolve().parent
hero_full = script_dir / hero_img_name
if not hero_full.exists():
    artifact_dir = pathlib.Path(r"C:\Users\acer\.gemini\antigravity-ide\brain\5b854538-8460-44c6-8de0-226e42f7159e")
    hero_full = artifact_dir / hero_img_name

if hero_full.exists():
    img_bytes = hero_full.read_bytes()
    b64 = base64.b64encode(img_bytes).decode()
    st.markdown(
        f"""
        <div class="hero-wrapper">
            <img src="data:image/png;base64,{b64}" alt="Fresh ingredients">
            <div class="hero-overlay">
                <p class="hero-title">🍳 RecipeAI</p>
                <p class="hero-sub">Tell me what's in your kitchen — I'll craft the perfect recipe.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
else:
    st.markdown(
        """
        <div class="hero-wrapper" style="background:linear-gradient(135deg,#1e293b,#0f172a);height:200px;">
            <div class="hero-overlay">
                <p class="hero-title">🍳 RecipeAI</p>
                <p class="hero-sub">Tell me what's in your kitchen — I'll craft the perfect recipe.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ── Session state ─────────────────────────────────────────────────────
if "ingredients" not in st.session_state:
    st.session_state.ingredients = []

# ── Input card ────────────────────────────────────────────────────────
st.markdown('<div class="glass-card">', unsafe_allow_html=True)
st.markdown('<div class="card-heading">🥗 Your Ingredients</div>', unsafe_allow_html=True)

col_input, col_btn = st.columns([4, 1])
with col_input:
    new_ingredient = st.text_input(
        "Add ingredient",
        placeholder="e.g. chicken, tomato, basil …",
        label_visibility="collapsed",
        key="ingredient_input",
    )
with col_btn:
    add_clicked = st.button("➕ Add", key="add_btn", use_container_width=True)

if add_clicked and new_ingredient.strip():
    cleaned = new_ingredient.strip().title()
    if cleaned not in st.session_state.ingredients:
        st.session_state.ingredients.append(cleaned)
        st.rerun()

# Show tags
if st.session_state.ingredients:
    tags_html = "".join(
        f'<span class="tag">{ing}</span>' for ing in st.session_state.ingredients
    )
    st.markdown(f'<div class="tag-container">{tags_html}</div>', unsafe_allow_html=True)

    if st.button("🗑️ Clear all", key="clear_btn"):
        st.session_state.ingredients = []
        st.rerun()
else:
    st.markdown(
        '<p style="color:#64748b;font-size:.88rem;margin-top:.5rem;">No ingredients added yet. Start typing above!</p>',
        unsafe_allow_html=True,
    )

st.markdown("</div>", unsafe_allow_html=True)

# ── Preferences card ─────────────────────────────────────────────────
st.markdown('<div class="glass-card">', unsafe_allow_html=True)
st.markdown('<div class="card-heading">⚙️ Preferences</div>', unsafe_allow_html=True)

col_cuisine, col_diet = st.columns(2)
with col_cuisine:
    cuisine = st.selectbox(
        "Cuisine",
        ["Any", "Indian", "Italian", "Mexican", "Chinese", "Japanese",
         "Thai", "French", "Mediterranean", "American", "Korean"],
        index=0,
    )
with col_diet:
    diet = st.selectbox(
        "Diet",
        ["Any", "Vegetarian", "Vegan", "Non-Vegetarian", "Jain",
         "Keto", "Gluten-Free", "Pescatarian"],
        index=0,
    )

st.markdown("</div>", unsafe_allow_html=True)

# ── Generate button ──────────────────────────────────────────────────
st.markdown('<div class="styled-divider"></div>', unsafe_allow_html=True)

generate_clicked = st.button("✨ Generate Recipe", key="generate_btn", use_container_width=True)

# ── Recipe generation ────────────────────────────────────────────────
def generate_recipe(ingredients: list[str], cuisine: str, diet: str) -> str:
    """Call Gemini to generate a recipe."""
    prompt = f"""
    Generate one detailed food recipe using these ingredients: {', '.join(ingredients)}
    Cuisine: {cuisine}
    Diet: {diet}

    Format the recipe with:
    - A creative recipe name (as a heading)
    - Prep time and cook time
    - Full list of ingredients with quantities
    - Step-by-step instructions
    - A short chef's tip at the end

    Use markdown formatting for headings, bold text, and numbered lists.
    Keep it concise but complete (under 250 words).
    """
    interaction = client.interactions.create(
        model="gemini-3.8-flash",
        input=prompt,
    )
    return interaction.output_text


if generate_clicked:
    if not st.session_state.ingredients:
        st.warning("🫙 Please add at least one ingredient first!")
    else:
        with st.spinner(""):
            # Custom spinner message
            placeholder = st.empty()
            placeholder.markdown(
                '<p style="text-align:center;color:#fdba74;font-size:.95rem;">🔮 Crafting your recipe with AI magic…</p>',
                unsafe_allow_html=True,
            )
            try:
                recipe_text = generate_recipe(
                    st.session_state.ingredients, cuisine, diet
                )
                placeholder.empty()

                st.markdown(
                    f'<div class="recipe-output">{st.markdown.__module__ and ""}'
                    f"</div>",
                    unsafe_allow_html=True,
                )
                # Use native markdown for proper rendering inside a styled container
                st.markdown(
                    f"""<div class="recipe-output">\n\n{recipe_text}\n\n</div>""",
                    unsafe_allow_html=True,
                )

            except Exception as exc:
                placeholder.empty()
                st.error(f"⚠️ Something went wrong: {exc}")

# ── Footer ────────────────────────────────────────────────────────────
st.markdown(
    '<div class="app-footer">Powered by <strong>Gemini 3.8 Flash</strong> · Built with Streamlit</div>',
    unsafe_allow_html=True,
)
