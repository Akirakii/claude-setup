"""B: burst case. Symptoms of one case show close together; helpers carry up to 2 items (two hands).
Best assignment of the 3 items to helpers (brute force), each helper's best route order."""
import random, itertools, statistics as st, sys
sys.path.insert(0, ".")
import functools
from symptoms_sim import path as _path, rand_pos as _rp, SPOTS, GROUPS, SEEN
path = functools.lru_cache(maxsize=None)(_path)
def rand_pos(rng):
    x, z = _rp(rng); return (round(x), round(z))

def helper_finish(rng, h, hp, pp, items, starts):
    # trips of <= 2 items (two hands); a trip starts once its items are noticed
    best = None
    for perm in itertools.permutations(items):
        trips = [list(perm[:2]), list(perm[2:])] if len(perm) > 2 else [list(perm)]
        t = 0.0; pos = hp; fins = {}
        for trip in trips:
            if not trip: continue
            t = max(t, max(starts[g] for g,_ in trip) + h["react"])
            for g,s in trip: t += path(pos, s)/h["speed"] + 0.3; pos = s
            t += path(pos, pp)/h["speed"]; pos = pp
            for g,_ in trip: t += 2.0; fins[g] = t
        if best is None or max(fins.values()) < max(best.values()): best = fins
    return best

def run(rng, helpers, gaps=(0,5,10), R=1/40, held=False, patient_fetches=False):
    order = rng.sample(["eyes","body","feel"],3)
    sym = {g: rng.choice(GROUPS[g]) for g in order}
    show = {g: gaps[i] for i,g in enumerate(order)}
    notice = {g: show[g] + (rng.uniform(1,6) if g in SEEN else 3.0) for g in order}
    pp = rand_pos(rng); hps = [rand_pos(rng) for _ in helpers]
    best = None
    for assign in itertools.product(range(len(helpers)), repeat=3):
        fins = {}
        for i in set(assign):
            its = [(g, SPOTS[sym[g]][1]) for k,g in enumerate(order) if assign[k]==i]
            fins.update(helper_finish(rng, helpers[i], hps[i], pp, its, notice))
        if best is None or max(fins.values()) < max(best.values()): best = fins
    done = best
    ev = sorted(set([0.0]+list(show.values())+list(done.values())))
    rate = R*(HOLD if held else 1)
    c = 0.0
    for a,b in zip(ev, ev[1:]+[1e9]):
        u = sum(1 for g in order if show[g]<=a<done[g])
        if u==0:
            if all(done[g]<=a for g in order): return False, c, a
            continue
        need = (1-c)/(rate*u)
        if a+need<=b: return True, 1, a+need
        c += rate*u*(b-a)
    return False, c, 0

HOLD = 0.75
H = {"speed":8.64,"react":0.0}; B = {"speed":7.0,"react":17.5}
def trial(name, helpers, n=400, **kw):
    rng = random.Random(3)
    r = [run(rng, helpers, **kw) for _ in range(n)]
    t = sum(x[0] for x in r)/n
    ok = [x for x in r if not x[0]]
    print(f"  {name:36s} turn {t*100:5.1f}%  curse left {st.mean(x[1] for x in ok) if ok else 0:.2f}  cured {st.mean(x[2] for x in ok) if ok else 0:4.1f}s")
for gaps,R in [] and [((0,5,10),1/40),((0,5,10),1/30),((0,8,16),1/36),((0,4,8),1/25)]:
    c = R*(gaps[1]-gaps[0]) + 2*R*(gaps[2]-gaps[1]); tt = gaps[2] + (1-c)/(3*R)
    print(f"== shows at {gaps}, R=1/{1/R:.0f}  nothing done -> turns at {tt:.0f}s; one symptom alone -> {1/R:.0f}s")
    trial("1 human (solo, 2 hands)", [H], gaps=gaps, R=R)
    trial("1 human, patient held by a 2nd", [H], gaps=gaps, R=R, held=True)
    trial("2 humans", [H]*2, gaps=gaps, R=R)
    trial("3 humans", [H]*3, gaps=gaps, R=R)
    trial("human + 3 slow bots", [H]+[B]*3, gaps=gaps, R=R)
    trial("4 slow bots (human sick)", [B]*4, gaps=gaps, R=R)
