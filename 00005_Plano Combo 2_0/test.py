
  def test_anterior_1_é_0(self):
    self.assertEqual(anterior(1), 0);

  def test_anterior_10_é_9(self):
    self.assertEqual(anterior(10), 9)

  def test_triplo_1_é_3(self):
    self.assertEqual(triplo(1), 3)

  def test_triplo_3_é_9(self):
    self.assertEqual(triplo(3), 9)

  def test_anterior_do_triplo_1_é_2(self):
    self.assertEqual(anterior_do_triplo(1), 2)

  def test_anterior_do_triplo_3_é_8(self):
    self.assertEqual(anterior_do_triplo(3), 8)

  def test_anterior_do_triplo_10_é_29(self):
    self.assertEqual(anterior_do_triplo(10), 29)



