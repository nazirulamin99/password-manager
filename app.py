import streamlit as st
from generator import generate_password
from utils import save_password_to_db, get_all_passwords, delete_password
from database import Base, engine
from models import Password


# Initialize the database
Base.metadata.create_all(bind=engine)


# Set up page config
st.set_page_config(page_title="Password Manager", page_icon="🔐", layout="centered")


# App Title & Intro
st.markdown("<h1 style='text-align: center;'>🔐 Password Manager</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Generate and manage your passwords securely</p>", unsafe_allow_html=True)
st.markdown("---")


# Initialize session state
if "generated_password" not in st.session_state:
    st.session_state.generated_password = ""
if "last_label" not in st.session_state:
    st.session_state.last_label = ""


# Password Settings Section
st.subheader("🛠️ Password Settings")

col1, col2 = st.columns(2)
with col1:
    length = st.slider("Password Length", 4, 64, 12)
    label = st.text_input("Label (e.g. Gmail, Facebook)")
with col2:
    use_upper = st.checkbox("Include Uppercase Letters", value=True)
    use_digits = st.checkbox("Include Numbers", value=True)
    use_symbols = st.checkbox("Include Symbols", value=True)


# Generate Password
if st.button("🚀 Generate Password"):
    try:
        password = generate_password(length, use_upper, use_digits, use_symbols)
        st.session_state.generated_password = password
        st.session_state.last_label = label
        st.success("✅ Password generated!")
        st.code(password, language="text")
    except Exception as e:
        st.error(f"❌ Error: {e}")


# Save Password Section
if st.session_state.generated_password:
    with st.expander("💾 Save Password to Database"):
        if st.button("Save This Password"):
            if st.session_state.last_label:
                save_password_to_db(st.session_state.last_label, st.session_state.generated_password)
                st.success("✅ Password saved to database!")
            else:
                st.warning("⚠️ Please enter a label before saving.")


# View + delete passwords
with st.expander("📂 View Saved Passwords"):
    saved_passwords = get_all_passwords()
    if saved_passwords:
        for pw in saved_passwords:
            with st.container():
                st.markdown(f"**🔖 {pw.label}** — 🕒 {pw.timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
                st.code(pw.password)

                delete_col, _ = st.columns([1, 5])
                with delete_col:
                    if st.button("🗑️ Delete", key=f"delete_{pw.id}"):
                        delete_password(pw.id)
                        st.success(f"Deleted password for {pw.label}")
                        st.rerun()  # Refresh to update the list

                st.markdown("---")
    else:
        st.info("No passwords saved yet.")

