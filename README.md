# PlayerTrend
## 1. Ativando o ambiente virtual
Certifique-se de estar na pasta do projeto no terminal

    .venv\Scripts\activate

## 2. Instalando as dependências (requisitos)

    pip install -r requisitos.txt
    pip install -r requisitos-testes.txt

## 3. Como configurar a API para obter a lista de jogos

 1. Acesse o [Steam Web API Documentation](https://steamapi.xpaw.me).
 2. Configure sua *WebAPI key*, o formato de saída como ***JSON*** e o *Pre-fill SteamID*.
 3. Procure na categoria *IStoreService* por [GetAppList](https://steamapi.xpaw.me/#IStoreService/GetAppList).
 4. Deixe todos os parâmetros do tipo **bool** desativados, para que sejam incluídos como *false* no endereço final da API, **com exceção de *include_games* que deve ser ativada**.
 5. O campo *max_results* deve ser preenchido com o valor **50000** (cinquenta mil)![Como deve ficar](https://i.imgur.com/xk9zYVS.png)
 6. Em **obter_jogos.py** cole o endereço da API gerada na variável *url*.
 7. Execute o arquivo com sua API através do comando: `python .\obter_jogos.py`
 ## 4. Iniciar a aplicação PlayerTrend para Steam
 
    python .\playertrend.py

 Para encerrar pressione CTRL + C no terminal.
 ## 5. Executando testes
 As dependências para execução dos testes estão em um arquivo txt separado, que teve o comando para instalação mencionado no tópico 2.

    pytest -v .\tests\test_playertrend.py
