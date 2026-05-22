import streamlit as st
import pandas as pd
import numpy as np
import joblib

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="🚀",
    layout="wide"
)

# ================= LOAD MODEL =================
@st.cache_resource
def load_model():
    model = joblib.load("Logistic (1).pkl")
    return model

model = load_model()

# ================= CUSTOM CSS =================
st.markdown("""
<style>

.stApp {
    background: linear-gradient(to right,#0f172a,#1e293b);
    color: white;
}

.main-title {
    text-align:center;
    font-size:55px;
    font-weight:bold;
    color:#38bdf8;
}

.sub-title {
    text-align:center;
    font-size:20px;
    color:#cbd5e1;
    margin-bottom:30px;
}

.card {
    background: rgba(255,255,255,0.08);
    padding:25px;
    border-radius:20px;
    backdrop-filter: blur(12px);
    box-shadow: 0 8px 32px rgba(0,0,0,0.3);
    margin-bottom:20px;
}

.stButton>button {
    width:100%;
    background: linear-gradient(90deg,#06b6d4,#3b82f6);
    color:white;
    border:none;
    border-radius:12px;
    height:55px;
    font-size:20px;
    font-weight:bold;
    transition:0.3s;
}

.stButton>button:hover {
    transform:scale(1.02);
}

.result-box {
    padding:30px;
    border-radius:18px;
    text-align:center;
    font-size:30px;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# ================= HEADER =================
st.markdown('<p class="main-title">📊 Customer Churn Prediction</p>', unsafe_allow_html=True)

st.markdown(
    '<p class="sub-title">AI Powered Interactive Dashboard using Machine Learning</p>',
    unsafe_allow_html=True
)

# ================= SIDEBAR =================
with st.sidebar:

    st.title("⚙️ Customer Settings")

    gender = st.selectbox("Gender", ["Male", "Female"])

    senior = st.selectbox(
        "Senior Citizen",
        [0,1]
    )

    partner = st.selectbox(
        "Partner",
        ["Yes","No"]
    )

    dependents = st.selectbox(
        "Dependents",
        ["Yes","No"]
    )

    tenure = st.slider(
        "Tenure",
        0,
        72,
        12
    )

    monthly_charges = st.slider(
        "Monthly Charges",
        0,
        150,
        70
    )

    total_charges = st.slider(
        "Total Charges",
        0,
        10000,
        1000
    )

# ================= MAIN COLUMNS =================
col1, col2 = st.columns([1.3,1])

# ================= LEFT SIDE =================
with col1:

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("👤 Customer Information")

    phone_service = st.selectbox(
        "Phone Service",
        ["Yes","No"]
    )

    internet_service = st.selectbox(
        "Internet Service",
        ["DSL","Fiber optic","No"]
    )

    contract = st.selectbox(
        "Contract Type",
        ["Month-to-month","One year","Two year"]
    )

    payment_method = st.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer",
            "Credit card"
        ]
    )

    paperless = st.selectbox(
        "Paperless Billing",
        ["Yes","No"]
    )

    st.markdown("</div>", unsafe_allow_html=True)

# ================= RIGHT SIDE =================
with col2:

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("📈 Live Dashboard")

    st.metric(
        "💰 Monthly Charges",
        f"₹ {monthly_charges}"
    )

    st.metric(
        "📅 Tenure",
        f"{tenure} Months"
    )

    st.metric(
        "💵 Total Charges",
        f"₹ {total_charges}"
    )

    risk = (
        "🔴 High"
        if monthly_charges > 80
        else "🟡 Moderate"
        if monthly_charges > 50
        else "🟢 Low"
    )

    st.progress(monthly_charges)

    st.write(f"### Churn Risk: {risk}")

    st.markdown("</div>", unsafe_allow_html=True)

# ================= INPUT DATA =================
input_df = pd.DataFrame({

    'gender':[gender],
    'SeniorCitizen':[senior],
    'Partner':[partner],
    'Dependents':[dependents],
    'tenure':[tenure],
    'PhoneService':[phone_service],
    'InternetService':[internet_service],
    'Contract':[contract],
    'PaperlessBilling':[paperless],
    'PaymentMethod':[payment_method],
    'MonthlyCharges':[monthly_charges],
    'TotalCharges':[total_charges]

})

# ================= PREDICTION =================
if st.button("🚀 Predict Customer Churn"):

    st.balloons()

    try:

        prediction = model.predict(input_df)

        if prediction[0] == 1:

            st.markdown(
                """
                <div class="result-box"
                style="background:#7f1d1d;color:#fecaca;">
                ❌ Customer is likely to CHURN
                </div>
                """,
                unsafe_allow_html=True
            )

        else:

            st.markdown(
                """
                <div class="result-box"
                style="background:#052e16;color:#bbf7d0;">
                ✅ Customer is likely to STAY
                </div>
                """,
                unsafe_allow_html=True
            )

    except Exception as e:

        st.error(f"Error: {e}")

# ================= FOOTER =================
st.markdown("---")

st.markdown(
    """
    <center>
    <h3>✨ Built with Streamlit + Machine Learning</h3>
    <p>Interactive Customer Churn Prediction Dashboard</p>
    </center>
    """,
    unsafe_allow_html=True
)

# ================= CUSTOM CSS =================
st.markdown("""
<style>

/* Background Animation */
.stApp {
    background: linear-gradient(-45deg, #0f172a, #1e293b, #0f766e, #1d4ed8);
    background-size: 400% 400%;
    animation: gradientBG 12s ease infinite;
    color: white;
    font-family: 'Poppins', sans-serif;
}

@keyframes gradientBG {
    0% {background-position:0% 50%;}
    50% {background-position:100% 50%;}
    100% {background-position:0% 50%;}
}

/* Main Title */
.main-title {
    text-align:center;
    font-size:60px;
    font-weight:800;
    background: linear-gradient(to right,#38bdf8,#22d3ee,#818cf8);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
    margin-bottom:10px;
}

/* Subtitle */
.sub-title {
    text-align:center;
    font-size:20px;
    color:#e2e8f0;
    margin-bottom:35px;
}

/* Glass Card */
.card {
    background: rgba(255,255,255,0.10);
    padding:30px;
    border-radius:24px;
    backdrop-filter: blur(14px);
    border:1px solid rgba(255,255,255,0.2);
    box-shadow: 0 8px 32px rgba(0,0,0,0.35);
    margin-bottom:20px;
    transition:0.3s;
}

.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 40px rgba(0,0,0,0.4);
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: rgba(15,23,42,0.9);
    border-right:1px solid rgba(255,255,255,0.1);
}

/* Input Boxes */
.stSelectbox div[data-baseweb="select"] {
    border-radius:12px;
}

.stSlider {
    padding-top:15px;
}

/* Button */
.stButton>button {
    width:100%;
    background: linear-gradient(90deg,#06b6d4,#3b82f6,#8b5cf6);
    color:white;
    border:none;
    border-radius:15px;
    height:60px;
    font-size:22px;
    font-weight:bold;
    transition:0.3s;
    box-shadow:0 6px 20px rgba(59,130,246,0.4);
}

.stButton>button:hover {
    transform:scale(1.03);
    box-shadow:0 8px 25px rgba(139,92,246,0.6);
}

/* Result Box */
.result-box {
    padding:35px;
    border-radius:20px;
    text-align:center;
    font-size:32px;
    font-weight:bold;
    margin-top:20px;
    animation: fadeIn 0.6s ease-in-out;
}

@keyframes fadeIn {
    from {
        opacity:0;
        transform:translateY(20px);
    }
    to {
        opacity:1;
        transform:translateY(0px);
    }
}

/* Metrics */
[data-testid="metric-container"] {
    background: rgba(255,255,255,0.08);
    border-radius:18px;
    padding:15px;
    border:1px solid rgba(255,255,255,0.1);
}

/* Footer */
footer {
    visibility:hidden;
}

</style>
""", unsafe_allow_html=True)







## stramilt krne ke liye pahle karte hai app.py file banate hai fir ui code fir run karte hai nerw terminal me jate hai 
# fir streamilt run app.py run karte hai streamilt diploy ho jat ahi