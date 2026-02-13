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
    conn = None

# 2. IPS PREMIUM CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Raleway:wght@300;400&display=swap');
    .stApp { background-color: #000000; color: #FFFFFF; font-family: 'Raleway', sans-serif; }
    .stTabs [data-baseweb="tab-list"] { background-color: #0A0A0A; border-bottom: 1px solid #111; justify-content: center; }
    .stTabs [data-baseweb="tab"] { color: #888 !important; font-weight: bold; font-size: 14px; letter-spacing: 1px;}
    .stTabs [aria-selected="true"] { color: #00D4FF !important; border-bottom: 2px solid #00D4FF; }
    .ips-title { font-family: 'Cinzel', serif; font-size: 60px; text-align: center; letter-spacing: 8px; margin-bottom: 0; color: #FFFFFF; }
    .ips-subtitle { font-family: 'Raleway', sans-serif; font-size: 14px; text-align: center; letter-spacing: 4px; color: #00D4FF; text-transform: uppercase; margin-bottom: 5px; }
    
    /* Single Secret Protocol Styling */
    .global-protocol { text-align: center; color: #FF4B4B; font-family: 'Courier New', monospace; font-size: 13px; font-weight: bold; margin-bottom: 30px; border-top: 1px solid #7B0000; border-bottom: 1px solid #7B0000; padding: 5px 0; max-width: 600px; margin-left: auto; margin-right: auto; }
    
    .ips-block { background-color: #0A0A0A; border-left: 3px solid #00D4FF; padding: 30px; margin: 30px 0; }
    .green-box-container { background-color: #0A0A0A; border: 1px solid #1A1A1A; padding: 35px; max-width: 550px; margin: 20px auto; border-radius: 8px; text-align: center; }
    .email-text { color: #2ECC71 !important; font-weight: bold; font-size: 22px; text-decoration: none; font-family: 'Courier New', monospace; }
    .stButton > button { background-color: #7B0000 !important; color: white; border-radius: 0; border: none; width: 100%; }
    h2, h3 { font-family: 'Cinzel', serif; letter-spacing: 2px; }
    </style>
""", unsafe_allow_html=True)

# 3. HEADER & GLOBAL PROTOCOL
st.markdown("<div class='ips-title'>D.H.R.U.V.A.</div>", unsafe_allow_html=True)
st.markdown("<div class='ips-subtitle'>National Research & Anomaly Society</div>", unsafe_allow_html=True)
# The Single Protocol below the name as requested
st.markdown("<div class='global-protocol'>> PROTOCOL: SECRECY IS THE SHIELD, LOGIC IS THE SWORD. SUBJECTIVITY DISCARDED.</div>", unsafe_allow_html=True)

# 4. TABS
tab1, tab2, tab3, tab4, tab5 = st.tabs(["HOME", "ABOUT US", "INVESTIGATIONS", "REPORT MYSTERY", "CONTACT"])

with tab1:
    st.markdown("<h2 style='text-align:center;'>CORE OPERATIONS & LEGACY</h2>", unsafe_allow_html=True)
    
    # Information about the Job/Organization
    st.markdown("""
    <div class='ips-block'>
    <h3>OUR MISSION: SCIENTIFIC INVESTIGATION</h3>
    <p>D.H.R.U.V.A. is not a ghost-hunting group; we are a dedicated research unit. Our job is to analyze unexplained environmental variables, 
    EMF fluctuations, and residual energy patterns using advanced engineering tools and data science. We bridge the gap between human 
    experience and empirical evidence. Our objective is to replace fear with verifiable data.</p>
    </div>
    """, unsafe_allow_html=True)

    # Information about Gaurav Tiwari
    col_i1, col_i2 = st.columns([1, 2])
    with col_i1:
        try: st.image("gaurav_tiwari.png", use_container_width=True)
        except: st.info("Late Rev. Gaurav Tiwari Image")
    with col_i2:
        st.markdown(f"""
        <div class='ips-block'>
        <h3>THE LEGACY: REV. GAURAV TIWARI</h3>
        <p>The foundation of our logical approach was laid by the <b>Late Rev. Gaurav Tiwari</b>, the pioneer of paranormal research in India. 
        His dedication to replacing blind faith with scientific methodology is our driving force. We follow his philosophy: 
        <i>\"Fear is just missing data. Logic is the cure.\"</i></p>
        <p>By studying his methods, D.H.R.U.V.A. continues the quest to understand the unseen through a lens of professional skepticism and respect.</p>
        </div>
        """, unsafe_allow_html=True)

with tab2:
    st.markdown("<h2>THE DIRECTORATE</h2>", unsafe_allow_html=True)
    col_dir1, col_dir2 = st.columns([1, 2])
    with col_dir1:
        try: st.image("director.png", width=300)
        except: st.info("Founder Photo")
    with col_dir2:
        st.markdown("<h3 style='color:#00D4FF !important;'>Pranav Anil Rahane</h3>", unsafe_allow_html=True)
        st.caption("Founder & Lead Investigator | CSE (AI & DS), IIIT Kottayam")
        st.write("Specializing in Digital Holistic Residual Unexplained Variable Analysis. Dedicated to the advancement of metaphysical science in India.")

with tab3:
    if conn:
        try:
            df_inv = conn.read(worksheet="Investigations")
            for _, m in df_inv.iterrows():
                st.markdown(f"<div class='ips-block'><h4>{m['Title']}</h4><p>{m['Details']}</p><b>VERDICT: {m['Verdict']}</b></div>", unsafe_allow_html=True)
        except: st.info("Public records currently restricted.")

with tab4:
    with st.form("anomaly_form", clear_on_submit=True):
        c1, c2 = st.columns(2)
        with c1: name = st.text_input("FULL NAME"); phone = st.text_input("CONTACT NO")
        with c2: loc = st.text_input("LOCATION"); m_type = st.selectbox("CATEGORY", ["Metaphysical", "UFO", "Environmental", "Other"])
        desc = st.text_area("INTEL DESCRIPTION")
        if st.form_submit_button("TRANSMIT INTEL"):
            if conn:
                try:
                    new_rep = pd.DataFrame([{"Timestamp": str(datetime.datetime.now()), "Name": name, "Phone": phone, "Loc": loc, "Type": m_type, "Desc": desc}])
                    existing = conn.read(worksheet="Reports")
                    updated = pd.concat([existing, new_rep], ignore_index=True)
                    conn.update(worksheet="Reports", data=updated)
                    st.success("INTEL ARCHIVED IN SECURE DATABASE.")
                except: st.error("Database error.")

with tab5:
    st.markdown(f'<div class="green-box-container"><div style="color:#555; text-align:left; font-size:12px;">Comms Channel:</div><a href="mailto:team.dhruva.research@gmail.com" class="email-text">✉️ team.dhruva.research@gmail.com</a></div>', unsafe_allow_html=True)
    with st.form("contact_form", clear_on_submit=True):
        cn = st.text_input("NAME"); ce = st.text_input("EMAIL"); cm = st.text_area("MESSAGE")
        if st.form_submit_button("SEND MESSAGE"):
            if conn:
                try:
                    new_msg = pd.DataFrame([{"Timestamp": str(datetime.datetime.now()), "Name": cn, "Email": ce, "Message": cm}])
                    existing = conn.read(worksheet="Messages")
                    updated = pd.concat([existing, new_msg], ignore_index=True)
                    conn.update(worksheet="Messages", data=updated)
                    st.success("TRANSMISSION COMPLETE.")
                except: st.error("Storage error.")

# 5. HIDDEN ADMIN CONTROL
if st.query_params.get("access") == "classified":
    with st.sidebar:
        st.markdown("### 🔐 HQ CONTROL")
        u = st.text_input("ID", key="ad_u"); p = st.text_input("KEY", type="password", key="ad_p")
        if st.button("LOGIN"):
            if u == "Pranav" and p == "DhruvaBot": st.session_state['logged_in'] = True
        
        if st.session_state.get('logged_in'):
            st.success("DIRECTOR ONLINE")
            if st.button("LOGOUT"): st.session_state['logged_in'] = False; st.rerun()
            with st.expander("📤 PUBLISH CASE"):
                with st.form("pub_case"):
                    mt = st.text_input("Title"); ms = st.selectbox("Verdict", ["SOLVED", "UNEXPLAINED"]); md = st.text_area("Details")
                    if st.form_submit_button("PUBLISH"):
                        if conn:
                            new_c = pd.DataFrame([{"Title": mt, "Verdict": ms, "Details": md, "Date": str(datetime.date.today())}])
                            try:
                                ex = conn.read(worksheet="Investigations")
                                up = pd.concat([ex, new_c], ignore_index=True)
                                conn.update(worksheet="Investigations", data=up)
                                st.success("Case Live.")
                            except: st.error("Error.")

st.markdown("<div style='text-align:center; color:#333; font-size:12px; padding:40px;'>© 2026 D.H.R.U.V.A. | LOGIC OVER FEAR</div>", unsafe_allow_html=True)
