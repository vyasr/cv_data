from __future__ import annotations

from pathlib import Path

from ruamel.yaml import YAML

from .schema import ProfessionalData

_DEFAULT_DATA_PATH = Path(__file__).parent.parent.parent / "data" / "professional.yaml"


def load_professional_data(path: str | Path | None = None) -> ProfessionalData:
    """Load and validate professional.yaml. Defaults to bundled data/professional.yaml."""
    if path is None:
        path = _DEFAULT_DATA_PATH
    data = YAML(typ="safe").load(Path(path))
    return ProfessionalData.model_validate(data)
