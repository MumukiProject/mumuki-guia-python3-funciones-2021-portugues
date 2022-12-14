
  def test_longitude_nome_completo_Cosme_Fulanito(self):
    self.assertEqual(comprimento_nome_completo("Cosme", "Fulanito"), 14)

  def test_longitude_nome_completo_John_Snow(self):
    self.assertEqual(comprimento_nome_completo("John", "Snow"), 9)

  def test_longitude_nome_completo_Juana_Azurduy(self):
    self.assertEqual(comprimento_nome_completo("Juana", "Azurduy"), 13)
    
  def test_não_falta_contemplar_o_espaço(self):
    resultado = False
    try:
      resultado = [
        comprimento_nome_completo("", ""),
        comprimento_nome_completo("abc", "d"),
      ] == [0, 4]
    except:
      pass
    if resultado:
      self.fail("Você precisa contemplar o espaço!")
    
      
