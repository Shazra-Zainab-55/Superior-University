movies = [
    ("AAA", 20000000),
    ("bbb", 9000000),
    ("ccc", 4500000),
    ("ddd", 379000000),
    ("eee", 365000000),
    ("fff", 356000000),
    ("ggg", 200000000)
]

def calculate_average_budget(movies):
    return sum(budget for _, budget in movies) / len(movies)

def high_budget_movies(movies, average_budget):
    return [(movie, budget, budget - average_budget) for movie, budget in movies if budget > average_budget]

def add_movies():
    for _ in range(int(input("How many movies would you like to add? "))):
        movies.append((input("Enter the movie name: "), int(input("Enter the budget: "))))

add_movies()
average_budget = calculate_average_budget(movies)
high_budget = high_budget_movies(movies, average_budget)

print(f"\nAverage movie budget: ${average_budget:,.2f}")
if high_budget:
    print("\nMovies exceeding the average budget:")
    for movie, budget, diff in high_budget:
        print(f"{movie}: ${budget:,.2f} (exceeds by ${diff:,.2f})")
    print(f"\nTotal movies exceeding the average: {len(high_budget)}")
else:
    print("No movies exceeded the average budget.")
