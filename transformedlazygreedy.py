
def eval_utility(c_i, full_cov, curr_cov):
    return len(c_i.intersection(full_cov.difference(curr_cov)))

def lazy_greedy_msc(cs, events):
    utilities = [None]*len(cs)
    cover_sets = []
    current_coverage = set()
    for i, sensor_c in enumerate(cs):
        utilities[i] = [i, eval_utility(sensor_c, events, current_coverage)]
    utilities.sort(key=lambda util: -util[1])

    while True:
        added_sets = len(cover_sets)

        if added_sets == len(utilities) or utilities[added_sets][1] == 0:
            # nothing more to add
            break

        cover_sets.append((cs[utilities[added_sets][0]], utilities[added_sets][0]))
        current_coverage.update(cs[utilities[added_sets][0]])
        utilities[added_sets][1] = -1

        if current_coverage == events:
            break;

        to_add_j = -1
        for j, i_utility in enumerate(utilities):
            if i_utility[1] == -1:
                continue
            to_add_j = j
            i_utility[1] = eval_utility(cs[i_utility[0]], events, current_coverage)
            if j+1 < len(utilities):
                # lazy: if current utility for sensors j is greater than last
                # utility of sensor j+1 (always decreasing), break
                if i_utility[1] > utilities[j+1][1]:
                    break
        if to_add_j != len(cover_sets):
            # sort again if disequalities chain is not respected
            utilities[len(cover_sets):to_add_j+1] = sorted(utilities[len(cover_sets):to_add_j+1], key=lambda util: -util[1])

    return cover_sets

def only_one(pair, c_i):
    return len(c_i.intersection(pair)) == 1

def mtc_to_msc(cs, events):
    cs_t = []
    for _ in range(len(cs)):
        cs_t.append(set())
    n = -1
    for i in range(len(events)):
        for j in range(i+1,len(events)):
            n += 1
            for sensor_i, c_i in enumerate(cs):
                if only_one({i, j}, c_i):
                    cs_t[sensor_i].add(n)
    events_t = set(range(n+1))
    return cs_t, events_t

def tlg(cs, events):
    return lazy_greedy_msc(*mtc_to_msc(cs, events))
