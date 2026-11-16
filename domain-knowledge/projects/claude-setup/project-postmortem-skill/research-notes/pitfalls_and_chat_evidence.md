# Pitfalls of postmortems, and chat transcripts as postmortem evidence

Scope: known biases in looking back at decisions, how good methods counter them, how researchers use diaries, decision logs and chat logs as data, how indie developers do design postmortems, and the risks when the AI that took part in the sessions also writes the analysis.
Research done 2026-11-16, 17 tool calls. Most sources are abstracts, search summaries or secondary write-ups; the ones read in full are marked [read in full].

## 1. The core biases: hindsight, outcome, counterfactuals, root cause, survivorship, self-report, single coder, blame

### Takeaway
Hindsight bias and outcome bias are well documented, and neither goes away when people are told to ignore what they know (Fischhoff found warning people did nothing). So the counter has to be structural: rebuild what was known before the outcome, judge the decision apart from the result, ask "how" instead of "why", and treat a single "root cause" as something the analyst chose, not something found. Published game postmortems carry known self-report and survivorship limits.

### Cited Findings

**Hindsight bias (Fischhoff 1975)**
- Paper: Fischhoff, "Hindsight ≠ foresight: The effect of outcome knowledge on judgment under uncertainty," J. Exp. Psych.: Human Perception and Performance 1, 288–299 — [PDF](https://is.muni.cz/el/phil/jaro2018/PSX_512/um/Fischhof_hindsight.pdf?lang=en)
- Knowing an outcome makes people judge it as more likely or inevitable ("creeping determinism"), and they don't notice the shift in their own judgment — [FORRT replication atlas](https://forrt.org/flora-replication-atlas/doi/10.1037/0096-1523.1.3.288/); [Scientific American blog](https://www.scientificamerican.com/blog/literally-psyched/the-perils-of-hindsight-judgment/)
- People with the outcome overestimated what they would have known without it, and what others actually knew — [FORRT](https://forrt.org/flora-replication-atlas/doi/10.1037/0096-1523.1.3.288/)
- Telling people to avoid hindsight bias did not reduce it (reported in search summaries of the paper; not checked against the full text) — [LessWrong summary](https://www.lesswrong.com/posts/fkM9XsNvXdYH6PPAx/hindsight-bias)
- Replications are mixed: FORRT lists 3 replications, 2 failed and 1 succeeded; a 2025 preregistered replication reported "low replicability" of the exact experiment, while Chen et al. 2021 (N=890) replicated Experiment 2 — [FORRT](https://forrt.org/flora-replication-atlas/doi/10.1037/0096-1523.1.3.288/). Caveat: this concerns the original paradigm. The general hindsight effect is widely replicated in other paradigms (assumed, not checked here).
- The hindsight effect was reported to almost vanish when the outcome was attributed to chance events nobody could foresee (from search summary; primary source not opened) — [Hindsight and Causality, U. Michigan](https://deepblue.lib.umich.edu/handle/2027.42/68984?show=full)

**Outcome bias (Baron & Hershey 1988)**
- J. Personality & Social Psych. 54, 569–579; five studies. The same decision was rated as better made, and its maker as more competent, when the outcome was good (e.g., a surgeon's risky operation) — [PDF](https://bear.warrington.ufl.edu/brenner/mar7588/Papers/baron-hershey-jpsp1988.pdf); [ALNAP record](https://library.alnap.org/node/67763)
- Replicated: Aiyer et al. 2023, N=692, between-subjects, same direction — [IRSP](https://reference-global.com/article/10.5334/irsp.751)
- People who said the outcome shouldn't count still showed the bias — [Colorado Judicial brief](https://coloradojudicial.gov/media/4413)

**Local rationality and the "new view" (Dekker, Woods)**
- Local rationality principle: "People do what makes sense to them at the time — given their goals, attentional focus, and knowledge — otherwise they wouldn't be doing it" — [Ted Neward notes on Dekker's Field Guide](https://research.tedneward.com/management/field-guide-to-understanding-human-error.html); [SKYbrary, Systems Thinking for Safety, Principle 2](https://skybrary.aero/index.php/Toolkit:Systems_Thinking_for_Safety/Principle_2._Local_Rationality)
- Dekker's old view treats "human error" as the cause; the new view treats it as a symptom tied to tools, tasks and environment — [Review of the Field Guide](https://roblog.co.uk/2021/10/the-field-guide-to-understanding-human-error/)
- Lineage: Woods et al., *Behind Human Error* (1994 report; 2nd ed. 2010 with Dekker, Cook, Johannesen, Sarter) — [psychsafety summary](https://explore.psychsafety.com/n/woods-et-al-1994/)

**Root cause fallacy, "why" vs "how", counterfactuals (Allspaw 2014)** [read in full]
- "Cause is something we construct, not find." Stopping at one cause meets a need for closure ("root cause seduction," citing Carroll); the analyst picks where the chain starts and stops — [Allspaw, The Infinite Hows](https://www.kitchensoap.com/2014/11/14/the-infinite-hows-or-the-dangers-of-the-five-whys/)
- "Why?" tends to turn into "who?" and points at personal faults; "how?" questions produce stories that hold real operational data — [same](https://www.kitchensoap.com/2014/11/14/the-infinite-hows-or-the-dangers-of-the-five-whys/)
- Counterfactual: calling an action "wrong" depends on knowing the outcome. He asks "why didn't we fail today?" to show that successes have many contributing conditions too — [same](https://www.kitchensoap.com/2014/11/14/the-infinite-hows-or-the-dangers-of-the-five-whys/)
- Quotes Dekker: "The worse the consequences, the more any preceding acts are seen as blameworthy" — [same](https://www.kitchensoap.com/2014/11/14/the-infinite-hows-or-the-dangers-of-the-five-whys/)
- Recommended questions (from Gary Klein): "What were you seeing?", "What were you expecting to happen?", "Did this situation fit a standard scenario?", "How did you judge you could influence the course of events?". Also: tell the person's story back to them to confirm it — [same](https://www.kitchensoap.com/2014/11/14/the-infinite-hows-or-the-dangers-of-the-five-whys/)
- Allspaw credits Todd Conklin, Sidney Dekker and Nancy Leveson for the ideas — [O'Reilly reprint](https://oreilly.com/ideas/the-infinite-hows)
- Five Whys began with Taiichi Ohno at Toyota; a parallel critique of it is Card 2017 in BMJ Quality & Safety — [Wikiwand: Five Whys](https://wikiwand.com/EN/Five_Whys)
- Allspaw's companion essay is "Each Necessary, But Only Jointly Sufficient" (cited in a search summary; not opened) — [InfoQ](https://www.infoq.com/news/2015/02/five-why)

**Self-report, selection and survivorship in published game postmortems**
- Shirinian 2011 [read in full]: 24 Game Developer postmortems (2008–2010), 5 right + 5 wrong items each, 240 items coded by one author by reading the content, not the headings. Caveats he gives: the data depends on the authors' "ability to present honest and complete information"; authors pick their own items, so "there is no guarantee that any given topic will be mentioned at all"; "we can never really know who is writing with candor"; every game shipped (survivorship). Findings: scope problems in 17/24 (71%); about half had very late feature changes; 29% committed to an inflexible design or plan — [Game Developer, Dissecting the Postmortem](https://gamedeveloper.com/audio/dissecting-the-postmortem-lessons-learned-from-two-years-of-game-development-self-reportage)
- Washburn et al., ICSE 2016 [read the PDF's methods, design and validity sections]: 155 Gamasutra postmortems over 16 years, 22 categories. Two authors coded the categories over iterative weeks and "discuss[ed] their qualitative tagging frequently" as their check on coder error (no inter-rater statistic reported). Threats they list: coding mistakes; self-reported postmortems "could be written by one particular set of game developers"; authors "may not report what actually happened during development or hide certain failures". Their answer was "we often find that the authors are very candid," plus releasing the raw data. Game design went wrong in 22% of postmortems, mainly from designs too ambitious to build and concepts that confused players (e.g., a GAMBIT prototype that "was not well thought-out and was boring to play") — [Washburn et al. PDF](https://thomas-zimmermann.com/publications/files/washburn-icse-2016.pdf); [UWaterloo page](https://swag.uwaterloo.ca/publications/what-went-right-and-what-went-wrong-an-analysis-of-155-postmortems-from-game-development.html)
- A 2020 extension (~200 postmortems, 1997–2019) reported that most main root causes were about people, not technology — [arXiv 2009.02440](https://www.arxiv.org/pdf/2009.02440)
- A commentary calls the postmortem set "a very self-selected group of projects" — [Never Work in Theory](https://neverworkintheory.org/2016/04/26/game-postmortems.html)

**Prospective hindsight / premortem (Klein)**
- Klein, "Performing a Project Premortem," HBR Sept 2007: imagine the project has already failed, then list the reasons. He cites Mitchell, Russo & Pennington 1989: imagining that an event already happened raised the ability to correctly name reasons for outcomes by 30% — [PDF copy](https://wiki.duraspace.org/download/attachments/104563925/ProjectPremortem.pdf?api=v2)
- Disputed: Jason Collins notes the 1989 study did not judge the quality of the reasons, so the safe reading is "more reasons," not "30% more accurate" — [Jason Collins](https://corporate.jasoncollins.blog/premortem); [Rework summary](https://resources.rework.com/libraries/project-management/pre-mortem)

### Inferences
- Warnings don't remove hindsight or outcome bias, so a postmortem needs steps that hide or separate the outcome. For example: write down what was known and expected before reading what happened; judge "was this a reasonable call given X" separately from "did it work".
- Rank "root cause" claims by how many contributing conditions they ignore. A design postmortem that ends on one cause ("the core loop was boring") has probably stopped where closure felt good (Allspaw).
- Survivorship cuts both ways for a solo designer. Published postmortems over-represent shipped games, so their "lessons" may not fit projects that died in prototype, which is where most "finding the fun" failures happen.
- Shirinian's point about missing topics applies to chat logs too: if a transcript never mentions a design problem, that doesn't mean the problem wasn't there.

### Gaps
- Meta-analyses of hindsight bias (e.g., Guilbault et al. 2004) and the Roese & Vohs 2012 review were not checked (named from memory, unverified).
- Hollnagel (ETTO principle, Safety-II, "what-you-look-for-is-what-you-find"), Cook's "How Complex Systems Fail" and Woods' "second story" were not fetched. They fit here but are uncited.
- No source measured the actual size of self-report bias in game postmortems; only the authors' caveats were found.
- Dekker's own text on counterfactuals ("should have / could have") was not read directly; only secondary summaries.

## 2. Diaries, decision logs, design rationale and chat logs as data

### Takeaway
Records made at the time beat accounts written later, because they hold what was known then. Each kind has known weaknesses: diaries trade recall accuracy against how much effort the entry takes, and keeping one changes behaviour; design rationale is rarely captured because capture is costly, and rebuilding it afterwards is a named method of its own. Process tracing (from political science and historical method) gives formal tests for how strongly a piece of evidence supports a causal story. Developer–AI chat logs are now an established data source (DevGPT), but most shared logs are single-turn.

### Cited Findings
- Diary study designs: "feedback" studies (answer in the moment) give more accurate recall but take more effort; "elicitation" studies (capture quickly in the moment, answer later) take less effort but recall can be inaccurate — [Wikipedia: Diary studies](https://en.wikipedia.org/wiki/Diary_studies)
- Reactivity: keeping a diary can change how people think and act (Hawthorne effect) — [Wikipedia](https://en.wikipedia.org/wiki/Diary_studies); [ETH food-waste methods paper](https://www.research-collection.ethz.ch/server/api/core/bitstreams/de5e2507-c2a2-405e-b6cb-4c254be2d6e8/content)
- Design rationale (Lee 1997, IEEE Expert 12(3)) covers the reasons for a decision, its justification, the alternatives considered and the trade-offs weighed — [WPI tech report citing Lee](https://discmaster.textfiles.com/file/11697/ftp.cs.wpi.edu.zip/ftp.cs.wpi.edu/pub/techreports/pdf/02-03.pdf)
- Lee's five capture methods: reconstruction, record and replay, methodical by-product, apprentice, automatic generation — [WPI tech report 99-27](https://discmaster.textfiles.com/file/11697/ftp.cs.wpi.edu.zip/ftp.cs.wpi.edu/pub/techreports/pdf/99-27.pdf)
- Capture stays the hard part: recording every decision, including rejected ones, is "time consuming and expensive"; detailed rationale "is still rarely produced in practice" — [Cambridge AI EDAM, Capturing and using design rationale](https://cambridge.org/core/services/aop-cambridge-core/content/view/90D195E500BD8688EBE7E8750C817A85/S0890060400001888a.pdf/capturing-and-using-design-rationale.pdf); [Design Society paper](https://collaborative.designsociety.org/download-publication/30650/IMPROVING+DESIGN+RATIONALE+CAPTURE+DURING+EMBODIMENT+DESIGN)
- Process tracing (Collier 2011, PS 44:4) is "the systematic examination of diagnostic evidence selected and analyzed in light of research questions and hypotheses." Hoop test: a necessary condition, where failing it rules out the explanation and passing only keeps it alive. Smoking-gun test: a sufficient condition, where passing it strongly supports the explanation and failing only weakens it — [BetterEvaluation: Understanding process tracing](https://www.betterevaluation.org/tools-resources/understanding-process-tracing)
- How strong a test is depends on how common the evidence is (Mahoney 2012); Bayesian readings treat pass/fail as a simplification — [Wikipedia: Process tracing](https://Www.wikipedia.org/wiki/Process_tracing); [Bennett & Checkel](https://edisciplinas.usp.br/pluginfile.php/5569087/mod_folder/content/0/Textos/Bennett%20and%20Checkel%2C%20Process%20Tracing%20%20From%20Metaphor%20to%20Analytic%20Tool.pdf)
- DevGPT (Xiao, Treude, Hata, Matsumoto): 4,733 shared ChatGPT links from 3,559 GitHub/Hacker News references; 29,778 prompts and answers, linked to commits, issues and PRs — [arXiv 2309.03914](https://arxiv.org/html/2309.03914v2)
- In the DevGPT PR and Issue subsets, 66.8% and 63.1% of conversations were single-turn — [HackerNoon, Building the DevGPT Dataset](https://hackernoon.com/lite/building-the-devgpt-dataset-for-developer-chatgpt-studies)
- Follow-up work studied which tasks developers ask for and how multi-turn dialogues develop — [UWaterloo summary](https://plg.uwaterloo.ca/~migod/846/current/summaries/20-Tongwei-ChatGPTconvos-summary.pdf)

### Inferences
- A designer–AI chat transcript is an unusually complete "record and replay" source in Lee's terms. It holds the proposals, the rejected options and the stated reasons at the time they were made, which is exactly what design rationale research says is usually lost. Its known weakness is the diary problem: what wasn't said isn't there. Playtest feelings and offline thinking are missing.
- Process tracing fits it well. Write rival explanations for a design failure (e.g., "the mechanic was never fun" vs "it was fun but buried under scope" vs "the test was wrong"), then look in the transcript for hoop evidence (things that must appear if an explanation is true) and smoking-gun evidence (things that would only appear if it is true).
- Time-stamped turns let the analyst stop reading at each decision point and record "known / expected / options at this point" before reading on. That is a direct way to apply local rationality and keep out hindsight.
- Transcripts are also reactive. The designer may phrase things for the AI, and the AI's replies shape later turns, so the log records the process and also took part in it.

### Gaps
- The NN/g diary study article could not be found or fetched, so its specific guidance is uncited.
- No study was found that uses chat logs to judge design decisions in particular (as opposed to coding tasks).
- No source was found on the risk of rationalization in "reconstruction"-style rationale.

## 3. Reconstructing "what was known at the time"

### Takeaway
The standard method is to rebuild the situation as the person saw it, step by step: what they were seeing and expecting, and how they judged their options (Klein's questions via Allspaw). Use the outcome only after that, and frame the question as "how did it make sense" rather than "why did they get it wrong" (Dekker's local rationality).

### Cited Findings
- Aim: understand "how it made sense for someone to do what they did" (bounded rationality, Simon) — [Allspaw](https://www.kitchensoap.com/2014/11/14/the-infinite-hows-or-the-dangers-of-the-five-whys/)
- Klein-derived questions about the situation as it looked then (seeing, expecting, standard scenario, ability to influence); tell the story back to the person to check it — [Allspaw](https://www.kitchensoap.com/2014/11/14/the-infinite-hows-or-the-dangers-of-the-five-whys/)
- "Only with the benefit of hindsight" can an action be labelled a bad decision or human error; things that look obvious afterwards are assumed to have been obvious at the time — [SKYbrary Principle 2](https://skybrary.aero/index.php/Toolkit:Systems_Thinking_for_Safety/Principle_2._Local_Rationality); [ISHN](https://www.ishn.com/articles/115103-hidden-drivers-of-safety-error-include-rationality-which-affects-human-behavior)
- People overestimate what they and others knew before the outcome (Fischhoff Exp. 2–3) — [FORRT](https://forrt.org/flora-replication-atlas/doi/10.1037/0096-1523.1.3.288/)

### Inferences
- Applied to transcripts: for each decision, take only the turns up to that point and record (a) the information available, (b) the goal stated then, (c) the options raised, including rejected ones, (d) what the designer expected to happen. Only then compare with what happened later.
- Separate three questions, so outcome bias doesn't decide the verdict: was the decision reasonable on that information; was the information gettable at a reasonable cost (e.g., a cheap prototype); did it turn out well.
- The solo designer is the best source on "what you were seeing." Tell the reconstruction back to them to check it (Allspaw), but expect their memory to have shifted with hindsight (Fischhoff). Where the transcript and the memory disagree, trust the transcript for facts and ask the designer about feelings.

### Gaps
- Dekker's specific "tunnel" image and his method steps were not read in the primary text.

## 4. Solo / indie postmortems on design failure ("finding the fun")

### Takeaway
The GDC Failure Workshops (2011, 2012) show a recurring underlying problem in indie design failures: the team was in love with the concept and didn't test early whether it played well. Speakers found this by asking what they avoided, not just what broke. Published postmortems put design failure at about 22% of "what went wrong" items and say it comes from over-ambition and confusing concepts.

### Cited Findings
- Shadow Physics (Steve Swink / Scott Anderson): "a great concept but not much fun"; people praised it from watching without playing — [Game Developer, GDC 2011](https://www.gamedeveloper.com/console/gdc-2011-game-designers-confront-learn-from-failure)
- 2D Boy, Robot and the Cities: six months wasted because the team "was more in love with the concept of the game, and not obsessed enough with making the game fun"; the gameplay prototype came too late — [Game Developer GDC 2011](https://www.gamedeveloper.com/game-platforms/gdc-2011-game-designers-confront-learn-from-failure); [Engadget](https://www.engadget.com/2011/03/03/totally-crazy-totally-canceled-indie-games-and-the-people-who/)
- George Fan (Cat-Mouse Foosball): too much going on; prototype as early as possible, since "you won't know whether a game is fun until you're actually playing it" — [Game Developer GDC 2011](https://www.gamedeveloper.com/console/gdc-2011-game-designers-confront-learn-from-failure)
- Chris Hecker (rock-climbing game): blamed tech ratholing, distractions and avoiding design work, which all led back to one core problem: "I was scared of game design" — [Game Developer GDC 2011](https://www.gamedeveloper.com/console/gdc-2011-game-designers-confront-learn-from-failure)
- GDC 2012 Failure Workshop: four studios on building success from failure — [Engadget 2012](https://www.engadget.com/2012-03-07-the-failure-workshop-how-four-studios-built-success-from-defeat.html); [Game Developer 2012](https://gamedeveloper.com/design/gdc-2012-game-devs-find-lessons-in-their-failures); [GDC Vault listing](https://www.gdcvault.com/play/1015751/contactUs)
- Frozen Synapse developers called Frozen Cortex "a conceptual failure" (not opened) — [PC Gamer](https://pcgamer.com/frozen-synapse-devs-on-why-frozen-cortex-was-a-conceptual-failure)
- Washburn et al.: game design went wrong in 22% of 155 postmortems (over-ambitious; confusing concepts); recommended prototypes as proof of concept and iterating on them — [PDF](https://thomas-zimmermann.com/publications/files/washburn-icse-2016.pdf)
- Shirinian: 29% committed to an inflexible design or plan partway through — [Game Developer](https://gamedeveloper.com/audio/dissecting-the-postmortem-lessons-learned-from-two-years-of-game-development-self-reportage)

### Inferences
- How these speakers found the underlying design problem: they moved from a list of production symptoms (tech, distractions, late prototype) to one behaviour that explains them all (avoiding the test of whether it's fun). In process-tracing terms, the "avoidance" explanation predicts that playable tests come late and concept work runs long. A transcript can check that with timestamps.
- A design postmortem works on a different variable than a production one. The question is "when did we first learn whether the core interaction was fun, and what delayed it", not "what slipped".
- Shadow Physics' "people praised it from watching" is an evidence-quality point. Praise from watching, or from a sketch, is weak evidence of fun compared with play. That applies directly to an AI agreeing with a design in chat.

### Gaps
- No primary GDC Vault videos or slides were viewed. All quotes come from Game Developer and Engadget coverage.
- No written method for solo postmortems (e.g., templates from solo devs) was found within the time budget.

## 5. Risks when the AI that took part also writes the analysis

### Takeaway
There is direct evidence for three problems: LLMs prefer their own outputs, and the preference grows with how well they recognize their own text (Panickssery et al. 2024); self-evaluation bias gets worse with repeated self-refinement and shrinks with accurate external feedback (Xu et al. 2024); and RLHF assistants are sycophantic, giving in to the user's stated views over multiple turns (Sharma et al. 2023; SYCON 2025). An AI analysing its own sessions with the designer is exposed to all three: it may defend its own suggestions, accept the designer's framing of what went wrong, and miss failures it took part in.

### Cited Findings
- Self-preference: LLM evaluators rate their own summaries above those by other LLMs and humans, even when humans rate them equal; there is a linear link between self-recognition and self-preference, and fine-tuning recognition moved preference, which suggests a causal link (GPT-3.5, GPT-4, Claude 2, Llama 2; summarization) — [Panickssery, Bowman, Feng, arXiv 2404.13076 / NeurIPS 2024](https://arxiv.org/html/2404.13076v1); [NeurIPS oral](https://nips.cc/virtual/2024/oral/97998)
- Some evaluators preferred text that was *labelled* as their own even when it wasn't; swapping the labels reversed the direction for some models and datasets — [Moonlight review](https://www.themoonlight.io/review/llm-evaluators-recognize-and-favor-their-own-generations); [Alignment Forum](https://alignmentforum.org/posts/CeCKzsKABGKt9aabb/llm-evaluators-recognize-and-favor-their-own-generations)
- Self-bias appeared in all 6 models tested (GPT-4, GPT-3.5, Gemini, LLaMA2, Mixtral, DeepSeek). Self-refinement improves fluency but amplifies self-bias; larger models and accurate external feedback reduce it — [Xu et al., ACL 2024, arXiv 2402.11436](https://arxiv.org/abs/2402.11436)
- Sycophancy appeared in all 5 assistants tested; humans and preference models favour answers that match the user's views; sycophancy is "a general behavior of RLHF models" — [Sharma et al., arXiv 2310.13548](https://arxiv.org/abs/2310.13548v2)
- Multi-turn: across 17 LLMs, sycophancy remains common; alignment tuning amplifies it; scaling and reasoning optimization help resist it; taking a third-person perspective cut sycophancy by up to 63.8% in the debate scenario — [SYCON Bench, arXiv 2505.23840](https://arxiv.org/abs/2505.23840v1)
- TRUTH DECAY measures sycophancy that builds up under repeated user pushback, including "mimicry" when a user states an answer as fact (results not checked) — [arXiv 2503.11656](https://alphaxiv.org/abs/2503.11656)

### Inferences
- Self-serving risk: when it judges the decisions, the AI will tend to rate its own past proposals better, and it can recognize its own turns in the transcript. Counter: hide who wrote what (relabel speakers as A/B), or have a separate model or a fresh context judge the decisions.
- Framing risk: if the designer's prompt names the cause ("why did X fail because of Y"), sycophancy research predicts the analysis will confirm Y. Counter: rival explanations written before reading the evidence, with hoop and smoking-gun tests (section 2), and a third-person framing (SYCON's 63.8% result, in a debate setting, not checked for analysis tasks).
- Hindsight risk: the analysing model reads the whole transcript, ending included. Counter: feed it the transcript cut off at each decision point.
- Single-coder risk: one AI coding the transcript is one coder. Washburn used two coders in discussion. A second independent pass, ideally by a different model or with the authors hidden, then reconciliation, is the nearest equivalent.
- Xu et al.'s fix (accurate external feedback) points to the designer's playtest results and actual play data as the external check, not the AI's own judgment on another pass.

### Gaps
- No study was found on LLMs summarizing or judging *a conversation they took part in* in particular. The evidence above comes from judging their own outputs and from sycophancy toward users, so applying it to self-involved retrospectives is an inference.
- Effect sizes for frontier 2025–2026 models (including Claude Opus versions) were not found; the self-preference results use older models.
- No research was found on whether hiding speaker identity in a transcript removes self-recognition (Panickssery suggests recognition comes from the text itself, so labels alone may not be enough; unverified).
