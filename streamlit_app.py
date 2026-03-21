import streamlit as st

st.set_page_config(
    page_title="Proporzionator",
    page_icon=":guardsman:",
    layout="wide",
    initial_sidebar_state="expanded"
)

#background 
def get_image_as_base64(file):
    import base64
    with open(file, "rb") as f:
        data = f.read()
        
    return base64.b64encode(data).decode()

img = get_image_as_base64("background.jpg")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: linear-gradient(rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.4)), url("data:image/jpeg;base64, {img}");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
    background-position: center;
}}
[data-testid="stHeader"] {{
    background-color: rgba(0, 0, 0, 0);
}}
[data-testid="stToolbar"] {{
    right: 2rem;
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)



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

st.markdown(
    """
    <div style="
        display:inline-block;
        background-color:#000000;
        color:white;
        padding:6px 12px;
        border-radius:6px;
        font-size:32px;
        font-weight:bold;
    ">
        Carboidrati
    </div>
    """,
    unsafe_allow_html=True
)

# Colonne sotto il titolo
c1, c2, c3 = st.columns([10, 5, 10])

with c1:
    selected_carboidrati = st.selectbox(
        "Quale carboidrato di riferimento?",
        carboidrati.keys(),
        key="carboidrati"
    )
    sel_qty = st.number_input(
        "Quanti grammi?",
        min_value=5,
        max_value=3000,
        step=5,
        key="carboidrati1"
    )
with c3:
    selected_variante_carboidrati = st.selectbox(
        "Quale carboidrato vuoi?",
        carboidrati.keys(),
        key="carboidrati2"
    )

qty_res =  (carboidrati[selected_variante_carboidrati] * sel_qty) / carboidrati[selected_carboidrati]
c1,c2 = st.columns([2,1])
with c2:
     st.markdown(f"""
    <div style="
        display:inline-block;
        background-color:#1f77b4;
        color:white;
        padding:4px 8px;
        border-radius:4px;
        font-size:24px;
        font-weight:bold;">
        Devi mangiare {qty_res:.0f} gr.
    </div>
""", unsafe_allow_html=True)
    
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

st.title("Proteine")
c1,c2,c3 = st.columns([10, 5, 10])

with c1:
    selected_proteine = st.selectbox(
        "Quale è la proteina di riferimento?",
        proteine.keys(),
        key="proteine"
    )
    sel_qty = st.number_input(
        "Quanti grammi?",
        min_value=5,
        max_value=3000,
        step=5,
        key="proteine1"
    )
with c3:
    selected_variante_proteine = st.selectbox(
        "Quale proteina vuoi?",
        proteine.keys(),
        key="proteine2"
    )

qty_res =  (proteine[selected_variante_proteine] * sel_qty) / proteine[selected_proteine]
c1,c2 = st.columns([2,1])
with c2:
     st.markdown(f"""
    <div style="
        display:inline-block;
        background-color:#1f77b4;
        color:white;
        padding:4px 8px;
        border-radius:4px;
        font-size:24px;
        font-weight:bold;">
        Devi mangiare {qty_res:.0f} gr.
    </div>
""", unsafe_allow_html=True)
    
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

st.title("Grassi")
c1,c2,c3 = st.columns([10, 5, 10])

with c1:
    selected_grassi = st.selectbox(
        "Quale è il grasso di riferimento?",
        grassi.keys(),
        key="grassi"
    )
    sel_qty = st.number_input(
        "Quanti grammi?",
        min_value=5,
        max_value=3000,
        step=5,
        key="grassi1"
    )
with c3:
    selected_variante_grassi = st.selectbox(
        "Quale grasso vuoi?",
        grassi.keys(),
        key="grassi2"
    )

qty_res =  (grassi[selected_variante_grassi] * sel_qty) / grassi[selected_grassi]
c1,c2 = st.columns([2,1])
with c2:
   st.markdown(f"""
    <div style="
        display:inline-block;
        background-color:#1f77b4;
        color:white;
        padding:4px 8px;
        border-radius:4px;
        font-size:24px;
        font-weight:bold;">
        Devi mangiare {qty_res:.0f} gr.
    </div>
""", unsafe_allow_html=True)

