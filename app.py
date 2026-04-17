

from flask import Flask

app = Flask(__name__)

@app.route("/")
def healthcheck():
    return {"status": "ok", "message": "Aplicação funcionando"}

@app.route("/vendas")
def vendas():
    return {
        "total_vendas": 150000,
        "ticket_medio": 320.50
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
