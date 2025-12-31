import random
import numpy as np

def generate_ping_times(work_duration_s, rest_duration_s, n_intervals, n_rounds = 3, warm_up_s=10, cooldown_s=5, min_interval_gap_s = 2, rest_first = True):
    """function to separate total time into fixed and random components and then integrate."""
    
    # Validation check
    assert work_duration_s > n_intervals * min_interval_gap_s, "Work duration must be greater than number of intervals times minimum interval gap."
    assert n_rounds > 0, "Number of rounds must be greater than zero."
    assert work_duration_s > 0, "Work duration must be greater than zero."
    assert rest_duration_s >= 0, "Rest duration must be non-negative."

    WORK = 0
    PING = 1
    REST = 2
    EXTRA= 3

    warmup = warm_up_s > 0
    rest = rest_duration_s > 0
    cooldown = cooldown_s > 0

    # initialize lists and dicts
    times = []
    pings = []
    random_intervals = {}

    # handle warm up period
    random_intervals["warm_up_start"] = 0
    random_intervals["session_start"] = warm_up_s

    # if there is a warm up period, add a ping at the start of it
    if warmup:
        times.append(random_intervals["warm_up_start"])
        pings.append(EXTRA)

    # generate work and rest periods
    for round in range(n_rounds):
            if rest_first:
                # in each round, rest comes first
                random_intervals[f"rest_{round}_start"] = warm_up_s + round * (work_duration_s + rest_duration_s)
                random_intervals[f"work_{round}_start"] = warm_up_s + round * (work_duration_s + rest_duration_s) + rest_duration_s

                # add pings for each period
                if rest:
                    # check if rest period is non-zero
                    times.append(random_intervals[f"rest_{round}_start"])
                    pings.append(REST)
                times.append(random_intervals[f"work_{round}_start"])
                pings.append(WORK)

                # generate random intervals within work period
                intervals = generate_random_intervals(work_duration_s, n_intervals, min_interval_gap_s)
                random_intervals[f"work_{round}_intervals"] = [(random_intervals[f"work_{round}_start"] + interval) for interval in intervals]
                times.extend(random_intervals[f"work_{round}_intervals"])
                pings.extend([PING] * n_intervals)
            else:
                # calculate timing for rest and work round with work first
                random_intervals[f"work_{round}_start"] = warm_up_s + round * (work_duration_s + rest_duration_s)
                random_intervals[f"rest_{round}_start"] = warm_up_s + round * (work_duration_s + rest_duration_s) + work_duration_s

                # check if work period is non-zero
                times.append(random_intervals[f"work_{round}_start"])
                pings.append(WORK)

                # generate random intervals within work period
                intervals = generate_random_intervals(work_duration_s, n_intervals, min_interval_gap_s)
                random_intervals[f"work_{round}_intervals"] = [(random_intervals[f"work_{round}_start"] + interval) for interval in intervals]
                times.extend(random_intervals[f"work_{round}_intervals"])
                pings.extend([PING] * n_intervals)                

                if rest:
                    times.append(random_intervals[f"rest_{round}_start"])
                    pings.append(REST)
        
    random_intervals["session_end"] = random_intervals["session_start"] + n_rounds * (work_duration_s + rest_duration_s)
    random_intervals["cool_down_end"] = random_intervals["session_end"] + cooldown

    times.append(random_intervals["session_end"])
    pings.append(EXTRA)

    if cooldown:
        times.append(random_intervals["cool_down_end"])
        pings.append(EXTRA)

    return times, pings

def generate_random_intervals(work_duration_s, n_intervals, min_interval_gap_s):
        """function to generate random intervals within a work period given constraints."""
        # fixed and random component
        fixed_comp = n_intervals * min_interval_gap_s
        random_comp = work_duration_s - (fixed_comp)

        # generate random portions
        wait_times = np.array([random.uniform(0,1) for i in range(n_intervals)])
        wait_times = wait_times * random_comp / sum(wait_times)

        # use wait times to get intervals
        random_intervals = [round(sum(wait_times[:i+1]) + (min_interval_gap_s*i), 3) for i in range(n_intervals)]

        return random_intervals

if __name__ == "__main__":
    n_rounds = 1
    work_duration_s = 180
    rest_duration_s = 30
    n_intervals = 26
    min_interval_gap_s = 3
    warm_up_s = 30
    cooldown_s = 450
    str_interval = [" "] * 180

    # generate a single set of random intervals for visualization
    intervals = generate_random_intervals(work_duration_s, n_intervals, min_interval_gap_s)
    for i, t in enumerate(intervals):
        # print(f"Step {i}: {t}")
        idx = round(t / work_duration_s * len(str_interval))
        str_interval[idx] = "*"

    print("\n\n\n")
    print("|", "".join(str_interval), "|")
    print("\n\n\n")

    times, pings = generate_ping_times(
         work_duration_s=work_duration_s, 
         rest_duration_s=rest_duration_s, 
         n_intervals=n_intervals,
         n_rounds=n_rounds, 
         min_interval_gap_s=min_interval_gap_s, 
         warm_up_s=warm_up_s, 
         cooldown_s=cooldown_s)
    print("Generated Ping Times (s):")
    for t, p in zip(times, pings):
        print(f"{t:>7.2f}s - Type: {p}")

