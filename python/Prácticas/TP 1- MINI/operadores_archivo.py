monto = 900
es_cliente_vip = False
tiene_cupon = True
if monto > 1000 and (es_cliente_vip or tiene_cupon):
    print ("Se aplica descuento")
else: 
    print ("No hay descuento")