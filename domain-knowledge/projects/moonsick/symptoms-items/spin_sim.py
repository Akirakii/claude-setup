"""C: symptoms land on anyone. Per-person spawn every I0 s on average (random group not already showing).
Everyone helps, nobody treats themselves. c_i rises R per untreated symptom; at 1 the friend turns (counted, reset)."""
import random, statistics as st, sys, functools
sys.path.insert(0, ".")
from symptoms_sim import path, rand_pos, SPOTS, GROUPS, SEEN

@functools.lru_cache(maxsize=None)
def P(a, b): return path(a, b)
def rp(rng): x, z = rand_pos(rng); return (round(x), round(z))

def night(rng, kinds, I0=40.0, R=1/60, T=600.0, dt=0.5):
    n = len(kinds)
    pos = [rp(rng) for _ in range(n)]
    c = [0.0]*n
    sym = [dict() for _ in range(n)]          # group -> [item, shown_t, noticed_t, assigned helper or None]
    busy = [0.0]*n                            # helper free at
    task = [None]*n
    turns = 0; t = 0.0; cooldown = [0.0]*n
    while t < T:
        for i in range(n):                    # spawn
            if t >= cooldown[i] and rng.random() < dt / I0:
                free = [g for g in GROUPS if g not in sym[i]]
                if free:
                    g = rng.choice(free); it = rng.choice(GROUPS[g])
                    note = t + (rng.uniform(1, 6) if g in SEEN else 3.0)
                    sym[i][g] = [it, t, note, None]
        for i in range(n):                    # assign noticed, unassigned tasks
            for g, s in sym[i].items():
                if s[3] is None and t >= s[2]:
                    best = None
                    for j in range(n):
                        if j == i: continue
                        k = kinds[j]
                        start = max(t + k["react"], busy[j])
                        eta = start + (P(pos[j], SPOTS[s[0]][1]) + P(SPOTS[s[0]][1], pos[i])) / k["speed"] + 0.3 + 2.0 + 1.5
                        if best is None or eta < best[0]: best = (eta, j)
                    eta, j = best; busy[j] = eta; s[3] = (j, eta)
        for i in range(n):                    # finish treatments, curse
            for g in list(sym[i]):
                s = sym[i][g]
                if s[3] and t >= s[3][1]:
                    pos[s[3][0]] = pos[i]; del sym[i][g]
            c[i] = max(0.0, c[i] + (R * len(sym[i]) if sym[i] else -R) * dt)
            if c[i] >= 1.0:
                turns += 1; c[i] = 0.0; sym[i].clear(); cooldown[i] = t + 60
                for j in range(n): cooldown[j] = max(cooldown[j], t + 30)   # the hunt pauses spawns
        t += dt
    return turns

H = {"speed":8.64, "react":0.0}; B = {"speed":7.0, "react":17.5}
def trial(name, kinds, n=60, **kw):
    rng = random.Random(5)
    r = [night(rng, kinds, **kw) for _ in range(n)]
    print(f"  {name:28s} turns per 10 min {st.mean(r):4.2f}  (nights with 0 turns {sum(x==0 for x in r)/n*100:3.0f}%)")
for I0, R in [(40, 1/60), (25, 1/60), (20, 1/45), (15, 1/45)]:
    print(f"== a symptom per person every ~{I0}s, one untreated symptom turns you in {1/R:.0f}s")
    trial("4 humans", [H]*4, I0=I0, R=R)
    trial("6 humans", [H]*6, I0=I0, R=R)
    trial("8 humans", [H]*8, I0=I0, R=R)
    trial("1 human + 5 slow bots", [H]+[B]*5, I0=I0, R=R)
