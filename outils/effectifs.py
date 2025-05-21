from statistiques import Statistiques
from typing import Any

class Effectifs(Statistiques):
  """
  Classe pour calculer les effectifs (occurrences) d'une série de données numériques.

  Exemple d'usage:
  ---------------
  >>> from outils.effectifs import Effectifs
  >>> data = [4, 6, 5, 5]
  >>> eff = Effectifs(data)
  >>> eff.effectif_partiel(5)
  2
  >>> eff.effectif_partiel()
  {4: 1, 6: 1, 5: 2}
  >>> eff.effectif_total
  4
  """
  def __init__(self, serie: list[Any]) -> None:
    super().__init__(serie)

  @property
  def effectif_total(self) -> int:
    """
    Nombre total d'éléments dans la série.

    :return: Le count de tous les éléments
    :rtype: int

    :Exemple:
    >>> from outils.effectifs import Effectifs
    >>> data = [4, 6, 5, 5]
    >>> eff = Effectifs(data)
    >>> eff.effectif_total
    4
    """
    return len(self.serie)

  def effectif_partiel(self, valeur: Any | None = None):  
    """
    Calcule les effectifs partiels selon une valeur ou retourne tous les effectifs.

    :param valeur:
    - None : retourne tous les effectifs (dict)
    - Autre : retourne l'effectif pour cette valeur spécifique (int)

    :return: 
    - Si valeur = None : dict {valeur: effectif} trié par ordre croissant
    - Sinon : int (nombre d'occurrences)
    Exemple d'usage:
    ---------------
    >>> from outils.effectifs import Effectifs
    >>> data = [4, 6, 5, 5]
    >>> eff = Effectifs(data)
    >>> eff.effectif_partiel()
    {4: 1, 6: 1, 5: 2}
    >>> eff.effectif_partiel(5)
    2
    >>> eff.effectif_partiel(2)
    Traceback (most recent call last):
    ...
    ValueError: Valeur non trouvée dans la série: 2
    >>> eff.effectif_partiel(2)
    Traceback (most recent call last):
    ...
    ValueError: Valeur non trouvée dans la série: 2
    """
    comptages = {}
    for item in self._serie:
      if isinstance(item, (int, float)):
        key = item
      else:
        raise TypeError(f"Anyype d'élément non pris en charge: {type(item)}")
        
      comptages[key] = comptages.get(key, 0) + 1

    if valeur is None:
      return comptages
    
    if valeur not in comptages:
      raise ValueError(f"Valeur non trouvée dans la série: {valeur}")
    
    return comptages[valeur]

  def effectif_cumule(self, mode: int = 0) -> int | float | list[int | float]:
    """
    Calcule la somme cumulative des valeurs numériques.

    :param mode: 
    - `0` ou rien : retourne la somme totale `(int)`
    - `1` : retourne une liste des cumuls `[v1, v2, ...]`
    >>> from outils.effectifs import Effectifs
    >>> data = [4, 6, 5, 5]
    >>> eff = Effectifs(data)
    >>> eff.effectif_cumule()
    20
    >>> eff.effectif_cumule(1)
    [4, 10, 15, 20]

    Exemple d'usage:
    ---------------
    >>> eff.effectif_cumule()
    20
    >>> eff.effectif_cumule(1)
    [4, 10, 15, 20]
    """
    cumulation = []
    valeur_actuelle = 0
    for nombre in self._serie:
      if isinstance(nombre, (int, float)):
        valeur_actuelle += nombre
        cumulation.append(valeur_actuelle)
      else:
        raise TypeError(f"Anyype d'élément non pris en charge: {type(nombre)}")
    
    if mode == 0:
      return valeur_actuelle
    else:
      return cumulation