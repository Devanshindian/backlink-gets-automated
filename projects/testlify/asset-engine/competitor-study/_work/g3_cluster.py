#!/usr/bin/env python3
import csv, json

rows = {}
with open('g3_in/free-test-assessment.tsv') as f:
    for x in csv.DictReader(f, delimiter='\t'):
        rows[x['RowID']] = (x['BrandFit'], x['Asset'])

# (idea, our_subject, [rowids]); brand_fit = dominant among members
C = [
 # ===== AI / ML / NLP / Deep learning skills tests =====
 ("Free AI & Machine Learning Skills Test for Hiring","Skills tests — AI & machine learning",
  ["1791","881","1627","1116","1793","2","1117","1628","2028","2252","743","7","1135"]),
 ("Free NLP Engineer Skills Test","Skills tests — AI & machine learning",["5","1795"]),
 ("Free AI Engineer Skills Assessment","Skills tests — AI & machine learning",["2255"]),
 ("Free Deep Learning Skills Test (PyTorch/TensorFlow)","Skills tests — AI & machine learning",["13"]),
 ("Free AI-Assisted Developer Skills Assessment","Skills tests — AI & machine learning",["2398"]),

 # ===== Data / analytics =====
 ("Free Data Science & Analytics Skills Test","Skills tests — data & analytics",["930"]),
 ("Free Data Analysis Skills Test for Hiring","Skills tests — data & analytics",["71","1986","1697"]),
 ("Free Python Data Science Skills Test","Skills tests — data & analytics",["1672","1751"]),
 ("Free Data Modeling Skills Test (ER Diagram Task)","Skills tests — data & analytics",["138"]),
 ("Free Big Data / Data Engineering Screening Guide","Skills tests — data & analytics",["1074"]),
 ("Free Power BI Skills Test","Skills tests — data & analytics",["93"]),

 # ===== Programming languages / frameworks (each language = distinct build) =====
 ("Free Python Developer Skills Test for Hiring","Skills tests — coding & technical",["1637","1832","52","1037","1038"]),
 ("Free Java Developer Skills Test for Hiring","Skills tests — coding & technical",
  ["1134","1169","1862","27","1312","1673","1743","1762","1763","1036"]),
 ("Free JavaScript Developer Skills Test","Skills tests — coding & technical",["45","1702","1744"]),
 ("Free C# / .NET Developer Skills Test","Skills tests — coding & technical",["1265","133","1742","1044"]),
 ("Free ASP.NET MVC Developer Test","Skills tests — coding & technical",["1311"]),
 ("Free C Programming Skills Test","Skills tests — coding & technical",["1181"]),
 ("Free Embedded C Skills Test (RTOS vs Bare-Metal)","Skills tests — coding & technical",["139"]),
 ("Free C++ Developer Skills Test","Skills tests — coding & technical",["1212","1983"]),
 ("Free PHP Developer Skills Test","Skills tests — coding & technical",["28","1750"]),
 ("Free Ruby Developer Skills Test","Skills tests — coding & technical",["908"]),
 ("Free Ruby on Rails Developer Test","Skills tests — coding & technical",["932"]),
 ("Free Node.js Developer Skills Test","Skills tests — coding & technical",["1314","1033"]),
 ("Free TypeScript Developer Skills Test","Skills tests — coding & technical",["1754"]),
 ("Free React Developer Skills Test","Skills tests — coding & technical",["1851","72","1674","1039"]),
 ("Free Angular Developer Skills Test","Skills tests — coding & technical",["1842","1226","1737","1738"]),
 ("Free Vue.js Developer Skills Test","Skills tests — coding & technical",["1755"]),
 ("Free HTML/CSS & Web Developer Skills Test","Skills tests — coding & technical",["1700","1756"]),
 ("Free WordPress Developer Skills Test","Skills tests — coding & technical",["1864","1703"]),
 ("Free Software Engineer Skills Test (DS&A, language-agnostic)","Skills tests — coding & technical",["1917","1648"]),
 ("Free Swift / iOS Developer Skills Test","Skills tests — coding & technical",["1629"]),
 ("Free SQL Skills Test for Hiring","Skills tests — coding & technical",["1630","54","1228","1984","1774"]),
 ("Free MS SQL Server / T-SQL Skills Test","Skills tests — coding & technical",["1631"]),
 ("Free QA Automation Skills Test (Selenium/Cypress/Playwright)","Skills tests — coding & technical",["1035"]),
 ("Free QA Engineer Skills Test","Skills tests — coding & technical",["1880"]),
 ("Free SAP SD Consultant/Analyst Assessment","Skills tests — coding & technical",["1042"]),
 ("Free Senior Network Engineer Skills Test","Skills tests — coding & technical",["1043"]),
 ("Free Linux & Systems / SysAdmin Skills Test","Skills tests — coding & technical",["1658"]),
 ("Free AWS Cloud Skills Test for Hiring","Skills tests — coding & technical",["1822","1027","1741"]),
 ("Free Cyber Security Skills Screener","Skills tests — coding & technical",["1028"]),
 ("Free Salesforce Skills Test","Skills tests — coding & technical",["947"]),
 ("Free Computer Programmer Aptitude Test (with coding)","Skills tests — coding & technical",["135"]),
 ("Free Technical Aptitude Test for Engineering Graduates","Skills tests — coding & technical",["1229"]),

 # ===== Office / productivity software =====
 ("Free Excel Skills Test for Hiring","Skills tests — office & productivity software",
  ["24","1644","1247","1305","2204","2243","1883"]),
 ("Free Advanced Excel Skills Test","Skills tests — office & productivity software",["1865","2242"]),
 ("Free MS Word Skills Test","Skills tests — office & productivity software",["1749"]),
 ("Free MS Office Skills Test (Word + Excel)","Skills tests — office & productivity software",["1748","1032"]),
 ("Free Basic Computer Skills Test for Hiring","Skills tests — office & productivity software",["1195","548","242"]),
 ("Free Typing Speed & Accuracy Test","Skills tests — office & productivity software",["1861","96","141"]),
 ("Free Data-Entry Speed & Accuracy Test","Skills tests — office & productivity software",["1987"]),

 # ===== Design / creative =====
 ("Free UX/UI Design Skills Test","Skills tests — design & creative",["1823"]),
 ("Free Graphic Designer Skills Test","Skills tests — design & creative",["70","1026"]),

 # ===== Cognitive / aptitude / reasoning =====
 ("Free Cognitive Ability Test for Hiring","Skills tests — cognitive & aptitude",
  ["1132","1172","134","1030","578","583","603"]),
 ("Free General Mental Ability Test","Skills tests — cognitive & aptitude",["1141"]),
 ("Free General Aptitude Test for Hiring","Skills tests — cognitive & aptitude",
  ["34","1246","1261","132","236","1739"]),
 ("Free Numerical Reasoning Test","Skills tests — cognitive & aptitude",["1213","1894","140"]),
 ("Free Quantitative Aptitude Test","Skills tests — cognitive & aptitude",["1186"]),
 ("Free Logical Reasoning Test","Skills tests — cognitive & aptitude",["1192","1227","91","1745"]),
 ("Free Verbal Reasoning Test","Skills tests — cognitive & aptitude",["142","243"]),
 ("Free Abstract Reasoning Test","Skills tests — cognitive & aptitude",["1645"]),
 ("Free Critical Thinking Test","Skills tests — cognitive & aptitude",["1818","19"]),
 ("Free Problem-Solving Skills Test","Skills tests — cognitive & aptitude",["1806","46"]),
 ("Free Analytical Skills Test","Skills tests — cognitive & aptitude",["1025"]),
 ("Free Fluid Intelligence Test","Skills tests — cognitive & aptitude",["44"]),
 ("Free Mechanical Reasoning Test","Skills tests — cognitive & aptitude",["1850"]),
 ("Free Attention to Detail Test","Skills tests — cognitive & aptitude",["1839","1740"]),
 ("Free Concentration & Attention Test","Skills tests — cognitive & aptitude",["706"]),
 ("Free Data Interpretation + Numerical + Spatial Reasoning Test","Skills tests — cognitive & aptitude",["137"]),
 ("Free Admin & Office Roles Aptitude Test","Skills tests — cognitive & aptitude",["905"]),
 ("Free Graphic Designer Aptitude Screener","Skills tests — cognitive & aptitude",["1026" if False else "x1"]),

 # ===== Language / communication =====
 ("Free Spoken English / English Proficiency Test (CEFR)","Skills tests — language & communication",
  ["1130","1155","1270","1316","907","974","701","996","2110","90"]),
 ("Language Proficiency Hiring Guide (CEFR levels by role)","Skills tests — language & communication",
  ["1907"]),
 ("Free Business English Proficiency Test","Skills tests — language & communication",["1698"]),
 ("Free Communication Skills Assessment","Skills tests — language & communication",["1154","1825"]),
 ("Free Grammar & Written Communication Test","Skills tests — language & communication",["540","545","1240","931"]),
 ("Free Basic Skills Test (Grammar+Spelling+Math+Verbal)","Skills tests — language & communication",["553"]),

 # ===== Sales & marketing roles =====
 ("Free Sales Skills Assessment","Skills tests — sales & marketing roles",
  ["35","1647","1286","2080","1041","1704","639","1235"]),
 ("Free Sales Manager / Sales & Marketing Manager Assessment","Skills tests — sales & marketing roles",["2143","2106"]),
 ("Free Marketing Manager Skills Assessment","Skills tests — sales & marketing roles",["2245"]),
 ("Free Digital Marketing Skills Test","Skills tests — sales & marketing roles",["38","1267"]),
 ("Free PPC Advertising Skills Test","Skills tests — sales & marketing roles",["1840"]),
 ("Free SEO Skills Test for Hiring","Skills tests — sales & marketing roles",["53","948","2248"]),
 ("Free Technical SEO Skills Test","Skills tests — sales & marketing roles",["1882"]),
 ("Free SEO Copywriting Skills Test","Skills tests — sales & marketing roles",["1944"]),
 ("Free Marketing Analytics Aptitude Test","Skills tests — sales & marketing roles",["1746"]),
 ("Free Copywriting Skills Test","Skills tests — sales & marketing roles",["42"]),
 ("Free Content Strategy Skills Test","Skills tests — sales & marketing roles",["136"]),
 ("Free Content & Writing Skills Screener","Skills tests — sales & marketing roles",["945"]),

 # ===== Customer-facing / admin / ops roles =====
 ("Free Customer Service Skills Test","Skills tests — customer-facing & support roles",["43","976","1643"]),
 ("Free Call Center Candidate Assessment Guide","Skills tests — customer-facing & support roles",["1321"]),
 ("Free Receptionist & Front-Office Skills Test","Skills tests — admin & operations roles",["1040","1752"]),
 ("Free Office Administrator Skills Test","Skills tests — admin & operations roles",["1034"]),
 ("Free Administrative Assistant Skills Test","Skills tests — admin & operations roles",["1641"]),
 ("Free Executive Assistant Skills Screener","Skills tests — admin & operations roles",["1029"]),

 # ===== Management / PM / agile roles =====
 ("Free Project Management Skills Test","Skills tests — management & PM roles",["1866","29","1660"]),
 ("Free Project Management Aptitude Test","Skills tests — management & PM roles",["1659"]),
 ("Free Scrum Master Skills Test","Skills tests — management & PM roles",["1881"]),
 ("Free Product Owner Skills Test","Skills tests — management & PM roles",["1943"]),
 ("Free Product Manager Skills Assessment","Skills tests — management & PM roles",["2247","2226"]),
 ("Free Leadership & People Management Skills Test/SJT","Skills tests — management & PM roles",["1879","1945","1290"]),

 # ===== HR / business / engineering / soft-skill roles =====
 ("Free Talent Acquisition Skills Assessment","Skills tests — HR & recruiting roles",["1852"]),
 ("Free HR Fundamentals Skills Test","Skills tests — HR & recruiting roles",["1985"]),
 ("Free Business Analyst Skills Assessment","Skills tests — business & finance roles",["1245"]),
 ("Free Auditor Aptitude Test","Skills tests — business & finance roles",["1266"]),
 ("Free Mechanical Engineer Skills & Aptitude Test","Skills tests — engineering roles",["1289","1747"]),
 ("Free Time Management Skills Test","Skills tests — soft skills",["1826"]),

 # ===== Personality / psychometric / behavioural =====
 ("Free DISC Personality Assessment","Personality & psychometric tests",["1916","1904"]),
 ("Free Big Five (OCEAN) Personality Test","Personality & psychometric tests",["1938","549","1906","165"]),
 ("Free Enneagram Personality Assessment","Personality & psychometric tests",["1939"]),
 ("Free Personality Fit Assessment for Hiring","Personality & psychometric tests",["1302","1315"]),
 ("Free Behavioral Assessment Screener","Personality & psychometric tests",["759","793"]),
 ("Free Emotional Intelligence Screener","Personality & psychometric tests",["572","636","637"]),
 ("Free Candidate Motivation Assessment","Personality & psychometric tests",["1878"]),
 ("Free Culture Add / Culture-Fit Assessment","Personality & psychometric tests",["1828"]),
 ("Cultural Fit Assessment in Hiring: Which Tools Have Evidence?","Personality & psychometric tests",["388"]),
 ("(Unclassified) strong — no obvious gap","Personality & psychometric tests",["1863"]),
 ("Free Job Fit Assessment (skills+values+context)","Personality & psychometric tests",["2210"]),

 # ===== Cross-role screeners / multi-skill bundles =====
 ("Free Entry-Level Hiring Skills Screener (grammar+reasoning+math)","Skills tests — multi-skill screeners",
  ["700","581"]),

 # ===== Test library / hub (one buildable directory) =====
 ("Testlify Free Assessment Library (role tests + sample Qs)","Assessment library / test hub",
  ["1801","1287","95","88","232","2377"]),

 # ===== Buyer guides / platform comparisons (content, not a test) =====
 ("Skills Assessment Platform Comparison (independent feature matrix)","Buyer guides — assessment platforms",
  ["2027","497","14","898","2049","1859","1884","59","82","87","933","936","988","916","2306","2307",
   "2319","2335","2336","2419","2386","2424","2428","2452","1053","1057","1065","1079","1087","1088",
   "1415","1231"]),
 ("Cognitive Aptitude Test Comparison (CCAT vs Wonderlic vs general)","Buyer guides — assessment platforms",
  ["528","531","570","582"]),
 ("Personality Assessment Tools Compared (Big5 vs DISC vs MBTI)","Buyer guides — assessment platforms",
  ["1128","1177","1160","1163","1234","1208","1284","1300","1249","538","92","102","573","1334"]),
 ("Psychometric / Behavioral Assessment Guide (validity-first)","Buyer guides — assessment platforms",
  ["1190","1216","1256","1320"]),
 ("Leadership Assessment Tools Compared","Buyer guides — assessment platforms",["1250","939"]),

 # ===== Decision guides / frameworks (which test for which role) =====
 ("Pre-Employment Test-Type & Role Selector Guide","Decision guides — test selection",
  ["1799","584","1205","94","86","235","954","800","1296","1271","1014","1017","1326","1275",
   "935","1294","2015","1281","89","787","978"]),
 ("Cognitive / Critical-Thinking Test Selector by Role","Decision guides — test selection",
  ["638"]),
 ("How to Design / Build a Skills Assessment (framework + template)","Decision guides — test selection",
  ["1196","924","951","1297","1078"]),
 ("Why Skills-Based Hiring Works (data-backed report)","Decision guides — test selection",
  ["1552","1263","1924"]),
 ("Assessment Validity & Reliability Checklist","Decision guides — test selection",
  ["119","722","906","1089","1095","1252","1215","26","166","2467","1491"]),
 ("Pre-Hire Skills-Gap Assessment Framework","Decision guides — test selection",
  ["1119","1238","1854"]),
 ("Pre-Employment Assessment Stack Builder (test-combination selector)","Decision guides — test selection",
  ["1133","1191","1193"]),
 ("Aptitude Tests in Hiring: Validity & When-to-Use Guide","Decision guides — test selection",
  ["1158"]),
 ("Virtual Assessment Center for Hiring (recruiter guide)","Decision guides — test selection",
  ["1164","1182"]),
 ("Live Walk-Through of a Skills Assessment (capability-testing demo)","Decision guides — test selection",
  ["2056"]),
 ("Microsoft Office Skills: Which to Test by Role (guide + samples)","Decision guides — test selection",
  ["911","799","707"]),
 ("Assessing Leadership Potential in Hiring (manager-track screening)","Decision guides — test selection",
  ["1242"]),
 ("One Test, Many Uses: Hiring + Onboarding Benchmark Guide","Decision guides — test selection",
  ["1243"]),
 ("The Science Behind Cognitive Assessments in Hiring","Decision guides — test selection",
  ["705"]),
]

