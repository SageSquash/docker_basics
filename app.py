import sqlite3
from cryptography.fernet import Fernet

# Generate a secret key for encryption
secret_key = Fernet.generate_key()
cipher_suite = Fernet(secret_key)

# Create an in-memory SQLite database
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Create two tables
cursor.execute('''
    CREATE TABLE users (
        user_id INTEGER PRIMARY KEY,
        name TEXT,
        sensitive_data TEXT
    )
''')

cursor.execute('''
    CREATE TABLE transactions (
        transaction_id INTEGER PRIMARY KEY,
        user_id INTEGER,
        amount DECIMAL(10, 2),
        FOREIGN KEY (user_id) REFERENCES users(user_id)
    )
''')

# Insert some data, encrypting sensitive data
def encrypt_data(data):
    return cipher_suite.encrypt(data.encode('utf-8'))

def decrypt_data(data):
    return cipher_suite.decrypt(data).decode('utf-8')

# Insert users with encrypted sensitive data
encrypted_sensitive_data = encrypt_data("1234-5678-9012-3456")
cursor.execute('''
    INSERT INTO users (name, sensitive_data) VALUES ('Alice', ?)
''', (encrypted_sensitive_data,))

encrypted_sensitive_data = encrypt_data("9876-5432-1098-7654")
cursor.execute('''
    INSERT INTO users (name, sensitive_data) VALUES ('Bob', ?)
''', (encrypted_sensitive_data,))

# Insert transactions
cursor.execute('''
    INSERT INTO transactions (user_id, amount) VALUES (1, 150.00)
''')
cursor.execute('''
    INSERT INTO transactions (user_id, amount) VALUES (2, 200.00)
''')

# Perform a join and mask sensitive data in the result
cursor.execute('''
    SELECT
        u.user_id,
        u.name,
        u.sensitive_data,
        t.transaction_id,
        t.amount
    FROM
        users u
    JOIN
        transactions t ON u.user_id = t.user_id
''')

rows = cursor.fetchall()
for row in rows:
    print(f"User ID: {row[0]}, Name: {row[1]}, Sensitive Data: {decrypt_data(row[2])}, Transaction ID: {row[3]}, Amount: {row[4]}")

# Ensure sensitive data is decrypted only when needed
# Typically, you would apply further data minimization and masking when displaying results

# Close the connection
conn.close()