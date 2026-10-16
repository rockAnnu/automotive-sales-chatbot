#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[4]:


df=pd.read_csv(r"E:\Data Analytic project\automotive_sales_data.csv")


# In[5]:


df.shape


# In[6]:


df.head()


# In[7]:


df.columns.tolist()


# In[33]:


get_ipython().system('pip install pandas plotly openai python-dotenv streamlit')


# In[8]:


import os
os.getcwd()


# In[9]:


import os

for root, dirs, files in os.walk(r"C:\Users\anami"):
    if "db.py" in files:
        print(os.path.join(root, "db.py"))


# In[10]:


import os
os.chdir(r"E:\Data Analytic project")


# In[11]:


os.listdir()


# In[12]:


get_ipython().run_line_magic('run', 'db.py')


# In[13]:


import os

print(os.listdir())


# In[14]:


import sqlite3
import pandas as pd

df = pd.read_csv("automotive_sales_data.csv")

conn = sqlite3.connect("analytics.db")

df.to_sql("sales", conn, if_exists="replace", index=False)

conn.close()

print("Database created successfully!")


# In[15]:


import sqlite3

conn = sqlite3.connect("analytics.db")

tables = conn.execute(
    "SELECT name FROM sqlite_master WHERE type='table';"
).fetchall()

print(tables)


# In[16]:


conn = sqlite3.connect("analytics.db")

result = conn.execute("SELECT * FROM sales LIMIT 5;").fetchall()

for row in result:
    print(row)

conn.close()


# In[17]:


import pandas as pd
import sqlite3

conn = sqlite3.connect("analytics.db")

df = pd.read_sql("SELECT * FROM sales LIMIT 10;", conn)

df


# In[18]:


df.columns.tolist()


# In[19]:


query = """
SELECT 
    region,
    SUM(sales_amount) AS total_sales
FROM sales
GROUP BY region
ORDER BY total_sales DESC;
"""

result = pd.read_sql(query, conn)

result


# In[20]:


df.columns.tolist()


# In[21]:


import analytics_engine


# In[22]:


from analytics_engine import question_to_sql


# In[23]:


get_ipython().run_cell_magic('writefile', '.env', 'OPENAI_API_KEY=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\nOPENAI_MODEL=gpt-5')


# In[24]:


import os

print(os.path.exists(".env"))


# In[25]:


from dotenv import load_dotenv
import os

load_dotenv()

print(bool(os.getenv("OPENAI_API_KEY")))


# API=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

# In[26]:


from dotenv import load_dotenv
import os

load_dotenv()

print(bool(os.getenv("OPENAI_API_KEY")))


# In[27]:


from dotenv import load_dotenv
import os

load_dotenv()

print(bool(os.getenv("OPENAI_API_KEY")))


# In[28]:


import os

os.chdir(r"E:\Data Analytic project")

print(os.getcwd())


# In[29]:


import os

print(os.listdir())


# In[30]:


import db

print(db.__file__)


# In[31]:


import sys
import importlib

sys.path.insert(0, r"E:\Data Analytic project")

import db
db = importlib.reload(db)

print(db.__file__)


# In[32]:


print(db.DATA_PATH)


# In[33]:


import importlib
import db

db = importlib.reload(db)

print(db.DATA_PATH)


# In[34]:


from dotenv import load_dotenv
import os

load_dotenv()

print(bool(os.getenv("OPENAI_API_KEY")))


# In[35]:


print(bool(os.getenv("OPENAI_API_KEY")))


# In[36]:


import sqlite3

conn = sqlite3.connect(r"E:\Data Analytic project\analytics.db")

tables = conn.execute("""
SELECT name
FROM sqlite_master
WHERE type='table';
""").fetchall()

print(tables)

conn.close()


# In[37]:


conn = sqlite3.connect(r"E:\Data Analytic project\analytics.db")

columns = conn.execute("PRAGMA table_info(sales);").fetchall()

for column in columns:
    print(column)

conn.close()


# In[38]:


conn = sqlite3.connect(r"E:\Data Analytic project\analytics.db")

result = conn.execute("""
SELECT COUNT(*)
FROM automotive_sales;
""").fetchone()

print(result)

conn.close()


# In[39]:


import sqlite3

conn = sqlite3.connect(r"E:\Data Analytic project\analytics.db")

for table in ["sales", "automotive_sales"]:
    print("\nTABLE:", table)
    
    columns = conn.execute(f"PRAGMA table_info({table});").fetchall()
    
    for column in columns:
        print(column)

conn.close()


