import math
import streamlit as st

# ------------------------------------------------------------
# Seiten-Konfiguration
# ------------------------------------------------------------
st.set_page_config(
    page_title="Wardogs Mörser Rechner",
    page_icon="🐺",
    layout="centered",
)

# ------------------------------------------------------------
# Custom CSS – "Wardogs" Militär-Look
# ------------------------------------------------------------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Oswald:wght@500;700&family=Share+Tech+Mono&display=swap');

    .stApp {
        background: radial-gradient(circle at top, #1b1f17 0%, #0c0e0a 70%);
        color: #d8d8c8;
        font-family: 'Share Tech Mono', monospace;
    }

    h1, h2, h3 {
        font-family: 'Oswald', sans-serif !important;
        letter-spacing: 2px;
        text-transform: uppercase;
    }

    .wd-header {
        text-align: center;
        padding: 1.2rem 0 0.5rem 0;
        border-bottom: 2px solid #6b7a3a;
        margin-bottom: 1.5rem;
    }
    .wd-title {
        font-size: 2.4rem;
        font-weight: 700;
        color: #b8c46a;
        margin-bottom: 0;
    }
    .wd-subtitle {
        color: #8a9a5b;
        font-size: 0.95rem;
        letter-spacing: 4px;
    }

    div[data-testid="stNumberInput"] label {
        color: #b8c46a !important;
        font-weight: bold;
        letter-spacing: 1px;
    }

    .stButton>button {
        background-color: #4a5a23;
        color: #eef0d8;
        border: 1px solid #8a9a5b;
        border-radius: 4px;
        font-family: 'Oswald', sans-serif;
        text-transform: uppercase;
        letter-spacing: 2px;
        width: 100%;
        padding: 0.6rem 0;
    }
    .stButton>button:hover {
        background-color: #6b7a3a;
        border-color: #b8c46a;
        color: #0c0e0a;
    }

    .wd-result {
        background-color: #1b1f17;
        border: 2px solid #8a9a5b;
        border-radius: 6px;
        padding: 1.2rem;
        text-align: center;
        margin-top: 1.5rem;
    }
    .wd-result-value {
        font-size: 2.6rem;
        color: #e2c94c;
        font-weight: bold;
    }
    .wd-result-label {
        color: #8a9a5b;
        letter-spacing: 3px;
        font-size: 0.85rem;
    }

    .wd-footer {
        text-align: center;
        margin-top: 3rem;
        padding-top: 1rem;
        border-top: 1px solid #3a3f2e;
        color: #6b6b5a;
        font-size: 0.85rem;
    }
    .wd-footer a {
        color: #8a9a5b;
        text-decoration: none;
        font-weight: bold;
    }
    .wd-footer a:hover {
        color: #e2c94c;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ------------------------------------------------------------
# Header
# ------------------------------------------------------------
st.markdown(
    """
    <div class="wd-header">
        <div class="wd-title">🐺 WARDOGS</div>
        <div class="wd-subtitle">MÖRSER · DISTANZRECHNER</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.write(
    "Gib die Koordinaten von **Ziel** und **Mörser** ein, um die Distanz zu berechnen."
)

# ------------------------------------------------------------
# Eingabe
# ------------------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    st.markdown("**🎯 Ziel**")
    x_ziel = st.number_input("X Ziel", value=0.0, format="%.2f", key="x_ziel")
    y_ziel = st.number_input("Y Ziel", value=0.0, format="%.2f", key="y_ziel")

with col2:
    st.markdown("**💣 Mörser**")
    x_moerser = st.number_input("X Mörser", value=0.0, format="%.2f", key="x_moerser")
    y_moerser = st.number_input("Y Mörser", value=0.0, format="%.2f", key="y_moerser")

# ------------------------------------------------------------
# Berechnung
# ------------------------------------------------------------
if st.button("Distanz berechnen"):
    distanz = math.sqrt((x_ziel - x_moerser) ** 2 + (y_ziel - y_moerser) ** 2) / 100

    st.markdown(
        f"""
        <div class="wd-result">
            <div class="wd-result-label">BERECHNETE DISTANZ</div>
            <div class="wd-result-value">{distanz:.2f}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ------------------------------------------------------------
# Footer / Discord
# ------------------------------------------------------------
st.markdown(
    """
    <div class="wd-footer">
        Wardogs Tool · gebaut für den Einsatz von Tescol<br>
        Join uns auf Discord: <a href="https://discord.gg/DEIN-INVITE-LINK" target="_blank">Placeholder</a>
    </div>
    """,
    unsafe_allow_html=True,
)
