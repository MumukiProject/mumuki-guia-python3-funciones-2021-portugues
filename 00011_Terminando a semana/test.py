
  def test_o_sábado_é_fim_de_semana(self):
    self.assertTrue(e_fim_de_semana("sábado") or e_fim_de_semana("sabado"))

  def test_o_domingo_é_fim_de_semana(self):
    self.assertTrue(e_fim_de_semana("domingo"))

  def test_a_segunda_não_é_fim_de_semana(self):
    self.assertFalse(e_fim_de_semana("lunes"))

  def test_a_sexta_não_é_fim_de_semana(self):
    self.assertFalse(e_fim_de_semana("viernes"))


