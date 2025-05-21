from statistiques import Statistiques
from typing import TypeVar
from outils.effectifs import Effectifs

T = TypeVar("T", int, float, str)

class Frequences(Statistiques[T]):
  def __init__(self, serie: list[T]):
    super().__init__(serie)
    self._eff = Effectifs(serie)

# freq = effectif du char / effectif cumulé
  def frequences(self, mode: int | str = 0):
    cumulation = []
    valeur_actuelle = 0
    for nombre in self._serie:
      if isinstance(nombre, (int, float)):
        valeur_actuelle += self._eff.effectif_partiel(nombre) 
        cumulation.append(str(valeur_actuelle))
      elif isinstance(nombre, str):
        valeur_actuelle += len(nombre)
        cumulation.append(str(valeur_actuelle))
      else:
        raise TypeError(f"Type d'élément non pris en charge: {type(nombre)}")
    if isinstance(mode, int):
      return valeur_actuelle
    elif isinstance(mode, str):
      return " -> ".join(map(str, cumulation))

  def frequence(self, caractere: T) -> float:
    if isinstance(caractere, str):
      c = len(caractere)
    else:
      c = caractere
    partiel = self._eff.effectif_partiel(c)
    if not isinstance(partiel, (int, float)):
      raise TypeError("effectif_partiel doit retourner un entier ou décimal")
    return partiel / self._eff.effectif_total()

  def frequence_cumulee(self, mode: int | str = 0):
    cumulation = []
    valeur_actuelle = 0
    for nombre in self.frequences():
      if isinstance(nombre, (int, float)):
        valeur_actuelle += nombre
        cumulation.append(str(valeur_actuelle))
      elif isinstance(nombre, str):
        valeur_actuelle += len(nombre)
        cumulation.append(str(valeur_actuelle))
      else:
        raise TypeError("Type non pris en charge pour la fréquence cumulée")
      
    if isinstance(mode, int):
      return valeur_actuelle
    elif isinstance(mode, str):
      return " -> ".join(map(str, cumulation))
    else:
      raise ValueError("Mode non pris en charge")
    
# exemples d'utilisation
if __name__ == "__main__":
  data = [1, 2, 3, "chat", "chien"]
  frequence = Frequences(data)
  print(f"Serie: {frequence._serie}")
  print(f"Eff. Total: {frequence._eff.effectif_total()}")
  print(f"Fréquences: {frequence.frequences()}")
  print(f"Fréquence de 'chat': {frequence.frequence('chat')}")
  print(f"Fréquence cumulée: {frequence.frequence_cumulee()}")
  print(f"Fréquence cumulée (str): {frequence.frequence_cumulee('')}")