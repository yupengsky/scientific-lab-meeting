#!/usr/bin/env python3
"""Deterministic structural validation for the expertise-first protocol."""
from __future__ import annotations
import hashlib, re, sys, tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AGENTS = {"topic_advisor":("gpt-5.6-sol","low"), "literature_scout":("gpt-5.6-luna","low"), "librarian":("gpt-5.6-luna","low"), "literature_mapper":("gpt-5.6-terra","low"), "candidate_framer":("gpt-5.6-terra","low"), "novelty_auditor":("gpt-5.6-terra","low"), "hamming":("gpt-5.6-terra","low"), "medawar":("gpt-5.6-terra","low"), "platt":("gpt-5.6-sol","low"), "alon":("gpt-5.6-terra","low"), "skeptical_pi":("gpt-5.6-sol","low")}
STAGES = ["WORKSPACE INITIALIZATION","BROAD FIELD DISCOVERY","STRUCTURAL COVERAGE EXPANSION","FIELD SATURATION GATE","HIGH-LEVERAGE EVIDENCE SELECTION + PAPER CARDS","EVIDENCE IDENTITY / DEPTH REPAIR","DEFINITIVE PROBLEM MAP","Uxx-SPECIFIC LITERATURE SATURATION","Uxx SATURATION GATE","CANDIDATE GENERATION + SCREENING","CANDIDATE PRIOR-ART / NOVELTY SATURATION","ROUND-1 BLIND CRITICS","REVIEW INTEGRITY + TARGETED REBUTTAL","DECISION-CRITICAL VERIFICATION + PI READINESS","INDEPENDENT SKEPTICAL PI","PORTFOLIO + PILOT SCARCITY","FINAL VALIDATION"]
IDS = ["WORKSPACE_INITIALIZATION","BROAD_FIELD_DISCOVERY","STRUCTURAL_COVERAGE_EXPANSION","FIELD_SATURATION_GATE","HIGH_LEVERAGE_EVIDENCE_SELECTION_PAPER_CARDS","EVIDENCE_IDENTITY_DEPTH_REPAIR","DEFINITIVE_PROBLEM_MAP","UXX_SPECIFIC_LITERATURE_SATURATION","UXX_SATURATION_GATE","CANDIDATE_GENERATION_SCREENING","CANDIDATE_PRIOR_ART_NOVELTY_SATURATION","ROUND_1_BLIND_CRITICS","REVIEW_INTEGRITY_TARGETED_REBUTTAL","DECISION_CRITICAL_VERIFICATION_PI_READINESS","INDEPENDENT_SKEPTICAL_PI","PORTFOLIO_PILOT_SCARCITY","FINAL_VALIDATION"]
CRITICS={"Hamming":{"IMPORTANT","QUESTIONABLE","LOW-VALUE"},"Medawar":{"TRACTABLE","WEAK ATTACK","CURRENTLY INSOLUBLE"},"Platt":{"PURSUE","REDESIGN","KILL"},"Alon":{"PURSUE","PILOT FIRST","QUESTIONABLE","KILL"}}
NOVELTY={"NEW QUESTION","UNRESOLVED EXISTING QUESTION","REPLICATION / RECONCILIATION","NEW DISCRIMINATOR FOR OLD QUESTION","NEW REGIME / BOUNDARY CONDITION","METHOD / MEASUREMENT ADVANCE"}

