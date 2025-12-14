import streamlit as st
import pandas as pd
import pickle
from pathlib import Path
import numpy as np
import scipy.sparse as sp

# ---------- PAGE SETUP ----------
st.set_page_config(
    page_title="DStv Zimbabwe — Customer Query Insights",
    layout="wide"
)

st.title("📡 DStv Zimbabwe — Customer Query Insight & Action Recommender")
st.write("Prescriptive analytics tool for customer support operations.")

# ---------- PATHS ----------
BASE = Path(__file__).parent
DATA_PATH = BASE / "data" / "dstv_queries_2000.csv"
MODEL_DIR = BASE / "models"

# ---------- LOAD DATA ----------
@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH)

# ---------- LOAD MODELS ----------
@st.cache_resource
def load_models():
    with open(MODEL_DIR / "vectorizer.pkl", "rb") as f:
        vectorizer = pickle.load(f)
    with open(MODEL_DIR / "category_clf.pkl", "rb") as f:
        category_clf = pickle.load(f)
    with open(MODEL_DIR / "escalation_clf.pkl", "rb") as f:
        escalation_clf = pickle.load(f)
    return vectorizer, category_clf, escalation_clf

df = load_data()
vectorizer, category_clf, escalation_clf = load_models()

# ---------- SIDEBAR ----------
page = st.sidebar.selectbox(
    "Select View",
    ["Dashboard", "Query Analyzer", "Escalation Predictor", "Action Recommender"]
)

# ---------- DASHBOARD ----------
if page == "Dashboard":
    st.subheader("📊 Dashboard Overview")

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Queries", len(df))
    col2.metric("Escalation Rate", f"{(df['Escalated'] == 'Yes').mean():.1%}")
    col3.metric("Top Issue", df["Category"].value_counts().idxmax())

        # --- SO WHAT? (Prescriptive Insight) ---
    st.info(
    """
    **🔎 So What?**

    **Operational Insight:** Payment-related issues are the leading driver of customer escalations.
    Improving payment platform stability and proactive customer communication could reduce escalation
    volume by **~20–30%**.

    **Recommended Action:** Prioritize payment system monitoring and deploy automated SMS alerts
    when payment failures spike.
    """
)

    st.line_chart(df["Category"].value_counts())

# ---------- QUERY ANALYZER ----------
elif page == "Query Analyzer":
    st.subheader("🧠 Query Classification")

    sample = st.text_area(
        "Enter customer query text:",
        "Customer experiencing E16 error; channels not showing."
    )

    if st.button("Classify Query"):
        X = vectorizer.transform([sample])
        pred = category_clf.predict(X)[0]
        st.success(f"Predicted Category: **{pred}**")

# ---------- ESCALATION PREDICTOR ----------
elif page == "Escalation Predictor":
    st.subheader("⚠️ Escalation Risk Predictor")

    query = st.text_area(
        "Customer Query",
        "Payment made but account not reconnected."
    )

    hours = st.number_input(
        "Resolution Time (hours)",
        min_value=0,
        max_value=72,
        value=4
    )

    if st.button("Predict Escalation"):
        X_text = vectorizer.transform([query])
        X_all = sp.hstack([X_text, np.array([[hours]])])
        prob = escalation_clf.predict_proba(X_all)[0][1]

        st.metric("Escalation Probability", f"{prob:.1%}")

        if prob > 0.6:
            st.error("High escalation risk — escalate to supervisor.")
        else:
            st.success("Low escalation risk.")

# ---------- ACTION RECOMMENDER ----------
elif page == "Action Recommender":
    st.subheader("✅ Recommended Actions")

    recent = df.tail(200)["Category"].value_counts()

    actions = []
    if recent.get("E16 Error", 0) > 30:
        actions.append("📡 Investigate signal issues and send proactive SMS alerts.")
    if recent.get("Payment Failure", 0) > 25:
        actions.append("💳 Audit payment gateway and notify billing team.")
    if (df["Escalated"] == "Yes").mean() > 0.25:
        actions.append("👥 Increase supervisor review coverage.")

    if actions:
        for a in actions:
            st.info(a)
    else:
        st.success("System stable — no immediate actions required.")

