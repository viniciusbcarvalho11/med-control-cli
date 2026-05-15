from unittest.mock import patch, MagicMock
import json
from src.api_client import search_medication_info


def test_search_medication_info_success():
    """Valida que a função processa corretamente uma resposta da API."""

    fake_response = {
        "results": [{
            "openfda": {
                "brand_name": ["Dipirona"],
                "generic_name": ["Metamizole"]
            },
            "purpose":  ["Analgésico e antitérmico"],
            "warnings": ["Não use em caso de alergia"]
        }]
    }

    mock_response = MagicMock()
    mock_response.read.return_value = json.dumps(fake_response).encode()
    mock_response.__enter__ = lambda s: s
    mock_response.__exit__ = MagicMock(return_value=False)

    with patch("urllib.request.urlopen", return_value=mock_response):
        result = search_medication_info("Dipirona")

    assert "Dipirona" in result
    assert "Metamizole" in result


def test_search_medication_info_failure():
    """Valida que a função retorna mensagem amigável quando a API falha."""

    with patch("urllib.request.urlopen", side_effect=Exception("timeout")):
        result = search_medication_info("Dipirona")

    assert "Não foi possível" in result


def test_search_medication_info_not_found():
    """Valida que a função retorna mensagem quando nenhum resultado é retornado."""

    fake_response = {"results": []}

    mock_response = MagicMock()
    mock_response.read.return_value = json.dumps(fake_response).encode()
    mock_response.__enter__ = lambda s: s
    mock_response.__exit__ = MagicMock(return_value=False)

    with patch("urllib.request.urlopen", return_value=mock_response):
        result = search_medication_info("xyzabc123")

    assert "Nenhuma informação" in result