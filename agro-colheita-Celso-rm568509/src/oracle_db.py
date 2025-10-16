import os, json

def _load_config():
    path = os.path.join(os.path.dirname(__file__), "..", "data", "config.json")
    if not os.path.exists(path):
        return {"oracle": {"enabled": False}}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def enviar_para_oracle(ops):
    cfg = _load_config().get("oracle", {})
    if not cfg.get("enabled"):
        return False, "Oracle desativado em data/config.json"

    try:
        import cx_Oracle  # type: ignore
    except Exception as e:
        return False, f"cx_Oracle não disponível: {e}"

    dsn = cfg.get("dsn")
    user = cfg.get("user")
    password = cfg.get("password")
    table = cfg.get("table", "OPERACOES_COLHEITA")

    if not all([dsn, user, password]):
        return False, "Configuração Oracle incompleta (dsn/user/password)."

    try:
        conn = cx_Oracle.connect(user=user, password=password, dsn=dsn)
        cur = conn.cursor()
        sql = f"INSERT INTO {table} (DATA, TALHAO, EQUIPE, COLHEDORA, PERDA_PCT, OBSERVACOES) VALUES (TO_DATE(:1,'YYYY-MM-DD'), :2, :3, :4, :5, :6)"
        for op in ops:
            cur.execute(sql, [
                op["data"], op["talhao"], op["equipe"], op["colhedora"],
                float(op["perda_pct"]), op.get("observacoes", "")
            ])
        conn.commit()
        cur.close()
        conn.close()
        return True, f"{len(ops)} registro(s) enviados para Oracle."
    except Exception as e:
        return False, f"Erro Oracle: {e}"
