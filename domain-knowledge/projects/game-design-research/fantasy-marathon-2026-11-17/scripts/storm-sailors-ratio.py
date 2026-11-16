import random, statistics as st
DT=0.05; RIP=2.0
def season(n,k,T0,h,plan,f,seed,storm=180,K=3.0):
    # rope i's boom sweeps the rope spots of the next k sailors. Sail slips T0*f**rips s after each trim (+-30%).
    # haul = stand at the rope h s. flap > 2 s = a rip, then one more per further 2 s. 5 rips = sail off (stops).
    # 'turns': crouch by default, stand only to haul, and start only when no friend I cross is standing.
    # 'through': same, but when my sail is about to rip I haul through a standing friend (knocked K s, haul lost).
    r=random.Random(seed); rips=[0]*n; per=[]; hits=0; first_off=None
    arc=[[(i+j)%n for j in range(1,k+1)] for i in range(n)]
    for s in range(5):
        nxt=[r.uniform(0,T0) for _ in range(n)]; flap=[None]*n; lastrip=[0]*n
        haul_end=[None]*n; down=[0.0]*n; rs=0; t=0.0
        while t<storm:
            for i in r.sample(range(n),n):
                if rips[i]>=5: continue
                if flap[i] is None:
                    if t>=nxt[i]: flap[i]=t; lastrip[i]=0
                    else: continue
                nr=int((t-flap[i])/RIP)
                if nr>lastrip[i]:
                    lastrip[i]=nr; rips[i]+=1; rs+=1
                    if rips[i]>=5:
                        haul_end[i]=None
                        if first_off is None: first_off=s+1
                        continue
                if t<down[i]: continue
                if haul_end[i] is not None:
                    if t>=haul_end[i]:
                        haul_end[i]=None; flap[i]=None; nxt[i]=t+T0*(f**rips[i])*r.uniform(0.7,1.3)
                    continue
                conf=[j for j in range(n) if j!=i and haul_end[j] is not None and (j in arc[i] or i in arc[j])]
                if conf:
                    if plan=='through' and (t-flap[i])%RIP > RIP-h-0.1:
                        for j in conf:
                            if j in arc[i]: haul_end[j]=None; down[j]=t+K; hits+=1
                        if any(i in arc[j] and j not in arc[i] for j in conf): continue
                    else: continue
                haul_end[i]=t+h
            t+=DT
        per.append(rs)
    return per,hits,first_off,sum(1 for x in rips if x>=5)
def run(*a):
    R=[season(*a,seed=sd) for sd in range(8)]
    per=[round(st.mean(x[0][s] for x in R),1) for s in range(5)]
    lost=sum(1 for x in R if x[3]>0)
    offs=[x[2] for x in R if x[2]]
    return per, round(st.mean(x[1] for x in R)), f"{lost}/8 seasons lose a sail"+(f", first in storm {min(offs)}" if offs else "")
print("columns: rips in storms 1..5 | boom hits per season | seasons out of 8 where a sail is torn off")
for f in (0.7,0.85):
  print(f"--- a ripped sail slips {int((1-f)*100)}% sooner per rip ---")
  for n,k in[(3,2),(6,2),(6,5)]:
    deg=min(2*k,n-1)
    for T0 in(6,4,3):
        for h in(0.3,0.6,1.0):
            row=f"n={n} cross={deg} slip={T0}s haul={h}s  need (cross+1)*haul={(deg+1)*h:.1f}s<2s; busy={(deg+1)*h/T0:.2f}"
            for plan in('turns','through'):
                per,hits,l=run(n,k,T0,h,plan,f)
                row+=f" | {plan}: {per} hits={hits} {l}"
            print(row)
