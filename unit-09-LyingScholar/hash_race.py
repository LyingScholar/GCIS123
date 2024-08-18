def hash_first_char(string):
    if string == "":
        return 0
    return ord(string[0])

def hash_sum(string):
    if string == "":
        return 0
    total = 0
    for char in string:
        total += ord(char)
    return total

def hash_positional_sum(string):
    total = 0
    prime_number = 31
    for i in range(len(string)):
        total += ord(string[i]) * (prime_number ** (len(string) - (i+1)))
    return total


def build_collision_counter(hash_function):
    collision_counter = {}
    with open("data/long_line_words.txt") as file:
        for line in file:
            hash_code = hash_function(line.strip())
            try:
                collision_counter[hash_code] = collision_counter[hash_code] + 1
            except:
                collision_counter[hash_code] = 1
    return collision_counter

def hash_test(collision_counter, hash_function):
    hash_name = hash_function.__name__
    total_collisions = 0
    for values in collision_counter:
        total_collisions += collision_counter[values] - 1
    # print(total_collisions)
    max_collisions = 0
    for values in collision_counter:
        collisions = collision_counter[values] - 1
        if collisions > max_collisions:
            max_collisions = collisions
    # print(max_collisions)
    
    total_hash_outputs = len(collision_counter)
    # total_hash_inputs = sum(collision_counter.values())
    total_hash_inputs = 0
    for values in collision_counter:
        total_hash_inputs += collision_counter[values]
    # print (total_hash_inputs)
    
    spread = total_hash_outputs / total_hash_inputs
    speed = compute_hash_time(hash_function)
    
    print("Hash Function:", hash_name)
    print("Total Collision Rate:", round(total_collisions *100 / total_hash_inputs, 2))
    print("Maximum Number of Collisions:", max_collisions)
    print("Spread:", round(spread, 2))
    print("Speed:", round(speed, 2), "seconds")

def compute_hash_time(hash_function):
    import time
    start_time = time.perf_counter()
    with open("data/long_line_words.txt") as file:
        for line in file:
            line = line.strip()
            hash_function(line)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    return elapsed_time


def hash_positional_sum_bonus(string, set_of_used_words={}):
    if string in set_of_used_words:
        return set_of_used_words[string]
    total = 0
    prime_number = 31
    for i in range(len(string)):
        total += ord(string[i]) * (prime_number ** (len(string) - (i+1)))
    set_of_used_words[string] = total
    return total

def main():
    # print(hash_positional_sum('bdca'))
    # print(build_collision_counter(hash_sum))
    # print(build_collision_counter(hash_positional_sum))
    # hash_test(build_collision_counter(hash_first_char), hash_first_char)
    
    hash_functions = [hash, hash_first_char, hash_sum, hash_positional_sum, hash_positional_sum_bonus]
    for hash_function in hash_functions:
        collision_counter = build_collision_counter(hash_function)
        hash_test(collision_counter, hash_function)
        
        # print(hash_positional_sum("data/long_line_words.txt"))
        # print(hash_positional_sum_bonus("data/long_line_words.txt"))
        

if __name__ == "__main__":
    main()