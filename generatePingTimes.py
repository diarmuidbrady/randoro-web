def generate_ping_times(T, N, L):
    """function to separate total time into fixed and random components and then integrate."""

    import random
    import numpy as np
    
    # Validation check
    assert T > N * L
    
    # fixed and random component
    fixed_comp = N * L
    random_comp = T - (N * L)

    # generate random portions
    wait_times = np.array([random.uniform(0,1) for i in range(N)])
    wait_times = wait_times * random_comp / sum(wait_times)

    # use wait times to get intervals
    random_intervals = [round(sum(wait_times[:i+1]) + (L*i), 3) for i in range(N)]

    return random_intervals

if __name__ == "__main__":
    T = 180
    N = 26
    L = 3
    str_interval = [" "] * 225
    for i, t in enumerate(generate_ping_times(T, N, L)):
        print(f"Step {i}: {t}")
        idx = round(t / T * len(str_interval))
        str_interval[idx] = "*"


    print("\n\n\n")
    print("|", "".join(str_interval), "|")
    print("\n\n\n")