class Validator:
 def __init__(self): self.errors=[]
 def error(self,x): self.errors.append(x)
 def text(self,p):
  try:return (ROOT/p).read_text(encoding="utf-8")
  except OSError as e:self.error(f"cannot read {p}: {e}");return ""
 @staticmethod
 def topic_snapshot(): return "sha256:"+hashlib.sha256((ROOT/"TOPIC.md").read_bytes()).hexdigest()
 @staticmethod
 def section(text, heading):
  m=re.search(rf"^## {re.escape(heading)}\s*$([\s\S]*?)(?=^## |\Z)",text,re.M);return m.group(1).strip() if m else ""
 def completed(self,state):
  got={}
  for mark,n,name in re.findall(r"^- \[([ xX])\] (\d+)\. (.+)$",state,re.M): got[int(n)]=(mark.lower()=="x",name)
  for i,name in enumerate(STAGES):
   if i not in got:self.error(f"RUN_STATE lacks stage {i}")
   elif got[i][1]!=name:self.error(f"RUN_STATE stage {i} name differs from WORKFLOW")
  done={i for i,v in got.items() if v[0]}
  if any(any(j not in done for j in range(i)) for i in done):self.error("RUN_STATE has non-contiguous completed stages")
  return done
 def validate_agents(self):
  config={}
  try:config=tomllib.loads(self.text(".codex/config.toml"))
  except tomllib.TOMLDecodeError as e:self.error(f"invalid TOML .codex/config.toml: {e}")
  roles=config.get("agents",{})
  for name,(model,effort) in AGENTS.items():
   ref=roles.get(name,{}).get("config_file")
   if ref!=f"agents/{name}.toml":self.error(f"agent {name} lacks exact config_file routing")
   path=ROOT/".codex/agents"/f"{name}.toml"
   try:data=tomllib.loads(path.read_text(encoding="utf-8-sig"))
   except Exception as e:self.error(f"invalid agent TOML {name}: {e}");continue
   if data.get("model")!=model:self.error(f"agent {name} has unexpected model: {data.get('model')}")
   if data.get("model_reasoning_effort")!=effort:self.error(f"agent {name} has unexpected reasoning effort: {data.get('model_reasoning_effort')}")
 def coverage(self,done):
  text=self.text("literature/COVERAGE.md")
  for h in ("Field-level explanatory families","Uxx-specific coverage"):
   if f"## {h}" not in text:self.error(f"COVERAGE lacks section: {h}")
  if 3 in done:
   for block in re.split(r"^### Family:",text,flags=re.M)[1:]:
    for f in ("EXPLANATORY FAMILY","PRIMARY SUPPORT","INDEPENDENT SUPPORT","COMPETING ACCOUNT","CONTRADICTORY / LIMITING EVIDENCE","DIRECT FOLLOW-UPS / REBUTTALS","RECENT CAPABILITY CHANGE","READING DEPTH","REMAINING GAP","STATUS"):
     if not re.search(rf"^{re.escape(f)}:\s*\S",block,re.M):self.error(f"FIELD COVERAGE missing {f}")
    if re.search(r"^STATUS:\s*READY",block,re.M) and re.search(r"^(PRIMARY SUPPORT|COMPETING ACCOUNT|READING DEPTH):\s*(NOT READY|NONE)\b",block,re.M):self.error("FIELD SATURATION claimed while a major structural gap is NOT READY")
  return text
 def cards(self,done):
  verified=[]
  for p in (ROOT/"literature/cards").glob("*.md"):
   if p.name=="TEMPLATE.md":continue
   t=p.read_text(encoding="utf-8")
   m=re.search(r"^\*\*IDENTITY_STATUS:\*\*\s*(.+)$",t,re.M)
   if not m or m.group(1).strip() not in {"VERIFIED","MISMATCH","UNRESOLVED"}:self.error(f"{p.relative_to(ROOT)} missing or invalid IDENTITY_STATUS")
   elif m.group(1).strip()=="VERIFIED":verified.append(p.name)
  return verified
 def candidates(self,done,verified):
  ids=[]
  for p in (ROOT/"candidates").glob("C[0-9][0-9][0-9].md"):
   ids.append(p.stem);t=p.read_text(encoding="utf-8")
   for f in ("NOVELTY TYPE","CLOSEST PRIOR WORK","WHAT PRIOR WORK ALREADY DID","WHAT THIS CANDIDATE ADDS","WHY THE DIFFERENCE IS SCIENTIFICALLY MATERIAL","NOVELTY SATURATION"):
    if not re.search(rf"^\*\*{re.escape(f)}:\*\*\s*\S",t,re.M):self.error(f"{p.relative_to(ROOT)} missing {f}")
   m=re.search(r"^\*\*NOVELTY TYPE:\*\*\s*(.+)$",t,re.M)
   if m and not any(x in m.group(1) for x in NOVELTY):self.error(f"{p.relative_to(ROOT)} invalid novelty classification")
   if 10 in done and not re.search(r"^\*\*NOVELTY SATURATION:\*\*\s*PASS\s*$",t,re.M):self.error(f"{p.relative_to(ROOT)} lacks novelty saturation PASS")
   for card in re.findall(r"literature/cards/([\w.-]+\.md)",t):
    if card not in verified:self.error(f"{p.relative_to(ROOT)} admits non-VERIFIED card into eligible evidence: {card}")
   if 11 in done:
    for role,verdicts in CRITICS.items():
     s=self.section(t,role);v=re.search(r"^VERDICT:\s*(.+)$",s,re.M);c=re.search(r"^CONFIDENCE:\s*(.+)$",s,re.M);r=re.search(r"^CONFIDENCE RATIONALE:\s*\S",s,re.M);n=re.search(r"^NEEDS_VERIFICATION:\s*(.+)$",s,re.M)
     if not v or v.group(1).strip() not in verdicts:self.error(f"{p.relative_to(ROOT)} invalid {role} verdict")
     if not c or c.group(1).strip() not in {"LOW","MEDIUM","HIGH"}:self.error(f"{p.relative_to(ROOT)} invalid confidence vocabulary")
     if not r:self.error(f"{p.relative_to(ROOT)} missing confidence rationale")
     if n and n.group(1).strip()!="NONE" and not all(x in s for x in ("SOURCE:","EXACT CLAIM TO VERIFY:","WHY IT COULD CHANGE THE VERDICT:")):self.error(f"{p.relative_to(ROOT)} invalid structured NEEDS_VERIFICATION")
   pi=self.section(t,"Skeptical PI");d=re.search(r"^DECISION:\s*(.+)$",pi,re.M)
   if d and d.group(1).strip()=="PILOT ONLY":
    for f in ("WHAT THE PILOT MUST DISTINGUISH","STOP CRITERION","GO CRITERION"):
     if not re.search(rf"^{re.escape(f)}:\s*(?!PENDING\b|NOT APPLICABLE)[^\n]+",pi,re.M):self.error(f"{p.relative_to(ROOT)} PILOT ONLY requires {f}")
   if d and d.group(1).strip()=="KILL":
    allowed="NOT APPLICABLE — fatal flaw is not pilot-resolvable"
    for f in ("CHEAPEST DECISIVE PILOT","WHAT THE PILOT MUST DISTINGUISH","STOP CRITERION","GO CRITERION"):
     m=re.search(rf"^{re.escape(f)}:\s*(.+)$",pi,re.M)
     if not m:self.error(f"{p.relative_to(ROOT)} KILL missing {f}")
     elif m.group(1).strip()=="PENDING":self.error(f"{p.relative_to(ROOT)} KILL has pending {f}")
  return ids
 def run(self):
  for p in ("AGENTS.md","WORKFLOW.md","README.md","TOPIC.md","RUN_STATE.md","literature/INDEX.md","literature/COVERAGE.md","literature/PROBLEM_MAP.md","literature/cards/TEMPLATE.md","candidates/TEMPLATE.md","candidates/SCREENING.md","outputs/README.md"):
   if not (ROOT/p).is_file():self.error(f"missing required file: {p}")
  self.validate_agents(); state=self.text("RUN_STATE.md");done=self.completed(state)
  status=(re.search(r"^STATUS:\s*(.+)$",state,re.M) or [None,""])[1].strip()
  current=(re.search(r"^CURRENT_STAGE:\s*(.+)$",state,re.M) or [None,""])[1].strip()
  if status not in {"NOT_STARTED","IN_PROGRESS","COMPLETE","BLOCKED"}:self.error("invalid STATUS")
  if status=="NOT_STARTED" and (done or current!=IDS[0]):self.error("NOT_STARTED state is not clean")
  if status=="NOT_STARTED" and "Replace this line with one broad scientific research direction" not in self.text("TOPIC.md"):self.error("NOT_STARTED TOPIC.md is not the generic placeholder")
  if status!="NOT_STARTED":
   snap=(re.search(r"^TOPIC_SNAPSHOT:\s*(.+)$",state,re.M) or [None,""])[1].strip()
   if snap!=self.topic_snapshot():self.error("TOPIC CHANGED — CLEAN START BRANCH REQUIRED")
  cov=self.coverage(done); verified=self.cards(done); ids=self.candidates(done,verified)
  if 8 in done:
   for node in re.findall(r"^#{1,6} (U\d+)\b",self.text("literature/PROBLEM_MAP.md"),re.M):
    block=(re.search(rf"^### Uxx: {node}\b([\s\S]*?)(?=^### |\Z)",cov,re.M) or [""])[0]
    for field in ("SUPPORTING EVIDENCE","COMPETING EXPLANATION","CONTRADICTORY / LIMITING EVIDENCE","DIRECT FOLLOW-UPS / REBUTTALS","RECENT CAPABILITY CHANGE","EVIDENCE DEPTH","TARGETED SEARCH RESULT","SATURATION","READY / NOT READY"):
     if not re.search(rf"^{re.escape(field)}:\s*\S",block,re.M):self.error(f"Uxx {node} lacks required coverage field: {field}")
  if 15 in done:
   for p in ("outputs/EXPERT_BRIEF.md","outputs/RESEARCH_QUESTIONS.md","outputs/FINAL_DECISION.md"):
    if not (ROOT/p).is_file():self.error(f"stage 15 missing {p}")
  if self.errors:
   print(f"STRUCTURAL VALIDATION FAILED ({len(self.errors)} error(s))");print(*["- "+e for e in self.errors],sep="\n");return 1
  print("STRUCTURAL VALIDATION PASSED");return 0
if __name__=="__main__": sys.exit(Validator().run())
