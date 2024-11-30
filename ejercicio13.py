
meses = 20
pago_inicial = 10
pago_mensual = pago_inicial
total_pagado = 0


for mes in range(1, meses + 1): 
    print(f"Mes {mes}: Debe pagar {pago_mensual} euros")
    total_pagado += pago_mensual  
    pago_mensual *= 2  


print(f"Total pagado después de {meses} meses: {total_pagado} euros")
