def getDeltas(people, maxBirthYear):
  deltas = dict()
  for person in people:
    if person.birth in deltas.keys():
      deltas[person.birth] += 1
    else:
      deltas[person.birth] = 1
    if person.death in deltas.keys():
      deltas[person.death] -= 1
    elif person.death not in deltas.keys() and person.death <= maxBirthYear: # We can skip deaths after the last birth year
      deltas[person.death] = -1
  return deltas


class Person:
  def __init__(self, birth=None, death=None):
    self.birth=birth
    self.death=death

def getPopulationPeak(people):
  maxBirthYear = getMaxBirthYear(people)
  deltas = getDeltas(people, maxBirthYear)
  currentSum = 0 
  maxSum = 0
  maxYear = 0
  for year in sorted(deltas.keys()):
    currentSum += deltas[year]
    if currentSum > maxSum:
      maxSum = currentSum
      maxYear = year
  return maxYear, maxSum

def getMaxBirthYear(people):
  return max(people, key=lambda x: x.birth).birth

testPeople = [
  Person(1750,1802),
  Person(2000,2010),
  Person(1645,1760),
  Person(1985,2002),
  Person(2000,2050),
  Person(2005,2080),
]

print(getPopulationPeak(testPeople))