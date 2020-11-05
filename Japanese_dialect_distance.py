from functools import lru_cache
from __future__ import unicode_literals

# Use the decorator to find the Levenstein distance between the Japanese dialect and the standard language.

@lru_cache(maxsize=4096)
def ld(s, t):
    if not s: return len(t)
    if not t: return len(s)
    if s[0] == t[0]: return ld(s[1:], t[1:])
    l1 = ld(s, t[1:])
    l2 = ld(s[1:], t)
    l3 = ld(s[1:], t[1:])
    return 1 + min(l1, l2, l3)


# ギャル語
print(ld('チョベリグ、チョベリバ', '超very good　超 very bad')) #result = 21
# 流行語
print(ld('タピる', 'タピオカを食べる')) #result = 5
# 琉球語
print(ld('はじめまして', 'はじみてぃやーさい')) #result = 7
print(ld('ありがとう',	'にふぇーでーびる')) #result = 8
