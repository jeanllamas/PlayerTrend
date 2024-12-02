from datetime import datetime
from flask import Flask, jsonify, redirect, render_template, request, url_for
from waitress import serve
from bs4 import BeautifulSoup
import logging, requests, locale, sqlite3, re, unicodedata

logging.basicConfig(level=logging.DEBUG)

playertrend = Flask(__name__)


def calcularRegressaoLinear(jogadores):
    n = len(jogadores)  # Quantidade de valores a serem considerados
    x = list(range(1, n + 1))  # Número de meses
    y = jogadores

    # Somatórios de cada coluna da fórmula de regressão linear
    soma_x = sum(x)
    soma_y = sum(y)
    soma_xy = sum(x[i] * y[i] for i in range(n))
    soma_x2 = sum(x_i**2 for x_i in x)

    # Coeficiente Angular (Inclinação)
    B = (n * soma_xy - soma_x * soma_y) / (n * soma_x2 - soma_x**2)

    # Intercepto (Reta)
    A = (soma_y - B * soma_x) / n

    # Regressão Linear
    y_previsto = [B * x_i + A for x_i in x]

    # Tendência da inclinação
    tendencia = "subir" if B > 0 else "descer"

    return y_previsto, tendencia


def gerarNomeMesesAnteriores():
    locale.setlocale(locale.LC_TIME, "pt_BR.UTF-8")

    data_atual = datetime.now()
    mes_atual = data_atual.month
    ano_atual = data_atual.year

    meses_anteriores = []

    for i in range(1, 13):
        mes = (mes_atual - i - 1) % 12 + 1
        ano = ano_atual if mes_atual - i > 0 else ano_atual - 1

        data = datetime(ano, mes, 1)
        meses_anteriores.append(data.strftime("%b/%y"))

    meses_anteriores.reverse()
    return meses_anteriores


@playertrend.route("/")
def telaInicial():
    return render_template("inicio.html")


def normalizar_pesquisa(pesquisa):
    pesquisa = pesquisa.lower()
    # Remove caracteres especiais
    pesquisa = re.sub(r"[^\w\s\-]|[®™:,'’‘“”]", "", pesquisa)
    # Troca vários espaços por um único
    pesquisa = re.sub(r"\s+", " ", pesquisa)
    return pesquisa.strip()


@playertrend.route("/busca", methods=["POST"])
def procurarJogo():
    nome_jogo = request.form.get("validarNome").strip()
    # Normaliza antes da busca
    nome_jogo = normalizar_pesquisa(nome_jogo)

    conn = sqlite3.connect("jogos_steam.db")
    c = conn.cursor()

    c.execute(
        """
        SELECT * FROM jogos 
        WHERE LOWER(nome) LIKE ?
        LIMIT 5
        """,
        (f"%{nome_jogo}%",),
    )
    jogos = c.fetchall()  # Busca até 5 correspondências

    conn.close()

    if jogos:
        # Se apenas um jogo for encontrado, redireciona diretamente para ele
        if len(jogos) == 1:
            return redirect(url_for("paginaJogo", id_jogo=jogos[0][0]))
        # Se mais de um jogo for encontrado, mostra as ocorrências
        else:
            return render_template("inicio.html", jogos=jogos)
    else:
        return render_template("inicio.html", erro="Jogo não encontrado.")


@playertrend.route("/dados/<id_jogo>")
def obterDadosJogo(id_jogo):
    url = f"https://steamcharts.com/app/{id_jogo}"
    resposta = requests.get(url)
    soup = BeautifulSoup(resposta.text, "html.parser")

    nome_jogo = soup.find(id="app-title")
    nome_jogo = nome_jogo.get_text()

    todos_os_meses = soup.find_all("td", class_="num-f")
    # Verifica se há dados suficientes com a quantidade de meses
    if len(todos_os_meses) < 12:
        return jsonify(erro="Não há dados suficientes para exibir o gráfico.")

    medias_mensais = [
        float(dado.get_text(strip=True).replace(",", ""))
        for dado in todos_os_meses[1:13]
    ][::-1]

    nomes_meses = gerarNomeMesesAnteriores()
    y_previsto, tendencia = calcularRegressaoLinear(medias_mensais)

    return jsonify(
        nome_jogo=nome_jogo,
        medias_mensais=medias_mensais,
        nomes_meses=nomes_meses,
        regressao_linear=y_previsto,
        tendencia=tendencia,
    )


@playertrend.route("/jogo/<id_jogo>")
def paginaJogo(id_jogo):
    return render_template("base_jogo.html", id_jogo=id_jogo)


if __name__ == "__main__":
    # serve(playertrend, host="127.0.0.1", port=4004)
    playertrend.run(host="127.0.0.1", port=4004, debug=True)
