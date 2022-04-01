import random
import math
from math import sin
from math import cos


def generateChromosome(chrom_Len):
    chromosome = [int(random.choice([1,0])) for i in range(chrom_Len)]
    return chromosome

def generatePopulation(popul_Len, chrom_Len):
    population = [generateChromosome(chrom_Len) for i in range(popul_Len)]
    return population

def decodeChrom(chrom):
    rax = 5
    ray = 5
    rbx = -5
    rby = -5
    sumGx = 0
    sumGy= 0
    sumkuadratx = 0
    sumkuadraty = 0
    for i in range(len(chrom)//2):
         sumGx = sumGx + chrom[i] * (2**(-(i+1)))
         sumkuadratx = sumkuadratx + (2**(-(i+1)))
    for i in range(len(chrom)//2, len(chrom)):
         sumGy = sumGy + chrom[i] * (2**(-(i+1)))
         sumkuadraty = sumkuadraty + (2**(-(i+1)))
    x = rbx + ((rax - rbx)/sumkuadratx)*sumGx
    y = rby + ((ray - rby)/sumkuadraty)*sumGy
    return x, y


def generateFitness(population):
    fitness = list()
    for i in population:
       x, y= decodeChrom(i)
       hxy = (((math.cos(x))+(math.sin(y)))**2)/((x**2)+(y**2))
       fitness.append(hxy)
    return fitness


def tournament(population, fitness, n):
    idx_chrom = random.sample(range (n), round(n/4))
    parent_candidate=[(fitness[idx_chrom[i]], population[idx_chrom[i]]) for i in range(round(n/4))]
    grade = sorted(parent_candidate, key=lambda x: x[0], reverse=True)
    parent = grade[0][1]
    return parent

def crossover(parent1, parent2, pc):
    if random.random()<pc:
        titik1 = random.randint(0, len(parent1)//2)
        titik2 = random.randint((len(parent1)//2)+1, len(parent1))
        parent1[titik1:titik2],parent2[titik1:titik2] = parent2[titik1:titik2], parent1[titik1:titik2]
    return parent1, parent2

def mutation(chrom, pm):
    for i in range(len(chrom)):
        if pm > random.random():
            if chrom[i] == 0:
                chrom[i] = 1
            else:
                chrom[i] = 0
    return chrom

def regeneration(new_population, population, fitness, popul_Len, chrom_Len, pc, pm):

   	while(len(new_population) < popul_Len):

           parent1 = tournament(population, fitness, popul_Len)
           parent2 = tournament(population, fitness, popul_Len)
           parent1 = list(parent1)
           parent2 = list(parent2)
           child1, child2 = crossover(parent1, parent2, pc)
           child1 = mutation(child1, pm)
           child2 = mutation(child2, pm)
           new_population.extend([child1, child2])

def elitisme(population, fitness):
    bestChrom = [(fitness[i], population[i]) for i in range(len(population))]
    grade = sorted(bestChrom, key=lambda x: x[0])
    return [grade[0][1]]



chrom_Len=22 #panjang 1 kromosom, yaitu 22 gen
popul_Len=200 #banyaknya kromosom, yaitu 200
pm=0.1
pc=0.7
generasi = 0 #banyaknya generasi/keturunan
population=generatePopulation(popul_Len, chrom_Len)
fitness=generateFitness(population)


for i in range(12000): 
    new_population = elitisme(population, fitness)
    regeneration(new_population, population, fitness, popul_Len, chrom_Len, pc, pm)
    population = new_population
    generasi += 1
    print("Generasi ke ", generasi, "\n", end="\n")
    fitness = generateFitness(population)

print("\n")

populasi_akhir=population
fitnes_akhir=generateFitness(populasi_akhir)
idx_min=fitness.index(min(fitness))
print("ini nilai fitness terkecil : ",fitness[idx_min])
print("ini isi kromosom : ", population[0])
nilaiXY = decodeChrom(population[idx_min])
print("nilai x dan y :",nilaiXY)
