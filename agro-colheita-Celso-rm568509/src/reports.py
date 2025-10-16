import os
from typing import List, Dict, Any
from collections import defaultdict

REPORTS_DIR = os.path.join(os.path.dirname(__file__), "..", "reports")

def _media(valores):
    return sum(valores) / len(valores) if valores else 0.0

def calcular_kpis(ops: List[Dict[str, Any]]) -> Dict[str, Any]:
    # "Tabela" em memória: lista de dicionários
    por_talhao = defaultdict(list)
    por_equipe = defaultdict(list)
    por_colhedora = defaultdict(list)

    for op in ops:
        por_talhao[op["talhao"]].append(op["perda_pct"])
        por_equipe[op["equipe"]].append(op["perda_pct"])
        por_colhedora[op["colhedora"]].append(op["perda_pct"])

    kpis = {
        "media_por_talhao": {k: _media(v) for k, v in por_talhao.items()},
        "media_por_equipe": {k: _media(v) for k, v in por_equipe.items()},
        "media_por_colhedora": {k: _media(v) for k, v in por_colhedora.items()},
        "total_registros": len(ops)
    }
    return kpis

def _sugestoes_boas_praticas() -> List[str]:
    return [
        "Ajustar velocidade da colhedora em talhões com cana acamada.",
        "Revisar altura de corte e calibragem de facas.",
        "Planejar colheita nas horas mais frescas para reduzir perdas mecânicas.",
        "Treinar equipe para inspeção visual rápida a cada troca de talhão.",
        "Verificar pneus/esteiras e patinagem em terrenos úmidos."
    ]

def gerar_relatorio_txt(ops: List[Dict[str, Any]], nome_arquivo: str = "relatorio-colheita.txt") -> str:
    os.makedirs(REPORTS_DIR, exist_ok=True)
    kpis = calcular_kpis(ops)

    # Ranking por talhão (top 5 maiores perdas)
    rank_talhoes = sorted(kpis["media_por_talhao"].items(), key=lambda x: x[1], reverse=True)[:5]

    linhas = []
    linhas.append("Relatório de Perdas na Colheita de Cana")
    linhas.append("=======================================")
    linhas.append(f"Total de registros: {kpis['total_registros']}\n")

    linhas.append("Top 5 talhões (maior perda média %):")
    if rank_talhoes:
        for i, (talhao, media) in enumerate(rank_talhoes, 1):
            linhas.append(f"{i}) {talhao:<15} {media:.2f}%")
    else:
        linhas.append("(sem dados)")

    linhas.append("\nSugestões de melhoria:")
    for s in _sugestoes_boas_praticas():
        linhas.append(f"- {s}")

    caminho = os.path.join(REPORTS_DIR, nome_arquivo)
    with open(caminho, "w", encoding="utf-8") as f:
        f.write("\n".join(linhas))

    return caminho
