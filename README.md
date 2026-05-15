# Med Control CLI

## Problema
Pessoas esquecem de tomar medicamentos corretamente.

## Solução
Aplicação em linha de comando para gerenciar medicamentos,
com integração à API pública Open FDA para exibir informações
oficiais sobre os medicamentos cadastrados.

## Funcionalidades
- Adicionar medicamento
- Listar medicamentos
- Marcar como tomado
- Buscar informações oficiais via API Open FDA

## Como executar

### Pré-requisitos
- Python 3.10+
- Git

### Instalação
```bash
git clone https://github.com/viniciusbcarvalho11/med-control-cli.git
cd med-control-cli
pip install -r requirements.txt
```

### Execução
```bash
python -m src.main
```

## Testes
```bash
python -m pytest
```

## Lint
```bash
ruff check .
```

## API utilizada
[Open FDA](https://api.fda.gov/drug/label.json) — gratuita, sem necessidade de cadastro.

## Versão
2.0.0

## Autor
Vinícius Brandão de Carvalho