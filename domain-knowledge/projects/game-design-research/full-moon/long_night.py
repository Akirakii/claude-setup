# Rough: one long night, deaths are final (caught or starved). Pressure rises through the night. Not play.
import random, statistics as st
def night(crew, cure_p, T, catch_p=0.5):
    living=crew; deaths=0; first=None; t=random.uniform(20,90); free_at=0
    while t<T and living>=2:
        k=t/T; L=75-15*k; f=1.3-0.7*k; dbl=0.10+0.20*k
        cases=[t]+([t+random.uniform(10,30)] if random.random()<dbl and living>=3 else [])
        ends=[]
        for s in cases:
            if s>=T or living<2: continue
            if random.random()<cure_p: ends.append(s+random.uniform(10,35)); continue
            turn=max(s+L,free_at)
            if turn>=T: ends.append(T); continue
            hunger=20+60/max(living-1,1)
            hunt_end=turn+(random.uniform(5,hunger) if random.random()<catch_p else hunger)
            deaths+=1; living-=1; first=first or turn; free_at=hunt_end; ends.append(turn)
        t=(max(ends) if ends else t)+180/max(living,1)*f*random.uniform(0.25,1.75)
    return deaths, first
for T in (720,900):
    for cp,lab in ((0.85,'good crew'),(0.65,'new crew')):
        r=[night(4,cp,T) for _ in range(4000)]; d=[x for x,_ in r]; fs=[f for _,f in r if f]
        print(f"{T//60} min night, 4 players, {lab}: deaths avg {st.mean(d):.1f}, half or more dead {sum(x>=2 for x in d)/40:.0f}%, "
              f"first death at ~{st.median(fs)/60:.1f} min (median)")
