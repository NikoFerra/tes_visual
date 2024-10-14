from psychopy import visual, event, core 
import os
import random
import pandas as pd


      
 # Configurar la ventana
win = visual.Window((1366, 768), fullscr=True, color=(0.5, 0.5, 0.5), units="pix", waitBlanking=True)
# Calcular el tamaño de la fuente proporcionalmente a la resolución
ancho_pantalla, alto_pantalla = win.size
tamaño_fuente = int(alto_pantalla * 0.04)  # Ajuste del tamaño de la fuente relativo a la altura de la pantalla



# Configuración y carga de archivos 
lista_imgI = []
lista_TiempoReaccion = []  # Lista para guardar los tiempos de reacción
lista_nombres = []  # Lista para guardar los nombres de los intentos
clock = core.Clock()
image_folder_der = "img_der/"
image_folder_isq = "img_isq/"
carpeta_mask = "msk/"
carpeta_txt= "txt/"


 # Cargar la imagen de la máscara
mask_der = os.path.join(carpeta_mask, "mask1.png")
mask_isq = os.path.join(carpeta_mask, "mask1.png")
mask2 = os.path.join(carpeta_mask, "mask2.png")  


# Diccionario con el nombre de las imágenes y la cantidad de veces que deben mostrarse
image_repetition_count = {
    'neutral.jpg': 8,
    'neutral_1.jpg': 10,
    'neutral_2.jpg': 10,
    'cara.jpg': 63,
    'cara_1.jpg': 8,
    'cara_2.jpg': 15,
    'casa.jpg': 63,
    'casa_1.jpg': 8,
    'casa_2.jpg': 15
}

cantidad_repe_tes = 2
cantidad_muestras_tes = 0

total_intentos_bucle = 5 
numero_intento_bucle = 0


txt1='Bienvenido(a), tu tarea es decidir si hay una imagen o no en la pantalla.\n''Si visualizas la imagen presiona la tecla "n".\n''Si no ves la imagen presiona la tecla "m".\n''Presiona SPACE para continuar.'
txt2='Las imágenes son difíciles de ver.\n''Basta con que veas parte de una imagen, su silueta, etc.\n''Ahora practicaremos antes de comenzar el test.\n''Presiona SPACE para continuar.' 
txtIntruciones='intrucciones'
txtDescanso='Tomate un descanso'  

salirBucle1 = True
salirBucle2 = True


captera_imgI = [f for f in os.listdir(image_folder_isq) if f.endswith(('.jpg', '.png', '.jpeg'))]
         
for image_file in captera_imgI:
    image_path = os.path.join(image_folder_isq, image_file)
    image_stim = visual.ImageStim(win=win, image=image_path, pos=(-350, 0), size=(350, 350), contrast=1) 
    lista_imgI.append(image_stim)              
         
# Lista de imágenes basada en las repeticiones
carpeta_imgD = list(image_repetition_count.keys())

test_images_1 = ['casa_1.jpg', 'casa_2.jpg', 'neutral_1.jpg', 'neutral_2.jpg', 'cara_1.jpg', 'cara_2.jpg']
test_images_2 = ['cara.jpg', 'casa.jpg', 'neutral.jpg']


random.shuffle(test_images_1)  # Mezclar las imágenes aleatoriamente
test_images_2 = random.choices(test_images_2, k=8)  # Elegir aleatoriamente 8 imágenes de esta lista
test_images = test_images_1 + test_images_2


# Cargar y mostrar la imagen "mask2"
mask2_stim_der = visual.ImageStim(win=win, image=mask2, pos=(400, 0), size=(400, 400))
mask2_stim_isq = visual.ImageStim(win=win, image=mask2, pos=(-400, 0), size=(400, 400))

# Crear el símbolo "+" rojo en el centro de cada imagen
plus_der = visual.TextStim(win=win, text="+", pos=(400, 0), color='red', height=40)
plus_isq = visual.TextStim(win=win, text="+", pos=(-400, 0), color='red', height=40)

cruz_der = visual.TextStim(win=win, text="+", pos=(350, 0), color='red', height=40)
cruz_izq = visual.TextStim(win=win, text="+", pos=(-350, 0), color='red', height=40)

txt_final = visual.TextStim(win=win, text="Hasta luego", pos=(0, 0), color='black', height=40)

