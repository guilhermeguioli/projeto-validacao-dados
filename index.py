# Projeto: Validação de Dados de Clientes e Transações
# Objetivo: Simular verificação de dados com regras de negócio!!
# Autor: Guilherme Oliveira
# Tecnologias: Python, pandas, numpy, regex
# Vizando a instrução detalhada em Etapas para facilitar o entendimento e a criação do projeto


# Etapa 1: Importação de bibliotecas essenciais
import pandas as pd
import numpy as np
import os
import webbrowser


# Etapa 2: Criando dados fictícios de clientes/transações
dados = {
    'nome': ['João', 'Maria', 'Pedro', 'Ana', 'Carlos'],
    'idade': [25, -3, 130, 40, 28],  # contém valores inválidos
    'email': ['joao@email.com', 'mariaemail.com', 'pedro@teste', 'ana@dominio.com', 'carlos@email.com'],
    'valor_transacao': [5000, 15000, 7500, 20000, 300]  # algumas transações acima de R$10.000
}

df = pd.DataFrame(dados)

# Visualizando os dados
print("Dados Originais:")
print(df)

# Etapa 3.1: Validar idade (negativa ou maior que 120)
df['erro_idade'] = (df['idade'] < 0) | (df['idade'] > 120)

# Etapa 3.2: Marcar transações acima de R$10.000 como alta prioridade
df['prioridade'] = np.where(df['valor_transacao'] > 10000, 'Alta', 'Normal')

# Etapa 3.3: Validar formato de e-mail básico
df['erro_email'] = ~df['email'].str.contains(r'^[\w\.-]+@[\w\.-]+\.\w+$', regex=True)

# Etapa 4: Filtrar linhas com erros
erros = df[(df['erro_idade']) | (df['erro_email'])]

print("Erros encontrados:")
print(erros[['nome', 'idade', 'email', 'erro_idade', 'erro_email']])

# Etapa 5: Criar sugestões de tratamento
def sugestao_tratamento(row):
    sugestoes = []
    if row['erro_idade']:
        sugestoes.append('Verificar idade (deve ser entre 0 e 120)')
    if row['erro_email']:
        sugestoes.append('Corrigir formato do e-mail')
    return ' | '.join(sugestoes)

erros = erros.copy()
erros['sugestao'] = erros.apply(sugestao_tratamento, axis=1)


# Etapa 6: Exibição dos resultados
print("Dados Originais:")
print(df)

print("Erros encontrados:")
print(erros[['nome', 'idade', 'email', 'erro_idade', 'erro_email']])

print("Sugestões de Tratamento:")
print(erros[['nome', 'sugestao']])

# Etapa 7: Exportar relatório para Excel
nome_arquivo = "relatorio_erros.xlsx"
erros.to_excel(nome_arquivo, index=False)
print(f"Relatório salvo como '{nome_arquivo}'")

# Etapa 8: Abrir automaticamente o arquivo Excel
caminho_completo = os.path.abspath(nome_arquivo)
webbrowser.open(caminho_completo)

# Etapa 9: Manter janela aberta no terminal (Windows)
input("Pressione Enter para finalizar...")