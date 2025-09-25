# E-Shop Brasil — Projeto Acadêmico

## 📌 Introdução
A **E-Shop Brasil** é uma grande plataforma de e-commerce que enfrenta desafios em **gestão de dados** (segurança, LGPD, personalização) e **logística** (estoque e entregas).  
Este projeto propõe uma solução prática usando **MongoDB, Streamlit e Docker**.

---

## 🎯 Objetivos
- Demonstrar CRUD em MongoDB.  
- Realizar consultas e concatenações de dados.  
- Fornecer uma interface simples em Streamlit.  
- Garantir reprodutibilidade com Docker.  

---

## 🏗 Arquitetura
- **MongoDB**: banco NoSQL.  
- **Streamlit**: interface gráfica.  
- **Docker Compose**: orquestração local.  

---

## ⚙️ Como Rodar
```bash
git clone https://github.com/seu-usuario/eshop-brasil-bd-bigdata.git
cd eshop-brasil-bd-bigdata
docker-compose up -d
streamlit run app.py
