import csv,json
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def severity(likelihood, impact):
    a,b=int(likelihood),int(impact)
    if not 1<=a<=5 or not 1<=b<=5:raise ValueError('Scores must be in 1..5')
    v=a*b
    return ('high' if v>=15 else 'medium' if v>=7 else 'low'),v

def main():
    with (ROOT/'data/risks.csv').open() as f:rows=list(csv.DictReader(f))
    for row in rows:row['severity'],row['score']=severity(row['likelihood'],row['impact'])
    report={'total':len(rows),'by_status':dict(Counter(r['status'] for r in rows)),
            'by_severity':dict(Counter(r['severity'] for r in rows)),
            'open_high_risks':[r['risk_id'] for r in rows if r['severity']=='high' and r['status']!='mitigated']}
    out=ROOT/'output/risk_summary.json';out.parent.mkdir(exist_ok=True);out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))
if __name__=='__main__':main()
