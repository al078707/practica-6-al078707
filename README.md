Explicación paso a paso del código
Paso 1: Importación de módulos
python
import math
from pprint import pprint
math: Este módulo se importa, aunque no se utiliza directamente en el código proporcionado. Sin embargo, es común que en cálculos de ingeniería se necesiten funciones matemáticas avanzadas (trigonometría, logaritmos, etc.).
pprint: Permite imprimir estructuras de datos complejas (como diccionarios o listas anidadas) de una manera más legible. No se usa directamente, pero podría ser útil para depurar o visualizar datos.
Paso 2: Definición de precios unitarios
python
unit_prices = {
    "concrete_m3": 1500.0,
    "steel_kg": 25.0,
    "masonry_m2": 400.0,
    "excavation_m3": 120.0,
    "backfill_m3": 80.0,
    "formwork_m2": 180.0,
    "beam_linear_m": 300.0,
    "column_unit": 800.0,
}
Se define un diccionario llamado unit_prices que contiene los precios unitarios de diferentes materiales y trabajos de construcción.
Los precios están en pesos mexicanos (MXN).
Este diccionario permite modificar fácilmente los precios sin tener que buscar y reemplazar valores en todo el código.
Paso 3: Definición de coeficientes y supuestos
python
steel_per_m3 = 80.0  # kg/m3
formwork_per_m3 = 2.5
Se definen dos variables que representan coeficientes importantes:
steel_per_m3: Cantidad de acero (en kg) necesaria por cada metro cúbico de concreto.
formwork_per_m3: Área de encofrado (en m²) necesaria por cada metro cúbico de concreto.
Estos coeficientes son supuestos y deberían ajustarse según las especificaciones del proyecto.
Paso 4: Definición de funciones de cuantificación
python
def vol_column(width_m, depth_m, height_m):
    return width_m * depth_m * height_m

def vol_beam(width_m, depth_m, length_m):
    return width_m * depth_m * length_m

def vol_slab(area_m2, thickness_m):
    return area_m2 * thickness_m

def vol_wall(length_m, height_m, thickness_m):
    return length_m * height_m * thickness_m

def vol_footing(length_m, width_m, depth_m):
    return length_m * width_m * depth_m

def steel_from_concrete_vol(vol_m3, steel_per_m3_local=steel_per_m3):
    return vol_m3 * steel_per_m3_local

def formwork_area_from_concrete(vol_m3, factor=formwork_per_m3):
    return vol_m3 * factor
