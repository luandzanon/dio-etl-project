# dio-etl-project

Este projeto explora os conceitos fundamentais de Engenharia de Dados e Ciência de Dados através da criação de um pipeline ETL (Extract, Transform, Load).

## 🎯 Objetivo

Replicar um fluxo prático de tratamento de dados:
1.  **Extração:** Leitura de dados de usuários a partir de arquivos CSV ou listas (solução alternativa à API).
2.  **Transformação:** Utilização de IA (ou lógica de script) para gerar mensagens de marketing personalizadas.
3.  **Carregamento:** Salvamento dos novos dados transformados em um arquivo de saída.

## Tecnologias

* **Python**
* **Pandas** (Manipulação de dados)
* **OpenAI API** (Opcional, para geração de texto via IA)

## Como Executar

1.  Clone o repositório.
2.  Instale as dependências necessárias:
    ```bash
    pip install pandas openai
    ```
3.  Execute o script principal para processar o arquivo `SDW2023.csv` (ou a lista interna) e gerar as saídas.

## Estrutura

O código foca na resiliência da aplicação, permitindo que o estudo continue mesmo sem a disponibilidade da API oficial, utilizando arquivos locais como fonte de dados.
