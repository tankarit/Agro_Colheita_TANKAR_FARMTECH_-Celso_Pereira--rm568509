import json, os
from typing import List, Dict, Any

DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "operacoes.json")

def carregar_operacoes() -> List[Dict[str, Any]]:
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def salvar_operacoes(ops: List[Dict[str, Any]]) -> None:
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(ops, f, ensure_ascii=False, indent=2)
