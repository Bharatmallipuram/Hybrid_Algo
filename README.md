# 🏆 Hybrid N-Queens Solver (Genetic Algorithm + Beam Search)

## 📌 Overview
This project implements a **hybrid algorithm** combining **Genetic Algorithm (GA)** and **Local Beam Search (LBS)** to efficiently solve the **N-Queens problem**. The algorithm finds a configuration where no two queens attack each other.

## 🎯 Problem Statement
The **N-Queens problem** requires placing `N` queens on an `N × N` chessboard such that **no two queens attack each other** (i.e., no two queens share the same row, column, or diagonal).

---

## 🚀 Features
- **Genetic Algorithm (GA)** for global search.
- **Local Beam Search (LBS)** to refine solutions.
- **Mutation & Crossover** for genetic evolution.
- **Configurable Parameters** like mutation rate, population size, and beam width.
- **Efficiently finds solutions for large N values**.

---

## ⚙️ Installation & Usage

### 🔹 Prerequisites
- Python 3.x

### 🔹 Run the Script
```bash
python n_queens_solver.py
```

### 🔹 Example Usage
```bash
Enter Number of Queens: 8
Solution: [4, 6, 0, 2, 7, 5, 3, 1]
Number of attacks: 0
Generation: 43
```
🇰 **Solution `[4, 6, 0, 2, 7, 5, 3, 1]`** places queens safely with **zero attacks**.

---

## 📝 Code Explanation

### **1️⃣ Generate Random Board**
```python
import random

def generate_board(n):
    return [random.randint(0, n-1) for _ in range(n)]
```
- Creates a **random queen placement** in an `N × N` chessboard.

### **2️⃣ Fitness Function (Attack Calculation)**
```python
def calculate_attacks(board):
    n = len(board)
    attacks = 0
    for i in range(n):
        for j in range(i+1, n):
            if board[i] == board[j] or abs(i - j) == abs(board[i] - board[j]):
                attacks += 1
    return attacks
```
- Counts **conflicting queens** based on row and diagonal positions.

### **3️⃣ Beam Search Optimization**
```python
def beam_search(parent, beam_width):
    while True:
        neighbors = [mutate(parent) for _ in range(beam_width)]
        best_neighbor = min(neighbors, key=calculate_attacks)

        if calculate_attacks(best_neighbor) >= calculate_attacks(parent):
            break  # Stop if no improvement
        parent = best_neighbor
    return parent
```
- **Mutates solutions** and picks the **best alternative**.

### **4️⃣ Crossover (Combining Two Solutions)**
```python
def crossover(parent1, parent2):
    n = len(parent1)
    crossover_point = random.randint(1, n-1)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child
```
- **Combines parts of two parents** to form a new solution.

### **5️⃣ Mutation (Small Random Change)**
```python
def mutate(board):
    n = len(board)
    mutated_board = board[:]
    index = random.randint(0, n-1)
    new_position = random.randint(0, n-1)
    mutated_board[index] = new_position
    return mutated_board
```
- **Randomly changes a queen’s position**.

### **6️⃣ Genetic Algorithm**
```python
def genetic_algorithm(n, population_size, mutation_rate, max_iterations, beam_width):
    population = [generate_board(n) for _ in range(population_size)]
    
    for generation in range(max_iterations):
        population.sort(key=calculate_attacks)
        if calculate_attacks(population[0]) == 0:
            return population[0], generation

        new_population = []
        for _ in range(population_size // 2):
            parent1, parent2 = random.choice(population), random.choice(population)
            parent1, parent2 = beam_search(parent1, beam_width), beam_search(parent2, beam_width)
            child = crossover(parent1, parent2)
            if random.random() < mutation_rate:
                child = mutate(child)
            new_population.append(child)

        population = new_population
    return population[0], max_iterations
```
- **Uses crossover, mutation, and beam search** for optimization.

---

## 🏋️ Running the Algorithm

```python
n = int(input("Enter Number of Queens: "))  
population_size = 50  
mutation_rate = 0.1
max_iterations = 1000  
beam_width = 10  

solution, generation = genetic_algorithm(n, population_size, mutation_rate, max_iterations, beam_width)
print("Solution:", solution)
print("Number of attacks:", calculate_attacks(solution))
print("Generation:", generation)
```

---

## 📊 Results & Performance
- **For `N=8`**, solutions are usually found in **< 100 generations**.
- **Beam Search improves** convergence speed.
- **Can handle large values of `N` (e.g., `N=100`) efficiently**.

---

## 🔧 Configuration Parameters
Modify these values in `n_queens_solver.py`:
```python
n = 8               # Number of Queens
population_size = 50  
mutation_rate = 0.1  
max_iterations = 1000  
beam_width = 10  
```

---

## 📀 Future Improvements
- **Hyperparameter tuning** for better performance.
- **Parallel processing** for faster execution.
- **Better mutation strategies** to improve search diversity.

---

## 👨‍💻 Author
- **M Bharat Kumar**  
- [GitHub Repository](https://github.com/Bharatmallipuram/Sentiment-Analysis)

---

## 📄 License
This project is licensed under the **MIT License**.

