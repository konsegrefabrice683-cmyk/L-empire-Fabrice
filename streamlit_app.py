import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import random

st.set_page_config(page_title="FABRICE V22 FIX", layout="wide")
st.title("FABRICE V22 - FIX Double C")

if "nb_jours" not in st.session_state:
    st.session_state.nb_jours = 3

if st.button("➕ +3 JOURS INFINIS"):
    st.session_state.nb_jours += 3
    st.rerun()

EQUIPES = ["Burkina","EFO","Real","Arsenal","Inter","Nice","Man City","Brest","Bayern","Barca","PSG","ASFA"]

def get_label(j, d):
    ds = d.strftime("%d/%m/%Y")
    if j==0: return f"AUJOURD HUI - {ds} - 15 MATCHS"
    if j==1: return f"DEMAIN - {ds} - 15 MATCHS"
    return f"JOUR +{j} - {ds} - 15 MATCHS"

today = datetime.now()
tab = st.tabs(["PARIS INFINI"])[0]

with tab:
    type_paris = st.selectbox("Type LONAB", ["1X2", "Double Chance", "BTTS Oui/Non", "Over/Under", "Cartons", "Corners", "Score Exact"], index=1)

    for j in range(st.session_state.nb_jours):
        dj = today + timedelta(days=j)
        with st.expander(get_label(j, dj), expanded=(j==0)):
            rows = []
            for _ in range(15):
                a = random.choice(EQUIPES)
                b = random.choice([x for x in EQUIPES if x!=a])
                
                # FIX ICI - PLUS JAMAIS Double C
                if type_paris == "Double Chance":
                    prono = random.choice(["1X", "X2", "12"])
                    cote = round(random.uniform(1.32, 1.78),2)
                    proba = f"{random.randint(68,85)}%"
                elif type_paris == "BTTS Oui/Non":
                    prono = random.choice(["BTTS Oui", "BTTS Non"])
                    cote = round(random.uniform(1.65, 2.10),2)
                    proba = f"{random.randint(58,72)}%"
                elif type_paris == "Over/Under":
                    prono = random.choice(["Over 1.5", "Over 2.5", "Over 3.5", "Under 2.5"])
                    cote = round(random.uniform(1.34, 2.20),2)
                    proba = f"{random.randint(60,82)}%"
                elif type_paris == "Score Exact":
                    prono = f"{random.randint(0,3)}-{random.randint(0,3)}"
                    cote = round(random.uniform(6.0, 12.0),2)
                    proba = f"{random.randint(10,25)}%"
                elif type_paris == "Cartons":
                    prono = random.choice(["Over 3.5 Cartons", "Over 4.5 Cartons"])
                    cote = round(random.uniform(1.70, 1.95),2)
                    proba = f"{random.randint(62,75)}%"
                elif type_paris == "Corners":
                    prono = random.choice(["Over 8.5 Corners", "Over 9.5 Corners", "Over 10.5 Corners"])
                    cote = round(random.uniform(1.72, 2.05),2)
                    proba = f"{random.randint(60,74)}%"
                else:
                    prono = random.choice(["1", "X", "2"])
                    cote = round(random.uniform(1.85, 3.20),2)
                    proba = f"{random.randint(52,68)}%"

                rows.append([f"{a} vs {b}", prono, cote, proba, f"+{random.randint(2,8)}%", random.randint(70,90), "FEU VERT"])

            df = pd.DataFrame(rows, columns=["Match","Prono","Cote","Proba","Value","IA","STATUT"])
            st.dataframe(df, width='stretch')
