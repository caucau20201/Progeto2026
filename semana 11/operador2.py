# Operador Boleano
# Dados do cliente 
tem_renda = True
sem_nome_sujo = True  
possui_garantir = False

#1. Operador AND(as duas codinções precisan ser verdadeiras).
aprovado_pela_renda = tem_renda and sem_nome_sujo
print("aprovado pelo perfil basico?", aprovado_pela_renda)

#2. Operador OR(pelo menos uma condição tem que ser verdadeira)
aprovado_pelo_score = tem_renda or possui_garantir
print("aprovado pelp score altenarnativo?", aprovado_pelo_score)

#3. Operador NOT (inverter o valor logica)
cliente_bloqueado = not sem_nome_sujo
print("o cliente esta bloqueado?", cliente_bloqueado)