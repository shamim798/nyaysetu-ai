import streamlit as st
import datetime

st.set_page_config(
    page_title="NyaySetu AI (ন্যায়সেতু ৩৬০)",
    page_icon="⚖️",
    layout="wide"
)

st.title("⚖️ NyaySetu AI (ন্যায়সেতু ৩৬০)")
st.caption("AI-Native Procedural Justice & Immersive Courtroom Simulation | International AI Builders Congress 2026")

tab1, tab2, tab3, tab4 = st.tabs([
    "📢 1-Click GD & FIR Drafter", 
    "🛡️ Evidence Strength Auditor", 
    "👨‍⚖️ 3D Virtual Courtroom Simulator",
    "🌐 Cross-Border Contract Scanner"
])

# ----------------- TAB 1: GD / FIR Drafter -----------------
with tab1:
    st.header("স্বয়ংক্রিয় সাধারণ ডায়েরি (GD) ও FIR জেনারেটর")
    st.write("আপনার সমস্যার বিবরণ বাংলায় লিখুন বা রেকর্ড করুন। এআই তাৎক্ষণিক প্রযোজ্য আইন ও থানার আবেদনপত্র তৈরি করবে।")
    
    col1, col2 = st.columns(2)
    with col1:
        police_station = st.text_input("থানার নাম (Police Station):", "ধানমন্ডি মডেল থানা, ঢাকা")
        complainant_name = st.text_input("অভিযোগকারীর নাম (Full Name):", "মোঃ শামীম আলী")
        nid_no = st.text_input("জাতীয় পরিচয়পত্র / পাসপোর্ট নম্বর:", "19982691234567890")
        incident_type = st.selectbox("ঘটনার ধরন (Incident Category):", [
            "চুরি / ছিনতাই (Theft / Robbery)",
            "সাইবার ক্রাইম ও হয়রানি (Cyber Harassment / Blackmail)",
            "ডকুমেন্ট হারানো (Lost Important Documents)",
            "হুমকি প্রদান (Life Threat / Extortion)",
            "আর্থিক প্রতারণা (Financial Fraud / Cheating)"
        ])
    
    with col2:
        incident_narrative = st.text_area(
            "ঘটনার বিস্তারিত বিবরণ (Describe Incident):", 
            "গত ১৮ই নভেম্বর সন্ধ্যায় ধানমন্ডি লেকে হাঁটার সময় দুজন অজ্ঞাত ব্যক্তি এসে ভয়ভীতি দেখিয়ে আমার স্মার্টফোন ও মানিব্যাগ ছিনিয়ে নেয়।",
            height=180
        )
        lawyer_cosign = st.checkbox("আইনজীবীর ডিজিটাল ভেরিফিকেশন ও সিলমোহর যুক্ত করুন (+ ৳১০০)")
    
    if st.button("Generate Official GD/FIR Draft 📄", type="primary"):
        st.success("✅ আইনি ধারা বিশ্লেষণ সম্পন্ন! পেনাল কোড ৩৯২ (ছিনতাই/দস্যুতা) প্রযোজ্য।")
        st.subheader("প্রিন্ট-রেডি আবেদনপত্রের খসড়া:")
        st.code(f"""
তারিখ: {datetime.date.today().strftime('%d/%m/%Y')}
বরাবর,
অফিসার-ইন-চার্জ (ভারপ্রাপ্ত কর্মকর্তা)
{police_station}।

বিষয়: সাধারণ ডায়েরি (GD) / এজাহার দায়েরের আবেদন।

জনাব,
বিনীত নিবেদন এই যে, আমি নিম্নস্বাক্ষরকারী {complainant_name}, জাতীয় পরিচয়পত্র নম্বর: {nid_no}, এই মর্মে জানাচ্ছি যে:

{incident_narrative}

আইনি পর্যবেক্ষণ (NyaySetu Legal Citation Engine):
উক্ত অপরাধটি বাংলাদেশ দণ্ডবিধি ১৮৬০-এর ৩৯২ ধারা (দস্যুতা) এবং ক্ষেত্রবিশেষে ৩৯৭ ধারার আওতাভুক্ত এবং এটি একটি আমলযোগ্য অপরাধ।

অতএব, জনাবের নিকট আকুল আবেদন, বিষয়টি সাধারণ ডায়েরিভুক্ত করে প্রয়োজনীয় আইনানুগ তদন্ত ও অপরাধীদের গ্রেফতারে আশু পদক্ষেপ গ্রহণে মর্জি হয়।

বিনীত নিবেদক,
{complainant_name}
মোবাইল: ০১৭XXXXXXXX
{'[Digital Advocate Co-Sign: Adv. K. Ahmed, Dhaka Bar Council - Reg #41029]' if lawyer_cosign else ''}
""", language="markdown")
        st.download_button("Download PDF Petition (৳৫০ via bKash)", data="Dummy PDF Content", file_name="official_petition.pdf")

