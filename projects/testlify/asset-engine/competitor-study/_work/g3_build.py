import json

clusters = [
    {"idea":"Generative AI in Hiring & Skills Assessment: Use Cases, Bias Risks & Implementation Checklist","brand_fit":"ADJACENT","our_subject":"AI in hiring — strategy & adoption","member_rowids":["317","2029"]},
    {"idea":"AI vs. Human in Hiring: Decision Framework with Scoring Rubric & Assessment Review","brand_fit":"CORE","our_subject":"AI in hiring — AI vs human decision","member_rowids":["2146"]},
    {"idea":"AI Hiring Tool Risk & Vendor Audit Checklist: Bias, Transparency & Fairness","brand_fit":"ADJACENT","our_subject":"AI in hiring — vendor risk audit","member_rowids":["329","2166"]},
    {"idea":"AI Cheating in Hiring Assessments: Prevalence Data, Detection & Prevention Playbook","brand_fit":"CORE","our_subject":"Assessment integrity — AI cheating","member_rowids":["715","2354"]},

    {"idea":"Skills-Based Talent Management: How Assessment Feeds Hiring, Development & Succession Planning","brand_fit":"ADJACENT","our_subject":"Skills-based talent management","member_rowids":["324","2435"]},
    {"idea":"Building a Skills Inventory & Org-Wide Skill-Gap Map from Hiring/Assessment Data","brand_fit":"CORE","our_subject":"Skills inventory & gap mapping","member_rowids":["472","2321","2361"]},
    {"idea":"Hiring Needs & Skills-Gap Analysis Template: Turning Role Requirements into an Assessment Plan","brand_fit":"ADJACENT","our_subject":"Skills-gap-first workforce planning","member_rowids":["1001","1010","2439","2445","2068"]},

    {"idea":"Skills-Based Hiring Inside a TA Strategy: Reduce Time-to-Fill, Improve Quality-of-Hire, Cut Bias","brand_fit":"ADJACENT","our_subject":"Skills-based hiring — TA strategy","member_rowids":["361","1933","2010"]},
    {"idea":"Assessment-Qualified Talent Pipeline: Pre-Qualifying & Engaging Passive Candidates with Skills Tests","brand_fit":"ADJACENT","our_subject":"Talent pipeline — passive candidates","member_rowids":["401","469","1149","1392"]},

    {"idea":"Pre-Employment Assessment: The Complete Guide to Test Types, Validity, Bias & Candidate Experience","brand_fit":"ADJACENT","our_subject":"Pre-employment assessment — overview","member_rowids":["367","895","1837"]},
    {"idea":"Skills Assessment Method Comparison: Validity Ratings, Use-Case Matrix & Decision Tree","brand_fit":"CORE","our_subject":"Assessment method comparison","member_rowids":["2415","2205"]},
    {"idea":"Candidate Screening Methods Compared: Validity, Bias Risk & Conversion Benchmarks","brand_fit":"CORE","our_subject":"Screening methods comparison","member_rowids":["64"]},
    {"idea":"Resume Screening vs. Skills Assessment: Validity Comparison & Transition-to-Skills-First Checklist","brand_fit":"CORE","our_subject":"Resume vs skills assessment","member_rowids":["2175"]},

    {"idea":"Recruitment ROI & Cost-Per-Hire Calculator + Benchmark Report","brand_fit":"CORE","our_subject":"Recruitment ROI calculator","member_rowids":["413","1411"]},
    {"idea":"The True Cost of a Bad Hire vs. Cost of Assessment: ROI Calculator","brand_fit":"CORE","our_subject":"Cost-of-bad-hire ROI calculator","member_rowids":["1376","1994"]},

    {"idea":"Quality-of-Hire Benchmark Report + Scorecard: How Assessments Predict 90-Day Performance","brand_fit":"CORE","our_subject":"Quality-of-hire benchmarks","member_rowids":["485","454"]},
    {"idea":"Using Skills-Assessment Data to Predict Hire Quality: Building & Validating a Predictive Model","brand_fit":"CORE","our_subject":"Predictive screening models","member_rowids":["470","1327","645"]},
    {"idea":"Hiring Analytics Playbook: Measuring the Predictive Power of Your Skills Assessments","brand_fit":"CORE","our_subject":"Hiring analytics & metrics","member_rowids":["1410","1448","2086"]},

    {"idea":"How Skills Assessments Reduce Time-to-Hire/Fill: Benchmarks & Optimised Assessment Workflow","brand_fit":"CORE","our_subject":"Time-to-hire & funnel speed","member_rowids":["1364","1381"]},
    {"idea":"Assessment in the Recruiting Funnel: Which Tests at Each Stage & Conversion Benchmarks","brand_fit":"TRANSPLANT","our_subject":"Assessment across the funnel","member_rowids":["1401","1405"]},

    {"idea":"Hiring Bias by Stage: Audit Checklist Mapping Bias Types to Resume, Skills Test & Interview","brand_fit":"CORE","our_subject":"Bias audit — by hiring stage","member_rowids":["1551","2129","2132","2009","214","2363"]},
    {"idea":"Bias in Pre-Employment Assessments: How Test Design Creates Adverse Impact + Bias-Check Checklist","brand_fit":"CORE","our_subject":"Assessment design bias / adverse impact","member_rowids":["1814","1539","2042"]},
    {"idea":"Diversity & Representation Through Assessment: Auditing Your Test Battery for Adverse Impact","brand_fit":"CORE","our_subject":"Diversity & representation audit","member_rowids":["1918","2131"]},
    {"idea":"How Structured Assessments Eliminate Cognitive Bias (Confirmation, Similarity, Contrast, Halo/Horn)","brand_fit":"CORE","our_subject":"Cognitive-bias elimination via structure","member_rowids":["2033","2095","2108","2200"]},
    {"idea":"Blind / Anonymized Hiring Implementation Guide: What to Anonymize at Each Stage","brand_fit":"CORE","our_subject":"Blind hiring implementation","member_rowids":["2096"]},
    {"idea":"Age-Neutral Assessment Design: Avoiding Age Discrimination + Compliance Checklist","brand_fit":"TRANSPLANT","our_subject":"Age-neutral assessment design","member_rowids":["2139"]},

    {"idea":"Assessment Integrity Playbook: Proctoring Level by Role, Cheat-Resistant Questions & Detection","brand_fit":"CORE","our_subject":"Assessment integrity & proctoring","member_rowids":["1152","2171","1298"]},
    {"idea":"How Skills Tests Catch Candidate Dishonesty: Resume Inflation vs. Test-Score Gaps + Checklist","brand_fit":"CORE","our_subject":"Detecting resume inflation via testing","member_rowids":["2133"]},

    {"idea":"Candidate Experience in Skills-Based Hiring: Benchmarks, Drop-Off Data & Employer Checklist","brand_fit":"CORE","our_subject":"Candidate experience & drop-off","member_rowids":["417","537","1189"]},
    {"idea":"Assessment-Ready Candidate Guide for Employers: What to Tell Candidates Before a Skills Test","brand_fit":"TRANSPLANT","our_subject":"Candidate prep communication","member_rowids":["530"]},

    {"idea":"Designing Online Skills Tests for Hiring: Format, Timing, Question Types & Candidate Experience","brand_fit":"TRANSPLANT","our_subject":"Online test design best practice","member_rowids":["1170"]},

    {"idea":"Assessment Centre vs. Online Skills Test: When Each Fits, with Cost-Validity Comparison","brand_fit":"ADJACENT","our_subject":"Assessment centre vs online test","member_rowids":["1173"]},
    {"idea":"Virtual Job Tryout vs. Skills Assessment: Role-by-Role Comparison Guide","brand_fit":"CORE","our_subject":"Job tryout vs skills test","member_rowids":["1813"]},
    {"idea":"Job Simulation Design Kit: Build, Score & Compare Role-Specific Simulations vs. Skills Tests","brand_fit":"CORE","our_subject":"Job simulation design","member_rowids":["2057","1873","2449"]},

    {"idea":"Personality Tests for Hiring: Big 5 vs. DISC vs. MBTI — Validity, Legal Defensibility & Samples","brand_fit":"CORE","our_subject":"Personality assessment in hiring","member_rowids":["1143","1872","1958","1325"]},
    {"idea":"Behavioral Assessment Battery Builder: Pairing Personality + Skills Tests","brand_fit":"CORE","our_subject":"Behavioral assessment battery","member_rowids":["1950"]},
    {"idea":"Cognitive Ability in Hiring: Score Meaning, Role Benchmarks, Legal Compliance & Sample Questions","brand_fit":"CORE","our_subject":"Cognitive ability testing","member_rowids":["1845","1951"]},
    {"idea":"Reasoning Skills Assessment Battery: Which Tests to Stack by Role + Benchmarks","brand_fit":"CORE","our_subject":"Reasoning assessment battery","member_rowids":["1890"]},

    {"idea":"How to Assess Work Ethic, Motivation & Conscientiousness Before Hiring","brand_fit":"CORE","our_subject":"Work ethic / conscientiousness assessment","member_rowids":["1602","2006"]},
    {"idea":"Hiring for Adaptability / Agility: Test Types, Sample Questions & Agility Score Framework","brand_fit":"ADJACENT","our_subject":"Adaptability / agility assessment","member_rowids":["1921"]},
    {"idea":"Learning Agility Assessment Guide: Structured Questions, Work-Task & Scoring Rubric","brand_fit":"CORE","our_subject":"Learning agility assessment","member_rowids":["2211"]},
    {"idea":"Leadership Agility Assessment: Situational Awareness, Decision Speed & Adaptability","brand_fit":"CORE","our_subject":"Leadership agility assessment","member_rowids":["1947"]},
    {"idea":"Assessing Observation & Attention-to-Detail: Role-by-Role Guide with Sample Questions","brand_fit":"CORE","our_subject":"Attention-to-detail assessment","member_rowids":["1889"]},
    {"idea":"How to Assess Dependability & Reliability: Behavioral Questions, Work-Sample & Rubric","brand_fit":"TRANSPLANT","our_subject":"Dependability assessment","member_rowids":["2296"]},
    {"idea":"The Soft Skills Assessment Playbook: 17 Skills, Sample Tasks & Scoring Rubrics","brand_fit":"CORE","our_subject":"Soft skills assessment","member_rowids":["2157"]},
    {"idea":"Hard Skills Assessment Guide: Testing In-Demand Hard Skills + Sample Questions per Skill","brand_fit":"CORE","our_subject":"Hard skills assessment","member_rowids":["2111","854"]},
    {"idea":"Problem-Solving Skills Assessment Toolkit: Test Scenarios, Live Coding Tasks & Interview Rubric","brand_fit":"CORE","our_subject":"Problem-solving assessment (technical)","member_rowids":["2256","2381"]},

    {"idea":"Structured Interview Toolkit: Role-by-Role Question Banks, Rubrics & Assessment-to-Interview Handoff","brand_fit":"CORE","our_subject":"Structured interview toolkit","member_rowids":["555","1905","1457","812","1553"]},
    {"idea":"Technical Interview Design Guide: Difficulty-Tiered Question Bank, Scorecard & Anti-Gaming Checklist","brand_fit":"CORE","our_subject":"Technical interview design","member_rowids":["2269"]},
    {"idea":"Peer & Collaborative Interview Toolkit: Question Templates, Evaluator Scorecard & Calibration Kit","brand_fit":"CORE","our_subject":"Peer / panel interview toolkit","member_rowids":["2213","1600"]},
    {"idea":"Pair Programming Interview Kit: Problem Sets, Dual-Dimension Rubric & Interviewer Setup","brand_fit":"CORE","our_subject":"Pair programming interview","member_rowids":["2455"]},

    {"idea":"Hackathon Hiring Evaluation Kit: Challenge Design, Scoring Rubric & Hiring-Decision Framework","brand_fit":"TRANSPLANT","our_subject":"Hackathon-based hiring","member_rowids":["1295","2298"]},

    {"idea":"Candidate Selection Scorecard: Weighting Skills Tests, Interviews & Checks into One Decision","brand_fit":"CORE","our_subject":"Final selection scorecard","member_rowids":["1888","2349"]},
    {"idea":"Application & Resume Review Scorecard: Weighted Criteria, Bias Flags & Skills-Test Integration","brand_fit":"CORE","our_subject":"Resume review scorecard","member_rowids":["181"]},
    {"idea":"Assessment Report Interpreter: A Recruiter's Guide to Reading Reports & Turning Them Into Interviews","brand_fit":"CORE","our_subject":"Reading assessment reports","member_rowids":["2313","616"]},
    {"idea":"How Non-Technical Hiring Managers Can Evaluate Developer / Tech Candidates","brand_fit":"CORE","our_subject":"Non-technical eval of developers","member_rowids":["1232","2441"]},

    {"idea":"The Skills-Based Hiring Implementation Checklist: 30-Step Rollout with Role-Level Templates","brand_fit":"CORE","our_subject":"Skills-based hiring rollout","member_rowids":["2300"]},
    {"idea":"Skills-Based Hiring Maturity Scorecard: Benchmark Your Process Across 5 Stages","brand_fit":"CORE","our_subject":"Hiring maturity benchmark","member_rowids":["2224"]},
    {"idea":"How Skills-Based Hiring Improves Retention: Assessment Accuracy vs. 12-Month Retention Data","brand_fit":"TRANSPLANT","our_subject":"Skills hiring & retention","member_rowids":["1999"]},

    {"idea":"High-Volume / Evergreen Hiring Assessment Playbook: Continuous Screening Funnel at Scale","brand_fit":"ADJACENT","our_subject":"High-volume screening","member_rowids":["2002","2463","1874"]},
    {"idea":"Startup Hiring Playbook: Screening 100+ Applicants with a Tiny Team Using Skills Tests","brand_fit":"ADJACENT","our_subject":"Startup / lean-team screening","member_rowids":["1929"]},
    {"idea":"Remote Hiring Assessment Playbook: Format, Proctoring & Which Competencies to Test Differently","brand_fit":"CORE","our_subject":"Remote hiring assessment","member_rowids":["926","2117","2440"]},
    {"idea":"Campus / Graduate Hiring Assessment Guide: Aptitude Tests & Coding Challenges at Scale","brand_fit":"TRANSPLANT","our_subject":"Campus / graduate hiring","member_rowids":["1187"]},
    {"idea":"How to Screen Freelancers & Project-Based Hires: Skills Assessment Framework + Brief Templates","brand_fit":"ADJACENT","our_subject":"Freelancer / contractor screening","member_rowids":["1857"]},

    {"idea":"Choosing a Skills Assessment Platform: Evaluation Framework, Feature Checklist & Vendor Comparison","brand_fit":"ADJACENT","our_subject":"Assessment platform buyer's guide","member_rowids":["464","1455"]},

    {"idea":"The Modern Hiring Manager's Assessment Playbook: Structured Interviews, Skills Tests & AI Reports","brand_fit":"CORE","our_subject":"Hiring manager assessment overview","member_rowids":["1068"]},
    {"idea":"Tech Talent Assessment Framework: Which Skills Tests for Common Technical Roles + Sample Questions","brand_fit":"CORE","our_subject":"Tech-talent multi-role framework","member_rowids":["1076"]},

    {"idea":"NLP Developer Skills Assessment Guide","brand_fit":"CORE","our_subject":"Role assessment — NLP developer","member_rowids":["885"]},
    {"idea":"AI Product Manager Skills Assessment Playbook","brand_fit":"CORE","our_subject":"Role assessment — AI product manager","member_rowids":["9","189"]},
    {"idea":"Financial Skills Roles Assessment Guide (Loan Officers, Credit Analysts, Advisors)","brand_fit":"CORE","our_subject":"Role assessment — financial roles","member_rowids":["2031","2161"]},
    {"idea":"Talent Acquisition Specialist Skills Assessment Framework","brand_fit":"CORE","our_subject":"Role assessment — TA specialist","member_rowids":["2065"]},
    {"idea":"Microsoft Office Skills Assessment Guide","brand_fit":"CORE","our_subject":"Role assessment — MS Office","member_rowids":["1841"]},
    {"idea":"Technical Writer Skills Assessment Blueprint","brand_fit":"CORE","our_subject":"Role assessment — technical writer","member_rowids":["1887"]},
    {"idea":"Marketing Manager Skills Assessment Playbook","brand_fit":"CORE","our_subject":"Role assessment — marketing manager","member_rowids":["1961"]},
    {"idea":"Marketing Roles Skills Assessment Starter Pack (Assistant, Coordinator, Analyst)","brand_fit":"TRANSPLANT","our_subject":"Role assessment — marketing junior roles","member_rowids":["2217"]},
    {"idea":"Admin & Receptionist Skills Assessment Guide","brand_fit":"CORE","our_subject":"Role assessment — admin/receptionist","member_rowids":["2084"]},
    {"idea":"WordPress Developer Skills Assessment Guide","brand_fit":"CORE","our_subject":"Role assessment — WordPress developer","member_rowids":["1892"]},
    {"idea":"Front-End Developer Skills Assessment Kit","brand_fit":"CORE","our_subject":"Role assessment — front-end developer","member_rowids":["952","960"]},
    {"idea":"Business Analyst Skills Assessment Kit","brand_fit":"CORE","our_subject":"Role assessment — business analyst","member_rowids":["1073"]},
    {"idea":"Android Developer Skills Assessment Kit","brand_fit":"CORE","our_subject":"Role assessment — Android developer","member_rowids":["1075"]},
    {"idea":"Software Engineer Structured Interview Kit","brand_fit":"CORE","our_subject":"Role assessment — software engineer","member_rowids":["58"]},
    {"idea":"Web Developer Technical Hiring Assessment Blueprint","brand_fit":"TRANSPLANT","our_subject":"Role assessment — web developer","member_rowids":["164","222"]},
    {"idea":"SEO Copywriter Screening Guide","brand_fit":"TRANSPLANT","our_subject":"Role assessment — SEO copywriter","member_rowids":["78"]},
    {"idea":"SQL Server DBA Assessment Guide","brand_fit":"TRANSPLANT","our_subject":"Role assessment — SQL Server DBA","member_rowids":["79"]},
    {"idea":"Chief of Staff Assessment Guide","brand_fit":"TRANSPLANT","our_subject":"Role assessment — chief of staff","member_rowids":["114"]},
    {"idea":"CTO Technical Assessment Design Guide","brand_fit":"TRANSPLANT","our_subject":"Role assessment — CTO","member_rowids":["115"]},
    {"idea":"Content Manager Assessment Guide","brand_fit":"TRANSPLANT","our_subject":"Role assessment — content manager","member_rowids":["116"]},
    {"idea":"Help Desk Technician Assessment Guide","brand_fit":"TRANSPLANT","our_subject":"Role assessment — help desk","member_rowids":["117"]},
    {"idea":"Customer Success Manager Assessment Guide","brand_fit":"TRANSPLANT","our_subject":"Role assessment — customer success manager","member_rowids":["161","193"]},
    {"idea":"Growth Marketer Hiring Assessment Kit","brand_fit":"TRANSPLANT","our_subject":"Role assessment — growth marketer","member_rowids":["162"]},
    {"idea":"SEO Specialist Hiring Assessment Guide","brand_fit":"TRANSPLANT","our_subject":"Role assessment — SEO specialist","member_rowids":["163"]},
    {"idea":"Accountant Pre-Employment Assessment Guide","brand_fit":"TRANSPLANT","our_subject":"Role assessment — accountant","member_rowids":["188"]},
    {"idea":"Auditor Pre-Employment Assessment Guide","brand_fit":"TRANSPLANT","our_subject":"Role assessment — auditor","member_rowids":["190"]},
    {"idea":"Cloud Engineer Technical Assessment Guide","brand_fit":"TRANSPLANT","our_subject":"Role assessment — cloud engineer","member_rowids":["191"]},
    {"idea":"Content Strategist Pre-Employment Assessment Guide","brand_fit":"TRANSPLANT","our_subject":"Role assessment — content strategist","member_rowids":["192"]},
    {"idea":"DevOps Engineer Technical Assessment Guide","brand_fit":"TRANSPLANT","our_subject":"Role assessment — DevOps engineer","member_rowids":["194"]},
    {"idea":"Ecommerce Manager Pre-Employment Assessment Guide","brand_fit":"TRANSPLANT","our_subject":"Role assessment — ecommerce manager","member_rowids":["195"]},
    {"idea":"Embedded Software Engineer Technical Assessment Guide","brand_fit":"TRANSPLANT","our_subject":"Role assessment — embedded SW engineer","member_rowids":["196"]},
    {"idea":"Flutter Developer Technical Assessment Guide","brand_fit":"TRANSPLANT","our_subject":"Role assessment — Flutter developer","member_rowids":["197"]},
    {"idea":"Manufacturing Specialist Pre-Employment Assessment Guide","brand_fit":"TRANSPLANT","our_subject":"Role assessment — manufacturing specialist","member_rowids":["198"]},
    {"idea":"Power Platform Developer Technical Assessment Guide","brand_fit":"TRANSPLANT","our_subject":"Role assessment — Power Platform developer","member_rowids":["199"]},
    {"idea":"Product Designer Hiring Assessment Guide","brand_fit":"TRANSPLANT","our_subject":"Role assessment — product designer","member_rowids":["200"]},
    {"idea":"React Native Developer Technical Assessment Guide","brand_fit":"TRANSPLANT","our_subject":"Role assessment — React Native developer","member_rowids":["201"]},
    {"idea":"Rust Developer Technical Assessment Guide","brand_fit":"TRANSPLANT","our_subject":"Role assessment — Rust developer","member_rowids":["202"]},
    {"idea":"Shopify Developer Technical Assessment Guide","brand_fit":"TRANSPLANT","our_subject":"Role assessment — Shopify developer","member_rowids":["203"]},
    {"idea":"Social Media Coordinator Pre-Employment Assessment Guide","brand_fit":"TRANSPLANT","our_subject":"Role assessment — social media coordinator","member_rowids":["204"]},
    {"idea":"System Analyst Pre-Employment Assessment Guide","brand_fit":"TRANSPLANT","our_subject":"Role assessment — system analyst","member_rowids":["206"]},
    {"idea":"Webmaster Technical Assessment Guide","brand_fit":"TRANSPLANT","our_subject":"Role assessment — webmaster","member_rowids":["207"]},
    {"idea":"Bootstrap Developer Assessment Guide","brand_fit":"TRANSPLANT","our_subject":"Role assessment — Bootstrap developer","member_rowids":["248"]},
    {"idea":"Selenium Automation Tester Hiring Assessment Guide","brand_fit":"TRANSPLANT","our_subject":"Role assessment — Selenium tester","member_rowids":["249"]},
    {"idea":"Operations Team Hiring Assessment Guide (6 Core Ops Roles)","brand_fit":"CORE","our_subject":"Role assessment — operations roles","member_rowids":["2020"]},
    {"idea":"Learning Agility Assessment for Engineers","brand_fit":"CORE","our_subject":"Role assessment — engineer learning agility","member_rowids":["2450"]},
]

