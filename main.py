from fastapi import FastAPI
from models import *
import config
import psycopg2

conn = psycopg2.connect(dbname=config.DBNAME, user=config.DBUSER, password=config.DBPASS, host=config.DBHOST)

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Meow!"}

@app.post("/login", response_model = AuthResp)
async def login(user: UserLogin):
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE login=%s AND password=%s;",(user.login,user.password))
    res = cur.fetchone()
    if (res):
        return AuthResp(res=res[0])
    else:
        return AuthResp(res=-1)

@app.post("/register", response_model = AuthResp)
async def register(user: UserLogin):
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE login=%s;",(user.login,))
    res = cur.fetchone()
    if (res):
        return AuthResp(res=-1)
    else:
        cur.execute("INSERT INTO users (login, password) VALUES (%s,%s) RETURNING id;",(user.login, user.password))
        newid = cur.fetchone()[0]
        conn.commit()
        return AuthResp(res=newid)