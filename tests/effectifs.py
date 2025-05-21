import unittest
from outils.effectifs import Effectifs

class TestEffectifs(unittest.TestCase):
  """Suite de tests pour la classe Effectifs"""
  
  def setUp(self):
    """Préparation des données de test.
    Vous pouves changer les données ici, 
    et les valeurs attendues dans les appels `assertEqual` ou `assertRaises`."""
    self.data_numerique = [4, 6, 5, 5]
    self.data_mixte = [4, "chat", 3.5, "chien", 2]
    self.eff_num = Effectifs(self.data_numerique)
    self.eff_mix = Effectifs(self.data_mixte)

  def test_init_accepte_types_valides(self):
    """Vérifie que l'initialisation accepte les types autorisés"""
    Effectifs([1, 2.5, "abc"])

  def test_init_rejete_types_invalides(self):
    """Vérifie le rejet des types non autorisés"""
    with self.assertRaises(TypeError):
      Effectifs([True, None])

  def test_effectif_total_numerique(self):
    """Teste le compte total sur données numériques"""
    self.assertEqual(self.eff_num.effectif_total, 4)

  def test_effectif_total_mixte(self):
    """Teste le compte total sur données mixtes"""
    self.assertEqual(self.eff_mix.effectif_total, 5)

  def test_effectif_partiel_complet(self):
    """Teste le dictionnaire complet des effectifs"""
    result = self.eff_mix.effectif_partiel()
    self.assertEqual(result, {4: 1, 3.5: 1, 5: 1, 2: 1})

  def test_effectif_partiel_valeur_specifique(self):
    """Teste la recherche d'effectif par valeur"""
    self.assertEqual(self.eff_num.effectif_partiel(5), 2)

  def test_effectif_partiel_valeur_inexistante(self):
    """Teste la gestion des valeurs absentes"""
    with self.assertRaises(ValueError):
      self.eff_num.effectif_partiel(99)

  def test_effectif_cumule_somme(self):
    """Teste le calcul de la somme cumulée"""
    self.assertEqual(self.eff_num.effectif_cumule(0), 20)

  def test_effectif_cumule_chaine(self):
    """Teste le formatage en chaîne"""
    self.assertEqual(self.eff_num.effectif_cumule(""), "4 -> 10 -> 15 -> 20")

  def test_serie_transformation(self):
    """Teste la transformation des strings en longueurs"""
    self.assertEqual(self.eff_mix.serie, [4, 4, 3.5, 5, 2])

if __name__ == '__main__':
  unittest.main()