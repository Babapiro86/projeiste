from flask import Flask, jsonify
from pathlib import Path
import random
import string

app = Flask(__name__)

B = [
    "Akıllı telefon ve sosyal medya dopamin bağımlılığını tetikleyebilir.",
    "Ekran süresini 2 saatin altında tutmak uykuyu iyileştirir.",
    "Sürekli bildirimler dikkat dağınıklığına yol açar.",
    "Mavi ışık melatonin salgısını azaltır.",
    "Dijital detoks zihinsel dinlenmeye yardımcı olur.",
    "Sosyal medya gerçek ilişkileri zayıflatabilir.",
    "Uygulama tasarımcıları bağımlılık mekanizmaları kullanır.",
    "FOMO telefona bakma isteğini artırır.",
    "Çocuklarda ekran bağımlılığı gelişimi geciktirebilir.",
    "Nomofobi (telefonsuz kalma korkusu) yaygındır.",
]

@app.route("/")
def i():
    # index.html dosyasının Python dosyasıyla aynı klasörde olduğundan emin ol
    try:
        html_content = (Path(__file__).parent / "index.html").read_text(encoding="utf-8")
    except FileNotFoundError:
        html_content = "<h1>Ana Sayfa</h1>" # Dosya yoksa hata vermemesi için
        
    links = """
    <br><br>
    <hr>
    <h3>Nereye gitmek istersin?</h3>
    <ul>
        <li><a href="/random_fact">Rastgele Bilgi Öğren</a></li>
        <li><a href="/yazi_tura">Yazı mı Tura mı?</a></li>
        <li><a href="/sifre_olustur">Güvenli Şifre Al</a></li>
    </ul>
    """
    return html_content + links

@app.route("/random_fact")
def random_fact():
    fact = random.choice(B)
    return f'<h1>Rastgele Gerçek</h1><p>{fact}</p><br><a href="/">Ana Sayfaya Dön</a>'

@app.route("/yazi_tura")
def yazi_tura():
    sonuc = random.choice(["YAZI", "TURA"])
    return f"""
        <h1>🪙 Yazı-Tura Sonucu</h1>
        <h2 style='color: blue;'>{sonuc}</h2>
        <br><a href="/yazi_tura">Tekrar At!</a> | <a href="/">Ana Sayfaya Dön</a>
    """

@app.route("/sifre_olustur")
def sifre():
    # HATA BURADAYDI: Karakter seçimi ve döngü tamamlandı
    karakterler = string.ascii_letters + string.digits + string.punctuation
    sifre_sonuc = "".join(random.choice(karakterler) for _ in range(12))
    return f"""
        <h1>🔐 Rastgele Şifre</h1>
        <code style='font-size: 20px; background: #eee; padding: 5px;'>{sifre_sonuc}</code>
        <p>Sayfayı yenileyerek yeni bir şifre alabilirsin.</p>
        <br><a href="/">Ana Sayfaya Dön</a>
    """

@app.route("/api/bilgi")
def a():
    return jsonify({"cumleler": random.sample(B, 3)})

# HATA BURADAYDI: Uygulamayı başlatan kısım eklendi
if __name__ == "__main__":
    app.run(debug=True)
