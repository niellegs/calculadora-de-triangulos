print('\033[33m-=-'*13)
print('\033[34mAnalisador de Triângulos')
print('\033[33m-=-\033[m'*13)
s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
if s1 < s2 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos acima PODEM formar um triângulo.')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo.')