Se definen varias funciones para calcular volúmenes y cantidades de materiales:
vol_column, vol_beam, vol_slab, vol_wall, vol_footing: Calculan el volumen de los elementos estructurales básicos.
steel_from_concrete_vol: Calcula la cantidad de acero necesaria a partir del volumen de concreto, utilizando el coeficiente steel_per_m3.
formwork_area_from_concrete: Calcula el área de encofrado necesaria a partir del volumen de concreto, utilizando el coeficiente formwork_per_m3.
Las funciones permiten reutilizar el código y facilitan la lectura del programa.
Paso 5: Definición de la entrada de datos (elementos)
python
elements = [
    [1, "column", [16, 0.40, 0.40, 3.0]],
    [2, "beam", [8, 0.30, 0.60, 6.0]],
    [3, "slab", [200.0, 0.12]],
    [4, "wall", [40.0, 3.0, 0.12]],
    [5, "footing", [16, 1.2, 1.2, 0.50]],
    [6, "excavation", [16 * 1.2 * 1.2 * 0.5]],
]
Se define una lista llamada elements que contiene la información de cada elemento de construcción.
Cada elemento es una lista que contiene:
eid: Un identificador único para el elemento.
etype: El tipo de elemento ("column", "beam", "slab", "wall", "footing", "excavation").
props: Una lista de propiedades específicas del elemento (dimensiones, cantidades, etc.).
Esta es la parte del código que se modificaría para ingresar los datos de un proyecto real.
Paso 6: Inicialización de listas para resultados
python
boq = []
material_summary = []
Se crean dos listas vacías:
boq (Bill of Quantities): Almacenará la información detallada de cada partida del presupuesto (descripción, cantidad, unidad, precio unitario, precio total).
material_summary: Almacenará un resumen de las cantidades de materiales por partida (concreto, acero, encofrado, etc.).
Paso 7: Iteración sobre los elementos y cálculo de cantidades y costos
python
for el in elements:
    eid = el[0]
    etype = el[1]
    props = el[2]
    description = ""
    qty = 0.0
    unit = ""
    total_price = 0.0

    conc = 0.0
    steel = 0.0
    formwork = 0.0
    masonry_area = 0.0
    excav = 0.0
    backfill = 0.0

    if etype == "column":
        count, w, d, h = props
        vol_each = vol_column(w, d, h)
        conc = vol_each * count
        steel = steel_from_concrete_vol(conc)
        formwork = formwork_area_from_concrete(conc)
        description = f"Columnas {count} (#{w:.2f}x{d:.2f} m, h={h:.2f} m)"
        qty = count
        unit = "u"
        cost_conc = conc * unit_prices["concrete_m3"]
        cost_steel = steel * unit_prices["steel_kg"]
        cost_form = formwork * unit_prices["formwork_m2"]
        total_price = cost_conc + cost_steel + cost_form

    elif etype == "beam":
        count, w, d, L = props
        vol_each = vol_beam(w, d, L)
        conc = vol_each * count
        steel = steel_from_concrete_vol(conc)
        formwork = formwork_area_from_concrete(conc)
        description = f"Vigas {count} (#{w:.2f}x{d:.2f} m, L={L:.2f} m)"
        qty = count
        unit = "u"
        cost_conc = conc * unit_prices["concrete_m3"]
        cost_steel = steel * unit_prices["steel_kg"]
        cost_form = formwork * unit_prices["formwork_m2"]
        total_price = cost_conc + cost_steel + cost_form

    elif etype == "slab":
        area, t = props
        conc = vol_slab(area, t)
        steel = steel_from_concrete_vol(conc)
        formwork = formwork_area_from_concrete(conc)
        description = f"Losa (Área={area:.1f} m2, espesor={t:.3f} m)"
        qty = area
        unit = "m2"
        cost_conc = conc * unit_prices["concrete_m3"]
        cost_steel = steel * unit_prices["steel_kg"]
        cost_form = formwork * unit_prices["formwork_m2"]
        total_price = cost_conc + cost_steel + cost_form

    elif etype == "wall":
        L_total, h, thick = props
        vol = vol_wall(L_total, h, thick)
        conc = 0.0
        masonry_area = L_total * h
        description = f"Muro (L={L_total:.1f} m, h={h:.2f} m, esp={thick:.3f} m)"
        qty = masonry_area
        unit = "m2"
        cost_masonry = masonry_area * unit_prices["masonry_m2"]
        total_price = cost_masonry

    elif etype == "footing":
        count, Lf, Wf, Df = props
        vol_each = vol_footing(Lf, Wf, Df)
        conc = vol_each * count
        steel = steel_from_concrete_vol(conc)
        formwork = formwork_area_from_concrete(conc)
        excav = vol_each * count
        backfill = vol_each * count * 0.5
        description = f"Zapata {count} (#{Lf:.2f}x{Wf:.2f}x{Df:.2f} m)"
        qty = count
        unit = "u"
        cost_conc = conc * unit_prices["concrete_m3"]
        cost_steel = steel * unit_prices["steel_kg"]
        cost_form = formwork * unit_prices["formwork_m2"]
        cost_excav = excav * unit_prices["excavation_m3"]
        cost_back = backfill * unit_prices["backfill_m3"]
        total_price = cost_conc + cost_steel + cost_form + cost_excav + cost_back

    elif etype == "excavation":
        vol = props[0]
        excav = vol
        description = f"Excavación (vol={vol:.2f} m3)"
        qty = vol
        unit = "m3"
        total_price = excav * unit_prices["excavation_m3"]

    else:
        description = f"Partida no reconocida (tipo={etype})"
        qty = 0.0
        unit = "na"
        total_price = 0.0

    boq.append([eid, etype, description, qty, unit, round(total_price / qty, 2) if qty not in (0, None) else 0.0, round(total_price, 2)])
    material_summary.append([eid, etype, round(conc, 4), round(steel, 2), round(formwork, 2), round(masonry_area, 4), round(excav, 4), round(backfill, 4)])
