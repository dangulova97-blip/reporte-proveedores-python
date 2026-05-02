import pandas as pd

# leer archivo
df = pd.read_excel('datos_proveedores.xlsx')

# limpiar datos
df = df.dropna()

# convertir monto a número
df['monto'] = pd.to_numeric(df['monto'], errors='coerce')

# resumen total por área
resumen_area = df.groupby('area')['monto'].sum()

print('Resumen por área:')
print(resumen_area)

# resumen por estado
resumen_estado = df.groupby('estado')['monto'].sum()

print('\nResumen por estado:')
print(resumen_estado)

# guardar resultados
with pd.ExcelWriter('reporte_final.xlsx') as writer:
    resumen_area.to_excel(writer, sheet_name='Por Area')
    resumen_estado.to_excel(writer, sheet_name='Por Estado')

# filtrar pendientes
pendientes = df[df['estado'] == 'Pendiente']

# resumen pendientes por area
resumen_pendientes = pendientes.groupby('area')['monto'].sum()

print('\nPendientes por área:')
print(resumen_pendientes)
