import sys, re, csv, os, time, numpy as np
csv.field_size_limit(1<<24)
sys.path.insert(0,"projects/testlify/asset-engine/clubbed/_work")
import rag
BASE="projects/testlify/asset-engine/clubbed"; IDX=BASE+"/_work/content-index"
REVIEW=BASE+"/clubbed-ideas-review.csv"; TOPK=15
LOCALES={"ar","pl","it","pt-br","no","ja","da","es","de","el","sv","nl","fr","pt","zh","ko","ru","tr","hi","id","th","vi"}
def foreign(u):
    m=re.match(r"https?://(?:www\.)?testlify\.com/([^/]+)/",u); return bool(m and m.group(1).lower() in LOCALES)
Vt,Mt=rag.load_vecs(IDX+"/title"); Vb,Mb=rag.load_vecs(IDX+"/body")
allurls=[m["url"] for m in Mt]; uidx={u:i for i,u in enumerate(allurls)}
body_uidx=np.array([uidx[m["url"]] for m in Mb])
cmap={};tmap={}
for r in csv.DictReader(open("projects/testlify/content-database.csv",encoding="utf-8")):
    cmap[r["URL"]]=r.get("Full content","") or ""; tmap[r["URL"]]=r.get("Title","") or ""
def query_text(asset):
    a=re.sub(r"\([^)]*\)"," ",asset or ""); return re.sub(r"\s+"," ",a).strip() or "untitled"
def retrieve(qtext,topk=TOPK):
    Q=rag.embed([qtext],"query"); Q=Q/(np.linalg.norm(Q,axis=1,keepdims=True)+1e-9); q=Q[0]
    tsim=Vt@q; bsim=Vb@q
    bb=np.full(len(allurls),-1.0,dtype=np.float32); np.maximum.at(bb,body_uidx,bsim)
    blended=rag.ALPHA*tsim+(1-rag.ALPHA)*bb
    cand=[allurls[k] for k in np.argsort(blended)[::-1] if not foreign(allurls[k])][:30]
    def mkdoc(u):
        d=(tmap[u][:200]+"\n"+cmap[u])[:rag.RERANK_DOC_CHARS].replace("\x00"," ").strip(); return d or "(no content)"
    docs=[mkdoc(u) for u in cand]
    try: order=rag.rerank(qtext,docs,min(topk,len(cand))); return [(cand[i],sc) for i,sc in order]
    except Exception as e: print("   fallback:",str(e)[:50],flush=True); return [(u,0.0) for u in cand[:topk]]
rows=list(csv.DictReader(open(REVIEW,encoding="utf-8"))); fields=list(rows[0].keys())
done=0
for n,r in enumerate(rows):
    if len([x for x in r["RAG candidates"].split(";") if x.strip()])>=TOPK: done+=1; continue
    res=retrieve(query_text(r["Asset"]))
    r["RAG candidates"]="; ".join(f"{tmap[u]} — {u} ({sc:.2f})" for u,sc in res)
    done+=1; time.sleep(1.0)
    if done%25==0:
        with open(REVIEW,"w",newline="",encoding="utf-8") as f:
            w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(rows)
        print(f"  {done}/{len(rows)} (saved)",flush=True)
with open(REVIEW,"w",newline="",encoding="utf-8") as f:
    w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(rows)
print("DONE top-15 retrieval:",done,flush=True)
