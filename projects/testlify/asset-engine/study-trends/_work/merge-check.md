# Merge-check — Study Trends (Testlify), 2026-06-29

**Method (honest record).** Stage 2a phrases were extracted by parallel sub-agents (one TSV per subreddit,
425/425 posts covered, validated 0 missing / 0 extra). Consolidation (2b) was done by me, not delegated:
I read all 1,092 phrases, drafted a shared-pain taxonomy, assigned every post to its dominant-pain tension,
then ran the per-phrase check below on the **kept** tensions and removed phrases that had bled in from a
post's secondary content. Off-brand pains are retained as **named buckets** (not a junk drawer) and examined
here by name, then DROPPED at Stage 3 against `brand-scope.md`. This file is written **before** `tensions.csv`.

The Stage-3 anchor is `competitor-study/brand-scope.md`: Testlify owns **skills tests & assessments,
skills-based hiring, interview process/integrity, proctoring & anti-cheating (incl. AI-cheating in
interviews), bias/fairness/defensibility**. Off-limits: HR-ops not tied to hiring, ATS/CRM product mechanics,
general workplace/management, pure jobseeker career-advice.

---

## KEPT TENSIONS (passed merge-check + Stage 3)

### ai_interview_cheating — KEEP-CORE  (14 posts, 38 raw phrases)
**Shared-pain sentence:** *Candidates are using AI tools live during interviews to feed themselves answers, and interviewers can no longer tell who actually has the skill.*
- PASS (core): ChatGPT detected live during interview · reading AI answers verbatim · candidates reading AI responses on screen · senior candidate reading AI answers live · eyes scanning screen during interview · AI tools coaching candidates live · proxy interviewers · AI candidate impersonation · camera refusal hiding fake candidate · recruiter-vs-candidate AI arms race · arms race between recruiter and candidate AI · recruiters can detect AI · detection liability gap · cheating via screen share caught · typed Leetcode editorial verbatim · fake power outage cheating · AI cheating in interviews · AI-polished pitches masking weak answers · fake interview bots.
- **SPLIT / removed (bled in from secondary post content):** "ChatGPT 5 marginal improvement", "LLM hitting capability ceiling", "AI not replacing engineers yet", "LLM-native distribution shift", "ChatGPT app store empty opportunity", "platform dependency risk" (these are AI-capability commentary, not interview cheating) → reassigned to ai_code_quality_decay / macro buckets; "CEO and CPO caught cheating", "conflict of interest in HR investigation", "anonymous email accusing new hire of fraud" (workplace misconduct, not interview AI) → workplace_misconduct_hr.
- Size: >15 phrases is justified — this is the single strongest, most on-brand tension (AI-cheating in interviews is named explicitly in brand-scope). Not a topic blob: every retained phrase fits the one sentence.

### ai_resume_flood — KEEP-CORE  (11 posts, 28 raw phrases)
**Shared-pain sentence:** *AI lets candidates mass-generate and mass-apply with near-identical resumes, so screeners can't separate real signal from AI noise and capable people get buried.*
- PASS: AI-generated resume noise · AI-written CVs undifferentiated · AI-filtered applications · AI-generated message accepted · AI raised hiring bar · AI doom loop applications · volume-driven screening collapse · unread resume pile · human screener rarity · mass applying backfires · mass applying kills rate · mass-applying grind · CV specificity over keywords · keyword mirroring works.
- SPLIT / removed: "2000 applications sent", "1% interview rate", "CS grads double unemployment rate", "junior roles eliminated", "entry-level six-figure myth" (job-market volume/macro, not the AI-noise pain) → macro_layoffs_displacement; "$300 resume tailoring services" → it_career_advice.
- Size: justified — the AI-noise-in-screening pain is one conflict; macro job-market phrases were split out.

### degree_vs_skills — KEEP-CORE  (10 posts, 25 raw phrases)
**Shared-pain sentence:** *Employers gate roles behind degrees/credentials and auto-reject capable self-taught and experienced people, even as everyone agrees the degree no longer proves ability.*
- PASS: degree requirement blocking experienced candidates · degree required bias · degree-only assumption fails · degree-not-required paradox · self-taught dev hiring · six figures without degree possible · college credential theatre · compliance over qualification · outdated hiring checkboxes · CS degree devalued · CS degree market broken · STEM degree worthless now · degree and certs still jobless · no degree no certs.
- SPLIT / removed: "ghost jobs in listings" → ghost_jobs; "H1B offshoring cited", "graduation into bad market", "entry-level IT jobs disappearing" → macro_layoffs_displacement; "Leetcode grind no mentorship" → leetcode_broken_technical; "cert plus helpdesk pivot works", "Boston market career map", "20k to 162k", "stepping-stone roles" → it_career_advice.
- Size: justified — the credential-vs-capability conflict is one pain; career/macro phrases split out.

