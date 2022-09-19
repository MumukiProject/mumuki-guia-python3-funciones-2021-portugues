class Test(unittest.TestCase):

  def test_as_11_nao_sao_a_hora_da_verdade(self):
    self.assertFalse(e_hora_da_verdade(11))

  def test_as_14_nao_sao_a_hora_da_verdade(self):
    self.assertFalse(e_hora_da_verdade(14))
    
  def test_as_12_sao_a_hora_da_verdade(self):
    self.assertTrue(e_hora_da_verdade(12))


