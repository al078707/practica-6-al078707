# ============================================
# SISTEMA DE PRESUPUESTO (listas y matrices)
# ============================================

# Cada partida será una lista con la siguiente estructura:
# [ nombre, tipo, dimensiones[], precio_unitario ]
#
# tipos posibles:
#  - "zapata"  -> requiere [largo, ancho, altura]
#  - "columna" -> requiere [seccion_lado, seccion_lado, altura]
#  - "muro"    -> requiere [largo, espesor, altura]
#  - "viga"    -> requiere [base, peralte, largo]

# -------------------------------
# 1. LISTA DE PARTIDAS (ejemplo)
# -------------------------------

partidas = [
    ["Zapata Z1", "zapata",  [2.0, 2.0, 0.5], 1500],  # precio por m³
    ["Columna C1", "columna", [0.3, 0.3, 3.0], 1800],
    ["Muro M1", "muro",       [4.0, 0.15, 2.8], 1600],
    ["Viga V1", "viga",       [0.25, 0.45, 5.0], 1700]
]

# -------------------------------
# 2. FUNCIONES DE CÁLCULO
# -------------------------------

def calcular_volumen(partida):
    tipo = partida[1]
    dims = partida[2]

    if tipo == "zapata":
        largo, ancho, h = dims
        return largo * ancho * h

    elif tipo == "columna":
        a, b, h = dims
        return a * b * h

    elif tipo == "muro":
        largo, e, h = dims
        return largo * e * h

    elif tipo == "viga":
        base, peralte, largo = dims
        return base * peralte * largo

    else:
        return 0

# -------------------------------
# 3. GENERACIÓN DE PRESUPUESTO
# -------------------------------

presupuesto = []  # matriz final: [nombre, volumen, precio_unitario, costo_total]

for p in partidas:
    nombre = p[0]
    volumen = calcular_volumen(p)
    pu = p[3]
    costo = volumen * pu

    presupuesto.append([nombre, volumen, pu, costo])

# -------------------------------
# 4. IMPRESIÓN DE RESULTADOS
# -------------------------------

print("\n===== PRESUPUESTO DE OBRA =====\n")

total = 0

for item in presupuesto:
    nombre, vol, pu, costo = item
    print(f"{nombre:12} | Volumen: {vol:.2f} m³ | PU: ${pu:.2f} | Total: ${costo:.2f}")
    total += costo

print("\n----------------------------------")
print(f" TOTAL GENERAL: ${total:.2f}")
print("----------------------------------\n")
