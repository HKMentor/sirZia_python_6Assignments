# 🔐 Secure Text Encryption & Decryption App

## About This Project
This project is part of my **Python learning journey**. It is a simple web application built using **Streamlit**, **hashlib**, and **Fernet** (from the `cryptography` library) to demonstrate basic concepts of encryption and decryption.

Users can **securely store text** by encrypting it with a passkey and later retrieve the original text by decrypting it with the same passkey. To enhance security, the app limits the number of wrong passkey attempts to 3, after which the user must log in again.

---

## 🐍 About Python
Python is a high-level, interpreted programming language known for its simplicity and readability. It supports multiple programming paradigms and is widely used for web development, data science, automation, and more. Python's rich ecosystem of libraries (like `cryptography` and `streamlit`) makes it a perfect choice for rapid application development and learning.

---

## 💡 Features

- **Text Encryption:** Encrypt your data with a custom passkey.
- **Secure Passkey Hashing:** Passkeys are hashed using SHA256 to protect sensitive information.
- **Decryption with Security:** Users can decrypt data by providing the correct passkey. After 3 wrong attempts, reauthorization is required.
- **Simple & Clean UI:** Built using Streamlit for easy interaction.

---

## 🚀 How to Use

1. Go to **Store Data** to input your text and create a passkey for encryption.
2. The app will generate an encrypted text string.
3. To retrieve your original text, go to **Retrieve Data** and enter the encrypted string along with the passkey.
4. If you enter a wrong passkey 3 times, you'll need to log in again via the **Login** page.

---

## 📜 اردو میں خلاصہ

یہ ایک ویب ایپ ہے جو صارف کو اپنا ٹیکسٹ **پاسکی کے ذریعے انکرپٹ** اور **ڈی کرپٹ** کرنے کی سہولت دیتی ہے۔  
اگر 3 بار غلط پاسکی دی جائے تو دوبارہ لاگ ان کی ضرورت پڑتی ہے تاکہ سیکورٹی کو یقینی بنایا جا سکے۔

---

## 📚 Libraries Used

- [Streamlit](https://streamlit.io/) — For building the web app interface  
- [hashlib](https://docs.python.org/3/library/hashlib.html) — For SHA256 passkey hashing  
- [cryptography (Fernet)](https://cryptography.io/en/latest/fernet/) — For encryption and decryption

---

## 🛠️ Installation & Running

```bash
pip install streamlit cryptography
streamlit run your_script_name.py
