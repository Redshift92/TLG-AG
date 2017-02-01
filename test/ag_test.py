import sys
sys.path.append('..')
import augmentedgreedy as ag
import test

test.add(ag.all_pair_subsets, ({1,2,3},), {frozenset([1,2]), frozenset([1,3]), frozenset([2,3])})

test.add(ag.alpha, ({1,3}, ag.all_pair_subsets({1,2,3})), {frozenset([1,2]), frozenset([2,3])})

test.run()
