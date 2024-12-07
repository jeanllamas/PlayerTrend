async function buscarDadosJogo() {
	document.getElementById("carregando").style.display = "flex";

	try {
		const response = await fetch(`/dados/${id_jogo}`);
		const dados_jogo = await response.json();

		if (dados_jogo.erro) {
			// Mensagem de erro
			document.getElementById("conteudo").innerHTML = `
				<div class="alert alert-danger" role="alert">
					${dados_jogo.erro}
				</div>
				<div class="row pt-5">
					<div id="col">
						<a class="btn btn-primary" href="/" role="button"><i
								class="bi bi-chevron-left"></i> Voltar</a>
					</div>
				</div>
			`;
			return;
		}

		document.getElementById("nomeJogo").innerText = dados_jogo.nome_jogo;
		document.getElementById("imagemJogo").src = `https://steamcharts.com/assets/steam-images/${id_jogo}.jpg`;
		document.getElementById("tendencia").innerText =
			"Tendência: " + (dados_jogo.tendencia === "subir" ? "⬆ Subindo" : "⬇ Descendo");

		const ctx = document.getElementById("graficoMeses").getContext("2d");
		new Chart(ctx, {
			type: "line",
			data: {
				labels: dados_jogo.nomes_meses,
				datasets: [
					{
						label: "Média de Jogadores",
						data: dados_jogo.medias_mensais,
						fill: false,
					},
					{
						label: "Cálculo de Tendência",
						data: dados_jogo.regressao_linear,
						borderDash: [5, 5],
						fill: false,
					},
				],
			},
			options: {
				maintainAspectRatio: false,
				responsive: true,
				elements: {
					point: {
						pointStyle: "rectRounded",
						radius: 5,
						hoverRadius: 10,
					},
				},
				scales: {
					y: {
						beginAtZero: true,
						grid: {
							display: false,
						},
					},
					x: {
						grid: {
							display: false,
						},
					},
				},
				interaction: {
					intersect: false,
				},
			},
		});
	} catch (error) {
		console.error("Erro ao buscar os dados do jogo:", error);
		document.getElementById("conteudo").innerHTML = `
			<div class="alert alert-danger" role="alert">
				Houve um erro ao carregar os dados do jogo.
			</div>
			<div class="row pt-5">
				<div id="col">
					<a class="btn btn-primary" href="/" role="button"><i
							class="bi bi-chevron-left"></i> Voltar</a>
				</div>
			</div>
		`;
	} finally {
		document.getElementById("carregando").style.display = "none";
		document.getElementById("conteudo").style.display = "flex";
	}
}

buscarDadosJogo();
