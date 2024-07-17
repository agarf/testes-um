import time

print('LISTAS')
time.sleep(5)
num = [2, 5, 9, 1]
print(num)
print('')

print('ADICIONAR UM NUMERO A LISTA')
time.sleep(5)
num.append(7)
print(num)
print('')

print('COLOCAR A LISTA EM ORDEM')
time.sleep(5)
num.sort()
print(num)
print('')

print('LISTA DE TRAZ PRA FRENTE')
time.sleep(5)
num.sort(reverse=True)
print(num)
print('')

print('LISTA É MUTAVEL')
time.sleep(5)
num[2] = 3
print(num)
print('')

print('CONTAR OS ELEMENTOS COM LEN')
time.sleep(5)
print(f'Essa lista {len(num)} elementos')
print('')

print('INSERIR VALORES EM UMA POSIÇAO')
time.sleep(5)
num.insert(2, 0)
print(num)
print('')

print('REMOVER O ÚLTIMO VALOR COM O COMANDO POP')
time.sleep(5)
num.pop()
print(num)
print('')

print('REMOVE O ELEMENTO 2 DA LISTA')
time.sleep(10)
num.pop(2)
print(num)
print('')

print('parei no minuto 19.20')

