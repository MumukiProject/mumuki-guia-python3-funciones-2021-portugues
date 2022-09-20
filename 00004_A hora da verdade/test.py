class Test(unittest.TestCase):

  def test_às_11_não_são_a_hora_da_verdade(self):
    self.assertFalse(e_hora_da_verdade(11))

  def test_às_14_não_são_a_hora_da_verdade(self):
    self.assertFalse(e_hora_da_verdade(14))
    
  def test_às_12_são_a_hora_da_verdade(self):
    self.assertTrue(e_hora_da_verdade(12))


