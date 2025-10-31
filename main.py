import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar radiografia 
img = cv2.imread('Imagenes/Sano1.jpeg', cv2.IMREAD_GRAYSCALE)

# Normalizar intensidades
img_norm = cv2.normalize(img.astype('float32'), None, 0, 1, cv2.NORM_MINMAX)

# Suavizado con filtro Gaussiano 
blur = cv2.GaussianBlur(img_norm, (7, 7), 0)

# Realce de contraste
img_enhanced = cv2.equalizeHist((blur * 255).astype(np.uint8))
img_enhanced = img_enhanced.astype('float32') / 255

# Detección múltiple de opacidades usando diferentes métodos

# Umbral adaptativo
mask1 = cv2.adaptiveThreshold((img_enhanced * 255).astype(np.uint8), 255,
                             cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                             cv2.THRESH_BINARY, 45, -8)

# Umbral Otsu 
_, mask2 = cv2.threshold((img_enhanced * 255).astype(np.uint8), 0, 255,
                         cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Combinar máscaras
mask_combined = cv2.bitwise_and(mask1, mask2)

# Inversion de mascara para obtener zonas opacas
mask_inv = cv2.bitwise_not(mask_combined)
masked_img = cv2.bitwise_and(img_enhanced, img_enhanced, mask=mask_inv)

# Detección de regiones conectadas para análisis
num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(mask_inv, connectivity=8)

significant_regions = 0
total_opaque_area = 0
for i in range(1, num_labels): 
    area = stats[i, cv2.CC_STAT_AREA]
    if area > 100:  
        significant_regions += 1
        total_opaque_area += area

# Mostrar resultados
plt.figure(figsize=(12, 5))

plt.subplot(2, 4, 1)
plt.imshow(img_norm, cmap="gray")
plt.title("Radiografía Original")
plt.axis("off")

plt.subplot(2, 4, 2)
plt.imshow(blur, cmap="gray")
plt.title("Imagen Suavizada")
plt.axis("off")

plt.subplot(2, 4, 3)
plt.imshow(img_enhanced, cmap="gray")
plt.title("Realce de Contraste")
plt.axis("off")

plt.subplot(2, 4, 4)
plt.imshow(mask1, cmap="gray")
plt.title("Máscara Adaptativa")
plt.axis("off")

plt.subplot(2, 4, 5)
plt.imshow(mask2, cmap="gray")
plt.title("Máscara Otsu")
plt.axis("off")

plt.subplot(2, 4, 6)
plt.imshow(mask_combined, cmap="gray")
plt.title("Máscara Combinada")
plt.axis("off")

plt.subplot(2, 4, 7)
plt.imshow(masked_img, cmap="gray")
plt.title("Zonas Opacas Detectadas")
plt.axis("off")

plt.subplot(2, 4, 8)
plt.text(0.1, 0.9, "RESULTADOS DEL ANÁLISIS", fontsize=12)
plt.text(0.1, 0.6, f"Regiones significativas: {significant_regions}", fontsize=10)

# Evaluación
if significant_regions > 8:
    evaluation = "ALTA OPACIDAD - Posible patología"
    color = "red"
elif significant_regions > 3:
    evaluation = "OPACIDAD MODERADA - Revisar"
    color = "orange"
else:
    evaluation = "BAJA OPACIDAD - Normal"
    color = "green"

plt.text(0.1, 0.3, f"Evaluación: {evaluation}", fontsize=11, color=color)
plt.axis('off')
plt.show()

# Mostrar resultados en consola
print("ANÁLISIS DE OPACIDADES EN RADIOGRAFÍA")
print(f"Número de regiones opacas significativas: {significant_regions}")
print(f"Evaluación: {evaluation}")