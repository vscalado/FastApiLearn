from fastapi import FastAPI

app = FastAPI()

@app.get('/helth-check')
def health_check():
    return True