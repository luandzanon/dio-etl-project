# ☕ Análise de Vendas & Pipeline ETL

Este projeto simula um desafio real de análise de dados: receber dados "sujos" de um sistema de vendas de cafeteria, processá-los através de um pipeline automatizado e gerar insights de negócio visuais.

Desenvolvido como parte do desafio da **DIO (Bootcamp Santander)**.

## Objetivo
Replicar um fluxo prático de tratamento de dados e analytics:
1.  **Engenharia de Dados:** Limpar e padronizar dados brutos.
2.  **Análise de Dados:** Gerar visualizações para responder perguntas de negócio.

## Estrutura do Projeto

* **`dirty_cafe_sales.csv`**: Arquivo original contendo erros de digitação, valores nulos e dados inconsistentes.
* **`etl.py`**: Script Python responsável por extrair, limpar, transformar e carregar os dados (ETL).
* **`clean_cafe_sales_processed.csv`**: Resultado final do pipeline, dados prontos para análise.
* **`cafe_sales_graphics.ipynb`**: Jupyter Notebook com storytelling de dados e gráficos.

## O Pipeline ETL

O script `etl.py` automatiza o tratamento de dados focando em:
1.  **Extract:** Leitura de arquivo CSV bruto.
2.  **Transform:**
    * Remoção de registros com erros de sistema (`ERROR`, `UNKNOWN`).
    * Tratamento de valores nulos (DropNA).
    * Tipagem eficiente (conversão para `category`, `int`, `float` e `datetime`).
    * Criação de novas colunas calculadas (`total_final`).
3.  **Load:** Exportação otimizada para CSV sem índices desnecessários.

## Visualização de Dados

No notebook `cafe_sales_graphics.ipynb`, utilizamos **Matplotlib** e **Seaborn** para responder perguntas de negócio:

* **Ranking de Produtos:** Quais itens são os principais da loja?
* **Tendência Temporal:** Como o faturamento evoluiu mês a mês?
* **Mix de Pagamento:** Qual a preferência dos clientes na hora de pagar?

## Como Executar

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/luandzanon/dio-etl-project.git
    ```

2.  **Instale as dependências:**
    ```bash
    pip install pandas matplotlib seaborn
    ```

3.  **Execute o Pipeline ETL:**
    ```bash
    python etl.py
    ```
    *Isso irá gerar o arquivo `clean_cafe_sales_processed.csv`.*

4.  **Abra a Análise:**
    Execute o arquivo `cafe_sales_graphics.ipynb` no Jupyter Notebook ou VS Code para visualizar os gráficos.

## Tecnologias

* **Python** 3.13.7
* **Pandas** (ETL e Manipulação)
* **Matplotlib & Seaborn** (Visualização de Dados)
* **Jupyter Notebook**
