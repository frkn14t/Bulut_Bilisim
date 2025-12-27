from flask import Flask

app = Flask(__name__)

@app.get("/")
def home():
    return "Hello from Cloud Run, HELLO FURKAN! GÜNCELLEME 2"

@app.get("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    # Cloud Run, PORT environment variable kullanır
    import os
    port = int(os.environ.get("PORT", "8080"))
    app.run(host="0.0.0.0", port=port)
