import hashlib

def hash_password(password):
    """
    Hash the password using SHA-256 and return the hexadecimal digest.
    """
    return hashlib.sha256(password.encode()).hexdigest()

def check_login(email, password, login_data):
    """
    Check if the email exists and the password matches the stored hash.
    """
    if email in login_data:
        return login_data[email] == hash_password(password)
    return False

def show_message(success):
    """
    Print login result message.
    """
    if success:
        print("✅ Login Successful!")
    else:
        print("❌ Login Failed! Please check your email or password.")

def main():
    # Login credentials (email: hashed_password)
    login_data = {
        "user@example.com": hash_password("securepassword123"),
        "admin@kalav.com": hash_password("mysecretpass")
    }

    print("🔐 Welcome to the Secure Login System")
    print("-" * 40)

    # User input
    email = input("📧 Enter Email: ").strip()
    password = input("🔑 Enter Password: ").strip()

    # Validate login
    result = check_login(email, password, login_data)
    show_message(result)

if __name__ == '__main__':
    main()
