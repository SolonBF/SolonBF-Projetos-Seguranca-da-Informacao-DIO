import random, string
# Tamanho da senha
tamanho = int(input('Digite o tamanho numérico da senha desejada: '))

# Caracteres usados nas senhas
chars = string.ascii_letters + string.digits + 'ç!@#$%&*()-=+,.;:/'

# Gerador de aleatórios
rnd = random.SystemRandom()

# Geração e impressão da senha na tela.
print(''.join(rnd.choice(chars) for i in range(tamanho)))



