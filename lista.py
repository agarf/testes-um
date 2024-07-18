import time

print('LISTAS')
num = [2, 5, 9, 1]
print(num)
print('')
time.sleep(10)

print('ADICIONAR UM NUMERO A LISTA')
num.append(7)
print(num)
print('')
time.sleep(10)

print('COLOCAR A LISTA EM ORDEM')
num.sort()
print(num)
print('')
time.sleep(10)

print('LISTA DE TRAZ PRA FRENTE')
num.sort(reverse=True)
print(num)
print('')
time.sleep(10)

print('LISTA É MUTAVEL')
num[2] = 3
print(num)
print('')
time.sleep(10)

print('CONTAR OS ELEMENTOS COM LEN')
print(f'Essa lista {len(num)} elementos')
print('')
time.sleep(10)

print('INSERIR VALORES EM UMA POSIÇAO')
num.insert(2, 0)
print(num)
print('')
time.sleep(10)

print('REMOVER O ÚLTIMO VALOR COM O COMANDO POP')
num.pop()
print(num)
print('')
time.sleep(10)

print('REMOVE O ELEMENTO 2 DA LISTA')
num.pop(2)
print(num)
print('')
time.sleep(10)

print('INSERIR MAIS UM 2')
num.insert(2, 2)
print(num)
print('')
time.sleep(10)

print('COMANDO REMOVE O NUMERO 2')
num.remove(2)
print(num)
print('')
time.sleep(10)

print('REMOVER UM NUMERO QUE PODE NAO ESTAR NA LISTA')
if 4 in num:
    num.remove(4)
else:
    print('Nao achei o número 4')
time.sleep(10)

print('FIM')
