from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from bson import ObjectId
from pymongo import MongoClient  
from datetime import datetime, date

client = MongoClient("mongodb+srv://joaograboski07:2305Graboskii@cluster0.74inz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["API"]  # banco
collection = db["JackAPI"]  # coleção

app = FastAPI()

class Pessoa(BaseModel):
    nome: str
    datanasc: date  

# função para colocar o horário no mínimo (p/ignorar hora)
def converter_data_para_datetime(data_nasc: date) -> datetime:
    return datetime.combine(data_nasc, datetime.min.time())

def serialize_id(pessoa):
    pessoa["_id"] = str(pessoa["_id"])  
    return pessoa

# Cadastrar Nova Pessoa
@app.post("/pessoas", response_model=Pessoa)
async def criar_pessoa(pessoa: Pessoa):
    pessoa_dict = pessoa.dict()
    pessoa_dict['datanasc'] = converter_data_para_datetime(pessoa.datanasc)
    result = collection.insert_one(pessoa_dict)  
    pessoa_dict["_id"] = str(result.inserted_id)  
    return pessoa_dict

# Listar Pessoas Cadastradas
@app.get("/pessoas", response_model=List[Pessoa])
async def listar_pessoas():
    pessoas = collection.find() 
    return [serialize_id(pessoa) for pessoa in pessoas]  

# Atualizar Pessoa do Cadastro
@app.put("/pessoas/{pessoa_id}", response_model=Pessoa)
async def atualizar_pessoa(pessoa_id: str, pessoa: Pessoa):
    pessoa_dict = pessoa.dict()
    if 'datanasc' in pessoa_dict:
        pessoa_dict['datanasc'] = converter_data_para_datetime(pessoa.datanasc)

    result = collection.update_one(
        {"_id": ObjectId(pessoa_id)}, {"$set": pessoa_dict}  
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Essa pessoa não existe no cadastro")
    
    pessoa_dict["_id"] = pessoa_id 
    return pessoa_dict

# Deletar Pessoa Cadastrada
@app.delete("/pessoas/{pessoa_id}", response_model=dict)
async def excluir_pessoa(pessoa_id: str):
    result = collection.delete_one({"_id": ObjectId(pessoa_id)})  
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Pessoa não encontrada")
    return {"message": "A pessoa foi excluída com sucesso"}
