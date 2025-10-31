# Detección de Opacidades en Radiografías Torácicas  
**Procesamiento de imágenes biomédicas con Python (OpenCV, NumPy y Matplotlib)**

Este proyecto utiliza técnicas básicas de **procesamiento digital de imágenes** para identificar **zonas opacas en radiografías de tórax**, las cuales pueden estar asociadas a patologías respiratorias como neumonía o fibrosis pulmonar.  

El objetivo es facilitar el **preprocesamiento y análisis visual** para apoyar al médico en la detección temprana de alteraciones pulmonares.  

---

## Descripción del proyecto

El algoritmo implementa una secuencia de pasos sencillos pero efectivos para mejorar la interpretación visual de una radiografía torácica:

1. **Carga y normalización de la imagen**  
   Convierte la radiografía a escala de grises y ajusta sus valores de intensidad entre 0 y 1.

2. **Suavizado mediante filtro Gaussiano**  
   Reduce el ruido sin perder detalles importantes.

3. **Realce de contraste**  
   Se aplica ecualización de histograma para mejorar la visibilidad de estructuras internas.

4. **Segmentación mediante umbrales múltiples**  
   Se combinan dos técnicas:  
   - **Umbral adaptativo (Gaussian Adaptive Threshold)**  
   - **Umbral de Otsu**  
   La combinación permite resaltar zonas brillantes u opacas con mayor precisión.

5. **Análisis morfológico y conteo de regiones opacas**  
   Se detectan componentes conectados y se cuantifican regiones con opacidades significativas.

6. **Evaluación automática**  
   Según el número de regiones opacas detectadas, se emite una evaluación:
   - **Baja opacidad — Pulmones normales**
   - **Opacidad moderada — Revisión recomendada**
   - **Alta opacidad — Posible patología**

## Archivos de entrada

- Las imágenes de radiografías de tórax usadas en este proyecto se obtuvieron de:

  [Kaggle Chest X-Ray Dataset](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia)

- Para reproducir el análisis, coloca las imágenes que quieras analizar dentro de la carpeta `/imagenes`.