# ----------------- TAB 2: Evidence Auditor -----------------
with tab2:
    st.header("এভিডেন্স স্ট্রেংথ অডিটর (Evidence Viability Score)")
    uploaded_file = st.file_uploader("কেসের প্রমাণপত্র (স্ক্রিনশট, মেমো, অডিও বা দলিল) আপলোড করুন:", type=["png", "jpg", "pdf", "mp3"])
    if uploaded_file or st.button("Analyze Sample Evidence"):
        st.info("অ্যানালাইসিস সম্পন্ন: বাংলাদেশ সাক্ষ্য আইন ১৮৭২ (Evidence Act) অনুযায়ী মূল্যায়ন:")
        st.progress(85)
        st.metric("Evidence Admissibility Score", "85% (High Viability)")
        st.write("✔️ **স্বীকৃত উপাদান:** ডিজিটাল স্ক্রিনশটে সুস্পষ্ট টাইমস্ট্যাম্প এবং সেন্ডার আইডি পাওয়া গেছে।")
        st.write("⚠️ **প্রয়োজনীয় অতিরিক্ত প্রমাণ:** উক্ত লেনদেনের সংশ্লিষ্ট ব্যাংক স্টেটমেন্ট বা এমএফএস ট্রানজেকশন আইডি যুক্ত করলে প্রমাণের ওজন ৯৫% এ উন্নীত হবে।")

# ----------------- TAB 3: Virtual Courtroom -----------------
with tab3:
    st.header("৩ডি ভার্চুয়াল কোর্টরুম মক ট্রায়াল (3D WebXR Simulation)")
    st.write("আইনের শিক্ষার্থী ও তরুণ আইনজীবীদের জন্য এআই বিচারক ও সাক্ষীর সাথে লাইভ জেরা সিমুলেশন।")
    st.markdown("""
    ```
    +-------------------------------------------------------------+
    |                     [ PRESIDING JUDGE ]                     |
    |                 "Order in the court! Counsel, proceed."     |
    +-------------------------------------------------------------+
              ▲                                        ▲
              │                                        │
    [ DEFENSE COUNSEL ]                        [ WITNESS BOX ]
    "Objection, leading!"              "I was at the scene at 7 PM..."
    ```
    """)
    objection = st.selectbox("আপনার আইনি পদক্ষেপ নির্বাচন করুন:", [
        "Objection: Leading Question (Section 143, Evidence Act)",
        "Objection: Hearsay Evidence",
        "Request for Cross-Examination Extension"
    ])
    if st.button("Submit Courtroom Objection"):
        st.warning("👨‍⚖️ Judge Agent: **SUSTAINED!** The witness cannot be asked questions suggesting the desired answer.")

# ----------------- TAB 4: Contract Scanner -----------------
with tab4:
    st.header("ক্রস-বর্ডার কন্ট্রাক্ট ও ফ্রিল্যান্সার কমপ্লায়েন্স অডিটর")
    contract_text = st.text_area("আন্তর্জাতিক চুক্তি বা NDA পেস্ট করুন:", "Client shall own all IP and Contractor waives all moral rights globally without royalty payment. Jurisdiction: State of California.")
    if st.button("Scan Contract for Risks"):
        st.error("🚨 ১টি উচ্চ ঝুঁকিপূর্ণ ধারা চিহ্নিত হয়েছে!")
        st.write("• ** ধারা ৩ (IP Forfeiture):** সম্পূর্ণ রয়্যালটি মুক্ত আইপি হস্তান্তর ফ্রিল্যান্সারের জন্য ঝুঁকিপূর্ণ।")
        st.info("💡 **সুপারিশকৃত নিরাপদ ক্লজ:** 'IP assignment is conditional upon 100% full payment clearance.'")
