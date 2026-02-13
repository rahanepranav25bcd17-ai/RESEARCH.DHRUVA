import streamlit as st
import pandas as pd
import datetime

# 1. PAGE CONFIG
st.set_page_config(page_title="D.H.R.U.V.A. HQ", page_icon="🦅", layout="wide")

# 2. DATABASE CONNECTION (SAFE WRAPPER)
conn = None
try:
    from streamlit_gsheets import GSheetsConnection
    conn = st.connection("gsheets", type=GSheetsConnection)
except Exception:
    st.warning("Database Connection Pending... Design is Active.")

# 3. IPS PREMIUM CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Raleway:wght@300;400&display=swap');
    .stApp { background-color: #000000; color: #FFFFFF; font-family: 'Raleway', sans-serif; }
    .ips-title { font-family: 'Cinzel', serif; font-size: 50px; text-align: center; color: #FFFFFF; margin-top: 20px; }
    .ips-subtitle { font-family: 'Raleway', sans-serif; font-size: 14px; text-align: center; color: #00D4FF; letter-spacing: 3px; margin-bottom: 30px; }
    .ips-block { background-color: #0A0A0A; border-left: 3px solid #00D4FF; padding: 25px; margin: 20px 0; }
    .green-box { background-color: #0A0A0A; border: 1px solid #1A1A1A; padding: 30px; border-radius: 8px; text-align: center; margin: 20px auto; max-width: 500px; }
    .email-text { color: #2ECC71 !important; font-weight: bold; font-size: 20px; text-decoration: none; }
    .stButton > button { background-color: #7B0000 !important; color: white; border-radius: 0; width: 100%; border: none; }
    </style>
""", unsafe_allow_html=True)

# 4. HEADER
st.markdown("<div class='ips-title'>D.H.R.U.V.A.</div>", unsafe_allow_html=True)
st.markdown("<div class='ips-subtitle'>National Research & Anomaly Society</div>", unsafe_allow_html=True)

# 5. TABS
tab1, tab2, tab3, tab4, tab5 = st.tabs(["HOME", "ABOUT US", "INVESTIGATIONS", "REPORT MYSTERY", "CONTACT"])

with tab1:
    st.markdown("<h2 style='text-align:center; font-family:Cinzel;'>WE INVESTIGATE WHAT OTHERS FEAR</h2>", unsafe_allow_html=True)
    c1, c2 = st.columns([1, 2])
    with c1:
        try: st.image("gaurav_tiwari.png")
        except: st.info("Gaurav Tiwari Image")
    with c2:
        st.markdown("<div class='ips-block'><h3>OUR INSPIRATION</h3><p style='font-style:italic;'>\"Fear is just missing data. Logic is the cure.\"</p><p style='color:#00D4FF;'>- Late Rev. Gaurav Tiwari</p></div>", unsafe_allow_html=True)

with tab2:
    st.markdown("### THE DIRECTORATE")
    st.write("We are a youth-led unit dedicated to uncovering truths through physics and engineering. Logic is our only tool.")

with tab3:
    if conn:
        try:
            df = conn.read(worksheet="Investigations")
            for _, m in df.iterrows():
                st.markdown(f"<div class='ips-block'><h4>{m['Title']}</h4><p>{m['Details']}</p><b>VERDICT: {m['Verdict']}</b></div>", unsafe_allow_html=True)
        except: st.info("No cases available in database.")
    else: st.info("Database not connected yet.")

with tab4:
    with st.form("anomaly_form", clear_on_submit=True):
        n = st.text_input("NAME"); ph = st.text_input("PHONE"); loc = st.text_input("LOCATION")
        dsc = st.text_area("DESCRIPTION")
        if st.form_submit_button("TRANSMIT INTEL"):
            if conn:
                try:
                    new_rep = pd.DataFrame([{"Timestamp": str(datetime.datetime.now()), "Name": n, "Phone": ph, "Loc": loc, "Desc": dsc}])
                    existing = conn.read(worksheet="Reports")
                    updated = pd.concat([existing, new_rep], ignore_index=True)
                    conn.update(worksheet="Reports", data=updated)
                    st.success("INTEL ARCHIVED.")
                except: st.error("Database Save Error.")
            else: st.warning("Cannot save: Database not connected.")

with tab5:
    st.markdown(f'<div class="green-box">Email:<br><a href="mailto:team.dhruva.research@gmail.com" class="email-text">✉️ team.dhruva.research@gmail.com</a></div>', unsafe_allow_html=True)
    with st.form("contact_form", clear_on_submit=True):
        cn = st.text_input("NAME"); ce = st.text_input("EMAIL"); cm = st.text_area("MESSAGE")
        if st.form_submit_button("SEND MESSAGE"):
            if conn:
                try:
                    new_msg = pd.DataFrame([{"Timestamp": str(datetime.datetime.now()), "Name": cn, "Email": ce, "Message": cm}])
                    existing = conn.read(worksheet="Messages")
                    updated = pd.concat([existing, new_msg], ignore_index=True)
                    conn.update(worksheet="Messages", data=updated)
                    st.success("MESSAGE SENT.")
                except: st.error("Database Save Error.")

# 6. HIDDEN ACCESS
if st.query_params.get("access") == "classified":
    with st.sidebar:
        st.markdown("### 🔐 HQ CONTROL")
        u = st.text_input("ID"); p = st.text_input("KEY", type="password")
        if st.button("LOGIN"):
            if u == "Pranav" and p == "DhruvaBot": st.session_state['logged_in'] = True
        
        if st.session_state.get('logged_in'):
            st.success("DIRECTOR ONLINE")
            with st.form("pub_case"):
                mt = st.text_input("Title"); ms = st.selectbox("Verdict", ["SOLVED", "DEBUNKED"]); md = st.text_area("Details")
                if st.form_submit_button("PUBLISH LIVE"):
                    if conn:
                        new_c = pd.DataFrame([{"Title": mt, "Verdict": ms, "Details": md, "Date": str(datetime.date.today())}])
                        try:
                            existing = conn.read(worksheet="Investigations")
                            updated = pd.concat([existing, new_c], ignore_index=True)
                            conn.update(worksheet="Investigations", data=updated)
                            st.success("Published.")
                        except: st.error("Update failed.")

st.markdown("<div style='text-align:center; color:#333; font-size:12px; padding:40px;'>© 2026 D.H.R.U.V.A. | LOGIC OVER FEAR</div>", unsafe_allow_html=True)
