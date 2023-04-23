#Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo. Em caso positivo, calcule o perímetro
# do triângulo e apresente a mensagem:

# Perimetro = XX.X


# Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura, mostrando a mensagem

# Area = XX.X

# Entrada
# A entrada contém três valores reais.

# Saída
# O resultado deve ser apresentado com uma casa decimal.

#Exemplo de Entrada	Exemplo de Saída
#6.0 4.0 2.0        Area = 10.0

if __name__ == '__main__':
    v = input('Digite três valores na mesma linha separando-os com um espaço: ').split()
    a, b, c = float(v[0]), float(v[1]), float(v[2])

    if a < (b+c) and b < (a+c) and c < (a+b):
        print('perímetro = {:.1f}'.format(a+b+c))
    else:
        print('Area = {:.1f}'.format((a+b)*c/2))
