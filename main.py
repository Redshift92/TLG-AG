import transformedlazygreedy as tlg
import augmentedgreedy as ag

links = set(range(0,10))

sensors_c = (
    {0,1,2,3,4}, # C0 (set of link faults detactable by sensor 0)
    {0,1,2,5,7},
    {0,1,3,4,5,6,8},
    {1,2,3,4,5,6,7,8,9},
    {0,2,3,5,6,7,9},
    {1,3,4,6,8,9},
    {3,4,5,6,7,8,9},
    {2,5,6,7,8,9}
)

print(tlg.tlg(sensors_c, links))
print(ag.ag(sensors_c, links))
