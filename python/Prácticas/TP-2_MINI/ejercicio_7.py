#Indicar qué imprime el siguiente código
#```python
#monto = 900
#es_cliente_vip = False
#tiene_cupon = True
monto = 900 #Declara una variable con el valor 900
es_cliente_vip = False #Establecer un valor falso para la variable es_cliente_vip
tiene_cupon = True #Establece el valor booleano verdadero para el caso de la variable tiene_cupon
if monto > 1000 and es_cliente_vip or tiene_cupon:#Presenta tres condiciones
#Evalúa las tres condiciones, cada una de las variables se ejecuta en determinado orden y verifica
#El monto(variable que vale 900), debe de ser mayor a 100 Y es_cliente_vip debe ser verdadero para que se aplique el descuento
#En cuyo caso tuviéramos el cupón y ese caso fuera verdadero, 
    print("Se aplica descuento")
else:
    print("No hay descuento")

