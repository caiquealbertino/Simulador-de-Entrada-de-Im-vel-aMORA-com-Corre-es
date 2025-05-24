print("\nBem-vindo ao simulador online de entrada de imóvel da aMORA\n")

#Entradas obrigatórias do usuário
valor_imovel = float(input("Indique o valor do imóvel: "))
percentual_entrada = float(input("Indique o percentual (%) da entrada: "))
duracao_contrato = int(input("Indique a duração do contrato em anos: "))
print("IGPM: 6% ao ano")
taxa_juros = float(input("Indique a taxa de juros anual para simulação (valor entre 5% e 12%): "))

#Fórmulas das variaveis
valor_entrada = valor_imovel * (percentual_entrada / 100)
total_a_guardar = valor_imovel * 0.15
parcela_mensal = total_a_guardar / (duracao_contrato * 12)

#Lista para armazenar os valores corrigidos por ano
parcela_anoN_igpm = []
parcela_anoN_juros = []

# Cálculo das correções para cada ano
for ano in range(1, duracao_contrato + 1):
    parcela_igpm = parcela_mensal * (1 + 0.06) ** (ano - 1)
    parcela_juros = parcela_mensal * (1 + taxa_juros / 100) ** (ano - 1)
    parcela_anoN_igpm.append(parcela_igpm)
    parcela_anoN_juros.append(parcela_juros)

#Saídas
print("\n=== Resultados ===")
print(f"Valor da entrada: R$ {valor_entrada:.2f}")
print(f"Valor a guardar: R$ {total_a_guardar:.2f}")
print(f"Valor mensal base: R$ {parcela_mensal:.2f}")

print("\nValor mensal corrigido pelo IGPM (6% ao ano):")
for i, valor in enumerate(parcela_anoN_igpm, 1):
    print(f"  - Ano {i}: R$ {valor:,.2f}")
    
print(f"\nValor mensal corrigido pela taxa de {taxa_juros}% ao ano:")
for i, valor in enumerate(parcela_anoN_juros, 1):
    print(f"  - Ano {i}: R$ {valor:,.2f}")
