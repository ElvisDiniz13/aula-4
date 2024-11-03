from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def say_hello()
    return{"FastAPI":"Hello"}

@app.get("/{name}")
def say_hi(name:str):
    return{"Name 404":"Não encontrado"}