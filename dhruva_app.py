import streamlit as st
import pandas as pd
import datetime

# 1. PAGE CONFIG
st.set_page_config(
    page_title="D.H.R.U.V.A. | National Anomaly Research",
    page_icon="🦅",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- DATABASE CONNECTION (PERMANENT) ---
conn = None
try:
    from streamlit_gsheets import GSheetsConnection
    conn = st.connection("gsheets", type=GSheetsConnection)
except Exception:
    st.warning("Database Connection Pending... Design is Active.")

# 2. IPS PREMIUM CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Raleway:wght@300;400&display=swap');
    .stApp { background-color: #000000; color: #FFFFFF; font-family: 'Raleway', sans-serif; }
    .stTabs [data-baseweb="tab-list"] { background-color: #0A0A0A; border-bottom: 1px solid #111; justify-content: center; }
    .stTabs [data-baseweb="tab"] { color: #888 !important; font-weight: bold; font-size: 14px; letter-spacing: 1px;}
    .stTabs [aria-selected="true"] { color: #00D4FF !important; border-bottom: 2px solid #00D4FF; }
    .ips-title { font-family: 'Cinzel', serif; font-size: 55px; text-align: center; letter-spacing: 5px; margin-bottom: 0; color: #FFFFFF; }
    .ips-subtitle { font-family: 'Raleway', sans-serif; font-size: 14px; text-align: center; letter-spacing: 4px; color: #00D4FF; text-transform: uppercase; margin-bottom: 30px; }
    .ips-block { background-color: #0A0A0A; border-left: 3px solid #00D4FF; padding: 30px; margin: 30px 0; }
    .protocol-section { border: 1px solid #7B0000; padding: 25px; background-color: #050000; margin-top: 40px; border-radius: 5px; }
    .protocol-header { color: #FF4B4B; font-family: 'Cinzel', serif; font-size: 20px; border-bottom: 1px solid #7B0000; margin-bottom: 15px; }
    .protocol-text { font-family: 'Courier New', monospace; color: #FF4B4B; font-size: 15px; line-height: 1.6; }
    .green-box-container { background-color: #0A0A0A; border: 1px solid #1A1A1A; padding: 35px; max-width: 550px; margin: 20px auto; border-radius: 8px; text-align: center; }
    .email-text { color: #2ECC71 !important; font-weight: bold; font-size: 22px; text-decoration: none; font-family: 'Courier New', monospace; }
    .stButton > button { background-color: #7B0000 !important; color: white; border-radius: 0; border: none; width: 100%; }
    </style>
""", unsafe_allow_html=True)

# 3. HEADER
col_h1, col_h2, col_h3 = st.columns([1, 4, 1])
with col_h2:
    try: st.image("logo.png", width=150)
    except: st.markdown("<h1 style='text-align:center;'>🦅</h1>", unsafe_allow_html=True)
    st.markdown("<div class='ips-title'>D.H.R.U.V.A.</div>", unsafe_allow_html=True)
    st.markdown("<div class='ips-subtitle'>National Research & Anomaly Society</div>", unsafe_allow_html=True)

# 4. TABS
tab1, tab2, tab3, tab4, tab5 = st.tabs(["HOME", "ABOUT US", "INVESTIGATIONS", "REPORT MYSTERY", "CONTACT"])

with tab1:
    st.markdown("<h2 style='text-align:center; font-family:Cinzel;'>WE INVESTIGATE WHAT OTHERS FEAR</h2>", unsafe_allow_html=True)
    col_i1, col_i2 = st.columns([1, 2])
    with col_i1:
        try: st.image("gaurav_tiwari.png", use_container_width=True)
        except: st.info("Late Rev. Gaurav Tiwari")
    with col_i2:
        st.markdown(f"<div class='ips-block'><h3 style='font-family:Cinzel;'>OUR INSPIRATION</h3><p style='font-style:italic; font-size:18px;'>\"Fear is just missing data. Logic is the cure.\"</p><p style='color:#00D4FF; font-weight:bold;'>- Late Rev. Gaurav Tiwari</p><p style='color:#666; font-size:14px;'>The pioneer who taught us to replace superstition with scientific research.</p></div>", unsafe_allow_html=True)
    
    # --- DHRUVA PROTOCOLS SECTION ---
    st.markdown("""
        <div class='protocol-section'>
        <div class='protocol-header'>🛡️ ESTABLISHED PROTOCOLS</div>
        <div class='protocol-text'>
        > PROTOCOL 01: SUBJECTIVITY DISCARDED. Only empirical data and physical evidence are admitted into the D.H.R.U.V.A. database.<br>
        > PROTOCOL 02: NEUTRALITY OBSERVED. We neither confirm nor deny without verification from our engineering and metaphysics divisions.<br>
        > PROTOCOL 03: ABSOLUTE PRIVACY. All citizen reports are encrypted and accessible only by the Director.
        </div>
        </div>
    """, unsafe_allow_html=True)

with tab2:
    st.markdown("<h2 style='font-family:Cinzel;'>THE DIRECTORATE</h2>", unsafe_allow_html=True)
    col_dir1, col_dir2 = st.columns([1, 2])
    with col_dir1:
        try: st.image("director.png", width=300)
        except: st.info("Founder Photo")
    with col_dir2:
        st.markdown("<h3 style='color:#00D4FF !important;'>Pranav Anil Rahane</h3>", unsafe_allow_html=True)
        st.caption("Founder & Lead Investigator | CSE (AI & DS), IIIT Kottayam")
        st.write("""
            D.H.R.U.V.A. (Digital Holistic Residual Unexplained Variable Analysis) was founded with a singular mission: 
            to bring the precision of modern data science and engineering to the study of anomalies. 
            As a student unit based at IIIT Kottayam, we use logic and physics to bridge the gap between 
            ancient Indian folklore and modern scientific verification.
        """)

with tab3:
    st.markdown("<h2 style='font-family:Cinzel; text-align:center;'>DECLASSIFIED CASE FILES</h2>", unsafe_allow_html=True)
    if conn:
        try:
            df_inv = conn.read(worksheet="Investigations")
            for _, m in df_inv.iterrows():
                st.markdown(f"<div class='ips-block'><h4>{m['Title']}</h4><p>{m['Details']}</p><b>VERDICT: {m['Verdict']}</b></div>", unsafe_allow_html=True)
        except: st.info("No cases currently declassified in the public database.")

with tab4:
    st.markdown("<h2 style='font-family:Cinzel; text-align:center;'>REPORT ANOMALY</h2>", unsafe_allow_html=True)
    with st.form("anomaly_form", clear_on_submit=True):
        c1, c2 = st.columns(2)
        with c1: name = st.text_input("FULL NAME"); phone = st.text_input("CONTACT NO")
        with c2: loc = st.text_input("LOCATION"); m_type = st.selectbox("CATEGORY", ["Haunting", "UFO", "Human Anomaly", "Other"])
        desc = st.text_area("DETAILED DESCRIPTION")
        if st.form_submit_button("TRANSMIT INTEL"):
            if conn:
                try:
                    new_rep = pd.DataFrame([{"Timestamp": str(datetime.datetime.now()), "Name": name, "Phone": phone, "Loc": loc, "Type": m_type, "Desc": desc}])
                    existing = conn.read(worksheet="Reports")
                    updated = pd.concat([existing, new_rep], ignore_index=True)
                    conn.update(worksheet="Reports", data=updated)
                    st.success("INTEL RECEIVED. SECURE ARCHIVE COMPLETE.")
                except: st.error("Database connection lost. Report not saved.")

with tab5:
    st.markdown(f'<div class="green-box-container"><div style="color:#555; text-align:left; font-size:12px;">Official Comms:</div><a href="mailto:team.dhruva.research@gmail.com" class="email-text">✉️ team.dhruva.research@gmail.com</a></div>', unsafe_allow_html=True)
    with st.form("contact_form", clear_on_submit=True):
        cn = st.text_input("NAME"); ce = st.text_input("EMAIL"); cm = st.text_area("MESSAGE")
        if st.form_submit_button("SEND MESSAGE"):
            if conn:
                try:
                    new_msg = pd.DataFrame([{"Timestamp": str(datetime.datetime.now()), "Name": cn, "Email": ce, "Message": cm}])
                    existing = conn.read(worksheet="Messages")
                    updated = pd.concat([existing, new_msg], ignore_index=True)
                    conn.update(worksheet="Messages", data=updated)
                    st.success("COMMUNICATION TRANSMITTED.")
                except: st.error("Storage error.")

# 5. HIDDEN HQ CONTROL
if st.query_params.get("access") == "classified":
    with st.sidebar:
        st.markdown("### 🔐 HQ CONTROL")
        u = st.text_input("ID", key="ad_u"); p = st.text_input("KEY", type="password", key="ad_p")
        if st.button("LOGIN"):
            if u == "Pranav" and p == "DhruvaBot": st.session_state['logged_in'] = True
            else: st.error("UNAUTHORIZED")
        
        if st.session_state.get('logged_in'):
            st.success("DIRECTOR ONLINE")
            if st.button("LOGOUT"): st.session_state['logged_in'] = False; st.rerun()
            with st.expander("📤 PUBLISH NEW CASE"):
                with st.form("pub_case"):
                    mt = st.text_input("Title"); ms = st.selectbox("Verdict", ["SOLVED", "UNEXPLAINED", "DEBUNKED"]); md = st.text_area("Details")
                    if st.form_submit_button("PUBLISH LIVE"):
                        if conn:
                            new_c = pd.DataFrame([{"Title": mt, "Verdict": ms, "Details": md, "Date": str(datetime.date.today())}])
                            try:
                                ex = conn.read(worksheet="Investigations")
                                up = pd.concat([ex, new_c], ignore_index=True)
                                conn.update(worksheet="Investigations", data=up)
                                st.success("Case Published.")
                            except: st.error("Update failed.")

st.markdown("<div style='text-align:center; color:#333; font-size:12px; padding:40px;'>© 2026 D.H.R.U.V.A. | LOGIC OVER FEAR</div>", unsafe_allow_html=True)
