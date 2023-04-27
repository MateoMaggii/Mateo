
#if anidados
ingreso_mensual = 10
gasto_mensual = 10000

if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0:
        print("estas en deficit")
    elif ingreso_mensual - gasto_mensual < 3000:
        print("estas gastando mucho, capaz no te alcanze")
    elif ingreso_mensual - gasto_mensual >= 3000:
        print("estas bien")
    
elif ingreso_mensual > 1000:
    print("estas bien en latinoamerica")
    
elif ingreso_mensual > 500:
    print("estas bien en argentina")
    
elif ingreso_mensual > 200:
    print("estas biuen en venezuela")
    
else: 
    print("sos pobre")
    
