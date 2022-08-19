
  def test_le_gusta_leer_25_es_verdadero(self):
    self.assertTrue(gosta_de_ler(25))
  
  def test_le_gusta_leer_80_es_verdadero(self):
    self.assertTrue(gosta_de_ler(80))
  
  def test_le_gusta_leer_1_es_falso(self):
    self.assertFalse(gosta_de_ler(1))
  
  def test_le_gusta_leer_15_es_falso(self):
    self.assertFalse(gosta_de_ler(15))
  
  