# In[40]:


import sqlite3

conn = sqlite3.connect(r"E:\Data Analytic project\analytics.db")

result = conn.execute("""
SELECT *
FROM sales
LIMIT 5;
""").fetchall()

for row in result:
    print(row)

conn.close()


# In[41]:


import sqlite3

conn = sqlite3.connect(r"E:\Data Analytic project\analytics.db")

result = conn.execute("""
SELECT region, SUM(sales_amount) AS total_sales
FROM sales
GROUP BY region
ORDER BY total_sales DESC;
""").fetchall()

for row in result:
    print(row)

conn.close()


# In[42]:


from db import run_query

result = run_query("""
SELECT region, SUM(sales_amount) AS total_sales
FROM automotive_sales
GROUP BY region
ORDER BY total_sales DESC;
""")

print(result)


# In[43]:


from analytics_engine import question_to_sql


# In[1]:


import ollama

response = ollama.chat(
    model='llama3.2',
    messages=[
        {'role': 'user', 'content': 'Hello'}
    ]
)

print(response['message']['content'])


# In[44]:


import sys
print(sys.executable)


# In[53]:


get_ipython().run_line_magic('pip', 'install ollama')


# In[45]:


import ollama

response = ollama.chat(
    model='llama3.2',
    messages=[
        {'role': 'user', 'content': 'Hello'}
    ]
)

print(response['message']['content'])


# In[46]:


import ollama

response = ollama.chat(
    model="llama3.2",
    messages=[
        {"role": "user", "content": "What is 2 + 2?"}
    ]
)

print(response["message"]["content"])


# In[47]:


import sqlite3

conn = sqlite3.connect(r"E:\Data Analytic project\analytics.db")

cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

print(cursor.fetchall())


# In[48]:


import sqlite3
import ollama

DB_PATH = r"E:\Data Analytic project\analytics.db"

schema = """
Table: sales

Columns:
- id: INTEGER
- date: TEXT
- year: INTEGER
- month_number: INTEGER
- month: TEXT
- financial_year: TEXT
- region: TEXT
- city: TEXT
- model: TEXT
- body_type: TEXT
- fuel_type: TEXT
- retail_volume: INTEGER
- avg_selling_price: INTEGER
- discount_pct: REAL
- sales_amount: REAL
- margin_pct: REAL
- customer_rating: REAL
"""

print(schema)


# In[49]:


def question_to_sql(question):

    prompt = f"""
You are a SQL expert.

Convert the user's question into SQLite SQL.

Database schema:
{schema}

Rules:
- Use only the sales table.
- Return ONLY the SQL query.
- Do not use markdown.
- Do not explain anything.

User question:
{question}
"""

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response["message"]["content"].strip()


# In[50]:


question = "Which region has the highest total sales?"

sql = question_to_sql(question)

print(sql)


# In[51]:


import sqlite3

conn = sqlite3.connect(r"E:\Data Analytic project\analytics.db")

result = conn.execute(sql).fetchone()

print("Highest sales region:", result[0])


# In[52]:


import sqlite3
import ollama

DB_PATH = r"E:\Data Analytic project\analytics.db"

schema = """
Table: sales

Columns:
id, date, year, month_number, month, financial_year,
region, city, model, body_type, fuel_type,
retail_volume, avg_selling_price, discount_pct,
sales_amount, margin_pct, customer_rating
"""

def ask_database(question):

    # 1. Ask Llama to generate SQL
    prompt = f"""
You are a SQL expert.

Convert the user's question into SQLite SQL.

Database schema:
{schema}

Rules:
- Use only the sales table.
- Return ONLY the SQL query.
- Do not use markdown.
- Do not explain anything.

User question:
{question}
"""

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    sql = response["message"]["content"].strip()

    # Remove markdown if Llama adds it
    sql = sql.replace("```sql", "").replace("```", "").strip()

    # 2. Execute SQL
    conn = sqlite3.connect(DB_PATH)

    try:
        result = conn.execute(sql).fetchall()
    finally:
        conn.close()

    # 3. Return SQL + result
    return sql, result


# In[53]:


sql, result = ask_database(
    "Which region has the highest total sales?"
)

print("SQL:")
print(sql)

print("\nResult:")
print(result)


# In[54]:


sql, result = ask_database(
    "What is the total sales amount?"
)

print("SQL:", sql)
print("Result:", result)


# In[55]:


sql, result = ask_database(
    "Which car model has the highest retail volume?"
)

print("SQL:", sql)
print("Result:", result)


# In[ ]:




