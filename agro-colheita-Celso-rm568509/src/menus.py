MENU_PRINCIPAL = (
    "\n=== CorteCerto – Controle de Perdas ===\n"
    "1) Cadastrar operação\n"
    "2) Listar operações\n"
    "3) Ver KPIs\n"
    "4) Gerar relatório TXT\n"
    "5) Enviar para Oracle (opcional)\n"
    "0) Sair\n"
)

def imprimir_operacao(op, idx):
    print(f"[{idx}] {op['data']} | Talhão: {op['talhao']} | Equipe: {op['equipe']} | Colhedora: {op['colhedora']} | Perda: {op['perda_pct']}%")
    if op.get("observacoes"):
        print(f"    Obs: {op['observacoes']}")
