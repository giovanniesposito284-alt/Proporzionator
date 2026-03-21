import streamlit as st
import base64
from datetime import datetime
import pandas as pd
from streamlit_gsheets import GSheetsConnection

def salva_richiesta(nome, messaggio):
    # Connessione a Google Sheets
    conn = st.connection("gsheets", type=GSheetsConnection)
    data_ora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    try:
        # worksheet="Foglio1" è il nome di default dei fogli Google
        existing_data = conn.read(worksheet="Foglio1", usecols=[0, 1, 2])
        existing_data = existing_data.dropna(how="all")
    except:
        existing_data = pd.DataFrame(columns=["Nome", "Messaggio", "Data"])

    nuova_riga = pd.DataFrame([{"Nome": nome, "Messaggio": messaggio, "Data": data_ora}])
    updated_df = pd.concat([existing_data, nuova_riga], ignore_index=True)
    
    conn.update(worksheet="Foglio1", data=updated_df)

st.set_page_config(
    page_title="Proporzionator",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

def check_password():
    def password_entered():
        if st.session_state["password"] == "Biscotto":
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Rimuove la password per sicurezza
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.markdown("<div style='text-align: center; margin-top: 100px;'><h2 style='color: white;'>🔒 Area Riservata</h2><p style='color: #ddd;'>Inserisci la password corretta per poter accedere all'app e calcolare i tuoi macronutrienti</p></div>", unsafe_allow_html=True)
        c1, c2, c3 = st.columns([1, 1, 1])
        with c2:
            st.text_input("🔑 Password", type="password", key="password", on_change=password_entered)
        return False
    elif not st.session_state["password_correct"]:
        st.markdown("<div style='text-align: center; margin-top: 100px;'><h2 style='color: white;'>🔒 Area Riservata</h2><p style='color: #ddd;'>Inserisci la password corretta per poter accedere all'app e calcolare i tuoi macronutrienti</p></div>", unsafe_allow_html=True)
        c1, c2, c3 = st.columns([1, 1, 1])
        with c2:
            st.text_input("🔑 Password", type="password", key="password", on_change=password_entered)
            st.error("❌ Password errata!")
        return False
    else:
        return True

if not check_password():
    st.stop()

#background logo
def get_image_as_base64(file):
    try:
        with open(file, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except:
        return ""

img = get_image_as_base64("background.jpg")

if img:
    logo_html = f"""
    <style>
    .logo-container {{
        position: absolute;
        top: 20px;
        right: 20px;
        z-index: 999999;
    }}
    .logo-img {{
        width: 160px;
        height: auto;
        border-radius: 12px;
        box-shadow: 0px 4px 6px rgba(0,0,0,0.3);
        transition: width 0.3s ease;
    }}
    @media (max-width: 768px) {{
        .logo-container {{
            top: 15px;
            right: 15px;
        }}
        .logo-img {{
            width: 80px;
            border-radius: 8px;
        }}
    }}
    </style>
    <div class="logo-container">
        <img src="data:image/jpeg;base64,{img}" class="logo-img">
    </div>
    """
    st.markdown(logo_html, unsafe_allow_html=True)

st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background-color: #0e1117;
}
[data-testid="stHeader"] {
    background-color: rgba(14, 17, 23, 0);
}

/* Rimpicciolisce il contenitore app del 30% solo su desktop (PC) e lo allinea a sinistra */
@media (min-width: 1024px) {
    .block-container {
        max-width: 70% !important;
        margin-left: 0 !important; /* Forza l'abbandono della centratura nativa */
        padding-left: 3rem !important;
    }
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    """
    <div style="text-align: left; margin-top: 10px; margin-bottom: 30px;">
        <h1 style="color: white; font-size: 40px; text-shadow: 2px 2px 4px rgba(0,0,0,0.6); margin-bottom: 0px;">⚖️ Proporzionator</h1>
        <p style="color: #eeeeee; font-size: 16px; text-shadow: 1px 1px 3px rgba(0,0,0,0.5);">Calcola le tue proporzioni in modo semplice e veloce!</p>
    </div>
    """, unsafe_allow_html=True
)

carboidrati = {
    "Biscotti Plasmon": 85,
    "Cereali non glassati": 80,
    "Cous Cous ": 80,
    "Crackers integrali": 105,
    "Farina d'avena": 100,
    "Farro": 95,
    "Gallette di riso": 77,
    "Gnocchi": 250,
    "Muslei": 90,
    "Pane": 135,
    "Pane integrale": 135,
    "Pasta all'uovo": 110,
    "Pasta bianca": 90,
    "Pasta fresca": 115,
    "Pasta integrale": 100,
    "Patate": 400,
    "Piadina integrale": 112.5,
    "Riso basmati": 80,
    "Riso bianco": 80,
    "Riso integrale": 84
}

proteine = {
    "Albume": 200,
    "Branzino": 140,
    "Bresaola": 65,
    "Carne rossa magra": 113,
    "Cozze": 180,
    "Fesa di tacchino": 120,
    "Feta greca": 150,
    "Fiocchi di latte": 200,
    "Gamberi sgusciati": 170,
    "Grana Padano 48 mesi": 70,
    "Latte proteico": 250,
    "Merluzzo": 160,
    "Pesce spada": 110,
    "Petto di pollo": 100,
    "Prosciutto cotto": 110,
    "Prosciutto crudo sgrassato": 75,
    "Salmone": 120,
    "Shaker": 15,
    "Skyr": 250,
    "Speck": 75,
    "Tonno fresco": 110,
    "Tonno in scatola al naturale": 110,
    "Total 0": 230,
    "Uova": 190,
    "Yogurt greco": 350
}

grassi = {
    "Avocado": 60,
    "Burro di arachidi": 18,
    "Cioccolato fondente al 80%": 19,
    "Mandorle": 18,
    "Noci": 15,
    "Olio extravergine di oliva": 9.1,
    "Pesto di pistacchi": 14,
    "Pistacchio": 16
}

def create_section(title, singular_title, icon, color, data_dict, key_suffix):
    st.markdown(f'''
        <div style="
            display: flex;
            align-items: center;
            background: linear-gradient(135deg, {color}dd, {color}ff);
            color: white;
            padding: 8px 16px;
            border-radius: 10px;
            font-size: 24px;
            font-weight: bold;
            margin-top: 10px;
            margin-bottom: 25px;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.5);
        ">
            <span style="font-size: 30px; margin-right: 15px; text-shadow: 2px 2px 4px rgba(0,0,0,0.4);">{icon}</span>
            {title}
        </div>
    ''', unsafe_allow_html=True)
    
    c_ref, c_qty, c_target, spacer = st.columns([3, 2, 3, 4])
    
    with c_ref:
        ref_item = st.selectbox(
            f"🔍 Quale {singular_title} di riferimento?",
            list(data_dict.keys()),
            key=f"ref_{key_suffix}"
        )
    with c_qty:
        qty = st.number_input(
            "⚖️ Quanti grammi?",
            min_value=5,
            max_value=3000,
            step=5,
            value=100,
            key=f"qty_{key_suffix}"
        )
        
    with c_target:
        target_item = st.selectbox(
            f"🍽️ Quale {singular_title} vuoi?",
            list(data_dict.keys()),
            key=f"target_{key_suffix}"
        )
        
    qty_res = (data_dict[target_item] * qty) / data_dict[ref_item]
    
    st.markdown(f'''
        <div style="
            display: flex;
            align-items: center;
            justify-content: center;
            background-color: rgba(30, 30, 30, 0.8);
            color: #ffffff;
            padding: 14px 30px;
            border-radius: 10px;
            border-left: 8px solid {color};
            font-size: 18px;
            font-weight: bold;
            margin: 28px auto 0 auto;
            width: fit-content;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.5);
            backdrop-filter: blur(5px);
        ">
            🎯 Devi mangiare <span style="color: {color}; margin: 0 8px; font-size: 24px; text-shadow: 1px 1px 2px rgba(0,0,0,0.8);">{qty_res:.0f} gr.</span>
        </div>
    ''', unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)

create_section("Carboidrati", "carboidrato", "🍞", "#FF9800", carboidrati, "carbs")
create_section("Proteine", "proteina", "🥩", "#E53935", proteine, "prot")
create_section("Grassi", "grasso", "🥑", "#43A047", grassi, "fat")

st.markdown("<br><hr style='border: 1px solid #444;'><br>", unsafe_allow_html=True)

st.markdown(f'''
    <div style="
        display: flex;
        align-items: center;
        background: linear-gradient(135deg, #1f77b4dd, #1f77b4ff);
        color: white;
        padding: 8px 16px;
        border-radius: 10px;
        font-size: 24px;
        font-weight: bold;
        margin-top: 10px;
        margin-bottom: 25px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.5);
    ">
        <span style="font-size: 30px; margin-right: 15px; text-shadow: 2px 2px 4px rgba(0,0,0,0.4);">📩</span>
        Hai delle richieste o suggerimenti?
    </div>
''', unsafe_allow_html=True)

with st.form("richiesta_alimenti_form", clear_on_submit=True):
    st.markdown("<p style='color: #eeeeee; font-size: 16px;'>Non trovi un alimento nella lista? Scrivici la tua richiesta qui sotto e cercheremo di aggiungerlo presto!</p>", unsafe_allow_html=True)
    nome = st.text_input("Il tuo nome (opzionale)")
    messaggio = st.text_area("Scrivi qui la tua richiesta o i suggerimenti...", height=100)
    submitted = st.form_submit_button("Invia Richiesta")
    if submitted:
        if messaggio.strip():
            salva_richiesta(nome, messaggio)
            st.success("✅ Grazie! La tua richiesta è stata salvata correttamente nel database.")
        else:
            st.warning("⚠️ Scrivi qualcosa prima di inviare!")
