# chat-style

Research behind the `coworker` output style (`~/.claude/output-styles/coworker.md`), how replies are written.
Tags: [source] / [read] / [opinion].

- **Models over-talk, even when told to be short.**
  Long answers are often less accurate, and LLM judges reward length, which pushes models toward it [source: YapBench, https://arxiv.org/pdf/2601.00624].
- **Users often prefer short answers for simple tasks** [source, secondhand via YapBench: Juneja et al. 2024].
  A Slack GPT-4 chatbot study found mixed reactions to length [source: https://arxiv.org/abs/2404.17025].
- **BLUF (bottom line up front)** means the key point first.
  It isn't a rule to be short; it makes the point hard to miss, and can read as blunt for sensitive news [source: https://sethsivak.substack.com/p/bottom-line-up-front, https://experience.dropbox.com/virtual-first-toolkit/communication/write-with-brevity].
- **Telegram style** (dropping pronouns and articles: "added to rule 21: …") comes from telegrams charged per word and lives on in texting; it signals speed and closeness [source: https://en.wikipedia.org/wiki/Telegram_style].
  It can cost clarity in technical messages or with strangers [opinion].
  Doc style guides forbid telegraphic language that drops words the meaning needs [source: https://documentation.avaya.com/en-us/home/bundle/avaya-documentation-standards/AvayaGISCustomerDocStandards/WritingConventions/Modifiers/DoNotOmitImportantWords.html].
  [read] So drop "I've", but never the noun that marks where an idea ends.
- **Slack advice:** one complete message, the answer first, no "hi", easy to scan [source: Grammarly, Talaera, Slack, LeadDev, Equal Experts; mostly blogs].
- **The user's own rule:** shrink the ideas, not the words; one idea per reply.

## Simple explanations (YouTube explainers, teaching)
Read through search summaries; only the Common Craft post was opened.
- **Big picture first, details only when asked.** Common Craft's Lee LeFever: forest before trees; "if we get to the details too quickly, we'll lose the audience" [source: https://news.commoncraft.com/posts/supporting-your-message-with-trees-branches-and-leaves, https://bobmorris.biz/?p=19283].
- **Cut what doesn't serve the point** (Mayer's coherence principle), and **split it into pieces the learner paces** (segmenting) [source: https://ugc.futurelearn.com/uploads/files/7d/d6/7dd6188d-c343-4311-b064-ac98d2c95abc/Multimedia_Principles._R._E._Mayer__2020.pdf, https://services.dartmouth.edu/TDClient/1806/Portal/KB/PrintArticle?ID=171655].
  [read] In chat, the user's next question is the next piece.
- **One core message, one idea per sentence** [source: https://edis.ifas.ufl.edu/publication/WC193, https://getproofed.com.au/writing-tips/how-to-write-an-explainer-video-script/].
- **Repeat key words on purpose;** listeners can't reread, so repeated words act as signposts [source: https://digfir-published.macmillanusa.com/smhandbook8e/smhandbook8e_ch04_13.html, https://www.npr.org/sections/npr-training/2025/05/31/g-s1-66074/would-you-say-it-that-way-tips-on-writing-for-your-voice].
  Repeating the noun prevents ambiguity [source: https://our-languages.canada.ca/en/writing-tips-plus/gender-inclusive-writing-repeat-the-noun].
  [read] So "symptoms design and items design", not "symptoms and items design" (the user's own rule).
- **About four things fit in working memory at once** [source: Cowan 2001, https://memory.psych.missouri.edu/assets/doc/articles/2001/cowan-bbs-2001.pdf]; the exact number is debated [source: https://journalofcognition.org/articles/387].
- **Concrete before abstract** (3Blue1Brown): open with an example, not the general idea [source: https://www.3blue1brown.com/faq/, https://blog.dropbox.com/topics/work-culture/grant-sanderson-channels-his-passion-for-math-into-marvelously-i].
- **Say the wrong idea, then fix it** (Veritasium).
  Derek Muller's PhD: clear lecture-style videos left students more sure of their wrong ideas; a dialogue that voiced the wrong idea and then corrected it taught significantly better, though viewers found it more confusing and worked harder [source: https://thejournal.com/articles/2015/05/05/watching-videos-does-not-necessarily-lead-to-learning.aspx, https://openjournals.library.sydney.edu.au/IISME/article/view/6345; the thesis itself not read].
  [read] Fits explaining a concept, not a status reply.

## Why one sentence reads hard
Case: "When something is waiting on your OK, those words are now in bold, and nothing is bold when nothing is waiting."
Read through search summaries.
- **Condition before the main point:** the reader has to reread to connect the two [source: https://www.plainlanguage.gov/guidelines/organize/place-the-main-idea-before-exceptions-and-conditions/].
- **"those words", "something" with no named thing:** the reader stops to guess what they point to [source: https://www.aje.com/arc/editing-tip-avoiding-vague-pronouns/, https://patthomson.net/2020/07/27/this-they-it-those-these-a-revision-strategy/].
- **Negation is slower to understand,** most of all with no context that sets it up [source: Clark & Chase 1972; Kaup & Lüdtke 2006, via https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2019.01227/pdf].
- **The same point turned around:** readers expect each part of a sentence to add something new, so they hunt for a difference that isn't there [from memory: Clark & Haviland 1977, "given-new contract"; the search didn't find it].
- **Abstract text is harder to understand and remember than concrete text** [source: Sadoski, Goetz & Rodriguez 2000, J. Educational Psychology 92:85–95, via https://www.wyliecomm.com/2020/02/concrete-images-in-writing].
  [read] Showing the bold would have beaten describing it.

## Asking questions
- **Ask directly**, with no "can I ask?" or "got a sec?" [source: https://thoughtbot.com/blog/how-to-ask-good-questions-online].
- **Give the context and narrow it** so it can be answered in one go [source: https://docs.glean.com/administration/assistant/slackbot/best-practices, https://tech.glints.com/an-engineers-guide-to-asking-better-questions-on-slack/].
- **When:** models tend to guess silently instead of raising an unclear point [source: https://arxiv.org/abs/2605.25284, preprint].
  People ask about what to do and rarely about what a word refers to, while LLMs do the opposite [source: https://arxiv.org/pdf/2507.10445, EMNLP 2025].
  [read] So: ask when the wording is ambiguous, and check facts yourself instead of asking.
- No source found for "one question at a time"; the user's own rule 4 says no list of questions at the end.

## Why the style rules weren't working
- **Curse of knowledge:** a writer can't imagine not knowing what they know, so their own labels seem clear to them ("my pick as the default", "two readings lead to different actions") [source: https://fs.blog/stephen-pinker-tells-us-why-our-professional-writing-sucks-and-what-to-do/].
  Fixes: everyday words, define or drop your own terms, reread as someone with zero context [source: https://blog.hubspot.com/marketing/writing-habit-curse-of-knowledge].
- **Plain language:** simple everyday words, short sentences (15–20 words), active voice, "you" [source: https://www.opm.gov/information-management/plain-language/, https://centerforplainlanguage.org/plain-language-top-ten-making-words-work/].
- **Examples beat abstract rules for surface style;** instructions give a steadier overall tone, so use both [source: https://arxiv.org/pdf/2509.14543v1, https://latitude.so/blog/how-examples-improve-llm-style-consistency].
  [read] So the coworker style writes each lesson as a general rule, with one of the user's rewrites under it as the example.
