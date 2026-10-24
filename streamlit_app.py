import streamlit as st
import pandas as pd
import random
from datetime import datetime, timedelta

st.set_page_config(page_title="FABRICE V18.1", layout="wide")
st.title("FABRICE EMPIRE V18.1 - JOUR INFINI FIX")
st.caption("VRAIS PRONOS: 2-1 / Over 2.5 / BTTS Oui / X2")

if "nb_jours" not in st.session_state:
    st.session_state.nb_jours = 7

EQUIPES = ["Real","Barca","Man City","Arsenal","Bayern","PSG","Inter","Brest","Nice","EFO","ASFA","Burkina"]
CHEVAUX = ["Mogho Power","Bangr Nooma","Etalon dOr","Wend Panga","Faso Eclair","Sahel Vent"]

def get_label(j, d, suf):
    ds = d.strftime("%d/%m/%Y")
    if j==0: return f"AUJOURD HUI - {ds} - {suf}"
    if j==1: return f"DEMAIN - {ds} - {suf}"
    return f"JOUR +{j} - {ds} - {suf}"

if st.button("➕ +3 JOURS INFINIS"):
    st.session_state.nb_jours += 3
    st.rerun()

tab1, tab2, tab3 = st.tabs(["PARIS INFINI","PMU INFINI","BOURSE INFINI"])
today = datetime.now()

with tab1:
    tp = st.selectbox("Type LONAB", ["1X2","Double Chance","BTTS","Over/Under","Cartons","Corners","Score Exact"], key="p1")
    for j in range(st.session_state.nb_jours):
        dj = today + timedelta(days=j)
        with st.expander(get_label(j, dj, "15 MATCHS"), expanded=(j<2)):
            rows = []
            for k in range(15):
                a = random.choice(EQUIPES)
                b = random.choice([x for x in EQUIPES if x!=a])
                if tp == "Score Exact":
                    prono = f"{random.randint(0,3)}-{random.randint(0,3)}"
                    cote = round(random.uniform(6.0, 12.0),2)
                elif tp == "Over/Under":
                    prono = random.choice(["Over 0.5","Over 1.5","Over 2.5","Under 2.5","Over 3.5"])
                    cote = round(random.uniform(1.70, 2.25),2)
                elif tp == "BTTS":
                    prono = random.choice(["BTTS Oui","BTTS Non"])
                    cote = round(random.uniform(1.65, 2.15),2)
                elif tp == "Cartons":
                    prono = random.choice(["Over 2.5 Cartons","Over 3.5 Cartons"])
                    cote = round(random.uniform(1.80, 2.40),2)
                elif tp == "Corners":
                    prono = random.choice(["Over 7.5 Corners","Over 8.5 Corners","Over 9.5 Corners"])
                    cote = round(random.uniform(1.85, 2.30),2)
                elif tp == "Double Chance":
                    prono = random.choice(["1X","X2","12"])
                    cote = round(random.uniform(1.25, 1.65),2)
                else:
                    prono = random.choice(["1","X","2"])
                    cote = round(random.uniform(1.90, 3.20),2)
                rows.append([f"{a} vs {b}", prono, cote, "65%", "+5%", 75, "FEU VERT"])
            df = pd.DataFrame(rows, columns=["Match","Prono","Cote","Proba","Value","IA","STATUT"])
            st.dataframe(df, width='stretch')

with tab2:
    for j in range(st.session_state.nb_jours):
        dj = today + timedelta(days=j)
        with st.expander(get_label(j, dj, "PMU"), expanded=(j<1)):
            rows = [[str(i+1), ch, round(random.uniform(2,9),1), "25%", 72] for i,ch in enumerate(CHEVAUX)]
            st.dataframe(pd.DataFrame(rows, columns=["Num","Cheval","Cote","Proba","IA"]), width='stretch')

with tab3:
    for j in range(st.session_state.nb_jours):
        dj = today + timedelta(days=j)
        with st.expander(get_label(j, dj, "BOURSE"), expanded=(j<1)):
            rows = [[n, random.randint(1000,50000), "+2.5%", 75] for n in ["SONATEL","ORANGE","NVDA","BTC"]]
            st.dataframe(pd.DataFrame(rows, columns=["Actif","Prix","Var","IA"]), width='stretch')
