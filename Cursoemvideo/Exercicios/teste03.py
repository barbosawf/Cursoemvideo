

def area_volume(raio, area_ou_volume):
    from math import pi

    area_ou_volume = area_ou_volume.strip().upper()
    area = 4 * pi * raio ** 2
    volume = (4 * pi * raio ** 3) / 3
    if area_ou_volume == "ÁREA" or area_ou_volume == "Area":
        return f'A área da esfera é {area:.2f} metros quadrados.'
    elif area_ou_volume == "VOLUME":
        return f'O volume da esfera é {volume:.2f} metros cúbicos.'
    else:
        return f'Default:\nA área da esfera é {area:.2f} metros quadrados.'


resp = area_volume(5, "volume")

print(resp)