# Configurar la máscara
mask_stim_der = visual.ImageStim(win=win, image=mask_der, pos=(350, 0), size=(450, 450))
mask_stim_isq = visual.ImageStim(win=win, image=mask_isq, pos=(-350, 0), size=(450, 450))


# Modificar el texto para mostrarlo en ambos lados de la pantalla
text_initial_left = visual.TextStim(win,text=txt1,color='black',pos=(-ancho_pantalla * 0.25, 0),height=tamaño_fuente,wrapWidth=ancho_pantalla * 0.4,alignText='center')
text_initial_right = visual.TextStim(win,text=txt1,color='black',pos=(ancho_pantalla * 0.25, 0),height=tamaño_fuente,wrapWidth=ancho_pantalla * 0.4,alignText='center')
text_second_left = visual.TextStim(win,text=txt2,color='black',pos=(-ancho_pantalla * 0.25, 0),height=tamaño_fuente,wrapWidth=ancho_pantalla * 0.4,alignText='center')
text_second_right = visual.TextStim(win,text=txt2,color='black',pos=(ancho_pantalla * 0.25, 0),height=tamaño_fuente,wrapWidth=ancho_pantalla * 0.4,alignText='center')

txt_intruccionesI = visual.TextStim(win,text=txtIntruciones,color='black',pos=(-ancho_pantalla * 0.25, 0),height=tamaño_fuente,wrapWidth=ancho_pantalla * 0.4,alignText='center')
txt_intruccionesD = visual.TextStim(win,text=txtIntruciones,color='black',pos=(ancho_pantalla * 0.25, 0),height=tamaño_fuente,wrapWidth=ancho_pantalla * 0.4,alignText='center')


def descanso():
    pause_textd = visual.TextStim(win=win, text=txtDescanso, pos=(ancho_pantalla * 0.25, 0),height=tamaño_fuente,wrapWidth=ancho_pantalla * 0.4,alignText='center')
    pause_texti = visual.TextStim(win=win, text=txtDescanso, pos=(-ancho_pantalla * 0.25, 0),height=tamaño_fuente,wrapWidth=ancho_pantalla * 0.4,alignText='center')
    pause_textd.draw()
    pause_texti.draw()
    win.flip()
    event.waitKeys(keyList=['space'])  


# Función para formatear el nombre de la imagen
def formatear_nombre_imagen(nombre_archivo):
    # Quitar la extensión del archivo (por ejemplo, ".jpg", ".png", etc.)
    nombre_sin_extension = os.path.splitext(nombre_archivo)[0]
    # Quitar los números que siguen al nombre de la imagen, como "_1", "_2"
    nombre_formateado = ''.join([i for i in nombre_sin_extension if not i.isdigit()])
    # Reemplazar los guiones bajos con espacios (opcional, si lo prefieres)
    nombre_formateado = nombre_formateado.replace('_', ' ')
    return nombre_formateado


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#+++++++++++++++++++++++++iniciacion de programa++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# Mostrar el texto inicial y esperar a que el usuario presione 'SPACE'
text_initial_left.draw()
text_initial_right.draw()
win.flip()
event.waitKeys(keyList=['space'])

# Mostrar el segundo texto y esperar a que el usuario presione 'SPACE'
text_second_left.draw()
text_second_right.draw()
win.flip()
event.waitKeys(keyList=['space'])

# Mostrar la imagen "mask2"
mask2_stim_der.draw()
mask2_stim_isq.draw()
plus_der.draw()
plus_isq.draw()
win.flip()

# Esperar a que el usuario presione 'SPACE'
event.waitKeys(keyList=['space'])


 #+++++++++++++++++++++++++++++++++++Tes 1++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Realizar los 16 intentos de prueba
