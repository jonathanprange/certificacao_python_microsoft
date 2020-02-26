# *************************************************** Execute Operações usando Tipos de Dados e Operadores (20-25%) *********************************************************** #


# Avaliar uma expressão para identificar o tipo de dados que o Python atribuirá a cada variável:
    # Identificar tipos de dados str, int, float e bool

variavel_tipo_str = '50'
variavel_tipo_int = 10
variavel_tipo_float = 10.5
variavel_tipo_bool = True # False

print('\n' + 20*'*' + 'Impressão dos tipos de dados' + 30*'*' + '\n')

print(f'\t variavel_tipo_str com o conteúdo: {variavel_tipo_str} = {type(variavel_tipo_str)}')
print(f'\t variavel_tipo_int com o conteúdo: {variavel_tipo_int} = {type(variavel_tipo_int)}')
print(f'\t variavel_tipo_float com o conteúdo: {variavel_tipo_float} = {type(variavel_tipo_float)}')
print(f'\t variavel_tipo_bool com o conteúdo: {variavel_tipo_bool} = {type(variavel_tipo_bool)}')

print('\n' + 17*'*' + 'Fim da impressão dos tipos de dados' + 26*'*')



# Executar operações de dados e tipos de dados:
    # Converter de um tipo de dados para outro tipo; 

# Convertendo tipo str
variavel_tipo_str_convertida_para_int = int(variavel_tipo_str) # ValueError: invalid literal for int() with base 10: 'String' (caso a string não seja um número).
variavel_tipo_str_convertida_para_float = float(variavel_tipo_str) # ValueError: could not convert string to float: 'String' (caso a string não seja um número).
variavel_tipo_str_convertida_para_bool = bool(variavel_tipo_str) # Converte para True ou False, dependendo da string ter conteúdo ou não respectivamente.

# Convertendo tipo int
variavel_tipo_int_convertida_para_str = str(variavel_tipo_int)
variavel_tipo_int_convertida_para_float = float(variavel_tipo_int)
variavel_tipo_int_convertida_para_bool = bool(variavel_tipo_int) # Converte para True ou False, dependendo do int ser diferente de 0 ou não respectivamente.

# Convertendo tipo float
variavel_tipo_float_convertida_para_str = str(variavel_tipo_float)
variavel_tipo_float_convertida_para_int = int(variavel_tipo_float) # Converte para int, perdendo todo o conteúdo após o ponto flutuante.
variavel_tipo_float_convertida_para_bool = bool(variavel_tipo_float) # Converte para True ou False, dependendo do float ser diferente de 0.0 ou não respectivamente.

# Convertendo tipo bool
variavel_tipo_bool_convertida_para_str = str(variavel_tipo_bool) # Converte uma string True ou False, dependendo do booleano ser True ou False respectivamente.
variavel_tipo_bool_convertida_para_int = int(variavel_tipo_bool) # Converte um int 1 ou 0, dependendo do booleano ser True ou False respectivamente.
variavel_tipo_bool_convertida_para_float = float(variavel_tipo_bool) # Converte um float 1.0 ou 0.0, dependendo do booleano ser True ou False respectivamente.

print('')
print(20*'*' + 'Impressão dos tipos de dados convertidos' + 36*'*' + '\n')

print(f'\t variavel_tipo_str_convertida_para_int com o conteúdo: {variavel_tipo_str_convertida_para_int} = {type(variavel_tipo_str_convertida_para_int)}')
print(f'\t variavel_tipo_str_convertida_para_float com o conteúdo: {variavel_tipo_str_convertida_para_float} = {type(variavel_tipo_str_convertida_para_float)}')
print(f'\t variavel_tipo_str_convertida_para_bool com o conteúdo: {variavel_tipo_str_convertida_para_bool} = {type(variavel_tipo_str_convertida_para_bool)}')
print(f'\t variavel_tipo_int_convertida_para_str com o conteúdo: {variavel_tipo_int_convertida_para_str} = {type(variavel_tipo_int_convertida_para_str)}')
print(f'\t variavel_tipo_int_convertida_para_float com o conteúdo: {variavel_tipo_int_convertida_para_float} = {type(variavel_tipo_int_convertida_para_float)}')
print(f'\t variavel_tipo_int_convertida_para_bool com o conteúdo: {variavel_tipo_int_convertida_para_bool} = {type(variavel_tipo_int_convertida_para_bool)}')
print(f'\t variavel_tipo_float_convertida_para_str com o conteúdo: {variavel_tipo_float_convertida_para_str} = {type(variavel_tipo_float_convertida_para_str)}')
print(f'\t variavel_tipo_float_convertida_para_int com o conteúdo: {variavel_tipo_float_convertida_para_int} = {type(variavel_tipo_float_convertida_para_int)}')
print(f'\t variavel_tipo_float_convertida_para_bool com o conteúdo: {variavel_tipo_float_convertida_para_bool} = {type(variavel_tipo_float_convertida_para_bool)}')
print(f'\t variavel_tipo_bool_convertida_para_str com o conteúdo: {variavel_tipo_bool_convertida_para_str} = {type(variavel_tipo_bool_convertida_para_str)}')
print(f'\t variavel_tipo_bool_convertida_para_int com o conteúdo: {variavel_tipo_bool_convertida_para_int} = {type(variavel_tipo_bool_convertida_para_int)}')
print(f'\t variavel_tipo_bool_convertida_para_float com o conteúdo: {variavel_tipo_bool_convertida_para_float} = {type(variavel_tipo_bool_convertida_para_float)}')

print('\n' + 20*'*' + 'Fim da impressão dos tipos de dados convertidos' + 30*'*')



# Executar operações de dados e tipos de dados:

    # construir estruturas de dados; 

        # (Lista, Dicionário, Tupla)




# Executar operações de dados e tipos de dados:

    # executar operações de indexação e corte