import os


def ejecutar():


    while True:

        try:
            os.system('clear')
            accion = int(input('''
            
                     ./~
           (=@@@@@@@=[}=================--
                     `\_
              _____________________
             |                     |   
             | ¿QUE QUIERES HACER? |
             |                     |
             | [1] AÑADIR NOTA     |
             | [2] VER NOTAS       |
             | [3] CERRAR APP      |
             |_____________________|

             ACCION: '''))

        except ValueError:
            print('!!! INSERTA SOLO NUMEROS !!!')

        if accion <= 0 and accion > 3:
            print('!!! INSERTA SOLO LOS NUMEROS DE LAS OPCIONES !!!')

        elif accion == 1:
            nota = input('AÑADE LA NOTA QUE DESEES:\n')
        
            with open('blog.txt','a') as f:
                f.write(f'{nota}\n')

        elif accion == 2:
            os.system('clear')
            
           
            
            print(f'''
              ____________________________________
             | ***** LISTA DE BLOG DE NOTAS ***** |
             
             ''')

            fr = open('blog.txt','r')

            for imprimir in fr:
                print(f'''                 -{imprimir}''')

            print('''
             |____________________________________| 
             
             ''')
            accion2 = input('APRIETA ENTER PARA VOLVER AL MENU\n')

            if accion2 == "":
                continue

       
        elif accion == 3:
            os.system('clear')
            break


if __name__ == "__main__":
    ejecutar()
