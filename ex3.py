import json

faturamento_diario = [
    {"dia": 1, "valor": 1000},
    {"dia": 2, "valor": 2500},
    {"dia": 3, "valor": 3000},
    {"dia": 4, "valor": 0},
    {"dia": 5, "valor": 500},
    {"dia": 6, "valor": 7000},
    {"dia": 7, "valor": 0},
    {"dia": 8, "valor": 200},
    {"dia": 9, "valor": 1300},
    {"dia": 10, "valor": 0},
    {"dia": 11, "valor": 4000},
    {"dia": 12, "valor": 3000},
    {"dia": 13, "valor": 3500},
    {"dia": 14, "valor": 0},
    {"dia": 15, "valor": 4500},
    {"dia": 16, "valor": 5000},
    {"dia": 17, "valor": 5500},
    {"dia": 18, "valor": 0},
    {"dia": 19, "valor": 0},
    {"dia": 20, "valor": 3200},
    {"dia": 21, "valor": 2100},
    {"dia": 22, "valor": 1800},
    {"dia": 23, "valor": 4000},
    {"dia": 24, "valor": 1000},
    {"dia": 25, "valor": 0},
    {"dia": 26, "valor": 0},
    {"dia": 27, "valor": 0},
    {"dia": 28, "valor": 6000},
    {"dia": 29, "valor": 7000},
    {"dia": 30, "valor": 8000}
]

with open('faturamento.json', 'w') as file:
    json.dump(faturamento_diario, file, indent=4)

with open('faturamento.json', 'r') as file:
    dados_faturamento = json.load(file)

faturamento_valido = [dia['valor'] for dia in dados_faturamento if dia['valor'] > 0]

menor_valor = min(faturamento_valido)
maior_valor = max(faturamento_valido)

media_mensal = sum(faturamento_valido) / len(faturamento_valido)

dias_acima_da_media = len([valor for valor in faturamento_valido if valor > media_mensal])

print(f"Menor valor de faturamento diário: {menor_valor:.2f}")
print(f"Maior valor de faturamento diário: {maior_valor:.2f}")
print(f"Número de dias com faturamento acima da média mensal: {dias_acima_da_media}")

