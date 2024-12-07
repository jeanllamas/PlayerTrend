from pytest_bdd import scenarios, given, when, then

scenarios("../features/consulta_jogos.feature")


# Scenario: Usuário insere um jogo válido
@given("O usuário está na tela de início")
def step_given(tela_inicio):
    pass


@when("O usuário procura pelo jogo Elden Ring")
def step_when(procura_elden_ring):
    pass


@when("O usuário clica no botão de pesquisar")
def step_when(clica_pesquisar):
    pass


@then("O usuário visualiza o gráfico, o nome do jogo e a tendência")
def step_then(tela_jogo):
    pass


# Scenario: Usuário obtêm mais de uma ocorrência
@given("O usuário está na tela de início")
def step_given(tela_inicio):
    pass


@when("O usuário procura pelo jogo Dark Souls")
def step_when(procura_dark_souls):
    pass


@when("O usuário clica no botão de pesquisar")
def step_when(clica_pesquisar):
    pass


@then("O sistema identifica mais de uma ocorrência")
def step_then(outras_ocorrencias):
    pass


@then("O usuário escolhe a opção do Dark Souls III")
def step_then(opcao_dark_souls):
    pass


@then("O usuário visualiza o gráfico, o nome do jogo e a tendência")
def step_then(tela_jogo):
    pass


# Scenario: Usuário insere um jogo inválido
@given("O usuário está na tela de início")
def step_given(tela_inicio):
    pass


@when("O usuário procura por Jogo Inválido")
def step_when(procura_jogo_invalido):
    pass


@when("O usuário clica no botão de pesquisar")
def step_when(clica_pesquisar):
    pass


@then("O usuário recebe um erro de jogo não encontrado")
def step_then(nao_encontrado):
    pass


# Scenario: Usuário não insere nada no campo de busca
@given("O usuário está na tela de início")
def step_given(tela_inicio):
    pass


@when("O usuário clica diretamente no botão de pesquisar")
def step_when(clica_pesquisar):
    pass


@then("O usuário recebe um alerta para inserir algum texto")
def step_then(inserir_texto):
    pass


# Scenario: Usuário insere um jogo sem dados suficientes
@given("O usuário está na tela de início")
def step_given(tela_inicio):
    pass


@when("O usuário procura por Silent Hill 2")
def step_when(procura_silent_hill):
    pass


@when("O usuário clica no botão de pesquisar")
def step_when(clica_pesquisar):
    pass


@then("O usuário recebe a mensagem de erro por dados insuficientes")
def step_then(sem_dados):
    pass


# Scenario: Usuário insere um jogo inexistente pela URL
@given("O usuário está na tela de início")
def step_given(tela_inicio):
    pass


@when("O usuário acessa pelo endereço um código de jogo inexistente")
def step_when(acessa_inexistente):
    pass


@then("O usuário recebe um erro de carregamento dos dados")
def step_then(sem_dados):
    pass