### softskill_culturefit_unmeasured — KEEP-CORE  (5 posts, 14 raw phrases)
**Shared-pain sentence:** *Soft skills, communication and "culture fit" decide who gets hired and fired, yet nobody measures them objectively before the hire — so "culture fit" becomes a cover for bias and bad calls.*
- PASS: no skills assessment · soft skills over technical · work style never assessed · "culture fit" cover for mismatch · culture fit hiring · culture fit disqualifier · environment over role · authenticity over performance · EQ invisible until hired · soft-skill assessment gap.
- SPLIT / removed: "candidate asks if interviewer pregnant", "repeated pregnancy questions" (interview-discrimination incident) → vague_rejections/workplace; "startup CEO conducting interview for personality fit only" kept (fits); "recovering bad interview" → misc.

### leetcode_broken_technical — KEEP-CORE  (4 posts, 11 raw phrases)
**Shared-pain sentence:** *Technical screening rewards memorized algorithm trivia and rote LeetCode grinding instead of real engineering work, so it selects for test-prep, not ability.*
- PASS: LeetCode pointless gatekeeping · blanking on syntax mid-interview · brain fart gets pass · Leetcode grind not landing jobs · AI before algorithms · skipping CS basics · freshmen skipping fundamentals.
- SPLIT / removed: "career fairs waste time", "recruiter indifference", "job-hopping resume red flag", "non-FAANG offer accepted" → misc / unrelated.

### remote_identity_fraud — KEEP-CORE  (3 posts, 9 phrases)
**Shared-pain sentence:** *Fake and proxy candidates — including organized rings using stolen identities — pass remote screening and background checks, so companies hire people who aren't who they claim to be.*
- PASS (all 9, clean): North Korean identity fraud hired · passed background checks with stolen identity · remote job verification gap · North Korean fake candidates · North Korean fake candidates passing screening · fraudulent remote applicants · fraudulent ID verification failure · stolen identity red flags · remote tech role infiltration.
- Small but coherent and squarely on-brand (remote test integrity); timely (2026 N. Korean-IT-worker story).

---

## OFF-BRAND / OFF-BUYER BUCKETS — examined by name, DROPPED at Stage 3

Each is a real shared pain but sits outside Testlify's scope; transplant checked, then dropped.

- **ats_keyword_filter (16 posts)** — pain: *resumes are killed by keyword bots before a human sees them.* Off-brand: ATS mechanics are an explicit product-lane exclusion (Recruiterflow/TalentLyft). Transplant considered ("assess capability, not keywords") but the topic is ATS-tooling, not assessment; the stronger screening-signal angle is already carried by `ai_resume_flood` and `degree_vs_skills`. DROP.
- **macro_layoffs_displacement (67 posts)** — pain: *tech layoffs, AI/offshoring displacement gut job security.* Off-brand macro-economics/career-market; no assessment angle. No transplant. DROP.
- **workplace_misconduct_hr (53 posts)** — pain: *employees face misconduct, retaliation, unfair termination and ignored complaints.* Off-brand HR-ops/employee-relations, not hiring. No transplant. DROP.
- **manager_people_mgmt (34 posts)** — pain: *managers struggle with PIPs, PTO, promotions, retention, RTO.* General management, off-brand. No transplant. DROP.
- **smallbiz_ops (25 posts)** — pain: *small-business owners fight bad clients, no-shows, cash flow, fake reviews.* Fully off-brand. DROP.
- **startup_founder (21 posts)** — pain: *founders wrestle fundraising, pitch decks, co-founder conflict, moats.* Off-brand. (One stray "paid assessment predicts performance" supports `degree_vs_skills`'s thesis but isn't its own tension.) DROP.
- **ai_code_quality_decay (18 posts)** — pain: *AI/vibe-coding is degrading code quality and developer craft.* Engineering-culture, off-buyer. No transplant. DROP.
- **it_career_advice (17 posts)** — pain: *how to break into IT — certs, help-desk, trades, job-hopping for pay.* Pure jobseeker career-advice, explicitly off-buyer. DROP.

## SMALL OFF-SCOPE / CANDIDATE-SIDE TENSIONS — DROPPED (≤8 posts each)
ghost_jobs, interview_rounds, comp_bait_switch, remote_mirage, pay_transparency, unrealistic_requirements,
vague_rejections, resume_gaps, age_discrimination, resume_lying, hiring_scams, unpaid_freework,
slow_hiring_process, overemployment_remote_trust, video_interview_dehumanizing — all are coherent pains but
either candidate-side career-advice, compensation/HR-ops, or recruiter-ops product-lane. Transplant checked:
the genuinely link-worthy assessment angles among them (skills-over-resume, interview integrity) are already
carried by the six kept CORE tensions, so these add no new ownable asset. DROP. *(ghost_jobs is a known
strong link format — "phantom-posting index" — but its subject is employer-honesty/job-market, not
assessment; logged here as a transplant-considered DROP rather than forcing an off-brand asset.)*

## misc
59 posts (13.9% of 425, under the 15% cap) — genuine no-shared-pain singletons across drama/one-off posts.
Re-mined: no remaining 3+ on-brand cluster worth promoting (the on-brand signal is captured above).
