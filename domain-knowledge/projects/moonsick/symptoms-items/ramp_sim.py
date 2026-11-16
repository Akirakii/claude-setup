import random, statistics as st, sys
sys.path.insert(0, ".")
import burst_sim as b
H = {"speed":8.64,"react":0.0}; B17 = {"speed":7.0,"react":17.5}; B6 = {"speed":7.0,"react":6.0}
def lerp(a, c, f): return a + (c - a) * f
crews = [("1 human", [H], False), ("2: 1 runs, 1 holds", [H], True), ("2 run", [H]*2, False),
         ("3: 2 run, 1 holds", [H]*2, True), ("3 run", [H]*3, False), ("6: 4 run, 1 holds", [H]*4, True),
         ("human + bots(17 s), bot holds", [H]+[B17]*3, True), ("human + bots(6 s), bot holds", [H]+[B6]*3, True),
         ("human sick, bots(6 s), bot holds", [B6]*3, True)]
print("night  S   R      " + " | ".join(c[0] for c in crews))
for f in [0.5, 0.65, 0.8, 1.0]:
    S = lerp(30, 8, f); R = 1 / lerp(120, 40, f)
    row = []
    for name, helpers, held in crews:
        rng = random.Random(11)
        n = 250
        r = [b.run(rng, helpers, gaps=(0, S, 2 * S), R=R, held=held) for _ in range(n)]
        row.append(f"{sum(x[0] for x in r) / n * 100:4.0f}%")
    print(f"{f:4.2f} {S:4.1f} 1/{1/R:3.0f}  " + " | ".join(row))
