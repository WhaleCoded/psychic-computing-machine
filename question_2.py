import os
from typing import Dict

FILE_NAME = "data.txt"
SOLUTION_NAME = "solution.json"


def verify_solution(candidate_solution: Dict[str, int]):
    # Verifiy solution
    with open(os.path.join(os.curdir, SOLUTION_NAME), "r") as f:
        import json

        solution: dict = json.load(f)

    errors_detected = False
    for word, count in candidate_solution.items():
        if word in solution:
            if solution[word] != count:
                errors_detected = True
                print(f"Word '{word}' has count {count}, but expected {solution[word]}")
        else:
            errors_detected = True
            print(f"Word '{word}' not found in solution")

    if len(candidate_solution) != len(solution):
        errors_detected = True
        print(
            f"Candidate solution has {len(candidate_solution)} unique words, but expected {len(solution)}"
        )

    if not errors_detected:
        print("All words match the solution!")
    else:
        print("Errors detected in the solution.")


if __name__ == "__main__":
    with open(os.path.join(os.curdir, FILE_NAME), "r") as f:
        loaded_text: str = f.read()

    # Please Note: it's is the same as its for this problem

    your_solution = {}

    # your code here

    verify_solution(your_solution)
