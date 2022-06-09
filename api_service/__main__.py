from fastapi import FastAPI, Query
import uvicorn

app = FastAPI()


@app.get("/address")
def root():
    """
    This is method to get data about entered ethereum address, please send the address parameter
    """
    return '15'


@app.post("/transaction")
def root():

    return '10'

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)