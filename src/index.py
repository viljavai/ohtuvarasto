from varasto import Varasto

def print_tulos(varasto, asia):
    print(f"{varasto}: {asia}")

def alustus():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)
    print("Luonnin jälkeen:")
    print_tulos("Mehuvarasto", mehua)
    print_tulos("Olutvarasto", olutta)
    return mehua, olutta

def olut_getterit(olutta):
    print("Olut getterit:")
    print(f"saldo = {olutta.saldo}")
    print(f"tilavuus = {olutta.tilavuus}")
    print(f"paljonko_mahtuu = {olutta.paljonko_mahtuu()}")

def mehu_setterit(mehua):
    print("Mehu setterit:")
    print("Lisätään 50.7")
    mehua.lisaa_varastoon(50.7)
    print_tulos("Mehuvarasto", mehua)
    print("Otetaan 3.14")
    mehua.ota_varastosta(3.14)
    print_tulos("Mehuvarasto", mehua)

def virhetilanteita():
    print("Virhetilanteita:")
    print("Varasto(-100.0);")
    huono = Varasto(-100.0)
    print(huono)

    print("Varasto(100.0, -50.7)")
    huono = Varasto(100.0, -50.7)
    print(huono)

def test_olut_getter(olutta):
    print(f"Olutvarasto: {olutta}")
    print("olutta.lisaa_varastoon(1000.0)")
    olutta.lisaa_varastoon(1000.0)
    print(f"Olutvarasto: {olutta}")

def test_mehu_setters(mehua):
    print(f"Mehuvarasto: {mehua}")
    print("mehua.lisaa_varastoon(-666.0)")
    mehua.lisaa_varastoon(-666.0)
    print(f"Mehuvarasto: {mehua}")

def test_olut_getter_0(olutta):
    print_tulos("Olutvarasto", olutta)
    print("olutta.ota_varastosta(1000.0)")
    saatiin = olutta.ota_varastosta(1000.0)
    print(f"saatiin {saatiin}")
    print_tulos("Olutvarasto", olutta)

def test_mehu_setter_neg(mehua):
    print_tulos("Mehuvarasto", mehua)
    print("mehua.otaVarastosta(-32.9)")
    saatiin = mehua.ota_varastosta(-32.9)
    print(f"saatiin {saatiin}")
    print_tulos("Mehuvarasto", mehua)

def main():
    mehua, olutta = alustus()
    olut_getterit(olutta)
    mehu_setterit(mehua)
    virhetilanteita()
    test_olut_getter(olutta)
    test_mehu_setters(mehua)
    test_olut_getter_0(olutta)
    test_mehu_setter_neg(mehua)


if __name__ == "__main__":
    main()
