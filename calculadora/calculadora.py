#def = definição, definição da função
#somar_dois = título da função, o underline é linguagem snack case

def somar_dois_numeros(num1, num2):   #  parenteses serve para enviar ou receber dados, enviar ou receber parametros
    #resultado = num1 + num2          # exemplo 1
    #return resultado                 # retorna resultado
    return  num1 + num2               # exemplo 2 reduzido do caso anterior

def subtrair_dois_numeros (num1, num2):
    return num1 - num2

def multiplicar_dois_numeros (num1, num2):
    return num1 * num2

def dividir_dois_numeros(num1, num2):
    try: 
        return num1 / num2
    except (ZeroDivisionError):
        return 'Erro: Não é possível dividir por zero'
    
    




