import GHPModuleInvest
valor_inicial = 1000
valor_final = 1500
anos = 5
taxa_anual = 6
valor_final_juros = GHPModuleInvest.in.calcular_juros_compostos(valor_inicial, taxa_anual, anos)
print(f"Valor final com juros compostos: R${valor_final_juros:.2f}")
