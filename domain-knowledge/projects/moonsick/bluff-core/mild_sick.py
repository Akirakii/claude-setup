# Numbers for "everyone a little sick" (Claude, 2026-11-15). Rates from design.md; trip time from critic r1.
import random
NIGHT=720
def rate(t): p=t/NIGHT; return (1/120)*(1-p)+(1/40)*p          # curse per s per untreated symptom
def interval(t): p=t/NIGHT; return 30*(1-p)+8*p                 # s between symptoms in a case
print("Full case: latest time each item can land (all 3 late by the same t) before turning")
for t0 in (60,360,660):
    lo,hi=0,60
    for _ in range(40):
        m=(lo+hi)/2; c=0; t=t0; iv=interval(t0)
        # symptom k shows at k*iv, treated m s later
        for k in range(3):
            c+=rate(t0+k*iv)*m
        lo,hi=(m,hi) if c<1 else (lo,m)
    print(f"  case starting {t0//60} min in: {lo:.0f} s per item")
FAR_TRIP=27; GIVE=2
WINDOW=45; GAPMIN,GAPMAX=90,180
random.seed(1)
for n in (4,8):
    per=[]
    for _ in range(2000):
        t=0;k=0
        while True:
            t+=random.uniform(GAPMIN,GAPMAX)
            if t>NIGHT: break
            k+=1
        per.append(k)
    avg=sum(per)/len(per)
    print(f"{n} friends: {avg:.1f} mild symptoms per friend a night, {avg*n/12:.1f} a minute in the house; "
          f"window {WINDOW} s vs far trip {FAR_TRIP}+{GIVE} s gives {WINDOW-FAR_TRIP-GIVE} s spare; "
          f"fetching ~{avg*20/60:.1f} min of 12 per friend (20 s a trip)")
