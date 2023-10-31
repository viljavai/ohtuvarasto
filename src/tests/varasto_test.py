import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)
    
    def test_vaara_tilavuus(self):
        self.varasto = Varasto(-2)
        self.assertAlmostEqual(self.varasto.tilavuus, 0.0)
    
    def test_vaara_saldo(self):
        self.varasto = Varasto(10,-2)
        self.assertAlmostEqual(self.varasto.saldo, 0.0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)
    
    def test_lisataan_liikaa(self):
        self.varasto.lisaa_varastoon(11)
        self.assertAlmostEqual(self.varasto.saldo, 10)
    
    def test_otetaan_liika(self):
        self.varasto.lisaa_varastoon(5)
        saatu_maara = self.varasto.ota_varastosta(6)
        self.assertAlmostEqual(saatu_maara, 5)
    
    def test_ottaminen_lisaa_tilaa(self):
        #testi rikottu!!
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)
    
    def test_ota_maara_negatiivinen(self):
        saatu_maara = self.varasto.ota_varastosta(-2)
        self.assertAlmostEqual(saatu_maara, 0.0)

    def test_lisaa_maara_negatiivinen(self):
        saatu_maara = self.varasto.lisaa_varastoon(-2)
        self.assertAlmostEqual(saatu_maara, None)
    
    def test_str(self):
        self.varasto = Varasto(10,5)
        saatu = str(self.varasto)
        self.assertEqual(saatu, "saldo = 5, vielä tilaa 5")