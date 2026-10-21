import streamlit as st
from dotenv import load_dotenv
from google import genai
from google.genai import types
import os

# ── Configuration ────────────────────────────────────────────────────────────
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))

st.set_page_config(
    page_title="CineBot — Movie Recommender",
    page_icon="🎬",
    layout="centered",
)

# ── Custom CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

/* ── Global ─────────────────────────────────────────── */
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* ── Hide default Streamlit chrome ──────────────────── */
#MainMenu, footer {visibility: hidden;}

/* ── Hero header ────────────────────────────────────── */
.hero {
    text-align: center;
    padding: 2.5rem 1rem 1.2rem;
}
.hero h1 {
    font-size: 2.4rem;
    font-weight: 700;
    background: linear-gradient(135deg, #e64a19, #ff9800, #ffc107);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: .25rem;
}
.hero p {
    color: #9e9e9e;
    font-size: .95rem;
    margin-top: 0;
}

/* ── Chat bubbles ───────────────────────────────────── */
.stChatMessage {
    border-radius: 14px !important;
    margin-bottom: .5rem !important;
    backdrop-filter: blur(6px);
}

/* ── Sidebar polish ─────────────────────────────────── */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #1a1a2e 0%, #16213e 100%);
}
section[data-testid="stSidebar"] .stMarkdown h2,
section[data-testid="stSidebar"] .stMarkdown h3,
section[data-testid="stSidebar"] .stMarkdown p,
section[data-testid="stSidebar"] .stMarkdown li {
    color: #e0e0e0 !important;
}

/* ── Pill badge for conversation count ──────────────── */
.msg-count {
    display: inline-block;
    background: linear-gradient(135deg, #e64a19, #ff9800);
    color: #fff;
    font-size: .75rem;
    font-weight: 600;
    padding: 2px 10px;
    border-radius: 999px;
    margin-left: .4rem;
    vertical-align: middle;
}

/* ── Input area ─────────────────────────────────────── */
.stChatInput > div {
    border-radius: 12px !important;
}
</style>
""", unsafe_allow_html=True)

# ── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    msg_count = len(st.session_state.get("messages", []))
    st.markdown(
        f"## 🎬 CineBot &nbsp;<span class='msg-count'>{msg_count} msgs</span>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "Your witty AI movie buff — powered by **Gemini**.  \n"
        "Tell me what you love (or hate) and I'll find you the perfect film."
    )

    st.divider()

    st.markdown("### 💡 Try asking")
    st.markdown(
        "- *I love sci‑fi but hate horror — what should I watch?*\n"
        "- *Suggest a feel‑good movie for a rainy day*\n"
        "- *What's a good thriller from the 2010s?*\n"
        )

    st.divider()

    if st.button("🗑️  New Conversation", use_container_width=True):
        st.session_state.conversation = []
        st.session_state.messages = []
        st.rerun()

# ── Session state init ───────────────────────────────────────────────────────
if "conversation" not in st.session_state:
    st.session_state.conversation = []      # Gemini-formatted history
if "messages" not in st.session_state:
    st.session_state.messages = []          # Display-only history

# ── Gemini client (cached) ───────────────────────────────────────────────────
@st.cache_resource
def get_client():
    return genai.Client()

client = get_client()

SYSTEM_INSTRUCTION = "You are a witty movie buff who loves making puns."

# ── Chat function (mirrors notebook logic) ───────────────────────────────────
def chat(user_message: str) -> str:
    """Send a message and return the assistant reply, maintaining full history."""
    st.session_state.conversation.append(
        {"role": "user", "parts": [{"text": user_message}]}
    )

    config = types.GenerateContentConfig(
        system_instruction=SYSTEM_INSTRUCTION,
    )

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=st.session_state.conversation,
        config=config,
    )
    reply = response.text

    st.session_state.conversation.append(
        {"role": "model", "parts": [{"text": reply}]}
    )
    return reply

# ── Hero ─────────────────────────────────────────────────────────────────────
st.markdown(
    '<div class="hero">'
    "<h1>🍿 CineBot</h1>"
    "<p>A movie‑recommending chatbot with memory — it remembers what you love.</p>"
    "</div>",
    unsafe_allow_html=True,
)

# ── Render chat history ─────────────────────────────────────────────────────
for msg in st.session_state.messages:
    with st.chat_message(msg["role"], avatar="🎬" if msg["role"] == "assistant" else "🧑"):
        st.markdown(msg["content"])

# ── Handle user input ───────────────────────────────────────────────────────
if prompt := st.chat_input("Ask me about movies…"):
    # Show user message immediately
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="🧑"):
        st.markdown(prompt)

    # Get and display assistant reply
    with st.chat_message("assistant", avatar="🎬"):
        with st.spinner("Thinking…"):
            try:
                reply = chat(prompt)
            except Exception as e:
                reply = f"⚠️ Something went wrong: `{e}`"
        st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.rerun()
