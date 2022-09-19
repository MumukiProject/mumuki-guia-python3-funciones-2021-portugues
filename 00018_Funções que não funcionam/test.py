
  def test_metade_de_2_e_1(self):
    self.assertEqual(metade(2), 1)


  def test_metade_de_20_e_10(self):
    self.assertEqual(metade(20), 10)


  def test_metade_de_10_e_5(self):
    self.assertEqual(metade(10), 5)
    

  def test_soma_comprimentos_de_ola_e_mundo_a_9(self):
    self.assertEqual(soma_longitudes("hola", "mundo"), 9)


  def test_soma_comprimentos_de_chova_e_cafe_e_6(self):
    self.assertEqual(soma_longitudes("llueva", "café"), 10)

