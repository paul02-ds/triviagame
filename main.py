# VARIABLES

pregunta = input('¡Hola, bienvenido! ¿estas listo para jugar?(si/no)')
total_p = 5
puntos = 0

# CODIGO


if pregunta.lower() == 'si':
    # PRIMERA PREGUNTA
    pregunta = input('1. ¿Cuando se fundo la asociacion?')
    if pregunta.lower() == '06/03/1902':
        puntos += 1
        print('¡Muy bien, la respuesta es correcta!')
    else:
        puntos -= 1
        print('Que mala suerte, la respuesta no es correcta')

    # SEGUNDA PREGUNTA
    pregunta = input('2.¿Cuantas Champions League ha ganado el Real Madrid?')
    if pregunta.lower() == '13 champions':
        puntos += 1
        print('¡Excelente!')
    else:
        puntos -= 1
        print('Incorrecto.')


    # TERCERA PREGUNTA
    pregunta = input('3.¿Que dorsal ha usado Cristiano Ronaldo en el Real Madrid?')
    if pregunta.lower() == '9 y 7':
        puntos += 1
        print('¡Correcto!')
    else:
        print('Incorrecto.')


    # CUARTA PREGUNTA
    pregunta = input('4.¿Cuantos goles ha marcado Benzema en esta temporada(La Liga)?')
    if pregunta.lower() == '23':
      puntos += 1
      print('¡Bravo bravo has acertado!')
    else:
      print('Muy mal')

    # PREGUNTA BONUS
    if puntos <= 2:
        pregunta = input('¡BONUS!¿Que dorsal usa Federico Valverde?')
        if pregunta.lower() == '15':
            print('¡Buena!')
        else:
            print('Mal.')

# FINAL
print('Muchas gracias por participar.')
print('Haz totalizado:' + str(puntos) + ' puntos.')
