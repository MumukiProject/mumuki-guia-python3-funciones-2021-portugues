
  def test_gosta_de_ler_25_é_verdadeiro(self):
    self.assertTrue(gosta_de_ler(25))
  
  def test_gosta_de_ler_80_é_verdadeiro(self):
    self.assertTrue(gosta_de_ler(80))
  
  def test_gosta_de_ler_1_é_falso(self):
    self.assertFalse(gosta_de_ler(1))
  
  def test_gosta_de_ler_15_é_falso(self):
    self.assertFalse(gosta_de_ler(15))
  
  
