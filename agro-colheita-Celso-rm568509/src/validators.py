from typing import Tuple

def validar_data(data: str) -> bool:
    # Validação simples YYYY-MM-DD (iniciante)
    if len(data) != 10: return False
    y, m, d = data.split("-")
    return y.isdigit() and m.isdigit() and d.isdigit()

def validar_percentual(valor_str: str) -> Tuple[bool, float]:
    try:
        v = float(valor_str.replace(",", "."))
        if 0 <= v <= 100:
            return True, v
        return False, 0.0
    except Exception:
        return False, 0.0

def nao_vazio(s: str) -> bool:
    return isinstance(s, str) and len(s.strip()) > 0
