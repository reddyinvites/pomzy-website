import streamlit as st

# Page config
st.set_page_config(page_title="Pomzy Connect", page_icon="🏠", layout="centered")

# Header
st.title("🏠 Pomzy Connect")
st.subheader("Find & Fill PG Beds Fast")

st.markdown("---")

# About
st.header("👤 About")
st.write("Pulla Reddy")
st.write("PG Accommodation Expert")
st.write("Founder & CEO")

st.markdown("---")

# Services
st.header("🚀 What We Do")
st.write("""
✔ We help PG owners fill vacant beds  
✔ We bring genuine students only  
✔ Fast filling service  
✔ Zero hassle for owners  
""")

st.markdown("---")

# Contact
st.header("📞 Contact")

st.write("📞 7702656073")

st.markdown("[💬 Chat on WhatsApp](https://wa.me/7702656073)")

st.markdown("---")

# Trust line
st.markdown(
    "<h3 style='text-align: center; color: #f4b400;'>We fill your vacant beds faster.</h3>",
    unsafe_allow_html=True
)
