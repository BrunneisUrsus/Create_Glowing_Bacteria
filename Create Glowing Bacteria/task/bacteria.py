def opposite(original):
    key = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return "".join(key[i] for i in original)


def cut(dna, restriction_1, restriction_2, comp=False):
    if comp is True:
        restriction_1 = restriction_1[::-1]
        # restriction_2 = restriction_2[::-1]
        limit_start = dna.find(restriction_1) + 5
        # limit_end = dna.rfind(restriction_2) + 5
        dna_cut = dna[limit_start:]
    else:
        limit_start = dna.find(restriction_1) + 1
        limit_end = dna.rfind(restriction_2) + 1
        dna_cut = dna[limit_start:limit_end]
    return dna_cut


def split_dna(dna, restriction, comp=False):
    limit = dna.find(restriction) + 1
    if comp:
        restriction = restriction[::-1]
        limit = dna.find(restriction) + 5
    if restriction in dna:
        dna_start = dna[:limit]
        dna_end = dna[limit:]
        return [dna_start, dna_end]
# bacteria = input()
# restriction_sites = input().split()
# a = cut(bacteria, restriction_sites[0], restriction_sites[1])
# opp_bacteria = opposite(bacteria)
# b = cut(opp_bacteria, restriction_sites[0], restriction_sites[1], comp=True)
# print(a)
# print(b[:len(a)])


name = input()
with open(f"{name}", "r") as text:
    result = text.read().split()
a = result[0]
b = result[1]
split_1 = split_dna(a, b)
bacteria = result[2]
restriction_a = result[3]
restriction_b = result[4]
c = cut(bacteria, restriction_a, restriction_b)
new_bacteria = [split_1[0], c, split_1[1]]
opp_new = opposite("".join(new_bacteria))
print("".join(new_bacteria))
print(opp_new)