Este es el corazón del programa. Itera sobre cada elemento en la lista elements.
Para cada elemento, extrae el tipo (etype) y las propiedades (props).
Utiliza una serie de sentencias if/elif/else para determinar el tipo de elemento y realizar los cálculos correspondientes:
Calcula el volumen de concreto, la cantidad de acero, el área de encofrado, etc., utilizando las funciones definidas en el Paso 4.
Calcula el costo total de la partida multiplicando las cantidades por los precios unitarios del diccionario unit_prices.
Crea una descripción textual de la partida.
Agrega la información de la partida a las listas boq y material_summary.
Paso 8: Cálculo de totales
python
total_concrete = sum(row[2] for row in material_summary)
total_steel = sum(row[3] for row in material_summary)
total_formwork = sum(row[4] for row in material_summary)
total_masonry_m2 = sum(row[5] for row in material_summary)
total_excav = sum(row[6] for row in material_summary)
total_backfill = sum(row[7] for row in material_summary)
total_budget = sum(row[6] for row in boq)
Calcula los totales de los diferentes materiales (concreto, acero, encofrado, etc.) sumando los valores correspondientes en la lista material_summary.
Calcula el presupuesto total sumando los precios totales de cada partida en la lista boq.
Paso 9: Impresión de resultados
python
print("\n--- CUANTIFICACIÓN Y PRESUPUESTO AUTOMÁTICO (Resumen) ---\n")
print("BOQ (partidas):")
print("ID | Tipo | Descripción | Cantidad | Unidad | Precio unitario | Total")
for row in boq:
    print(f"{row[0]:>2} | {row[1]:<6} | {row[2]:<60} | {row[3]:>8} | {row[4]:<4} | ${row[5]:>10,.2f} | ${row[6]:>10,.2f}")

print("\nDetalle de materiales por partida:")
print("ID | Tipo | Concreto m3 | Acero kg | Encofrado m2 | Mampostería m2 | Excav m3 | Backfill m3")
for row in material_summary:
    print(f"{row[0]:>2} | {row[1]:<6} | {row[2]:>11.4f} | {row[3]:>8.2f} | {row[4]:>12.2f} | {row[5]:>13.2f} | {row[6]:>8.3f} | {row[7]:>10.3f}")

print("\nTotales de materiales:")
print(f"  Concreto total: {total_concrete:.4f} m3")
print(f"  Acero total: {total_steel:.2f} kg")
print(f"  Encofrado total: {total_formwork:.2f} m2")
print(f"  Mampostería total: {total_masonry_m2:.2f} m2")
print(f"  Excavación total: {total_excav:.3f} m3")
print(f"  Backfill total: {total_backfill:.3f} m3")
print(f"\nPresupuesto total: ${total_budget:,.2f} MXN\n")

print("Sugerencias:")
print(" - Revisa los coeficientes de acero y encofrado por m3 según los planos estructurales reales.")
print(" - Añadir partidas de acabados, instalaciones, mano de obra directa y gastos generales/beneficio.")
print(" - Vincular con un catálogo de precios actualizado para mayor precisión.\n")
Imprime los resultados en un formato legible:
El BOQ (Bill of Quantities) con la descripción, cantidad, unidad, precio unitario y precio total de cada partida.
Un resumen de las cantidades de materiales por partida.
Los totales de cada material.
El presupuesto total.
Incluye algunas sugerencias para mejorar la precisión del presupuesto.
