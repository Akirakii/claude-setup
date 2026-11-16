"""Toy model for idea 9 (hide from friends the moon has turned).
Not a game simulation: no walking, no chases, no sound, no cure. It only asks whether
"does any human last until dawn" swings with the numbers or sits at 0% / 100%.

N friends, S hiding spots, a night of T seconds. One friend turns at a random time in the first 120 s.
Each wolf checks one spot every c seconds, never rechecking a spot it has already checked itself.
A human found is turned at once and starts checking. Humans never move (the worst case for them),
or re-hide every `move` seconds to a random free spot (move>0).
"""
import random, itertools, statistics

def night(N, S, T, c, move, rng):
    humans = {i: s for i, s in enumerate(rng.sample(range(S), N))}
    first = rng.randrange(N)
    t0 = rng.uniform(20, 120)
    del humans[first]
    wolves = [{'next': t0 + c, 'seen': set()}]
    t = t0
    turned_at = {first: t0}
    events = []
    next_move = t0 + move if move > 0 else float('inf')
    while humans:
        w = min(wolves, key=lambda x: x['next'])
        t = min(w['next'], next_move)
        if t >= T:
            break
        if t == next_move:
            taken = set(humans.values())
            for h in list(humans):
                free = [s for s in range(S) if s not in taken]
                if free:
                    taken.discard(humans[h]); humans[h] = rng.choice(free); taken.add(humans[h])
            for x in wolves:
                x['seen'].clear()
            next_move += move
            continue
        choices = [s for s in range(S) if s not in w['seen']] or list(range(S))
        s = rng.choice(choices)
        w['seen'].add(s)
        w['next'] = t + c
        for h, hs in list(humans.items()):
            if hs == s:
                del humans[h]
                turned_at[h] = t
                wolves.append({'next': t + c, 'seen': set()})
    survived = len(humans)
    last = max(turned_at.values()) if not humans else T
    return survived, last

def run(N, S, T, c, move, n=4000, seed=1):
    rng = random.Random(seed)
    res = [night(N, S, T, c, move, rng) for _ in range(n)]
    p_any = sum(1 for s, _ in res if s > 0) / n
    mean_left = statistics.mean(s for s, _ in res)
    return p_any, mean_left

if __name__ == '__main__':
    T = 300
    print('N  S   c  move | humans win  mean humans left at dawn')
    rows = []
    for N, S, c, move in itertools.product((3, 4, 6), (12, 24, 40), (4, 8, 12), (0, 45)):
        p, m = run(N, S, T, c, move)
        rows.append((N, S, c, move, p, m))
        print(f'{N}  {S:<3} {c:<2} {move:<4} | {p:6.0%}      {m:.2f}')
    free = sum(1 for r in rows if r[4] >= 0.95)
    lost = sum(1 for r in rows if r[4] <= 0.05)
    mid = len(rows) - free - lost
    print(f'\n{len(rows)} settings: humans nearly always win in {free}, nearly never in {lost}, in between in {mid}')
    band = [r for r in rows if 0.25 <= r[4] <= 0.75]
    print(f'settings where humans win between 25% and 75% of nights: {len(band)}')
    for r in band:
        print('  ', r[:4], f'{r[4]:.0%}')