while cantidad_muestras_tes < cantidad_repe_tes and salirBucle1:
    


    # Filtrar solo las imágenes que aún no han alcanzado su límite de repeticiones
    available_images = [img for img, count in image_repetition_count.items() if count > 0]
    
    if not available_images:
        break  # Si no quedan imágenes disponibles, salir del bucle
    
    # Elegir una imagen aleatoria de las disponibles
    random_image_der = random.choice(available_images)
    image_path_der = os.path.join(image_folder_der, random_image_der)
    
    # Cargar y mostrar la imagen en la derecha
    image_stim_der = visual.ImageStim(win=win, image=image_path_der, pos=(350, 0), size=(350, 350), contrast=0)

    # Mostrar el nombre de la imagen seleccionada en la pantalla por 1 segundo
    nombre_formateado = formatear_nombre_imagen(random_image_der)
    nombre_img = nombre_formateado
    imagen_derecha = visual.TextStim(win=win, text=f"{nombre_img}", pos=(400, 0), color='black', height=40)
    image_izquierda = visual.TextStim(win=win, text=f"{nombre_img}", pos=(-400, 0), color='black', height=40)
    
    
    imagen_derecha.draw()
    image_izquierda.draw()
    win.flip()
    core.wait(0.7)  # Esperar 0.7 segundo antes de mostrar las imágenes

    if len(lista_imgI) > 0:
        # Iniciar la transición de contraste durante 6 segundos
        plus_isq.draw()
        clock.reset()
        img_isq_index = 0
        while clock.getTime() < 6.5:  # Transición de 6 segundos
            contrast_der = clock.getTime() / 6.0  # Contraste de 0% a 100%
            contrast_isq = 1.0 - contrast_der  # Contraste de 100% a 0%

            # Ajustar el contraste de la imagen derecha
            image_stim_der.contrast = contrast_der
            image_stim_der.draw()

            # Ajustar el contraste de la imagen izquierda
            lista_imgI[img_isq_index].contrast = contrast_isq
            lista_imgI[img_isq_index].draw()

            # Dibujar las máscaras sobre las imágenes
            mask_stim_der.draw()
            mask_stim_isq.draw()
            cruz_der.draw()
            cruz_izq.draw()
            # Actualizar la ventana
            win.flip()

            # Cambio de imagen de la izquierda cada 6 segundos dividido por el número de imágenes
            img_change_interval = 6.5 / len(lista_imgI)
            if clock.getTime() >= img_isq_index * img_change_interval and img_isq_index < len(lista_imgI) - 1:
                img_isq_index += 1  # Pasar a la siguiente imagen de la izquierda


    
    cerrar = event.getKeys()
    if 'space' in cerrar:
        salirBucle1 = False
    # Restar uno al contador de la imagen seleccionada
    image_repetition_count[random_image_der] -= 1

    # Incrementar el número de intentos
    cantidad_muestras_tes += 1



#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


