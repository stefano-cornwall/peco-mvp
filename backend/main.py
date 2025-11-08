from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "PeCo by Nexense backend running"}
