# import math


# points = [
#     ('A', (525,187)), ('B', (295,946)), ('C', (364,787)), ('D', (533,5)),
#     ('E', (203,862)), ('F', (625,11)), ('G', (824,675)), ('H', (369,58)),
#     ('I', (308,785)), ('J', (726,766)), ('K', (155,22)), ('L', (197,879)),
#     ('M', (881,599)), ('N', (862,953)), ('O', (328,391)), ('P', (983,744)),
#     ('Q', (426,695)), ('R', (478,583)), ('S', (821,911)), ('T', (79,60)),
#     ('U', (665,272)), ('V', (191,773)), ('W', (114,281)), ('X', (800,567)),
#     ('Y', (222,693)), ('Z', (846,961)), ('a', (215,740)), ('b', (353,769)),
#     ('c', (750,726)), ('d', (908,909)), ('e', (309,658)), ('f', (867,649)),
#     ('g', (592,106)), ('h', (16,637)), ('i', (54,796)), ('j', (449,649)),
#     ('k', (980,654)), ('l', (594,819)), ('m', (764,101)), ('n', (921,307)),
#     ('o', (928,647)), ('p', (738,196)), ('q', (550,578)), ('r', (478,489)),
#     ('s', (449,755)), ('t', (189,415)), ('u', (433,545)), ('v', (967,478)),
#     ('w', (149,416)), ('x', (144,117)), ('y', (298,972)), ('z', (854,144))
# ]

# # Toroidal distance function
# def torus_dist(p1, p2):
#     dx = min(abs(p1[0] - p2[0]), 1000 - abs(p1[0] - p2[0]))
#     dy = min(abs(p1[1] - p2[1]), 1000 - abs(p1[1] - p2[1]))
#     return math.hypot(dx, dy)

# # Build tour using nearest neighbor
# def nearest_neighbor(points):
#     remaining = points[:]
#     path = [remaining.pop(0)]  # start at first point
#     while remaining:
#         last = path[-1][1]
#         next_point = min(remaining, key=lambda p: torus_dist(last, p[1]))
#         path.append(next_point)
#         remaining.remove(next_point)
#     return path

# # Run algorithm
# path = nearest_neighbor(points)
# labels = [label for label, _ in path]
# # Add return to start
# labels.append(labels[0])

# # Output 52-character path
# print("".join(labels))


'''-------------------------------------------------
import math
import random
import time

# List of 52 points labeled A-Z and a-z with (x, y) coordinates
points = {
    'A': (525, 187), 'B': (295, 946), 'C': (364, 787), 'D': (533, 5),
    'E': (203, 862), 'F': (625, 11), 'G': (824, 675), 'H': (369, 58),
    'I': (308, 785), 'J': (726, 766), 'K': (155, 22), 'L': (197, 879),
    'M': (881, 599), 'N': (862, 953), 'O': (328, 391), 'P': (983, 744),
    'Q': (426, 695), 'R': (478, 583), 'S': (821, 911), 'T': (79, 60),
    'U': (665, 272), 'V': (191, 773), 'W': (114, 281), 'X': (800, 567),
    'Y': (222, 693), 'Z': (846, 961), 'a': (215, 740), 'b': (353, 769),
    'c': (750, 726), 'd': (908, 909), 'e': (309, 658), 'f': (867, 649),
    'g': (592, 106), 'h': (16, 637), 'i': (54, 796), 'j': (449, 649),
    'k': (980, 654), 'l': (594, 819), 'm': (764, 101), 'n': (921, 307),
    'o': (928, 647), 'p': (738, 196), 'q': (550, 578), 'r': (478, 489),
    's': (449, 755), 't': (189, 415), 'u': (433, 545), 'v': (967, 478),
    'w': (149, 416), 'x': (144, 117), 'y': (298, 972), 'z': (854, 144),
}

def toroidal_distance(a, b, size=1000):
    x1, y1 = points[a]
    x2, y2 = points[b]
    dx = min(abs(x1 - x2), size - abs(x1 - x2))
    dy = min(abs(y1 - y2), size - abs(y1 - y2))
    return math.hypot(dx, dy)

def total_distance(route):
    return sum(toroidal_distance(route[i], route[(i + 1) % len(route)]) for i in range(len(route)))

def greedy_route(start):
    unvisited = set(points.keys())
    route = [start]
    unvisited.remove(start)
    while unvisited:
        last = route[-1]
        next_point = min(unvisited, key=lambda p: toroidal_distance(last, p))
        route.append(next_point)
        unvisited.remove(next_point)
    return route

def two_opt(route):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                if j - i == 1:
                    continue
                new_route = route[:i] + route[i:j][::-1] + route[j:]
                if total_distance(new_route) < total_distance(route):
                    route = new_route
                    improved = True
    return route

def simulated_annealing(route, initial_temp=10000, cooling_rate=0.995, temp_min=0.01, max_time=600):
    current_route = route[:]
    current_distance = total_distance(current_route)
    best_route = current_route[:]
    best_distance = current_distance

    temp = initial_temp
    start_time = time.time()

    while temp > temp_min and (time.time() - start_time < max_time):
        i, j = sorted(random.sample(range(len(route)), 2))
        if i == j:
            continue
        new_route = current_route[:]
        new_route[i:j] = reversed(current_route[i:j])
        new_distance = total_distance(new_route)

        if new_distance < current_distance or random.random() < math.exp((current_distance - new_distance) / temp):
            current_route = new_route
            current_distance = new_distance
            if new_distance < best_distance:
                best_route = new_route
                best_distance = new_distance

        temp *= cooling_rate

    return best_route, best_distance


if __name__ == "__main__":
    best_overall_route = None
    best_overall_dist = float("inf")

    for start in points:
        print(f"Trying greedy path from {start}...")
        greedy = greedy_route(start)
        opt_route = two_opt(greedy)
        sa_route, sa_dist = simulated_annealing(opt_route, max_time=300)

        if sa_dist < best_overall_dist:
            best_overall_dist = sa_dist
            best_overall_route = sa_route

    print("\n✅ Best route found:")
    print(' '.join(best_overall_route))
    print(f"\n📏 Path length: {best_overall_dist}")
------------------------------------------'''

