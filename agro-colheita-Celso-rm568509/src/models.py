from dataclasses import dataclass, asdict
from typing import Dict, Any

@dataclass
class Operacao:
    data: str          # "YYYY-MM-DD"
    talhao: str
    equipe: str
    colhedora: str
    perda_pct: float   # 0.0 - 100.0
    observacoes: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
