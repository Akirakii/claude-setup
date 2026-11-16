# Rough estimate: catches per night, hunts pausing the case clock (A) vs not (B). Many assumptions; not play.
import random, statistics as st
def night(n, crew, cure_p, mode, catch_p=0.5, T=360):
    L = 75 - 4*(n-1); f = 1.3 - 0.175*(n-1); dbl = 0.10 + 0.05*(n-1)
    living = crew; out = 0; catches = 0; t = random.uniform(20, 90)
    creature_free_at = 0  # when the current creature resolves
    while t < T and living >= 1:
        cases = [t] + ([t + random.uniform(10, 30)] if random.random() < dbl and living >= 3 else [])
        end_times = []
        for start in cases:
            if start >= T or living < 1: continue
            if random.random() < cure_p:
                end_times.append(start + random.uniform(10, 35)); continue
            turn = max(start + L, creature_free_at)          # U8: waits for the current creature
            if turn >= T: end_times.append(T); continue
            prey = living - 1
            hunger = 20 + 60 / max(prey, 1)
            if prey >= 1 and random.random() < catch_p:
                hunt_end = turn + random.uniform(5, hunger); catches += 1; living -= 1   # victim dead till dawn
            else:
                hunt_end = turn + hunger; living -= 1; out += 1                          # creature starves, out till dawn
            creature_free_at = hunt_end
            end_times.append(turn if mode == 'B' else hunt_end)
        last = max(end_times) if end_times else t
        gap = 180 / max(living, 1) * f * random.uniform(0.25, 1.75)
        t = last + gap
    return catches
for mode in 'AB':
    for cure_p, label in ((0.85, 'good crew'), (0.65, 'new crew')):
        row = []
        for n in (1, 3, 5):
            xs = [night(n, 4, cure_p, mode) for _ in range(4000)]
            row.append(f"night {n}: {st.mean(xs):.2f} avg, {sum(x>=2 for x in xs)/len(xs)*100:.0f}% nights with 2+")
        print(mode, label, ' | '.join(row))
