# Cross-industry methods for reviewing a single failed project or incident

Tags used below: **[verified]** = read in the cited page this session. **[secondary]** = from a secondary source summarising the primary. **[unverified: memory]** = from the researcher's prior knowledge of the primary text; not confirmed in a fetched source this session. Several primary sources could not be fetched: the HBR pre-mortem full text (paywall), the CAST handbook PDF (certificate/connection errors at psas.scripts.mit.edu and sunnyday.mit.edu), the BMJ Quality & Safety London Protocol 2024 paper (HTTP 403), the London Protocol 2024 PDF (Google Docs export 400), TC 25-20 itself, and retrospectives.com (DNS failure).

## What are the exact steps of each method, and what goes in and comes out of each step?

### Takeaway
Almost every method has the same skeleton: (1) agree what was meant to happen and set the safety rules, (2) rebuild a factual timeline, (3) find the problems or gaps, (4) explain why they happened, (5) commit to owned actions, (6) share the record. The methods differ in step 4: one "why" chain (5 Whys/COE/A3), contributory-factor categories (London Protocol), a control-structure model (CAST), or studying normal work (Learning Teams/Safety-II).

### Cited Findings

**US Army After Action Review (AAR)**
- Four questions, in one common wording: what was expected to happen, what actually happened, what went well and why, what can be improved and how. [secondary] — [CEBMA guide to the AAR (UC Davis host)](https://tcec.sf.ucdavis.edu/sites/g/files/dgvnsk5301/files/inline-files/CEBMAGuide-to-the-after_action_review_CEBMA.ORG_.pdf)
- Another source words the same four questions differently: the goal, what happened, why it happened, how to do it differently. The structure is the same: what was planned vs what happened, then causes, then improvements. [secondary] — [ADI After Action Review Guide](https://www.adi.org/downloads/After-Action-Review-Guide.pdf)
- Formal vs informal: both use the same format and questions. A formal AAR is planned ahead and run by a facilitator or trained "AAR conductor". An informal AAR is run by the people who did the work, often right after it. Small units tend to run informal ones. [secondary] — [CEBMA guide](https://tcec.sf.ucdavis.edu/sites/g/files/dgvnsk5301/files/inline-files/CEBMAGuide-to-the-after_action_review_CEBMA.ORG_.pdf); [Wikipedia: After-action review](https://www.wikipedia.org/wiki/After-action_review)
- Steps with inputs and outputs [unverified: memory of TC 25-20, 1993]:
  1. Plan. In: the training event and its objectives. Out: who attends, when and where, the observers.
  2. Prepare. In: observer notes, the site, any recordings. Out: a chronology of key events and the discussion points.
  3. Conduct. In: the participants and the four questions. Out: a shared account of what happened, with sustains (what to keep) and improves (what to change).
  4. Follow up. In: the improves. Out: retraining, and changes to plans or standard procedures.
  - TC 25-20 says an AAR is "not a critique" and pins down the expected standard before discussing performance. [unverified: memory]

**Google SRE postmortem**
- Triggers are set before any incident: user-visible downtime or degradation past a threshold, any data loss, on-call intervention (rollback, rerouting), resolution time past a threshold, or a monitoring failure. Any stakeholder may ask for a postmortem. [verified] — [SRE book, Postmortem Culture](https://sre.google/sre-book/postmortem-culture/)
- Process: Draft (in: incident data. Out: first draft in a shared doc) → Review (senior engineers check it against criteria; review sessions close open comments) → Publish (shared widely, added to a team/org repository). [verified] — [Postmortem Culture](https://sre.google/sre-book/postmortem-culture/)
- Review criteria: "Was key incident data collected for posterity?", "Are the impact assessments complete?", "Was the root cause sufficiently deep?", "Is the action plan appropriate and are resulting bug fixes at appropriate priority?", "Did we share the outcome with relevant stakeholders?" [verified] — [Postmortem Culture](https://sre.google/sre-book/postmortem-culture/)
- Output document sections (example): Date, Authors, Status, Summary, Impact, Root Causes, Trigger, Resolution, Detection, Action Items, Lessons Learned (What went well / What went wrong / Where we got lucky), Timeline, Supporting information. The example root cause reads "Cascading failure due to combination of exceptionally high load and a resource leak". [verified] — [SRE book, Example Postmortem](https://sre.google/sre-book/example-postmortem/)

**Amazon Correction of Errors (COE)**
- Precondition: "It is imperative that the negative impact caused by the event be mitigated before the COE process begins." [verified] — [AWS blog: Why you should develop a COE](https://aws.amazon.com/blogs/mt/why-you-should-develop-a-correction-of-error-coe)
- Document sections and what each produces [verified, same source]:
  - Summary: written last, placed first. It must stand alone for a non-technical reader ("as if it were going to travel as an email update to your company's main stakeholder").
  - Impact: customer and business impact, measured.
  - Timeline: in time order, from "the first trigger that led to the problem".
  - Metrics: how the impact is defined, how it was detected, how it is monitored. Missing metrics are "a red flag".
  - Incident questions: detection, diagnosis, mitigation, prevention.
  - Five Whys: sits under Prevention. Stop "when you are confident that you have found the root causes". It may take more than five whys.
  - Action items: "Each action item must state its priority, who is the person responsible, and a due date".
  - Related items: other COEs and documents.
- A re:Invent 2022 deck gives the same anatomy: summary, impact, timeline, metrics, event questions, 5 whys, action items, related items. [secondary: AWS-authored slides, not opened] — [ARC308 deck](https://d1.awsstatic.com/events/Summits/reinvent2022/ARC308_Improving-resiliency-with-the-correction-of-error-process.pdf)
- A worked fictional example walks through each section. [not fetched] — [AWS blog: Creating a COE document](https://aws.amazon.com/blogs/mt/creating-a-correction-of-errors-document/)
- In November 2025 AWS added a guided Five Whys section to CloudWatch incident reports. [secondary: search snippet] — [AWS What's New](https://aws.amazon.com/about-aws/whats-new/2025/11/amazon-cloudwatch-incident-reports-five-whys-analysis)

**Toyota A3 report and 5 Whys**
- An A3 has a left side for the current situation and the nature of the issue, and a right side for the countermeasures considered, tested and chosen, plus "who will do what when". It closes with "the evidence that the issue has actually been addressed". LEI says the A3 "is not a template" but a thinking process, and also uses it as a storyboard, a report, and a coaching tool where managers ask questions instead of giving answers. [verified] — [LEI Lexicon: A3 Report](https://www.lean.org/lexicon-terms/a3-report/)
- Common A3 section labels: Background, Current condition, Goal/target, Root cause analysis, Countermeasures, Implementation plan, Follow-up. Each step follows PDCA. [unverified: memory of Shook, *Managing to Learn*, LEI 2008; the LEI lexicon page does not list these labels or mention PDCA]
- 5 Whys: "the practice of asking why repeatedly whenever a problem is encountered in order to get beyond the obvious symptoms". Ohno's example: a blown fuse, traced through lubrication, a worn pump shaft, and finally a missing strainer. "The specific number five is not the point." For a "gap from standard" problem the stages are: specific problem definition → goal setting → root cause analysis → countermeasures → checks, standards and follow-up. [verified] — [LEI Lexicon: 5 Whys](https://www.lean.org/lexicon-terms/5-whys/)

**London Protocol (healthcare)**
- Core questions: what happened (outcome and chronology), how it happened (care delivery problems), why it happened (contributory factors). [secondary] — [HealthManagement.org: The London Protocol](https://healthmanagement.org/pdf/article/the-london-protocol)
- A care delivery problem counts only if care went beyond safe practice and could have affected the outcome. One problem can have many contributory factors. [secondary] — [cause-x: London Protocol framework](https://cause-x.squarespace.com/framework-lp)
- 2004 steps with inputs and outputs [unverified: memory of Taylor-Adams & Vincent 2004, Imperial College copy at [londonprotocol_e.pdf](https://t4awstest.cc.ic.ac.uk/media/imperial-college/medicine/surgery-cancer/pstrc/londonprotocol_e.pdf), not opened]:
  1. Identification and decision to investigate. In: the incident report. Out: a go/no-go decision and the scope.
  2. Select the investigation team. Out: an independent, mixed-skill team.
  3. Organise and gather data. In: records, statements, structured interviews. Out: the evidence set.
  4. Determine the incident chronology. Out: a timeline (narrative, time-person grid, or flow chart).
  5. Identify care delivery problems. In: the chronology. Out: a list of points where care went beyond safe limits.
  6. Identify contributory factors. In: each care delivery problem. Out: the factors behind it, sorted into patient, task and technology, individual staff, team, work environment, organisation and management, and institutional context.
  7. Make recommendations and develop an action plan. Out: actions ranked by priority, each with an owner and a date.
- 2024 edition (title "Systems Analysis of Clinical Incidents: The London Protocol 2024"): its contents list sections on care provided, defences and barriers, and "eight levels of safety". It then runs from determining the chronology, through identifying "care management problems" (the 2004 term was "care delivery problems"), to contributory factors and assessing the wider organisation. [secondary: search-result summary of the PDF contents] — [London Protocol 2024 PDF (Google Docs)](https://docs.google.com/document/d/1fRQypw2deM5su4ar8C8jEL3MfPHflA89zmSg7SWxtuM/export?format=pdf)
- Main changes in 2024, per the BMJ Quality & Safety development paper (Vincent et al., published 22 Feb 2025, DOI 10.1136/bmjqs-2024-017987):
  - more emphasis and guidance on engaging patients and families as partners in the investigation;
  - the value of a small number of in-depth analyses, combined with thematic reviews of wider problems.
  [secondary: search snippet of the abstract] — [BMJ Qual Saf](https://qualitysafety.bmj.com/content/early/2025/02/22/bmjqs-2024-017987)
- Authorship conflict: PSNet credits Taylor-Adams & Vincent (NIHR NW London PSRC, Oct 2024). The PDF credits Vincent, Adams, Bellandi, Higham, Michel and Staines. — [PSNet](https://psnet.ahrq.gov/issue/systems-analysis-critical-incidents-london-protocol); [Q Community event](https://q.health.org.uk/get-involved/events/systems-analysis-of-clinical-incidents-the-london-protocol-2024)

**STAMP/CAST (Leveson)**
- The goal of the analysis is "to identify the limitations of the safety control structure that allowed the loss and identify how to strengthen the structure in the future". [secondary: quoted from the handbook in search results] — [MIT OCW 16.63 lecture notes](https://ocw.mit.edu/courses/16-63j-system-safety-spring-2016/d2501c7b1ce13719f38812e6d249dbee_MIT16_63JS16_LecNotes6.pdf); [Entropic Thoughts](https://entropicthoughts.com/root-cause-analysis-youre-doing-it-wrong)
- Steps with inputs and outputs [unverified: memory of the CAST Handbook, 2019; secondary sources confirm only "model the control structure, analyze each component, identify systemic factors"]:
  1. Assemble basic information. In: the loss, the hazards, the system boundary, the physical events. Out: a hazard list, the safety constraints, and a proximate event chain.
  2. Model the safety control structure. Out: a diagram of the controllers (people, organisations, software) and their control and feedback links.
  3. Analyse each component in the loss. Out: for each controller, its responsibilities, what it did, its process model (what it believed), its context, and why its actions made sense to it at the time.
  4. Identify control-structure flaws (systemic factors). Out: problems spread across components, such as communication and coordination, safety culture, changes over time, and the safety information system.
  5. Create an improvement program. Out: recommendations that change the structure, plus a way to follow them up.

**Dekker's "new view" / Safety-II / Learning Teams**
- Safety-II studies "work as done", the ordinary adjustments people make to keep things running, instead of only what failed. [secondary] — [ISHN](https://ishn.com/articles/108748-ways-to-simplify-safety-improve-performance); [SHP Online: Do we need a new view of safety?](https://www.shponline.co.uk/culture-and-behaviours/do-we-need-a-new-view-of-safety/amp/)
- A patient-safety paper says traditional RCA limits learning because it looks mainly at what went wrong. It proposes adding a comparison of work-as-imagined with work-as-done, and a look at what went well. [secondary] — [PSNet record](https://psnet.ahrq.gov/node/866621/psn-pdf)
- Learning Teams: the "soak time" step is a deliberate pause between sessions, which "predictably allows at least some of the Learning Team members to think of and offer additional information". After it, the team reviews what it found. [secondary: book chapter snippet, author unconfirmed] — [Taylor & Francis chapter](https://www.taylorfrancis.com/books/9781315382302/chapters/10.1201/b20559-13)
- A principle from *The Practice of Learning Teams* (Sutton, McCarthy, Robinson): workers know the problem best. [secondary: podcast blurb] — [Everand podcast](https://www.everand.com/podcast/631638187/Dr-Todd-Conklin-on-the-past-present-and-future-of-Learning-Teams-Part-Two-Welcome-to-the-3rd-Episode-of-the-podcast-series-Our-super-special-gues)
- Learning Team steps [unverified: memory of Conklin, *Better Safety*/*Pre-Accident Investigations*]:
  1. Frame the event. Out: an open question, not a cause to confirm.
  2. First session (learning mode). In: the workers who do the job. Out: a picture of how the work is normally done.
  3. Soak time. Out: new information from members after time to think.
  4. Second session (fix mode). Out: defences and changes, owned by the workers.
  5. Track the changes.

**Agile retrospectives**
- Derby & Larsen's five stages:
  1. Set the stage. Out: the team is ready and the purpose is framed.
  2. Gather data. Out: "a shared mental model of what happened".
  3. Generate insights. Out: why things happened and how the data connects.
  4. Decide what to do. Out: a few experiments or actions.
  5. Close. Out: a recap and a review of the retrospective itself.
  Skipping a stage weakens shared understanding and buy-in. [secondary] — [O'Reilly, *Agile Retrospectives* 2nd ed.](https://www.oreilly.com/library/view/agile-retrospectives-2nd/9798888650868/f_0010.xhtml); [Applied Frameworks](https://agile.appliedframeworks.com/applied-frameworks-agile-blog/agile-retrospective-framework-in-five-steps); [cPrime](https://www.cprime.com/?p=18348)
- Prime Directive: teams often read it aloud at the start of a retrospective. Its gist is to assume everyone did their best given what they knew at the time. [secondary] — [ThoughtWorks: Prime Directive, not just Star Trek](https://www.thoughtworks.com/en-ca/insights/blog/prime-directive-not-just-star-trek)
- Exact text [unverified: memory of Kerth, *Project Retrospectives*, 2001]: "Regardless of what we discover, we understand and truly believe that everyone did the best job they could, given what they knew at the time, their skills and abilities, the resources available, and the situation at hand."
- Kerth's project retrospective [unverified: memory]: a facilitated session of 2–3 days at the end of a project, run off-site. It includes building a project timeline from everyone's memories and artifacts, an emotions seismograph (a line of how people felt over time), and asking "what did we do well", "what did we learn", "what should we do differently", and "what still puzzles us".

**Pre-mortem (Klein)**
- Premise: "team members assume that the project they are planning has just failed" and generate plausible reasons. It works by "making it safe for dissenters who are knowledgeable about the undertaking and worried about its weaknesses to speak up". [verified: HBR summary page only] — [Klein, HBR 2007](https://hbr.org/2007/09/performing-a-project-premortem)
- Steps [unverified: memory of the full HBR article, which is paywalled]:
  1. Brief the team on the plan.
  2. The leader says the project has failed spectacularly.
  3. Each person writes reasons for the failure alone, for about 2 minutes.
  4. Go round the room; each person reads one reason at a time until all are listed.
  5. The project manager reviews the list and strengthens the plan.
  6. Revisit the list later in the project.
- The "prospective hindsight raises the ability to identify reasons by 30%" figure (Mitchell, Russo & Pennington 1989) [unverified: memory; not in the fetched page].

**UX research synthesis**
- Affinity diagramming, per NN/g:
  1. Generate notes. In: research observations or ideas. Out: an unsorted board. People write alone, 5–10 minutes.
  2. Cluster. Out: labelled themes. Uneven cluster sizes are normal.
  3. Prioritise. Out: ranked clusters and action items, each with an owner. Dot voting is used when there is no consensus.
  [verified] — [NN/g: Affinity Diagramming](https://www.nngroup.com/articles/affinity-diagram/)
- Journey/timeline reconstruction of project evidence: no source was fetched (see Gaps).

### Inferences
- All methods except Safety-II and Learning Teams reduce to: timeline → problem points → causes → owned actions. The real choice between them is the causal model in the "why" step.
- The COE and the SRE postmortem are both document-first, written mainly by one author and then reviewed. That makes them the easiest to adapt for a solo person.

### Gaps
- TC 25-20's exact step names and wording were not read in the primary.
- The full HBR pre-mortem text and the 30% statistic are unverified.
- CAST step names come from memory; the handbook PDF failed to load.
- London Protocol 2004 and 2024 step lists are partly from memory; the 2024 full text and the BMJ paper were not readable (403/400).
- The Learning Teams step sequence is not confirmed by any primary source.
- I found no source on "journey/timeline reconstruction" as a UX method applied to project post-mortems. Journey mapping literature (e.g. NN/g) was not fetched.

## Which methods favour one root cause vs several contributing factors, and why?

### Takeaway
5 Whys and the classic A3 lean toward a single chain ending in "the root cause". COE and SRE use the 5-whys vocabulary but write "root causes" in the plural. The London Protocol, CAST and Safety-II reject a single cause outright: in their models an accident is many interacting factors or control flaws.

### Cited Findings
- 5 Whys aims to keep asking "until the root cause is reached and eliminated". LEI's page does not discuss problems with several contributing causes. [verified] — [LEI: 5 Whys](https://www.lean.org/lexicon-terms/5-whys/)
- AWS COE says to stop "when you are confident that you have found the root causes" (plural). It does not say whether an incident has one cause or many. [verified] — [AWS COE blog](https://aws.amazon.com/blogs/mt/why-you-should-develop-a-correction-of-error-coe)
- Google SRE uses "root cause(s)" and "contributing causes" side by side without defining the difference. Its example root cause is a combination ("high load and a resource leak"). It also lists the trigger separately from the root cause. [verified] — [Postmortem Culture](https://sre.google/sre-book/postmortem-culture/); [Example Postmortem](https://sre.google/sre-book/example-postmortem/)
- CAST: "Don't assume accidents are due to one 'root cause' or a few 'probable causes'... most accidents are actually due to many interacting causes." [secondary quote of the handbook] — [Entropic Thoughts](https://entropicthoughts.com/root-cause-analysis-youre-doing-it-wrong); [MIT OCW notes](https://ocw.mit.edu/courses/16-63j-system-safety-spring-2016/d2501c7b1ce13719f38812e6d249dbee_MIT16_63JS16_LecNotes6.pdf)
- London Protocol: one care delivery problem can have many contributory factors, grouped by factor type. Factors that point to general unit-level problems are the ones that should drive change. [secondary] — [cause-x](https://cause-x.squarespace.com/framework-lp); [HealthManagement.org](https://healthmanagement.org/pdf/article/the-london-protocol)
- The 2024 London Protocol favours a few in-depth analyses plus thematic reviews across incidents, which is a step away from per-incident root causes. [secondary] — [BMJ Qual Saf 2025](https://qualitysafety.bmj.com/content/early/2025/02/22/bmjqs-2024-017987)
- Safety-II critics of RCA say it limits learning by looking only at failure. Some critics of the new view in turn warn that rejecting RCA wholesale "throws out the baby with the bathwater". [secondary] — [PSNet](https://psnet.ahrq.gov/node/866621/psn-pdf); [MATEC conf paper](https://www.matec-conferences.org/articles/matecconf/pdf/2019/22/matecconf_icsc_eswc2018_01003.pdf)

### Inferences
- The split follows the causal model. Linear-chain methods come from manufacturing machine faults, where a single physical cause is plausible: Ohno's fuse, pump and strainer. System methods come from complex sociotechnical accidents (hospitals, aviation, process plants), where many conditions combine.
- For a failed project, which is sociotechnical, multi-factor framing fits better. 5 Whys is still useful per factor, as AWS uses it.

### Gaps
- No primary source compares single-cause and multi-factor outcomes empirically.

## How does each method handle "what went well", blame, and hindsight?

### Takeaway
Blame: all modern methods say they are blameless (SRE, COE, the Prime Directive, CAST, the London Protocol), each in its own wording. "What went well" is built into the AAR, SRE's Lessons Learned, Kerth and Safety-II. COE and 5 Whys/A3 leave it out. Hindsight bias is named explicitly only in CAST (and in Dekker, per memory). The Prime Directive and SRE's "did the right thing with the information they had" handle it by assumption, not by a technique.

### Cited Findings
- SRE: blameless means focusing on contributing causes "without indicting any individual or team for bad or inappropriate behavior", and assuming participants "had good intentions and did the right thing with the information they had". The Postmortem Culture chapter does not discuss hindsight bias or "what went well". [verified] — [Postmortem Culture](https://sre.google/sre-book/postmortem-culture/)
- The SRE template does include "What went well / What went wrong / Where we got lucky". [verified] — [Example Postmortem](https://sre.google/sre-book/example-postmortem/)
- COE: "It is not a process for finding whom to blame". The 5 Whys is applied "in a blame-free way, focused on finding the 'why' rather than blaming 'who'". The COE has no what-went-well section. [verified] — [AWS COE blog](https://aws.amazon.com/blogs/mt/why-you-should-develop-a-correction-of-error-coe)
- AAR: "what went well and why" is one of the four questions. [secondary] — [CEBMA guide](https://tcec.sf.ucdavis.edu/sites/g/files/dgvnsk5301/files/inline-files/CEBMAGuide-to-the-after_action_review_CEBMA.ORG_.pdf)
- CAST: "Blame is the enemy of safety." Analysis should find design flaws, not blame operators for their consequences. The words "should have", "could have" or "if only" are a sign of hindsight bias. [secondary quote of the handbook] — [Entropic Thoughts](https://entropicthoughts.com/root-cause-analysis-youre-doing-it-wrong); [MIT OCW](https://ocw.mit.edu/courses/16-63j-system-safety-spring-2016/d2501c7b1ce13719f38812e6d249dbee_MIT16_63JS16_LecNotes6.pdf)
- Safety-II and the patient-safety RCA critique add "what went well" and the work-as-imagined vs work-as-done gap. [secondary] — [PSNet](https://psnet.ahrq.gov/node/866621/psn-pdf); [Drilling Contractor: investigating what goes right](https://drillingcontractor.org/new-safety-perspective-focuses-on-investigating-what-goes-right-32256)
- Prime Directive: assume everyone did their best given what they knew at the time. [secondary] — [ThoughtWorks](https://www.thoughtworks.com/en-ca/insights/blog/prime-directive-not-just-star-trek)
- Pre-mortem: it avoids hindsight by design, because the failure is imagined before it happens. It also makes dissent safe. [verified: summary] — [HBR](https://hbr.org/2007/09/performing-a-project-premortem)
- Dekker's countermeasure to hindsight is to ask why the action made sense to the person at the time, not what they "failed" to do (the "local rationality" principle), and to avoid counterfactual language. [unverified: memory of Dekker, *The Field Guide to Understanding 'Human Error'*]
- London Protocol: it states its purpose is to move away from blame and towards systems. [unverified: memory of the 2004 text]

### Inferences
- "Blameless" alone does not stop hindsight bias. Only CAST and Dekker give a concrete check: flag "should have / could have / if only", and ask why the action made sense at the time. That check works well for a solo reviewer, who has no group to catch their own hindsight.
- Methods without a "what went well" step (COE, 5 Whys) risk throwing away practices that worked.

### Gaps
- I did not read primary Dekker or Hollnagel texts this session.
- The London Protocol's exact blame and hindsight wording is not verified.

## Which steps work for a solo person with no team?

### Takeaway
Solo-friendly steps: building the timeline from artifacts, the AAR's four questions, an SRE or COE-style written document, 5 Whys applied to each factor, the London Protocol contributory-factor checklist, the CAST "why did this make sense at the time" and hindsight-word check, solo affinity clustering of notes, and a pre-mortem written alone before the next project. Team-dependent steps: Learning Teams sessions, the round-robin parts of the pre-mortem and retros, dot voting, and the independent review that SRE and COE rely on.

### Cited Findings
- The informal AAR is run by the people who did the work, right after it, with no facilitator needed. [secondary] — [CEBMA guide](https://tcec.sf.ucdavis.edu/sites/g/files/dgvnsk5301/files/inline-files/CEBMAGuide-to-the-after_action_review_CEBMA.ORG_.pdf)
- SRE and COE are written documents. The COE summary is written last, for a reader with no context. SRE's quality gate is a review by others. [verified] — [AWS COE](https://aws.amazon.com/blogs/mt/why-you-should-develop-a-correction-of-error-coe); [SRE](https://sre.google/sre-book/postmortem-culture/)
- LEI frames the A3 as a thinking process that "can be followed with or without a physical A3", and as a coaching dialogue between manager and author. [verified] — [LEI A3](https://www.lean.org/lexicon-terms/a3-report/)
- NN/g says an affinity diagram "is best created as a team", and gives no solo guidance. [verified] — [NN/g](https://www.nngroup.com/articles/affinity-diagram/)
- Learning Teams depend on workers' group knowledge and on soak time between sessions. [secondary] — [Taylor & Francis chapter](https://www.taylorfrancis.com/books/9781315382302/chapters/10.1201/b20559-13)
- The pre-mortem's value is making dissenters safe to speak, which assumes a group. [verified: summary] — [HBR](https://hbr.org/2007/09/performing-a-project-premortem)

### Inferences
- A solo reviewer loses the main thing groups supply: other views, which correct one person's single story and hindsight. Possible stand-ins are:
  - (a) the artifacts as "witnesses": commit logs, chats and notes;
  - (b) a delay between drafting and reviewing, like soak time;
  - (c) an outside reviewer or critic for the review step;
  - (d) the explicit hindsight-word check from CAST.
  These substitutions are the researcher's inference, not from a source.
- Soak time transfers to solo work: draft the analysis, wait, then reread. This is inferred.

### Gaps
- No source found that specifically adapts any of these methods for solo practitioners.
