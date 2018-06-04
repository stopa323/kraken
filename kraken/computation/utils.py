import itertools
from math import log


def log_weight(edges):
    """Transform edge data to allow finding negative cycles.

    :param list edges: List of edge tuples (start_node, end_node, weight).
    """
    return map(lambda t: (t[0], t[1], -log(t[2], 2)), edges)


def cycle_profit(cycle, edges):
    """Calculate profit of the cycle.

    :param list cycle: List of node names.
    :param list edges: List of edge tuples (start_node, end_node, weight).

    :returns Numeric value representing profit of the cycle.
    """
    # copy first element at the end
    cycle.append(cycle[0])

    # generate trading pairs e.g. [1,2,3,4] -> [(1,2), (2,3), (3,4)]
    s1, s2 = itertools.tee(cycle)
    s2.next()
    trading_pairs = itertools.izip(s1, s2)

    ex_rates = map(lambda tp: edge_weight(tp[0], tp[1], edges), trading_pairs)
    profit = reduce((lambda v1, v2: v1 * v2), ex_rates)

    return profit


def cycle_filter(cycles, edges, max_cycle=None, min_cycle=None, min_profit=1.0):
    """Compute profit for all cyclec and perform optional filtering.

    :param list cycle: List of node names.
    :param list edges: List of edge tuples (start_node, end_node).
    :param int max_cycle: Maximum acceptable length of the cycle
    :param int min_cycle: Minimum acceptable length of the cycle
    :param int min_profit: Minimum acceptable profit of the cycle

    :returns list of tuples (cycle, profit)
    """
    _cycles = cycles
    if type(max_cycle) is int and max_cycle > 0:
        _cycles = filter(lambda c: len(c) <= max_cycle, _cycles)

    if type(min_cycle) is int and min_cycle > 0:
        _cycles = filter(lambda c: len(c) >= min_cycle, _cycles)

    result = list()
    for c in _cycles:
        raw_profit = cycle_profit(c, edges)
        if raw_profit >= min_profit:
            result.append((c, raw_profit))

    return result


def edge_weight(start_node, end_node, edges):
    """Get edge weight.

    :param string start_node: Edge beginning node
    :param string start_node: Edge trailing node
    :param list edges: List of edge tuples (start_node, end_node, weight).

    :returns Numeric value of edge weight, 0 if no such edge found.
    """
    match = filter(lambda e: e[0] == start_node and e[1] == end_node, edges)

    if len(match) != 1:
        print('Edge (%s, %s) not found or duplicated.' % (start_node, end_node))
        return 0

    return match[0][2]
