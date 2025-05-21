from typing import Any

class Statistiques:
  """
  Classe de base pour les opérations statistiques sur des données numériques.

  :param serie: Liste d'éléments numériques à analyser. Peut contenir :
  - Nombres (`int|float`)
  - Tout autre type lèvera une `TypeError`
  
  Exemple d'usage:
  ---------------
  - Utilisation de la classe de base:
  
  >>> from statistiques import Statistiques
  >>> data = [1, 2, 3, 4, 5]
  >>> stats = Statistiques(data)
  >>> stats.serie
  [1, 2, 3, 4, 5]

  - Utilisation avec l'inhéritance:

  >>> from statistiques import Statistiques
  >>> from typing import TypeVar
  >>> class Exemple(Statistiques):
  ...   def __init__(self, serie: list):
  ...     super().__init__(serie)
  ...     # définir des variables supplémentaires ici
  """
  def __init__(self, serie: list[Any]) -> None:
    self._serie = serie
    for i in serie:
      if not isinstance(i, (int, float)):
        raise TypeError(f"Type non pris en charge: {type(i)}")
  
  @property
  def serie(self) -> list[Any]:
    """Retourne la série de données numériques originale."""
    return self._serie