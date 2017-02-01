import sys
sys.path.append('..')
import transformedlazygreedy as tlg
import test

test.add(tlg.only_one, ({1,2}, {1,2,3}), False)
test.add(tlg.only_one, ({1,2},{1,3}), True)

test.add(tlg.eval_utility, ({1,2}, {1,2,3,4}, {4}), 2)

cs = (
    {1,2,3},
    {4,5},
    {1,2,3,4}
)
events = {1,2,3,4,5}
test.add(tlg.lazy_greedy_msc, (cs, events), [({1,2,3,4}, 2), ({4,5}, 1)])

cs = (
    {1,2},
    {4,5},
    {5}
)
events = {1,2,3,4,5}
test.add(tlg.lazy_greedy_msc, (cs, events), [({1,2}, 0), ({4,5}, 1)])

cs = (
    {1,2},
    {4,5}
)
events = {1,2,3,4,5}
test.add(tlg.lazy_greedy_msc, (cs, events), [({1,2}, 0), ({4,5}, 1)])

cs = (
    {0,1},
    {2},
)
events = {0,1,2}
res = (
    [
        {1,2},
        {1,2}
    ],
    {0,1,2}
)
test.add(tlg.mtc_to_msc, (cs, events), res)

test.run()