# strip placeholder buckets that were toggled off
C = [(i,s,[r for r in ids if not r.startswith("x")]) for (i,s,ids) in C]
C = [c for c in C if c[2]]

# coverage / dup check
seen=set(); dup=[]
for _,_,ids in C:
    for r in ids:
        if r in seen: dup.append(r)
        seen.add(r)
missing=[r for r in rows if r not in seen]
extra=[r for r in seen if r not in rows]
print("clusters:",len(C),"dups:",dup,"missing:",len(missing),missing,"extra:",extra)

assert not dup and not missing and not extra, "coverage failure"

def dominant_fit(ids):
    from collections import Counter
    c=Counter(rows[r][0] for r in ids)
    # tie-break preference: CORE > TRANSPLANT > ADJACENT
    order={'CORE':0,'TRANSPLANT':1,'ADJACENT':2}
    return sorted(c.items(), key=lambda kv:(-kv[1], order.get(kv[0],9)))[0][0]

with open('g3_ideas/free-test-assessment.jsonl','w') as out:
    for idea,subj,ids in C:
        obj={"idea":idea,"brand_fit":dominant_fit(ids),"our_subject":subj,
             "member_rowids":[str(r) for r in ids]}
        out.write(json.dumps(obj,ensure_ascii=False)+"\n")

# verify written file covers exactly all rows once
chk=set(); n=0
with open('g3_ideas/free-test-assessment.jsonl') as f:
    for line in f:
        n+=1
        for r in json.loads(line)["member_rowids"]:
            assert r not in chk, f"dup {r}"
            chk.add(r)
print("WROTE",n,"ideas; covered",len(chk),"rows; all covered:",chk==set(rows))
