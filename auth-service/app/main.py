from fastapi import FastAPI, HTTPException
from sqlmodel import Session, select


from app.database import engine, create_db
from app.models.Usuario import User, UserIn  
from app.core.seguridad import encrypt_password_aes, decrypt_password_aes
app = FastAPI(title="API Auth Simple")


@app.on_event("startup")
def on_startup():
    create_db()

@app.post("/register")
def register(user: User): 
    with Session(engine) as session:
        existing = session.exec(select(User).where(User.username == user.username)).first()
        if existing:
            raise HTTPException(status_code=400, detail="El usuario ya existe")

       
        user.encrypted_password = encrypt_password_aes(user.encrypted_password)
        
        session.add(user)
        session.commit()
        session.refresh(user)
        return {"message": "Usuario registrado correctamente", "username": user.username}

@app.post("/login")
def login(user: User):
    with Session(engine) as session:
        db_user = session.exec(select(User).where(User.username == user.username)).first()
        if not db_user:
            return {"message": "Login fallido"}

        password_real = decrypt_password_aes(db_user.encrypted_password)
        if user.encrypted_password == password_real:
            return {"message": "Login exitoso"}

        return {"message": "Login fallido"}