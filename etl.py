import pandas as pd

def extract_data(file_path):
    cols_load = ['Transaction ID', 'Item', 'Quantity', 'Price Per Unit', 'Payment Method', 'Location', 'Transaction Date'] # Escolhe na variável os campos necessários
    
    df = pd.read_csv(
        file_path,
        usecols=cols_load, # Carrega apenas as colunas necessárias
        na_values=['ERROR', 'UNKNOWN'], # Altera os erros para nulo
        parse_dates=['Transaction Date'] # Conversão para data no nível de motor, sem precisar carregar em texto e posteriormente converter em data.
    ).dropna()
    
    return df

def transform_data(df):
    cols_new = ['id_transacao', 'item', 'quantidade', 'preco_unitario', 'metodo_pagamento', 'local', 'data_transacao']
    df.columns = cols_new # Renomeia todas colunas

    df = df.astype({ # Melhores tipos a serem utilizados; Downcasting para otimizar memória
        'id_transacao': 'string',
        'item': 'category',
        'quantidade': 'int32',
        'preco_unitario': 'float32',
        'metodo_pagamento': 'category',
        'local': 'category'
    })

    df['total_final'] = df['quantidade'] * df['preco_unitario'] # Nova coluna

    # Sugerir cross-sell baseado no item
    def gerar_oferta(item):
        item_str = str(item).lower()
        if 'coffee' in item_str or 'tea' in item_str:
            return "Que tal um bolo para acompanhar na próxima?"
        elif 'cake' in item_str or 'cookie' in item_str:
            return "Um cafézinho cairia bem com isso!"
        else:
            return "Obrigado pela preferência!"

    df['mensagem_marketing'] = df['item'].apply(gerar_oferta) # Nova coluna que aplica a própria função linha por linha
    
    return df

def load_data(df, output_path):
    df.to_csv(output_path, index=False)
    print(f"Arquivo salvo com sucesso em: {output_path}")

# Se é o arquivo principal, executa. Se foi importado por outro, não executa e disponibiliza as funções para serem utilizadas.
if __name__ == "__main__": 
    arquivo_entrada = 'dirty_cafe_sales.csv'
    arquivo_saida = 'clean_cafe_sales.csv'

    dados_brutos = extract_data(arquivo_entrada)
    dados_transformados = transform_data(dados_brutos)
    load_data(dados_transformados, arquivo_saida)
    
    print(dados_transformados.head())