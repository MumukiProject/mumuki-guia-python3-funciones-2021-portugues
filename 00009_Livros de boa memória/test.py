
  def test_gosta_de_ler_25_e_verdadeiro(self):
    self.assertTrue(gosta_de_ler(25))
  
  def test_gosta_de_ler_80_e_verdadeiro(self):
    self.assertTrue(gosta_de_ler(80))
  
  def test_gosta_de_ler_1_e_falso(self):
    self.assertFalse(gosta_de_ler(1))
  
  def test_gosta_de_ler_15_e_falso(self):
    self.assertFalse(gosta_de_ler(15))
  
  
