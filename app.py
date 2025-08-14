from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
import time

app = Flask(__name__)

# Lista de fontes de notícias (título e URL)
SOURCES = [
    # Internacionais
    {"name": "CoinDesk", "url": "https://www.coindesk.com/"},
    {"name": "CoinTelegraph", "url": "https://cointelegraph.com/"},
    {"name": "CryptoSlate", "url": "https://cryptoslate.com/"},
    {"name": "The Block", "url": "https://www.theblock.co/"},
    {"name": "Bitcoin Magazine", "url": "https://bitcoinmagazine.com/"},
    
    # Nacionais
    {"name": "Portal do Bitcoin", "url": "https://portaldobitcoin.com/"},
    {"name": "CriptoFácil", "url": "https://www.criptofacil.com/"},
    {"name": "Livecoins", "url": "https://www.livecoins.com.br/"},
    {"name": "BitcoinTrade Blog", "url": "https://blog.bitcointrade.com.br/"},
    {"name": "Cointelegraph Brasil", "url": "https://br.cointelegraph.com/"}
]

# Cache para notícias
CACHE = {"timestamp": 0, "noticias": []}
CACHE_TTL = 600  # 10 minutos

def coletar_noticias():
    global CACHE
    # Retorna cache se ainda válido
    if time.time() - CACHE["timestamp"] < CACHE_TTL:
        return CACHE["noticias"]

    noticias = []
    for source in SOURCES:
        try:
            response = requests.get(source["url"], timeout=5)
            soup = BeautifulSoup(response.content, "html.parser")
            
            # Pegando os títulos mais comuns de notícias (h2 e h3)
            for tag in soup.find_all(["h2", "h3"], limit=5):
                title = tag.get_text(strip=True)
                link = tag.find("a")
                url = link["href"] if link else source["url"]
                noticias.append({
                    "titulo": title,
                    "link": url,
                    "fonte": source["name"]
                })
        except:
            continue

    # Atualiza cache
    CACHE = {"timestamp": time.time(), "noticias": noticias}
    return noticias

@app.route("/")
def home():
    return render_template("home.html", title="Gustavo Franco")

@app.route("/news")
def news():
    noticias = coletar_noticias()
    return render_template("news.html", title="Notícias de Cripto", noticias=noticias)

if __name__ == "__main__":
    app.run(debug=True)
