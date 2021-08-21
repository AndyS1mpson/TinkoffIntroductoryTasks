"""Tablecloth shop task."""
from typing import Tuple

def does_cover(tc: Tuple) -> bool:
    """Check if the tablecloth will cover the table or not.

    Args:
        tb (Tuple): table.
        tc (Tuple): tablecloth.

    Returns:
        bool: will it cover or not.
    """
    tb = (w, h)
    if (tc[0] >= tb[0] and tc[1] >= tb[1]) or \
        (tc[0] >= tb[1] and tc[1] >= tb[0]):
        return True
    return False


n = int(input())                    # tablecloth number
w, h = map(int, input().split())    # wieght and height of table
tableclothes = []

# height, width and cost of tableclothes available in the store
for i in range(n):
    wi, hi, ci = map(int, input().split())
    tableclothes.append((wi, hi, ci))


matching_tableclothes = list(filter(does_cover, tableclothes))

opt_t = min(matching_tableclothes, key=lambda tc: tc[2])
print(opt_t[2])