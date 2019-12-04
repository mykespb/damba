#!/usr/bin/env python

# tools for runner of damba web
# tools.py 
# ver. 1.0. run 2019-11-21
# Mikhail Kolodin

# --------------- bazed ULID

def bazed_ulid(n):
    """ recode number in ULID format """

    baza = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    bl = len(baza)
    res = ''
    if n == 0:
        return '0'
    while n:
        r = n % bl
        n //= bl
        res = baza[r] + res

    return res

# the end.
# =======================================================