txt_intruccionesI.draw()
txt_intruccionesD.draw()
win.flip()
event.waitKeys(keyList=['space'])

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#++++++++++++++++++++++++++++++++++++Inicio Ejercicio +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Bucle principal para mostrar las imágenes
while numero_intento_bucle < total_intentos_bucle and salirBucle2:
    # Pausa en el intento 50, 100 y 150
    keys = event.waitKeys(maxWait=7, keyList=['n', 'space', 'h'], timeStamped=clock)
    if numero_intento_bucle in [50, 100, 150]:
        descanso()

    # Filtrar solo las imágenes que aún no han alcanzado su límite de repeticiones
    available_images = [img for img, count in image_repetition_count.items() if count > 0]
    random_image_der = random.choice(available_images)
    image_path_der = os.path.join(image_folder_der, random_image_der)
    
    # Cargar y mostrar la imagen en la derecha
    image_stim_der = visual.ImageStim(win=win, image=image_path_der, pos=(350, 0), size=(350, 350), contrast=0)

    # Mostrar el nombre de la imagen seleccionada en la pantalla por 1 segundo
    nombre_formateado = formatear_nombre_imagen(random_image_der)
    nombre_img = nombre_formateado
    imagen_derecha = visual.TextStim(win=win, text=f"{nombre_img}", pos=(400, 0), color='black', height=40)
    image_izquierda = visual.TextStim(win=win, text=f"{nombre_img}", pos=(-400, 0), color='black', height=40)
    trial_number_text = visual.TextStim(win=win, text=f"{numero_intento_bucle}", pos=(0, -alto_pantalla * 0.45), color='black', height=40)

    imagen_derecha.draw()
    image_izquierda.draw()
    win.flip()
    core.wait(0.7)  # Esperar 0.7 segundo antes de mostrar las imágenes



    if len(lista_imgI) > 0:
        # Iniciar la transición de contraste durante 6 segundos
        plus_isq.draw()
        clock.reset()
        img_isq_index = 0
        while clock.getTime() < 6.5:  # Transición de 6 segundos
            contrast_der = clock.getTime() / 6.0  # Contraste de 0% a 100%
            contrast_isq = 1.0 - contrast_der  # Contraste de 100% a 0%

            # Ajustar el contraste de la imagen derecha
            image_stim_der.contrast = contrast_der
            image_stim_der.draw()

            # Ajustar el contraste de la imagen izquierda
            lista_imgI[img_isq_index].contrast = contrast_isq
            lista_imgI[img_isq_index].draw()

            # Dibujar las máscaras sobre las imágenes
            mask_stim_der.draw()
            mask_stim_isq.draw()
            cruz_der.draw()
            cruz_izq.draw()
            trial_number_text.draw()
            # Actualizar la ventana
            win.flip()

            # Cambio de imagen de la izquierda cada 6 segundos dividido por el número de imágenes
            img_change_interval = 6.5 / len(lista_imgI)
            if clock.getTime() >= img_isq_index * img_change_interval and img_isq_index < len(lista_imgI) - 1:
                img_isq_index += 1  # Pasar a la siguiente imagen de la izquierda


    image_repetition_count[random_image_der] -= 1

        # Incrementar el número de intentos
    numero_intento_bucle += 1
    
    if keys:
        for key, reaction_time in keys:
            if key == 'n':
                trial_name = f"Intento {numero_intento_bucle}"
                lista_TiempoReaccion.append(f"{reaction_time:.3f} seg")
                lista_nombres.append(trial_name)
            elif key == 'h':
                trial_name = f"Intento {numero_intento_bucle}"
                lista_TiempoReaccion.append("No registrado")
                lista_nombres.append(trial_name)
            elif key == 'space':
                # Mostrar los tiempos en el lado izquierdo
                for i, (trial_name, time) in enumerate(zip(lista_nombres, lista_TiempoReaccion)):
                    text = visual.TextStim(win=win, text=f"{trial_name}: {time}", pos=(-400, 200 - i * 50), color='black', height=30)
                    text.draw()

                # Mostrar un recuadro en el lado derecho para ingresar el nombre
                text_name_prompt = visual.TextStim(win=win, text="Ingrese su nombre:", pos=(400, 100), color='black', height=40)
                text_name_box = visual.Rect(win=win, width=500, height=50, pos=(400, 0), fillColor='white', lineColor='black')
                text_name_box.draw()
                text_name_prompt.draw()
                win.flip()

                # Capturar el nombre del usuario
                name = []
                while True:
                    name_keys = event.waitKeys()
                    if 'return' in name_keys:
                        break
                    elif 'backspace' in name_keys:
                        if name:
                            name.pop()
                    else:
                        name.extend(name_keys)
                    # Mostrar el nombre que se está escribiendo
                    name_text = visual.TextStim(win=win, text="".join(name), pos=(400, 0), color='black', height=40)
                    text_name_box.draw()
                    text_name_prompt.draw()
                    name_text.draw()
                    win.flip()

                user_name = "".join(name)

                # Guardar los tiempos y nombres de intentos en un archivo Excel
                file_name = os.path.join(carpeta_txt, f"tiempos_{user_name}.xlsx")
                df = pd.DataFrame({'Intento': lista_nombres, 'Tiempo (segundos)': lista_TiempoReaccion})
                df.to_excel(file_name, index=False)

                # Mostrar el mensaje de despedida
                txt_final = visual.TextStim(win=win, text="Hasta luego", pos=(0, 0), color='black', height=40)
                txt_final.draw()
                win.flip()

                core.wait(1)  # Esperar 1 segundo
                win.close()
                core.quit()
                break  # Salir del bucle

        # Decrementar el contador de repeticiones de la imagen
       
    else:
        # No se presionó ninguna tecla
        trial_name = f"Intento {numero_intento_bucle}"
        lista_TiempoReaccion.append("no toco")
        lista_nombres.append(trial_name)
        clock.reset()  # Reiniciar el temporizador
        continue  # Reiniciar el bucle sin incrementar el contador


    tecla = event.getKeys()
    if 'p' in tecla:
        salirBucle2 = False






core.wait(1)  # Esperar 1 segundo
win.close()
core.quit()

  
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
