
import pytest

from validazione import valida_mese, valida_valori


def test_mese_valido():
    assert valida_mese("Gennaio", set()) == "gennaio"


def test_mese_duplicato():
    with pytest.raises(ValueError, match="duplicato"):
        valida_mese("GENNAIO", {"gennaio"})


def test_mese_non_riconosciuto():
    with pytest.raises(ValueError, match="non riconosciuto"):
        valida_mese("Smarchio", set())


def test_consumo_negativo():
    with pytest.raises(ValueError, match="negativi"):
        valida_valori(-10, 0.25)


def test_valori_validi():
    valida_valori(120, 0.25)
