import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return """
<!DOCTYPE html>
<html lang="fr"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"/>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<style>
*{margin:0;padding:0;box-sizing:border-box;font-family:-apple-system,BlinkMacSystemFont,sans-serif}
body{background:#F6F1E8;padding-bottom:80px}
.header{height:110px;background:linear-gradient(rgba(0,0,0,0.3),rgba(0,0,0,0.3)),url('https://images.unsplash.com/photo-1509316975850-ff9c5deb0cd9') center/cover;color:white;padding:20px 16px;display:flex;flex-direction:column;justify-content:center}
.header h1{font-size:24px;font-weight:900;letter-spacing:-0.5px}
.header p{font-size:11px;opacity:0.9;margin-top:4px}
#map{height:220px;width:100%;z-index:1}
.route-bar{background:white;margin:-15px 12px 0;position:relative;z-index:2;border-radius:30px;padding:10px 12px;display:flex;align-items:center;justify-content:space-between;box-shadow:0 4px 20px rgba(0,0,0,0.15)}
.dot{width:28px;height:28px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:bold;font-size:12px;color:white}
.dotA{background:#00C853}.dotB{background:#D50000}
.route-line{flex:1;margin:0 8px;display:flex;align-items:center}
.route-line b{font-size:13px;margin-left:6px}
.dist{background:black;color:white;padding:6px 10px;border-radius:20px;font-size:12px;font-weight:bold}
.section{padding:14px 12px 0}
.section-title{font-size:14px;font-weight:800;display:flex;justify-content:space-between}
.badge{background:#FFE082;padding:4px 10px;border-radius:20px;font-size:11px}
.grid{display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px;margin-top:10px}
.card{background:white;border-radius:16px;padding:12px;border:2px solid transparent;cursor:pointer;transition:0.2s}
.card.active{border-color:#00C853;background:#F1F8E9}
.card h3{font-size:13px;margin-top:6px}
.card p{font-size:10px;color:#666;margin-top:2px}
.price{margin-top:8px;display:flex;justify-content:space-between;align-items:end}
.price b{font-size:14px}
.price span{font-size:8px;color:#999;text-align:right;line-height:9px}
.grid2{display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px;margin-top:8px}
.card-dark{background:black;color:white;border-radius:16px;padding:12px;cursor:pointer}
.card-dark.active{border:2px solid #FF6B00}
.card-green{background:#0B3D20;color:white;border-radius:16px;padding:12px;border:2px solid transparent}
.card-green.active{border-color:#00C853;transform:scale(1.02)}
.card-brown{background:#4E342E;color:white;border-radius:16px;padding:12px}
.price-box{background:white;border-radius:16px;padding:12px;margin:12px;display:flex;justify-content:space-between;align-items:center;box-shadow:0 2px 10px rgba(0,0,0,0.08)}
.pill{padding:4px 8px;border-radius:20px;font-size:10px;font-weight:bold}
.btns{display:flex;gap:8px;padding:0 12px}
.btn{flex:1;padding:14px;border-radius:12px;font-weight:800;border:none;font-size:13px;cursor:pointer}
.btn-black{background:black;color:white}.btn-white{background:white;border:1px solid #ddd}
.nav{position:fixed;bottom:0;left:0;right:0;background:white;display:flex;justify-content:space-around;padding:8px 0 14px;border-top:1px solid #eee;z-index:10}
.nav div{text-align:center;font-size:10px;color:#888}
.nav .active{color:black;font-weight:bold}
.icon{font-size:18px}
</style></head><body>
<div class="header"><h1>OU ALLONS-NOUS?</h1><p>Nature Burkinabé • Baobabs • Ouagadougou</p></div>
<div id="map"></div>
<div class="route-bar">
  <div style="display:flex;align-items:center;flex:1"><div class="dot dotA">A</div><div class="route-line"><b id="from">Secteur 35</b></div></div>
  <div style="display:flex;align-items:center;flex:1"><div class="dot dotB">B</div><div class="route-line"><b id="to">Kalgodin</b></div></div>
  <div class="dist" id="dist">3.7km</div>
</div>
<div class="section">
  <div class="section-title"><span>CHOISIR • <span style="color:#00C853">ULTRA</span></span><span class="badge" id="routeBadge">Secteur 10 → Kalgodin</span></div>
  <div class="grid">
    <div class="card active" onclick="selectRide(this,'economie',1321)"><div class="icon">🚗</div><h3>ECONOMIE</h3><p>Voiture clim • 4 places</p><div class="price"><b>1321F</b><span>40F E<br>225F A</span></div></div>
    <div class="card" onclick="selectRide(this,'moto',991)"><div class="icon">🏍️</div><h3>MOTO</h3><p>Rapide • 1 place</p><div class="price"><b>991F</b><span>30F E<br>168F A</span></div></div>
    <div class="card" onclick="selectRide(this,'tricycle',1189)"><div class="icon">🛺</div><h3>TRICYCLE</h3><p>Bagage • 3 places</p><div class="price"><b>1189F</b><span>36F E<br>202F A</span></div></div>
  </div>
  <div class="grid2">
    <div class="card-dark" onclick="selectRide(this,'pro',2774)"><div class="icon">🎩</div><h3>PRO</h3><p style="font-size:9px;opacity:0.7">Business • Costume</p><div class="price" style="margin-top:12px"><b>2774F</b><span style="color:#aaa">83F E<br>472F A</span></div></div>
    <div class="card-green active" onclick="selectRide(this,'ultra',3831)"><div class="icon">🚙</div><h3>ULTRA</h3><p style="font-size:9px">SUV Nature BF</p><div class="price" style="margin-top:12px"><b>3831F</b><span>115F E<br>651F A</span></div></div>
    <div class="card-brown" onclick="selectRide(this,'except',6605)"><div class="icon">👑</div><h3>EXCEPT</h3><p style="font-size:9px">V8 Luxe • VIP</p><div class="price" style="margin-top:12px"><b>6605F</b><span>198F E<br>1123F A</span></div></div>
  </div>
</div>
<div class="price-box">
  <div><b id="totalPrice" style="font-size:18px">1321 FCFA</b><p style="font-size:10px;color:#666">💰 1321F CASH • 🚗 1.9km • bouge</p></div>
  <div style="display:flex;gap:4px"><span class="pill" style="background:#E8F5E9">1056F 80%</span><span class="pill" style="background:#FFF3E0">225F 17%</span><span class="pill" style="background:#FFEBEE">40F 3%</span></div>
</div>
<div class="btns">
  <button class="btn btn-black" onclick="commander()">⚡ COMMANDER <span id="btnPrice">1321F</span></button>
  <button class="btn btn-white" onclick="voirChauffeurs()">👀 CHAUFFEURS</button>
</div>
<div class="nav">
  <div class="active"><div class="icon">🏠</div>Accueil</div>
  <div onclick="voirChauffeurs()"><div class="icon">🚗</div>Chauffeurs</div>
  <div><div class="icon">📜</div>Courses</div>
  <div><div class="icon">👤</div>Profil</div>
  <div onclick="openMenu()"><div class="icon">☰</div>Menu</div>
</div>
<script>
let currentPrice=1321;
var map=L.map('map',{zoomControl:false}).setView([12.3714,-1.5197],13);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);
let a=L.marker([12.3714,-1.5197]).addTo(map);
let b=L.marker([12.355,-1.48]).addTo(map);
let carIcon=L.divIcon({html:'<div style="background:black;border-radius:50%;width:28px;height:28px;display:flex;align-items:center;justify-content:center">🚗</div>',className:'',iconSize:[28,28]});
let car=L.marker([12.365,-1.505],{icon:carIcon}).addTo(map);
let line=L.polyline([[12.3714,-1.5197],[12.355,-1.48]],{color:'#00C853',weight:4,dashArray:'10,10'}).addTo(map);
function selectRide(el,type,price){
  document.querySelectorAll('.card,.card-dark,.card-green,.card-brown').forEach(c=>c.classList.remove('active'));
  el.classList.add('active');currentPrice=price;
  document.getElementById('totalPrice').innerText=price+' FCFA';
  document.getElementById('btnPrice').innerText=price+'F';
}
function commander(){
  let msg=`Bonjour Wataotao! Je commande course ${document.getElementById('from').innerText} -> ${document.getElementById('to').innerText} - ${currentPrice}F - Type ULTRA`;
  window.open('https://wa.me/22670000000?text='+encodeURIComponent(msg),'_blank');
}
function voirChauffeurs(){alert('🚗 Chauffeur le plus proche: Moussa - 2min - Toyota Corolla blanche - 12.36,-1.51 - Il arrive!');}
function openMenu(){alert('MENU WATAOTAO:\\n\\n👤 Profil\\n💰 Parrainage: Invite ami = 500F\\n🎧 Support: +226 70 00 00 00\\n📜 Mes courses\\n⚙️ Paramètres\\n\\nTexte Grand CARACTÈRE et minuscule comme Uber');}
// animation voiture
let i=0;setInterval(()=>{i+=0.02;if(i>1)i=0;let lat=12.3714+(12.355-12.3714)*i;let lng=-1.5197+(-1.48+1.5197)*i;car.setLatLng([lat,lng])},200);
</script></body></html>
    """
if __name__=='__main__':
    port=int(os.environ.get('PORT',5000));app.run(host='0.0.0.0',port=port)
