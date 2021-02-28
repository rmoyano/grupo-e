print("Bienvenido a la tarea del grupo E.") 
nombre = input("Ingrese nombre: ")
apellido = input("Ingrese apellido: ")
print('Sus datos son:{0} {1} '.format(nombre, apellido))

import time
 
def validateDateEs(date):
    """
    Funcion para validar una fecha en formato:
        dd/mm/yyyy, dd/mm/yy, d/m/yy, dd/mm/yyyy hh:mm:ss, dd/mm/yy hh:mm:ss, d/m/yy h:m:s
    """
    for format in ['%d/%m/%Y', '%d/%m/%y', '%d/%m/%Y %H:%M:%S', '%d/%m/%y %H:%M:%S']:
        try:
            result = time.strptime(date, format)
            return True
        except:
            pass
    return False
 
entrada = input("Ingrese fecha Nacimiento en formato dd/mm/yyyy: ")
 
if validateDateEs(entrada):
    print('Fecha correcta')
else:
    print('Fecha incorrecta')