import math
import random
import time

# Points
points = {
    'A': (525,187), 'B': (295,946), 'C': (364,787), 'D': (533,5), 'E': (203,862), 'F': (625,11),
    'G': (824,675), 'H': (369,58), 'I': (308,785), 'J': (726,766), 'K': (155,22), 'L': (197,879),
    'M': (881,599), 'N': (862,953), 'O': (328,391), 'P': (983,744), 'Q': (426,695), 'R': (478,583),
    'S': (821,911), 'T': (79,60), 'U': (665,272), 'V': (191,773), 'W': (114,281), 'X': (800,567),
    'Y': (222,693), 'Z': (846,961), 'a': (215,740), 'b': (353,769), 'c': (750,726), 'd': (908,909),
    'e': (309,658), 'f': (867,649), 'g': (592,106), 'h': (16,637), 'i': (54,796), 'j': (449,649),
    'k': (980,654), 'l': (594,819), 'm': (764,101), 'n': (921,307), 'o': (928,647), 'p': (738,196),
    'q': (550,578), 'r': (478,489), 's': (449,755), 't': (189,415), 'u': (433,545), 'v': (967,478),
    'w': (149,416), 'x': (144,117), 'y': (298,972), 'z': (854,144),
}

GRID_SIZE = 1000

# Toroidal distance function
def toroidal_distance(a, b):
    dx = min(abs(a[0] - b[0]), GRID_SIZE - abs(a[0] - b[0]))
    dy = min(abs(a[1] - b[1]), GRID_SIZE - abs(a[1] - b[1]))
    return math.hypot(dx, dy)

# Total distance of a tour
def total_distance(path):
    return sum(toroidal_distance(points[path[i]], points[path[(i+1)%len(path)]]) for i in range(len(path)))

# 2-opt improvement (lightweight)
def two_opt(route):
    best = route[:]
    best_dist = total_distance(best)
    for _ in range(120):  # Only 10 random swaps to keep it fast
        i, j = sorted(random.sample(range(len(route)), 2))
        if i == 0 and j == len(route)-1: continue
        new = best[:i] + best[i:j+1][::-1] + best[j+1:]
        new_dist = total_distance(new)
        if new_dist < best_dist:
            best, best_dist = new, new_dist
    return best

# Crossover (order-based)
def crossover(parent1, parent2):
    a, b = sorted(random.sample(range(len(parent1)), 2))
    child = parent1[a:b]
    for p in parent2:
        if p not in child:
            child.append(p)
    return child

# Mutation (swap)
def mutate(route, rate=0.02):
    for i in range(len(route)):
        if random.random() < rate:
            j = random.randint(0, len(route) - 1)
            route[i], route[j] = route[j], route[i]

# Genetic Algorithm
def genetic_algorithm(pop_size=100, generations=1000, mutation_rate=0.02):
    population = [random.sample(list(points.keys()), 52) for _ in range(pop_size)]
    best = min(population, key=total_distance)
    best_dist = total_distance(best)
    print(f"Initial distance: {best_dist:.4f}")

    for gen in range(generations):
        population = sorted(population, key=total_distance)
        elites = population[:10]  # Keep top 10
        new_population = elites[:]

        while len(new_population) < pop_size:
            p1, p2 = random.sample(elites, 2)
            child = crossover(p1, p2)
            mutate(child, mutation_rate)
            child = two_opt(child)
            new_population.append(child)

        population = new_population
        current_best = min(population, key=total_distance)
        current_dist = total_distance(current_best)
        if current_dist < best_dist:
            best = current_best
            best_dist = current_dist
            print(f"Gen {gen+1}: New best {best_dist:.4f}")

    return best, best_dist

# Run
start = time.time()
path, dist = genetic_algorithm(pop_size=280, generations=5000)
end = time.time()

print("\nBest path:", ''.join(path))
print("Best distance:", dist)
print("Time:", round(end - start, 2), "seconds")

