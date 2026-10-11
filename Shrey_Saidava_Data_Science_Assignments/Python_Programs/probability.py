import random
def calculate_probability(favorable_outcomes, total_outcomes):
    if total_outcomes <= 0: return 0
    return favorable_outcomes / total_outcomes
results = [random.choice(["Heads", "Tails"]) for _ in range(20)]
print(results)
print("Experimental probability of heads:", results.count("Heads") / 20)
print("Probability of even die roll:", calculate_probability(3, 6))
