import streamlit as st
import hashlib
from cryptography.fernet import Fernet

# App Title and Session State Initialization
st.set_page_config(page_title="🔐 HooriaKha Secure Vault", layout="centered")
st.title("🔐 HooriaKha's Secure Vault")

# Generate Key (Should be stored securely in production)
KEY = Fernet.generate_key()
cipher = Fernet(KEY)

# In-memory store for encrypted data
stored_data = {}  # Format: { "encrypted_text": {"encrypted_text": ..., "passkey": ...} }
if "failed_attempts" not in st.session_state:
    st.session_state.failed_attempts = 0

# ------------------------ Utility Functions ------------------------

def hash_passkey(passkey):
    """Hashes the passkey for secure comparison."""
    return hashlib.sha256(passkey.encode()).hexdigest()

def encrypt_data(text, passkey):
    """Encrypts the data using Fernet and returns it."""
    return cipher.encrypt(text.encode()).decode()

def decrypt_data(encrypted_text, passkey):
    """Attempts to decrypt data using the passkey."""
    hashed_passkey = hash_passkey(passkey)

    if encrypted_text in stored_data:
        if stored_data[encrypted_text]["passkey"] == hashed_passkey:
            st.session_state.failed_attempts = 0  # Reset on success
            return cipher.decrypt(encrypted_text.encode()).decode()

    st.session_state.failed_attempts += 1
    return None

# ------------------------ Sidebar Menu ------------------------

menu = ["🏠 Home", "🗄️ Store Data", "🔍 Retrieve Data", "🔐 Re-Login"]
choice = st.sidebar.selectbox("📍 Navigate", menu)

# ------------------------ Pages ------------------------

if choice == "🏠 Home":
    st.subheader("Welcome to HooriaKha's Secure Vault 🔐")
    st.markdown("""
        - Use **'Store Data'** to encrypt and save your sensitive text.
        - Use **'Retrieve Data'** to decrypt it using your passkey.
        - After **3 failed attempts**, re-login to continue.
    """)
    st.info("Your privacy is our top priority 🛡️")

elif choice == "🗄️ Store Data":
    st.subheader("🗄️ Secure Your Data")
    user_data = st.text_area("✍️ Enter the text you want to encrypt:")
    passkey = st.text_input("🔑 Create a passkey:", type="password")

    if st.button("🔒 Encrypt & Save"):
        if user_data and passkey:
            hashed_passkey = hash_passkey(passkey)
            encrypted_text = encrypt_data(user_data, passkey)
            stored_data[encrypted_text] = {
                "encrypted_text": encrypted_text,
                "passkey": hashed_passkey
            }
            st.success("✅ Successfully encrypted and saved!")
            st.code(encrypted_text, language="text")
        else:
            st.warning("⚠️ Both fields are required!")

elif choice == "🔍 Retrieve Data":
    if st.session_state.failed_attempts >= 3:
        st.warning("🚫 Too many failed attempts! Please reauthorize.")
        st.stop()

    st.subheader("🔍 Decrypt Your Data")
    encrypted_text = st.text_area("🔐 Paste your encrypted data here:")
    passkey = st.text_input("🔑 Enter your passkey:", type="password")

    if st.button("🔓 Decrypt"):
        if encrypted_text and passkey:
            result = decrypt_data(encrypted_text, passkey)
            if result:
                st.success("🎉 Decryption successful!")
                st.code(result, language="text")
            else:
                attempts_left = 3 - st.session_state.failed_attempts
                st.error(f"❌ Incorrect passkey. Attempts left: {attempts_left}")
                if st.session_state.failed_attempts >= 3:
                    st.warning("🔐 Redirecting to Re-Login page...")
                    st.experimental_rerun()
        else:
            st.warning("⚠️ Please fill both fields.")

elif choice == "🔐 Re-Login":
    st.subheader("🔐 Reauthorize Access")
    login_pass = st.text_input("🔑 Enter Master Password (admin123):", type="password")

    if st.button("✅ Login"):
        if login_pass == "admin123":
            st.session_state.failed_attempts = 0
            st.success("✅ Access restored! You can now try again.")
            st.experimental_rerun()
        else:
            st.error("❌ Incorrect master password!")
