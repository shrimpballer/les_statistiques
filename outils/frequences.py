from statistiques import Statistiques
from typing import Any
from outils.effectifs import Effectifs

class Frequences(Statistiques):
  """
  Classe pour calculer les fréquences et fréquences cumulées d'une série de données numériques.

  Exemple d'usage:
  ---------------
  >>> from outils.frequences import Frequences
  >>> data = [1, 2, 2, 3]
  >>> freq = Frequences(data)
  >>> freq.frequence_partielle(2)
  0.5
  >>> freq.frequence_cumulee(mode=1)
  [0.25, 0.75, 1.0]
  >>> freq.frequence_cumulee()
  1.0
  """

  def __init__(self, serie: list[Any]):
    super().__init__(serie)
    self._eff = Effectifs(serie)

  def frequence_cumulee(self, mode: int = 0) -> float | list[float]:
    """
    Calcule la fréquence cumulée des valeurs numériques.

    :param mode: 
    - 0 (défaut) : retourne la fréquence cumulée totale (float)
    - 1 : retourne une liste des fréquences cumulées [f1, f2, ...]

    :return: float ou list[float]
    :raises TypeError: Si un élément n'est pas numérique
    :raises ValueError: Si l'effectif total est zéro

    Exemple d'usage:
    ---------------
    >>> freq = Frequences([1, 2, 2, 3])
    >>> freq.frequence_cumulee()
    1.0
    >>> freq.frequence_cumulee(mode=1)
    [0.25, 0.75, 1.0]
    """
    effectifs = self._eff.effectif_partiel()
    total = self._eff.effectif_total
    if total == 0:
      raise ValueError("L'effectif cumulé ne peut pas être zéro")
    sorted_keys = sorted(effectifs.keys())
    cumulation = []
    valeur_actuelle = 0.0
    for key in sorted_keys:
      valeur_actuelle += effectifs[key] / total
      cumulation.append(valeur_actuelle)
    if mode == 0:
      return valeur_actuelle
    else:
      return cumulation

  def frequence_partielle(self, valeur: Any) -> float:
    """
    Calcule la fréquence partielle d'une valeur numérique.

    :param valeur: La valeur numérique dont on veut la fréquence
    :type valeur: int | float
    :return: Fréquence de la valeur (float)
    :raises TypeError: Si la valeur n'est pas numérique
    :raises ValueError: Si l'effectif total est zéro

    Exemple d'usage:
    ---------------
    >>> freq = Frequences([1, 2, 2, 3])
    >>> freq.frequence_partielle(2)
    0.5
    >>> freq.frequence_partielle(1)
    0.25
    >>> freq.frequence_partielle(3)
    0.25
    """
    if not isinstance(valeur, (int, float)):
      raise TypeError("La valeur doit être numérique")
    partiel = self._eff.effectif_partiel(valeur)
    total = self._eff.effectif_total
    if not isinstance(partiel, (int, float)):
      raise TypeError("effectif_partiel doit retourner un entier ou décimal")
    if total == 0:
      raise ValueError("L'effectif total ne peut pas être zéro")
    return partiel / total # type: ignore