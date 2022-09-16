class Test(unittest.TestCase):

  def test_Rosario_não_é_maior_que_Bahia_Blanca(self):
    self.assertFalse(e_mais_longo_que("Rosario", "Bahía Blanca"))

  def test_Valle_de_Uco_é_maior_que_La_Punta(self):
    self.assertTrue(e_mais_longo_que("Valle de Uco", "La Punta"))