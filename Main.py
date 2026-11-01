import itertools
import time

digits = ['2', '3', '5', '6', '8', '9']

target_number = "598362" 

print("=== BRUTE FORCE SIMULATION PROGRAM ===")
print(f"looking for targets: {target_number} from digits {digits}\n")

start_time = time.time()
attempt_count = 0
found = False

for p in itertools.permutations(digits):
    attempt_count += 1
    guess = "".join(p)
    
    if attempt_count <= 5:
        print(f"try the combination of-{attempt_count}: {guess}")

    if guess == target_number:
        found = True
        end_time = time.time()
        print("\n[!] FOUND!")
        print(f"Correct combination  : {guess}")
        print(f"Total trials         : {attempt_count} time")
        print(f"Execution time       : {end_time - start_time:.6f} second")
        break

if not found:
    print("\n[x] Target not found in combination.")
