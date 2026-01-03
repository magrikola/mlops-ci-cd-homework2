from fastapi import FastAPI


from src.feature_engineering import hash_feature


app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/predict")
def predict(text: str, buckets: int = 1000):
    return {"bucket": hash_feature(text, buckets)}
