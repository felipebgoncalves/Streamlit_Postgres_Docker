import streamlit as st
import psycopg2
import os

# Connect to the PostgreSQL database
def connect_db():
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST'),
        database=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASS'),
        port=os.getenv('DB_PORT')
        )
    return conn

def create_table():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS messages (message TEXT)")
    conn.commit()
    cur.close()
    conn.close()

def add_message(message: str):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO messages (message) VALUES (%s)", (message,))
    conn.commit()
    cur.close()
    conn.close()

def get_messages():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT message FROM messages")
    messages = cur.fetchall()
    cur.close()
    conn.close()
    return messages

def main():
    st.title("Message Board")
    create_table()

    message = st.text_input('Add a new message:')
    if st.button('Submit'):
        add_message(message)
        st.success('Message added successfully!')

    st.subheader('Messages')
    messages = get_messages()

    for message in messages:
        st.write(message[0])


if __name__ == '__main__':
    main()