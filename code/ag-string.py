import random

model = input("Digite o modelo: ")
# gera indivíduos com o mesmo tamanho do modelo informado
chromosome_size = len(model)
# tamanho da populacao (stático)
population_size = 100
# critério de parada: tolerância 
#   (ou seja, quando encontrar um indivíduo igual ao meu modelo)
#
# entretanto, se for muito custoso, encontrar esse indivíduo, 
#   critério de parada: número de gerações
generations = 10000

# Escolha ponderada: 
#   
def weighted_choice(items):
  total_weight = sum((item[1] for item in items))
  element = random.uniform(0, total_weight)
  for item, weight in items:
    if element < weight:
      return item
    element = element - weight
  return item

# caracter randomico
def random_character():
  return chr(int(random.randrange(32, 255, 1)))

# gerar uma populacao inicial
def random_population():
  population = []
  for i in range(population_size):
    chromosome = ""
    for j in range(chromosome_size):
      chromosome += random_character()
    population.append(chromosome)
  return population

def fitness(chromosome):
  fitness = 0
  for i in range(chromosome_size):
    fitness += abs(ord(chromosome[i]) - ord(model[i]))
  return fitness

# mutacao de um individuo
def mutation(chromosome):
  chromosome_outside = ""
  mutation_chance = 100
  for i in range(chromosome_size):
    if int(random.random() * mutation_chance) == 1:
      chromosome_outside += random_character()
    else:
      chromosome_outside += chromosome[i]
  return chromosome_outside

# cruzamento entre dois individuos
def crossover(chromosome1, chromosome2):
  position = int(random.random() * chromosome_size)
  return (chromosome1[:position] + chromosome2[position:], chromosome2[:position] + chromosome1[position:])

# Se o seu módulo não for o programa principal, 
#   mas foi importado por outro, então __name__ será "foo", 
#   não "__main__" e ele ignorará o corpo da instrução if
if __name__ == "__main__":
  population = random_population()
  for generation in range(generations):
    print("Geração %s | População: '%s'" % (generation, population[0]))
    weight_population = []
    if(population[0] == model):
      break
    for individual in population:
      fitness_value = fitness(individual)
      if fitness_value == 0:
        pair = (individual, 1.0)
      else:
        pair = (individual, 1.0 / fitness_value)
      weight_population.append(pair)
    population = []
    for i in range(int(population_size)):
      individual1 = weighted_choice(weight_population)
      individual2 = weighted_choice(weight_population)
      individual1, individual2 = crossover(individual1, individual2)
      population.append(mutation(individual1))
      population.append(mutation(individual2))
  fit_string = population[0]
  minimum_fitness = fitness(population[0])
  for individual in population:
    fit_individual = fitness(individual)
    if fit_individual <= minimum_fitness:
      fit_string = individual
      minimum_fitness = fit_individual
  print("População Final: %s" % fit_string)