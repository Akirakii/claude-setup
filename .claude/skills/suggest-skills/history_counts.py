"""Count what the user asks for most, from Claude Code's prompt history (~/.claude/history.jsonl).
Usage: python3 -I history_counts.py [keyword-regex ...]
No args: top 2- and 3-word phrases (common words skipped). With args: how many prompts match each regex."""
import collections, json, os, re, sys
STOP = set("a an the and or to of in on for with is it i you we this that be can should could would do does did "
           "my me your our us at as by from if so but not no yes ok okay just like then also lets let's please "
           "what how why when where which there here are was were will have has had into about more less very".split())
rows = []
for line in open(os.path.expanduser("~/.claude/history.jsonl")):
    try:
        t = (json.loads(line).get("display") or "").lower()
    except ValueError:
        continue
    if t and not t.startswith("/"):
        rows.append(t)
print("prompts:", len(rows))
if len(sys.argv) > 1:
    for k in sys.argv[1:]:
        print(f"{sum(1 for t in rows if re.search(k, t)):6d}  {k}")
    sys.exit()
grams = collections.Counter()
for t in rows:
    w = [x for x in re.findall(r"[a-z][a-z'-]+", t) if x not in STOP]
    for n in (2, 3):
        for i in range(len(w) - n + 1):
            grams[" ".join(w[i:i + n])] += 1
for g, c in grams.most_common(60):
    print(f"{c:6d}  {g}")
