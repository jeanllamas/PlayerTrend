Feature: Testes de uso do PlayerTrend para Steam
    Scenario: Usuário insere um jogo válido
        Given O usuário está na tela de início
        When O usuário procura pelo jogo Elden Ring
        And O usuário clica no botão de pesquisar
        Then O usuário visualiza o gráfico, o nome do jogo e a tendência

    Scenario: Usuário obtêm mais de uma ocorrência
        Given O usuário está na tela de início
        When O usuário procura pelo jogo Dark Souls
        And O usuário clica no botão de pesquisar
        Then O sistema identifica mais de uma ocorrência
        And O usuário escolhe a opção do Dark Souls III
        And O usuário visualiza o gráfico, o nome do jogo e a tendência

    Scenario: Usuário insere um jogo inválido
        Given O usuário está na tela de início
        When O usuário procura por Jogo Inválido
        And O usuário clica no botão de pesquisar
        Then O usuário recebe um erro de jogo não encontrado

    Scenario: Usuário não insere nada no campo de busca
        Given O usuário está na tela de início
        When O usuário clica diretamente no botão de pesquisar
        Then O usuário recebe um alerta para inserir algum texto

    Scenario: Usuário insere um jogo sem dados suficientes
        Given O usuário está na tela de início
        When O usuário procura por Silent Hill 2
        And O usuário clica no botão de pesquisar
        Then O usuário recebe a mensagem de erro por dados insuficientes

    Scenario: Usuário insere um jogo inexistente pela URL
        Given O usuário está na tela de início
        When O usuário acessa pelo endereço um código de jogo inexistente
        Then O usuário recebe um erro de carregamento dos dados