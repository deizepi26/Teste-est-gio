def inverter_string(s):
    string_invertida = ""
    for i in range(len(s) - 1, -1, -1):
        string_invertida += s[i]

    return string_invertida

entrada_usuario = input("Digite uma string para inverter: ")

resultado = inverter_string(entrada_usuario)
print(f"String invertida: {resultado}")

