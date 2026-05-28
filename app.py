from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hola Mundo"}

@app.get("/sumar")
def sumar(a: int, b: int):
    return {"resultado": a + b}
