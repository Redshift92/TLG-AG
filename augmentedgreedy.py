# Copyright 2017 Lorenzo Rizzello
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.

def alpha(Y, beta_X):
    res = set()
    for a in beta_X:
        if len(Y.intersection(a)) == 1:
            res.add(frozenset(a))
    return res

def all_pair_subsets(X):
    processed, res = set(), set()
    for x in X:
        processed.add(x)
        for y in X.difference(processed):
            res.add(frozenset([x,y]))
    return res


def ag(cs, events):
    cover_sets = []
    current_coverage = set()
    G = [None] * len(cs)
    G[0] = set()
    j = 1
    max_utility = 1
    while max_utility > 0:
        not_inc_n = len(events) - len(current_coverage)
        max_utility, max_utility_i, max_structs = -1, -1, {}
        for sensor_i, c_i in enumerate(cs):
            Xi = c_i.difference(current_coverage) # detectable by sensor i, not already covered
            kij = len(Xi)
            xi = kij*(not_inc_n - kij)
            Yi = c_i.intersection(current_coverage) # detectable by sensor i, already covered
            yi = sum([ len(alpha(Yi, G[t])) for t in range(j) ])
            utility = xi + yi
            if utility > max_utility:
                max_utility, max_utility_i = utility, sensor_i
                max_structs = { 'c': c_i, 'X': Xi, 'Y': Yi }
        if max_utility > 0:
            cover_sets.append((max_structs['c'], max_utility_i))
            current_coverage.update(max_structs['c'])
            G[j] = all_pair_subsets(max_structs['X'])
            for t in range(j):
                G[t] = G[t].difference(alpha(max_structs['Y'], G[t]))
            j += 1
    return cover_sets
