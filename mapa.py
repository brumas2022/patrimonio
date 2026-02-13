import pandas as pd
import re

def dms_to_decimal(degrees, minutes, seconds, direction):
    decimal = float(degrees) + float(minutes)/60 + float(seconds)/3600
    if direction in ['S', 'W']:
        decimal *= -1
    return decimal

def parse_dms(dms_str):
    if pd.isna(dms_str) or dms_str == "": return None
    # Limpa a string e extrai números e direção
    parts = re.findall(r"(\d+\.?\d*)\s*(\d+\.?\d*)\s*(\d+\.?\d*)\s*([NSEW])", str(dms_str))
    if parts:
        d, m, s, dir = parts[0]
        return dms_to_decimal(d, m, s, dir)
    return None

# Lista de arquivos que você enviou
arquivos = [
    'UNIDADES_SANEAR_2025.xlsx - POÇOS ATIVOS.csv',
    'UNIDADES_SANEAR_2025.xlsx - RESERVATÓRIOS.csv',
    'UNIDADES_SANEAR_2025.xlsx - EEAT.csv'
]

lista_final = []

for arquivo in arquivos:
    try:
        df = pd.read_csv(arquivo)
        # Identifica a categoria pelo nome do arquivo
        categoria = arquivo.split('-')[-1].replace('.csv', '').strip()
        
        for _, row in df.iterrows():
            lat = parse_dms(row['LATITUDE_Y'])
            long = parse_dms(row['LONGITUDE_X'])
            
            if lat and long:
                lista_final.append({
                    'Nome': row['NOME'],
                    'Categoria': categoria,
                    'Bairro': row['BAIRRO'],
                    'Latitude': lat,
                    'Longitude': long,
                    'Status': row['ATIVA/INATIVA']
                })
    except:
        continue

# Gera o arquivo pronto para o Google Maps
df_mapa = pd.DataFrame(lista_final)
df_mapa.to_csv('MAPA_FINAL_SANEAR.csv', index=False)
print("Arquivo 'MAPA_FINAL_SANEAR.csv' gerado com sucesso!")