
  def test_el_sabado_es_fin_de_semana(self):
    self.assertTrue(e_fim_de_semana("sábado") or e_fim_de_semana("sabado"))

  def test_el_domingo_es_fin_de_semana(self):
    self.assertTrue(e_fim_de_semana("domingo"))

  def test_el_lunes_no_es_fin_de_semana(self):
    self.assertFalse(e_fim_de_semana("lunes"))

  def test_el_viernes_no_es_fin_de_semana(self):
    self.assertFalse(e_fim_de_semana("viernes"))


