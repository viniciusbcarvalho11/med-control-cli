import urllib.request
import urllib.parse
import json


def search_medication_info(name: str) -> str:
    try:
        query = urllib.parse.quote(name)
        url = (
            f"https://api.fda.gov/drug/label.json"
            f"?search=openfda.brand_name:{query}&limit=1"
        )

        req = urllib.request.Request(
            url, headers={"User-Agent": "MedControlCLI/1.0"}
        )

        with urllib.request.urlopen(req, timeout=5) as response:
            data = json.loads(response.read().decode())
            results = data.get("results", [])

            if not results:
                return "Nenhuma informação encontrada na Open FDA."

            result = results[0]
            openfda = result.get("openfda", {})

            brand   = openfda.get("brand_name", ["N/A"])[0]
            generic = openfda.get("generic_name", ["N/A"])[0]
            purpose = result.get("purpose", ["N/A"])[0]
            warning = result.get("warnings", ["N/A"])[0][:300]

            return (
                f"\n--- Informações Open FDA ---\n"
                f"Nome comercial : {brand}\n"
                f"Nome genérico  : {generic}\n"
                f"Finalidade     : {purpose}\n"
                f"Aviso          : {warning}...\n"
                f"----------------------------"
            )

    except Exception:
        return "Não foi possível buscar informações na Open FDA."