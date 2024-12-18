# IA1pn.py - Módulo principal que importa los demás módulos

import IA2pn
import IA3pn
import IA4pn
import IA5pn
import IA6pn

def main():
    # Paso 1: Preparar los datos
        print("Preparando los datos...")
            data = IA2pn.preprocesar_datos("dataset.csv")
                
                    # Paso 2: Entrenar el modelo
                        print("Entrenando el modelo...")
                            modelo = IA3pn.entrenar_modelo(data)
                                
                                    # Paso 3: Evaluar el modelo
                                        print("Evaluando el modelo...")
                                            resultados = IA4pn.evaluar_modelo(modelo, data)
                                                
                                                    # Paso 4: Realizar predicciones
                                                        print("Realizando predicciones...")
                                                            predicciones = IA5pn.realizar_predicciones(modelo, data)
                                                                
                                                                    # Paso 5: Guardar resultados
                                                                        print("Guardando resultados...")
                                                                            IA6pn.guardar_resultados(predicciones)
                                                                                
                                                                                    print("¡Proceso completado!")

                                                                                    # Ejecutar el flujo principal
                                                                                    if __name__ == "__main__":
                                                                                        main()