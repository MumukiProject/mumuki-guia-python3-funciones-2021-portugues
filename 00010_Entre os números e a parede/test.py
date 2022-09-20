
  def test_está_entre_10_1_10_é_False(self):
    self.assertFalse(esta_entre(10, 1, 10))

  def test_está_entre_4_4_9_é_False(self):
    self.assertFalse(esta_entre(4, 4, 9))

  def test_está_entre_12_1_10_é_False(self):
    self.assertFalse(esta_entre(12, 1, 10))

  def test_está_entre_200_54_112_é_False(self):
    self.assertFalse(esta_entre(200, 54, 112))

  def test_está_entre_67_0_100_é_True(self):
    self.assertTrue(esta_entre(67, 0, 100))

  def test_está_entre_2_0_100_é_True(self):
    self.assertTrue(esta_entre(2, 0, 100))

  def test_está_fora_de_alcance_0_1_10_é_False(self):
    self.assertTrue(esta_fora_de_alcance(0, 1, 10))

  def test_está_fora_de_alcance_12_1_10_é_True(self):
    self.assertTrue(esta_fora_de_alcance(12, 1, 10))

  def test_está_fora_de_alcance_200_54_112_é_True(self):
    self.assertTrue(esta_fora_de_alcance(200, 54, 112))

  def test_está_fora_de_alcance_67_0_100_é_False(self):
    self.assertFalse(esta_fora_de_alcance(67, 0, 100))

  def test_está_fora_de_alcance_2_0_100_é_False(self):
    self.assertFalse(esta_fora_de_alcance(2, 0, 100))


