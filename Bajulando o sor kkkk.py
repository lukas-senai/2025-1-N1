import time

def efeito_digitacao(texto, delay=0.1):
    for caractere in texto:
        print(caractere, end='', flush=True)
        time.sleep(delay)
    print()

efeito_digitacao("Prepare-se para ser bajulado kkkkk", 0.1)

print("carregando", end='', flush=True)
efeito_digitacao("...", 0.4)

print("carregando", end='', flush=True)
efeito_digitacao("...", 0.4)

print("carregando", end='', flush=True)
efeito_digitacao("...", 0.4)

efeito_digitacao("É nóis pa krl sor iiihhhuuuu❤️ ❤️ ❤️", 0.2)

print("fim do programa")