import requests, sqlite3, time
from playertrend import normalizar_pesquisa as normalizar_nome


def obter_jogos(ultimo_appid=None):
    url = f"SUA URL DE API AQUI ENTRE AS ASPAS DUPLAS"
    if ultimo_appid:
        url += f"&last_appid={ultimo_appid}"

    response = requests.get(url)
    response.raise_for_status()
    return response.json()


conn = sqlite3.connect("jogos_steam.db")
c = conn.cursor()

c.execute(
    """
    CREATE TABLE IF NOT EXISTS jogos (
        app_id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL
    )
    """
)

ultimo_appid = None
while True:
    # Obter os dados da API
    dados = obter_jogos(ultimo_appid)

    # Extrair a lista de jogos
    jogos = dados["response"]["apps"]

    for jogo in jogos:
        nome = normalizar_nome(jogo["name"])  # Normaliza o nome antes de inserir
        c.execute(
            "INSERT OR IGNORE INTO jogos (app_id, nome) VALUES (?, ?)",
            (jogo["appid"], nome),
        )

    conn.commit()

    # Verificar se há mais resultados para buscar
    if not dados["response"].get("have_more_results"):
        break

    # Atualizar o ultimo_appid para a próxima requisição
    ultimo_appid = dados["response"].get("last_appid")

    if not ultimo_appid:
        break

    time.sleep(3)

conn.close()

print("Todos os jogos foram inseridos no banco de dados")
