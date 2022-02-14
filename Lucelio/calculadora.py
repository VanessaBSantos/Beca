class calculadora:
    
    def soma (a,b):
        res = a + b
        #print (res)
        return (res)
    
    def subtrai (c,d):
        sub = c - d
        #print (sub)
        return (sub)
    
    def multiplica (e,f):
        multi = e * f
        #print (multi)
        return (multi)
    
    def divisao (g,h):
        divide = g / h
        #print (divide)
        return (divide)
    
resSoma =       calculadora.soma        (3,55)
resSubtrai =    calculadora.subtrai     (23,32)
resMultiplica = calculadora.multiplica  (32,3)
resDivisao =    calculadora.divisao     (3,4)

lista = {"Soma":            resSoma,
         "Subtração":       resSubtrai,
         "Multiplicação":   resMultiplica,
         "Divisão":         resDivisao}

print ("\n",lista)

    