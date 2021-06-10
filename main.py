# VARIABLES

ans = input("¿Hola, estas listo para jugar? (si/no)")
total_preguntas = 4
puntuacion = 0

# CODIGO(if,else,bool)

if ans.lower() == 'si':
    ans = input("1)¿Cuantas Champions league ha ganado el Real Madrid?")
    if ans.lower() == '13' or '13 champions league':
        puntuacion += 1
        print('¡Buena! has acertado, ahora tienes: ' + str(puntuacion) + " puntos.")
    else:
        puntuacion -= 1
        print("Incorrecto, ahora tienes: " + str(puntuacion) + " puntos.")   
   #<---------------//SEGUNDA PREGUNTA//------------------------->
    ans = input('2)¿Cuando se fundo la asociación deportiva?')
    if ans.lower() == '06/03/1902' or '6 de marzo del 1902':
        puntuacion += 1
        print('¡Muy bien tio! ahora tienes: ' + str(puntuacion) + ' puntos.')
    else:
        puntuacion -= 1
        print('Dale tio no puedes equivocarte, ahora tienes: ' + str(puntuacion) + " puntos.")
    #<------------------//TERCERA PREGUNTA//-------------------------->
    ans = input('Ultima pregunta...¿Cuantas Champions ha ganado Cristiano Ronaldo en total y en el Real Madrid?')
    if ans.lower() == '3 y 5' or '3 champions en el Real y 5 en total' and puntuacion >= 3:
            print("¡Exacto! buen trabajo has respondido bien a todas las preguntas.")
    else:
        print('Incorrecto!')
    #<----------------//SCORE//------------------------>
    if puntuacion > 3:
        print('No te preocupes aqui tienes un bonus.')
        ans = input('(Bonus) Que numero de dorsal usa Federico Valverde?')
        if ans.lower() == '15':
            puntuacion += 1
            print("Muy bien ahora tienes: " + str(puntuacion) + " puntos.")  
                 
print("Okay hasta luego")
