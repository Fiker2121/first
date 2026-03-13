import streamlit as st
import pandas as pd
import os
from streamlit_option_menu import option_menu
from datetime import datetime

# የገጽ መገለጫ
st.set_page_config(page_title="Dr. Ayele Gebreselassie | Medical Center", page_icon="🏥", layout="wide")

# --- 1. ዳታቤዝ ፋንክሽን ---
def save_data(name, phone, date, time, reason):
    file_name = "appointments.csv"
    new_data = pd.DataFrame([[name, phone, date, time, reason, datetime.now().strftime("%Y-%m-%d %H:%M")]],
                            columns=["ስም", "ስልክ", "ቀን", "ሰዓት", "ምክንያት", "የመዝገብ ሰዓት"])
    if not os.path.isfile(file_name):
        new_data.to_csv(file_name, index=False)
    else:
        new_data.to_csv(file_name, mode='a', index=False, header=False)

# --- 2. የጎን ማውጫ (Navigation) ---
with st.sidebar:
    st.markdown("### 🏥 ዶ/ር አየለ ገብረስላሴ")
    selected = option_menu(
        menu_title="ዋና ዝርዝር",
        options=["መነሻ (Home)", "አገልግሎቶች", "የፎቶ ጋለሪ", "ቀጠሮ መያዣ", "የዶክተር መግቢያ"],
        icons=["house", "briefcase", "images", "calendar-check", "lock"],
        menu_icon="cast", default_index=0,
    )
    
    st.markdown("---")
    st.markdown("### 📱 ያግኙን (Social Media)")
    # 5 የማህበራዊ ሚዲያ ሊንኮች
    st.markdown("[🔵 Facebook](https://facebook.com/ayele.gebreselassie)")
    st.markdown("[📸 Instagram](https://instagram.com)")
    st.markdown("[🐦 X (Twitter)](https://twitter.com)")
    st.markdown("[🎬 YouTube](https://youtube.com)")
    st.markdown("[💬 Telegram](https://t.me)")

# --- 3. መነሻ ገጽ (Home) - 10 ይዘቶች (Contents) ---
if selected == "መነሻ (Home)":
    st.title("እንኳን ወደ ዶ/ር አየለ ገብረስላሴ የሕክምና ማዕከል በሰላም መጡ")
    
    # ይዘት 1: ዋና ምስል
    st.image("https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?ixlib=rb-1.2.1&auto=format&fit=crop&w=1200&q=80")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("### 1. ራዕያችን")
        st.info("በኢትዮጵያ ቀዳሚ እና ተመራጭ የውስጥ ደዌ ሕክምና ማዕከል መሆን።")
        
        st.write("### 2. ተልእኳችን")
        st.write("ዘመናዊ የሕክምና ጥበባትን በመጠቀም የታካሚዎቻችንን ጤና መመለስ።")

    with col2:
        st.write("### 3. የሥራ ሰዓት")
        st.success("ሰኞ - ቅዳሜ፡ ከጠዋቱ 2:00 - ከሰዓት 12:00")
        
        st.write("### 4. አድራሻ")
        st.write("አዲስ አበባ፣ ተክለሃይማኖት አካባቢ፣ የትዕግስት ሕንፃ 2ኛ ፎቅ።")

    st.markdown("---")
    # ይዘት 5-10 በካርድ መልክ
    st.write("### ተጨማሪ መረጃዎች")
    c1, c2, c3 = st.columns(3)
    c1.metric("ታካሚዎች", "5000+", "+12%")
    c2.metric("ልምድ", "15 ዓመታት", "Expert")
    c3.metric("ውጤታማነት", "98%", "Excellent")
    
    st.write("#### 8. የጤና ምክር")
    st.warning("በቀን ቢያንስ 8 ብርጭቆ ውሃ መጠጣት ለጤናዎ ወሳኝ ነው።")
    
    st.write("#### 9. ልዩ ቅናሾች")
    st.write("ለአረጋውያን በየሳምንቱ ረቡዕ የ20% ቅናሽ እናደርጋለን።")
    
    st.write("#### 10. የኢንሹራንስ አገልግሎት")
    st.write("ከሁሉም ዋና ዋና የኢንሹራንስ ኩባንያዎች ጋር እንሰራለን።")

# --- 4. አገልግሎቶች ---
elif selected == "አገልግሎቶች":
    st.title("💉 የምንሰጣቸው አገልግሎቶች")
    services = ["አጠቃላይ ምርመራ", "የልብ ጤና ክትትል", "የስኳር በሽታ ቁጥጥር", "የደም ግፊት ሕክምና", "የላቦራቶሪ አገልግሎት", "የአልትራሳውንድ ምርመራ"]
    for s in services:
        st.write(f"- {s}")

# --- 5. የፎቶ ጋለሪ (15 Photos Placeholder) ---
elif selected == "የፎቶ ጋለሪ":
    st.title("🖼️ የማዕከላችን የፎቶ ጋለሪ")
    st.write("የማዕከላችንን ገጽታ በእነዚህ ምስሎች ይመልከቱ")
    
    # ለ15 ፎቶዎች የሚሆን ግሪድ (Grid)
    cols = st.columns(3)
    for i in range(15):
        with cols[i % 3]:
            # እዚህ ጋር ትክክለኛ የፎቶ ሊንኮችን መተካት ትችላለህ
            st.image(f"https://picsum.photos/400/300?random={i}", caption=f"ምስል {i+1}", use_container_width=True)

# --- 6. ቀጠሮ መያዣ ---
elif selected == "ቀጠሮ መያዣ":
    st.title("📅 ቀጠሮ ይያዙ")
    with st.form("appoint_form"):
        name = st.text_input("ሙሉ ስም")
        phone = st.text_input("ስልክ ቁጥር")
        date = st.date_input("ቀን")
        reason = st.text_area("ምክንያት")
        if st.form_submit_button("መዝግብ"):
            save_data(name, phone, date, "Not Set", reason)
            st.success("ተመዝግቧል!")

# --- 7. የዶክተር መግቢያ ---
elif selected == "የዶክተር መግቢያ":
    st.title("🔐 Admin Panel")
    pw = st.text_input("Password", type="password")
    if pw == "ayele123":
        if os.path.exists("appointments.csv"):
            df = pd.read_csv("appointments.csv")
            st.table(df)