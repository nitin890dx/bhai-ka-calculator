import streamlit as st

st.set_page_config(page_title="Bhai ka Calculator", page_icon="🧮")
st.title("🧮 Bhai ka Calculator - PRO MAX")

# Photo wala Feature
photo = st.file_uploader("Apni Photo Lagao 📸", type=["jpg", "png"])
if photo:
    st.image(photo, caption="Mera Bhai Engineer!", width=200)
    st.balloons()

st.write("---")

col1, col2 = st.columns(2)
with col1:
    a = st.number_input("Pahla Number 🔢", value=0.0)
with col2:
    b = st.number_input("Dusra Number 🔢", value=0.0)

kaam = st.selectbox("Kya Karna Hai? 🤔", ["➕ Jodna", "➖ Ghatana", "✖️ Guna", "➗ Bhaag"])

if st.button("JAWAB DIKHAO 🚀"):
    if "Jodna" in kaam:
        st.success(f"Jawab hai: {a+b}")
    elif "Ghatana" in kaam:
        st.success(f"Jawab hai: {a-b}")
    elif "Guna" in kaam:
        st.success(f"Jawab hai: {a*b}")
    elif "Bhaag" in kaam:
        if b != 0:
            st.success(f"Jawab hai: {a/b}")
        else:
            st.error("Abe 0 se bhaag nahi hota! 😅")
