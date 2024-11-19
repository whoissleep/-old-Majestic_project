import psycopg2
import numpy as np
import pickle

conn = psycopg2.connect(
    dbname="clothes_db",
    user='test_user',
    password='123123',
    host='localhost',
    port="5432"
)

curr = conn.cursor()

def create_table(lang):
    curr.execute(f"""
    CREATE TABLE IF NOT EXISTS clothes_{lang} (
        id SERIAL PRIMARY KEY,
        clothes VARCHAR(255),
        vectors FLOAT8[]
    );
    """)
    conn.commit()
    print(f"Done for {lang} language")


def insert_data(language, clothes_names, vectors):

    conn = psycopg2.connect(
        dbname="clothes_db",
        user='test_user',
        password='123123',
        host='localhost',
        port="5432"
    )

    curr = conn.cursor()
    
    for clothes_name, vector in zip(clothes_names, vectors):
        vector_list = vector.tolist() if isinstance(vector, np.ndarray) else vector
        
        curr.execute(f"""
        INSERT INTO clothes_{language} (clothes, vectors)
        VALUES (%s, %s);
        """, (clothes_name, vector_list))

    conn.commit()
    curr.close()
    conn.close()

def fetch_data(language):
    conn = psycopg2.connect(
        dbname="clothes_db",
        user='test_user',
        password='123123',
        host='localhost',
        port="5432"
    )

    curr = conn.cursor()

    curr.execute(f"SELECT clothes, vectors FROM clothes_{language};")
    rows = curr.fetchall()

    clothes_dict = {}

    for row in rows:
        clothes_name = row[0]
        vector = pickle.loads(row[1]) if isinstance(row[1], bytes) else row[1]
        
        clothes_dict[clothes_name] = vector

    curr.close()
    conn.close()

    return clothes_dict

langs = ['ru', 'en', 'pl', 'pt', 'ukr', 'de']
for lang in langs:
    create_table(lang)

curr.close()
conn.close()