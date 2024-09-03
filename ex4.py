faturamento_estado = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

total_faturamento = sum(faturamento_estado.values())

percentual_representacao = {
    estado: (valor / total_faturamento) * 100
    for estado, valor in faturamento_estado.items()
}

print(f"Valor total de faturamento: R${total_faturamento:.2f}")
print("\nPercentual de representação por estado:")
for estado, percentual in percentual_representacao.items():
    print(f"{estado}: {percentual:.2f}%")

