from typing import Dict, Any, List, Tuple
from models import Operacao
from validators import validar_data, validar_percentual, nao_vazio
from storage import carregar_operacoes, salvar_operacoes
from reports import calcular_kpis, gerar_relatorio_txt
from oracle_db import enviar_para_oracle
from menus import MENU_PRINCIPAL, imprimir_operacao

def add_operacao(ops: List[Dict[str, Any]]) -> None:
    print("\nCadastro de operação de colheita")
    data = input("Data (YYYY-MM-DD): ").strip()
    if not validar_data(data):
        print("Data inválida. Use YYYY-MM-DD.")
        return

    talhao = input("Talhão: ").strip()
    if not nao_vazio(talhao):
        print("Talhão inválido.")
        return

    equipe = input("Equipe: ").strip()
    if not nao_vazio(equipe):
        print("Equipe inválida.")
        return

    colhedora = input("Colhedora: ").strip()
    if not nao_vazio(colhedora):
        print("Colhedora inválida.")
        return

    ok, perda_pct = validar_percentual(input("Perda estimada (%): ").strip())
    if not ok:
        print("Perda inválida. Use número entre 0 e 100.")
        return

    obs = input("Observações (opcional): ").strip()

    op = Operacao(
        data=data, talhao=talhao, equipe=equipe, colhedora=colhedora,
        perda_pct=perda_pct, observacoes=obs
    ).to_dict()

    ops.append(op)
    salvar_operacoes(ops)
    print("✔ Operação salva!")

def listar_operacoes(ops: List[Dict[str, Any]]) -> None:
    if not ops:
        print("(sem registros)")
        return
    for idx, op in enumerate(ops, 1):
        imprimir_operacao(op, idx)

def ver_kpis(ops: List[Dict[str, Any]]) -> None:
    k = calcular_kpis(ops)
    print("\nKPIs")
    print("----")
    print(f"Total de registros: {k['total_registros']}")
    print("\nMédia de perdas por talhão:")
    for t, v in k["media_por_talhao"].items():
        print(f"- {t:<15} {v:.2f}%")
    print("\nMédia de perdas por equipe:")
    for t, v in k["media_por_equipe"].items():
        print(f"- {t:<15} {v:.2f}%")
    print("\nMédia de perdas por colhedora:")
    for t, v in k["media_por_colhedora"].items():
        print(f"- {t:<15} {v:.2f}%")

def gerar_relatorio(ops: List[Dict[str, Any]]) -> None:
    nome = input("Nome do arquivo (padrão: relatorio-colheita.txt): ").strip() or "relatorio-colheita.txt"
    caminho = gerar_relatorio_txt(ops, nome)
    print(f"✔ Relatório gerado em: {caminho}")

def enviar_oracle(ops: List[Dict[str, Any]]) -> None:
    if not ops:
        print("(sem registros para enviar)")
        return
    ok, msg = enviar_para_oracle(ops)
    status = "✔" if ok else "✖"
    print(f"{status} {msg}")

def main():
    ops = carregar_operacoes()
    while True:
        print(MENU_PRINCIPAL)
        escolha = input("Escolha: ").strip()
        if escolha == "1":
            add_operacao(ops)
        elif escolha == "2":
            listar_operacoes(ops)
        elif escolha == "3":
            ver_kpis(ops)
        elif escolha == "4":
            gerar_relatorio(ops)
        elif escolha == "5":
            enviar_oracle(ops)
        elif escolha == "0":
            print("Até mais!")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
