
import random

def generate_board(n):
    random_list = []
    for _ in range(n):
        random_list.append(random.randint(0, n-1))
    return random_list

def calculate_attacks(board):
    n = len(board)
    attacks = 0
    for i in range(n):
        for j in range(i+1, n):
            if board[i] == board[j] or abs(i - j) == abs(board[i] - board[j]):
                attacks += 1
    return attacks

def beam_search(parent, beam_width):
    current_solution = parent

    while True:
        best_neighbor = []
        neighbors = []
        for _ in range(beam_width):
            neighbor = mutate(parent)
            neighbors.append(neighbor)
    
        best_neighbor = min(neighbors, key=calculate_attacks)

        if calculate_attacks(best_neighbor) >= calculate_attacks(current_solution):  
            break
        current_solution = best_neighbor
    return current_solution

def crossover(parent1, parent2):
    n = len(parent1)
    crossover_point = random.randint(1, n-1)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child

def mutate(board):
    n = len(board)
    mutated_board = board[:]
    index = random.randint(0, n-1)
    new_position = random.randint(0, n-1)
    mutated_board[index] = new_position
    return mutated_board

def genetic_algorithm(n, population_size, mutation_rate, max_iterations, beam_width):

    population = []
    for _ in range(population_size):
        individual = generate_board(n)
        population.append(individual)

    generation = 0 

    for _ in range(max_iterations):
        population = sorted(population, key=calculate_attacks)
        if calculate_attacks(population[0]) == 0:
            return population[0], generation 

        new_population = []
        for _ in range(population_size // 2):
            parent1 = random.choice(population)
            parent2 = random.choice(population)
            parent1_bs = beam_search(parent1, beam_width)
            parent2_bs = beam_search(parent2, beam_width)
            child = crossover(parent1_bs, parent2_bs)
            if random.random() < mutation_rate:
                child = mutate(child)
            new_population.append(child)

        population = new_population
        generation += 1  

    return population[0], generation  


n = int(input("Enter Number of Queens: "))  
population_size = 50  
mutation_rate = 0.1 
max_iterations = 1000  
beam_width = 10  

solution, generation = genetic_algorithm(n, population_size, mutation_rate, max_iterations, beam_width)
print("Solution:", solution)
print("Number of attacks:", calculate_attacks(solution))
print("Generation:", generation)

