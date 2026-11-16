"""Moonsick symptoms sim: one case, item-by-item treatment on the real map (mansion.gd layout).
Curse c rises R per untreated showing symptom per second; turn at c>=1; all 3 treated = cured."""
import random, math, heapq, sys, statistics as st

# rooms (x0, z0, w, d) from mansion.gd ROOMS; garden south of z=10
ROOMS = {"kitchen":(-15,-10,10,10),"hall":(-5,-10,10,10),"study":(5,-10,10,10),
         "dining":(-15,0,10,10),"conserv":(-5,0,10,10),"cellar":(5,0,10,10),"garden":(-15,10,30,25)}
DOORS = [("kitchen","hall",(-5,-5)),("dining","conserv",(-5,5)),("hall","study",(5,-5)),("conserv","cellar",(5,5)),
         ("kitchen","dining",(-10,0)),("hall","conserv",(0,0)),("study","cellar",(10,0)),("conserv","garden",(0,10))]
SPOTS = {"sunglasses":("hall",(-3.5,-9)),"cucumber":("conserv",(-3,8)),"razor":("study",(10,-7)),
         "bone":("garden",(-8,20)),"coffee":("kitchen",(-13,-8)),"bucket":("cellar",(12,8)),
         "eyepatch":("dining",(-12,5)),"wolfsbane":("garden",(3.4,24))}
GROUPS = {"eyes":["sunglasses","cucumber"],"body":["razor","bone"],"feel":["coffee","bucket","eyepatch"]}
SEEN = {"eyes","body"}

def room_of(p):
    for n,(x,z,w,d) in ROOMS.items():
        if x<=p[0]<=x+w and z<=p[1]<=z+d: return n
    return "garden"
def d(a,b): return math.hypot(a[0]-b[0],a[1]-b[1])
def path(a,b):
    ra, rb = room_of(a), room_of(b)
    if ra==rb: return d(a,b)*1.15
    # dijkstra over door points
    nodes = {i:p for i,(_,_,p) in enumerate(DOORS)}
    best = {}
    pq = []
    for i,(r1,r2,p) in enumerate(DOORS):
        if ra in (r1,r2): heapq.heappush(pq,(d(a,p),i))
    while pq:
        cost,i = heapq.heappop(pq)
        if i in best: continue
        best[i]=cost
        r1,r2,p = DOORS[i]
        for j,(s1,s2,q) in enumerate(DOORS):
            if j not in best and ({s1,s2}&{r1,r2}): heapq.heappush(pq,(cost+d(p,q),j))
    out = min(best[i]+d(DOORS[i][2],b) for i in best if rb in DOORS[i][:2])
    return out*1.15
def rand_pos(rng, garden_w=0.15):
    names = list(ROOMS); w = [1,1,1,1,1,1,garden_w*6]
    n = rng.choices(names, w)[0]; x,z,ww,dd = ROOMS[n]
    if n=="garden": dd = 15
    return (x+rng.uniform(1,ww-1), z+rng.uniform(1,dd-1))

def run_case(rng, helpers, S=30.0, R=1/120, held=False, wrong_p=0.0, jump=0.2, patient_tells=3.0):
    """helpers: list of dicts {speed, react} . returns (turned, c_at_end, t_end)"""
    order = rng.sample(["eyes","body","feel"],3)
    sym = {g: rng.choice(GROUPS[g]) for g in order}
    show = {g: i*S for i,g in enumerate(order)}
    ppos = rand_pos(rng)
    hpos = [rand_pos(rng) for _ in helpers]
    free_at = [0.0]*len(helpers)
    done = {}
    for g in order:  # greedy: each symptom, best helper by finish time
        t0 = show[g]
        best = None
        for i,h in enumerate(helpers):
            notice = h["react"] + (rng.uniform(1,6) if g in SEEN else patient_tells)
            start = max(t0+notice, free_at[i])
            item = SPOTS[sym[g]][1]
            dist = path(hpos[i], item) + path(item, ppos)
            fin = start + dist/h["speed"] + 0.3 + 2.0
            if best is None or fin < best[0]: best = (fin, i, item)
        fin,i,item = best
        if rng.random() < wrong_p: fin += 0  # wrong item handled below
        done[g] = fin; free_at[i] = fin; hpos[i] = ppos
    # integrate curse
    events = sorted(set([0.0]+list(show.values())+list(done.values())))
    rate = R*(0.5 if held else 1.0)
    c = 0.0
    wrong = rng.random() < wrong_p
    if wrong: c += jump
    for a,b in zip(events, events[1:]+[1e9]):
        u = sum(1 for g in order if show[g]<=a and done[g]>a)
        if u==0:
            if all(done[g]<=a for g in order): return (False, c, a)
            continue
        need = (1-c)/(rate*u)
        if a+need <= b: return (True, 1.0, a+need)
        c += rate*u*(b-a)
    return (False,c,0)

def trial(name, helpers, n=4000, **kw):
    rng = random.Random(7)
    res = [run_case(rng, helpers, **kw) for _ in range(n)]
    turned = sum(r[0] for r in res)/n
    cs = [r[1] for r in res if not r[0]]
    ts = [r[2] for r in res if not r[0]]
    print(f"{name:44s} turn {turned*100:5.1f}%  curse at cure {st.mean(cs) if cs else 0:.2f}  cured at {st.mean(ts) if ts else 0:5.1f}s")

HUMAN = {"speed":8.64/1.0, "react":0.0}
BOT = {"speed":7.0, "react":17.5}   # user: bots react ~15-20 s later
if __name__=="__main__":
    for S,R,label in [(30,1/120,"dusk S30 R1/120"),(20,1/90,"dawn S20 R1/90"),(25,1/80,"tight S25 R1/80"),(20,1/60,"brutal S20 R1/60")]:
        print("==", label)
        trial("1 helper human (solo)", [HUMAN], S=S, R=R)
        trial("1 helper human, patient held? (2nd person)", [HUMAN], S=S, R=R, held=True)
        trial("human + 4 slow bots (human healthy)", [HUMAN]+[BOT]*4, S=S, R=R)
        trial("5 slow bots (human is the patient)", [BOT]*5, S=S, R=R)
        trial("1 slow bot only", [BOT], S=S, R=R)
        trial("3 humans", [HUMAN]*3, S=S, R=R)
        trial("7 humans", [HUMAN]*7, S=S, R=R)
        trial("3 humans, 1 wrong item (20%)", [HUMAN]*3, S=S, R=R, wrong_p=0.2)
