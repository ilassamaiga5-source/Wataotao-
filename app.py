import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html><head><meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body{margin:0;font-family:sans-serif;background:#FFF7ED;text-align:center}
        .top{background:#FF6B00;color:white;padding:25px}
        .logo{font-size:38px;font-weight:bold}
        .card{background:white;margin:15px;border-radius:16px;padding:20px;box-shadow:0 4px 12px rgba(0,0,0,0.1)}
        .btn{background:#25D366;color:white;padding:16px 32px;border-radius:30px;text-decoration:none;display:inline-block;font-weight:bold;font-size:18px;margin-top:10px}
        .btn2{background:#FF6B00}
        .grid{display:grid;grid-template-columns:1fr 1fr;gap:10px}
        .item{background:#FFF0E0;padding:15px;border-radius:12px}
    </style></head><body>
        <div class="top"><div class="logo">WATAOTAO 🛵</div><p>Livraison rapide Ouaga - Le client est roi</p></div>
        <div class="card"><h3>Bienvenue sur Wataotao Client!</h3><p>Commande ton plat, colis, course en 1 clic</p>
        <a class="btn" href="https://wa.me/22600000000?text=Bonjour Wataotao, je veux commander">Commander sur WhatsApp</a></div>
        <div class="card"><div class="grid">
            <div class="item">🍔<br><b>Restauration</b></div>
            <div class="item">📦<br><b>Colis</b></div>
            <div class="item">🛒<br><b>Courses</b></div>
            <div class="item">🏍️<br><b>Courses Moto</b></div>
        </div></div>
        <div class="card"><p>📍 Ouagadougou, Kadiogo - Disponible 7j/7</p><a class="btn btn2" href="tel:+22600000000">Appeler un livreur</a></div>
    </body></html>
    """
if __name__ == '__main__':
    port=int(os.environ.get('PORT',5000))
    app.run(host='0.0.0.0',port=port)
