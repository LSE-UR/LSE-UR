import os
import shutil


def obtener_info_video(ruta_video):
    """
    Obtiene información de un vídeo a partir de su ruta y nombre.

    Args:
        ruta_video (str): Ruta completa del archivo de vídeo.

    Returns:
        dict: Diccionario con la información del vídeo.
    """

    info_video = {}
    # Obtener extensión y tamaño del vídeo
    info_video["extension"] = os.path.splitext(ruta_video)[1]
    info_video["tamaño_mb"] = os.path.getsize(ruta_video) / (1024 * 1024)  # Tamaño en MB

    # Obtener información del nombre del vídeo
    nombre_video = os.path.basename(ruta_video)
    partes_nombre = nombre_video.split("_")

    if len(partes_nombre) == 6: #Verificamos que el nombre tenga la estructura correcta
        info_video["id"] = partes_nombre[1]
        info_video["numero_video"] = partes_nombre[2]
        info_video["tipo_camara"] = partes_nombre[3]
        if(info_video["tipo_camara"]=="camera2"):
            info_video["tipo_camara"]="microsoft_rightView_RGB"
        elif (info_video["tipo_camara"] == "camera1"):
            info_video["tipo_camara"]="logitech_leftView_RGB"
        else:
            print(partes_nombre,"mal")
        info_video["gesto"] = partes_nombre[4] #Eliminamos la extension
        info_video["mano_usada"] = partes_nombre[5].split(".")[0] #Eliminamos el gesto
    elif len(partes_nombre) == 7:
        info_video["id"] = partes_nombre[1]
        info_video["numero_video"] = partes_nombre[2]
        if len(partes_nombre[0].split("video")[0])!=0:
            info_video["tipo_camara"] = partes_nombre[4] + "_frontView_"+partes_nombre[0].split("video")[0]
        else:
            info_video["tipo_camara"] = partes_nombre[4] + "_frontView_RGB"

        info_video["gesto"] = partes_nombre[5]  # Eliminamos la extension
        info_video["mano_usada"] = partes_nombre[6].split(".")[0]  # Eliminamos el gesto

    return info_video

# Ejemplo de uso
# ruta_video = "video_001_0_camera1_A_rightHand.mp4"
# info = obtener_info_video(ruta_video)
#
# # Imprimir la información
# for clave, valor in info.items():
#     print(f"{clave}: {valor}")

# Ejemplo para obtener información de todos los videos en una carpeta

carpeta_videos = "../../mirari" #Colocamos la ruta de la carpeta donde se encuentren los videos
# for nombre_archivo in os.listdir(carpeta_videos):

for root, dirs, files in os.walk(carpeta_videos):
        for file in files:
            nombre_final = ""
            if file.endswith((".mkv", ".mp4", ".avi", ".mov")): #Filtramos por los formatos de video más comunes
                ruta_completa = os.path.join(root, file)
                info = obtener_info_video(ruta_completa)
                nombre_final = "bi_"+info["tipo_camara"]+"_"+info["gesto"]+"_"+info["mano_usada"]+"_"+info["id"]+"_"+info["numero_video"]+info["extension"]
                print("\n")
                print(file)
                print(nombre_final)
                shutil.copy(ruta_completa, "../../datasetLSE_prueba/"+nombre_final)
                # print(f"\nInformación de {file}:")
                # for clave, valor in info.items():
                #     print(f"  {clave}: {valor}")