seen = set()
out = []
for c in clusters:
    ids = [r for r in c["member_rowids"] if r not in seen]
    for r in ids:
        seen.add(r)
    if not ids:
        continue
    c["member_rowids"] = ids
    out.append(c)

all_ids = ["317","2029","324","329","885","361","9","367","2256","2031","401","413","417","454","464","469","470","472","2033","485","1143","1149","2269","530","1813","895","1814","1152","1364","2042","537","1376","1170","1381","1173","1539","2057","1837","1551","1553","1841","2065","1187","1189","1392","1845","2068","1857","555","1401","1405","1872","1873","1874","1410","1411","1600","1602","1887","1888","1889","1890","1892","2084","2086","1232","1905","2095","1918","1921","1929","1933","2096","926","1947","1950","1951","1958","1961","2108","2111","2117","58","64","1295","1298","1448","1455","1457","1994","1999","2002","2006","2009","2010","2020","2129","2131","2132","2133","78","79","616","952","960","1325","1327","2139","2146","2157","2161","2166","2171","2175","2296","2298","2300","114","115","116","117","645","812","1001","1010","2200","2205","2211","2213","2217","2224","2313","2321","161","162","163","164","181","188","189","190","191","192","193","194","195","196","197","198","199","200","201","202","203","204","206","207","214","222","715","854","1068","1073","1075","1076","2349","2354","2361","2363","248","249","2381","2415","2435","2439","2440","2441","2445","2449","2450","2455","2463"]

missing = [r for r in all_ids if r not in seen]
extra = [r for r in seen if r not in all_ids]
print("clusters:", len(out))
print("covered:", len(seen), "of", len(set(all_ids)), "| input distinct:", len(set(all_ids)), "| input total:", len(all_ids))
print("MISSING:", missing)
print("EXTRA:", extra)

if not missing and not extra:
    with open("/Users/devanshasawa/Desktop/SEO by Devansh/Backlink gets Automated/projects/testlify/asset-engine/competitor-study/_work/g3_ideas/guide-pillar.jsonl","w") as f:
        for c in out:
            f.write(json.dumps(c)+"\n")
    print("WROTE", len(out), "ideas")
else:
    print("NOT WRITTEN - fix coverage")
