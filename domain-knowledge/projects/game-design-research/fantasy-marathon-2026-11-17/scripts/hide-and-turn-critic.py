"""Critic's variant of hide-and-turn-ratio.py. Same toy (no walking, no sound), with switches:
 move      : hiders re-hide every `move` s (0 = never)
 q         : chance a moving hider is seen and turned while crossing (the written risk; original = 0)
 shared    : wolves share one 'seen' set and a new wolf inherits it (friends on voice splitting rooms)
 know_reset: original clears every wolf's memory at the instant hiders move (wolves 'know' they moved)
 tell      : chance a just-turned friend knows where each other human is hiding (they hid together / talked)
Also records per-player human time and when things happen."""
import random, statistics, itertools, sys

def night(N,S,T,c,move,rng,q=0.0,shared=False,know_reset=True,tell=0.0):
    humans={i:s for i,s in enumerate(rng.sample(range(S),N))}
    first=rng.randrange(N); t0=rng.uniform(20,120); del humans[first]
    common=set()
    wolves=[{'next':t0+c,'seen':common if shared else set(),'todo':[]}]
    turned={first:t0}
    nm=t0+move if move>0 else float('inf')
    def turn(h,t):
        hs=humans.pop(h); turned[h]=t
        w={'next':t+c,'seen':common if shared else set(),'todo':[]}
        for o,os_ in humans.items():
            if rng.random()<tell: w['todo'].append(o)
        wolves.append(w)
    while humans:
        w=min(wolves,key=lambda x:x['next']); t=min(w['next'],nm)
        if t>=T: break
        if t==nm:
            taken=set(humans.values())
            for h in list(humans):
                if rng.random()<q: turn(h,t); continue
                free=[s for s in range(S) if s not in taken]
                taken.discard(humans[h]); humans[h]=rng.choice(free); taken.add(humans[h])
            if know_reset:
                common.clear()
                for x in wolves: x['seen'].clear()
            nm+=move; continue
        s=None
        while w['todo']:
            o=w['todo'].pop()
            if o in humans: s=humans[o]; break
        if s is None:
            ch=[x for x in range(S) if x not in w['seen']] or list(range(S))
            s=rng.choice(ch)
        w['seen'].add(s); w['next']=t+c
        for h,hs in list(humans.items()):
            if hs==s: turn(h,t)
    end = T if humans else max(turned.values())
    return len(humans), turned, end, t0

def stats(N,S,c,move,n=4000,seed=1,T=300,**kw):
    rng=random.Random(seed); win=0; ends=[]; firstcatch=[]; hunter_alone=[]; lasthuman_alone=[]; early=0
    for _ in range(n):
        left,turned,end,t0=night(N,S,T,c,move,rng,**kw)
        win+= left>0; ends.append(end)
        ts=sorted(turned.values())
        fc = ts[1] if len(ts)>1 else T
        firstcatch.append(fc-t0)            # seconds the first hunter hunts alone
        if left==0: early+=1
        # time the last human (or last one caught) spends as the only human
        if len(ts)>=N-1:
            lasthuman_alone.append(end-ts[N-2])
    return dict(win=win/n, end=statistics.mean(ends), alone_hunter=statistics.mean(firstcatch),
                nocatch=sum(1 for x in firstcatch if x>=T-120)/n,
                last_alone=statistics.mean(lasthuman_alone) if lasthuman_alone else 0, allcaught=early/n)

if __name__=='__main__':
    print('A. baseline, the band settings: how a night goes')
    for N,S,c,m in [(3,24,12,45),(3,40,8,45),(4,24,12,45),(4,40,8,45),(6,24,12,45),(6,40,8,45)]:
        r=stats(N,S,c,m); print(f' N{N} S{S} c{c} m{m}: win {r["win"]:.0%} night ends {r["end"]:.0f}s; first hunter alone {r["alone_hunter"]:.0f}s; last human alone {r["last_alone"]:.0f}s; all caught {r["allcaught"]:.0%}')
    print('B. how often to move (free in the original)')
    for N,S,c in [(4,24,12),(4,40,8),(6,40,8)]:
        print(f' N{N} S{S} c{c}:', '  '.join(f'move {m}: {stats(N,S,c,m)["win"]:.0%}' for m in (0,90,45,20,10,5)))
    print('C. moving with a chance q of being seen (the written risk)')
    for N,S,c in [(4,24,12),(4,40,8),(6,40,8)]:
        print(f' N{N} S{S} c{c}: stay {stats(N,S,c,0)["win"]:.0%} |', '  '.join(f'q{q}: {stats(N,S,c,45,q=q)["win"]:.0%}' for q in (0,0.05,0.1,0.2,0.3)))
    print('D. wolves share what they searched (voice) ')
    for N,S,c,m in [(3,24,12,45),(4,24,12,45),(4,40,8,45),(6,24,12,45),(6,40,8,45),(4,40,8,0),(6,40,8,0),(6,40,12,0)]:
        print(f' N{N} S{S} c{c} m{m}: own memory {stats(N,S,c,m)["win"]:.0%} -> shared {stats(N,S,c,m,shared=True)["win"]:.0%}')
    print('E. a turned friend knows where others hid (tell)')
    for N,S,c,m in [(4,24,12,0),(4,40,8,0),(6,40,8,0),(6,40,12,0),(4,40,12,0),(4,40,8,45),(6,40,8,45)]:
        print(f' N{N} S{S} c{c} m{m}:', '  '.join(f'tell {k}: {stats(N,S,c,m,tell=k)["win"]:.0%}' for k in (0,0.5,1.0)))
    print('F. full 54 grid with shared memory: count the 25-75% band')
    rows=[]
    for N,S,c,m in itertools.product((3,4,6),(12,24,40),(4,8,12),(0,45)):
        rows.append((N,S,c,m,stats(N,S,c,m,n=2000,shared=True)["win"]))
    band=[r for r in rows if .25<=r[4]<=.75]
    print(' band',len(band),'of 54; never',sum(1 for r in rows if r[4]<=.05)); print(' ',[(r[:4],round(r[4],2)) for r in band])
    print('G. whole-house check time vs night: S*c seconds for one hunter')
    for S,c in itertools.product((12,24,40),(4,8,12)): print(f'  S{S} c{c}: {S*c}s', end=';')
    print()
