import streamlit as st
from pymongo import MongoClient
import pandas as pd
from faker import Faker

# ---------- CONFIGURAÇÃO ----------
MONGO_USER = "admin"
MONGO_PASS = "example"
MONGO_HOST = "mongo"  # Nome do serviço no docker-compose
MONGO_PORT = 27017
DB_NAME = "eshop_db"
COLLECTION_NAME = "clientes"

# ---------- CONEXÃO COM MONGO ----------
client = MongoClient(f"mongodb://{MONGO_USER}:{MONGO_PASS}@{MONGO_HOST}:{MONGO_PORT}/")
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

fake = Faker()

# ---------- POPULAÇÃO AUTOMÁTICA ----------
if collection.count_documents({}) == 0:  # Só popula se não houver clientes
    clientes_iniciais = []
    for _ in range(50):  # 50 clientes fictícios
        clientes_iniciais.append({
            "nome": fake.name(),
            "email": fake.email(),
            "cidade": fake.city(),
            "estado": fake.state(),
            "telefone": fake.phone_number()
        })
    collection.insert_many(clientes_iniciais)

# ---------- STREAMLIT ----------
st.title("E-Shop Brasil - Gestão de Clientes")

# ---------- MENU ----------
menu = ["Listar Clientes", "Adicionar Cliente", "Exportar CSV"]
escolha = st.sidebar.selectbox("Menu", menu)

# ---------- LISTAR CLIENTES ----------
if escolha == "Listar Clientes":
    dados = list(collection.find())
    if dados:
        df = pd.DataFrame(dados)
        st.dataframe(df.drop(columns=["_id"]))
    else:
        st.warning("Nenhum cliente cadastrado!")

# ---------- ADICIONAR CLIENTE ----------
elif escolha == "Adicionar Cliente":
    st.subheader("Adicionar Novo Cliente")
    nome = st.text_input("Nome")
    email = st.text_input("Email")
    cidade = st.text_input("Cidade")
    estado = st.text_input("Estado")
    telefone = st.text_input("Telefone")

    if st.button("Adicionar"):
        if nome and email:
            collection.insert_one({
                "nome": nome,
                "email": email,
                "cidade": cidade,
                "estado": estado,
                "telefone": telefone
            })
            st.success(f"Cliente {nome} adicionado!")
        else:
            st.error("Nome e Email são obrigatórios!")

# ---------- EXPORTAR CSV ----------
elif escolha == "Exportar CSV":
    dados = list(collection.find())
    if dados:
        df = pd.DataFrame(dados).drop(columns=["_id"])
        df.to_csv("clientes.csv", index=False)
        st.success("Arquivo clientes.csv gerado!")
        st.download_button("Baixar CSV", df.to_csv(index=False), file_name="clientes.csv")
    else:
        st.warning("Nenhum cliente para exportar!")
