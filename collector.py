"""Coletor de dados públicos. Não executa ordens nem acessa carteiras."""
import json, pathlib, datetime, urllib.request, urllib.parse, time
ROOT=pathlib.Path(__file__).resolve().parent
BASE='https://api.dexscreener.com'
HEADERS={'User-Agent':'FomoMatrixResearch/1.0','Accept':'application/json'}
def get(path):
    req=urllib.request.Request(BASE+path,headers=HEADERS)
    with urllib.request.urlopen(req,timeout=20) as resp:
        return json.load(resp)
def main():
    boosted=get('/token-boosts/latest/v1')
    if not isinstance(boosted,list): raise ValueError('Unexpected boosts response')
    targets=[]; seen=set()
    for item in boosted:
        chain=item.get('chainId'); address=item.get('tokenAddress')
        if chain not in ('solana','bsc') or not address or (chain,address) in seen: continue
        targets.append((chain,address));seen.add((chain,address))
        if len(targets)==20:break
    rows=[]
    for chain,address in targets:
        try:
            pairs=get('/token-pairs/v1/'+urllib.parse.quote(chain,safe='')+'/'+urllib.parse.quote(address,safe=''))
            if not isinstance(pairs,list):continue
            valid=[p for p in pairs if p.get('chainId')==chain and p.get('baseToken',{}).get('address','').lower()==address.lower()]
            if not valid:continue
            p=max(valid,key=lambda x:float((x.get('liquidity') or {}).get('usd') or 0))
            row={'id':address,'chain':'SOL' if chain=='solana' else 'BSC','name':str((p.get('baseToken') or {}).get('name') or 'Token')[:55], 'symbol':str((p.get('baseToken') or {}).get('symbol') or '?')[:16], 'price':float(p.get('priceUsd') or 0),'liq':float((p.get('liquidity') or {}).get('usd') or 0),'vol':float((p.get('volume') or {}).get('h24') or 0),'url':str(p.get('url') or ''),'pairAddress':str(p.get('pairAddress') or '')}
            if row['price']>0:rows.append(row)
        except (ValueError,KeyError,TimeoutError, OSError) as exc:
            print('Skipping',chain,address,str(exc)[:120])
        time.sleep(.15)
    if not rows: raise RuntimeError('No valid pairs. Refusing to overwrite previous snapshot.')
    stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
    out=ROOT/'data'/'latest.json';out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps({'source':'DexScreener token boosts (promoted, nonrepresentative)','collected_at':stamp,'tokens':rows},ensure_ascii=False,indent=2),encoding='utf-8')
    history=ROOT/'data'/'history.jsonl'
    with history.open('a',encoding='utf-8') as f:
        for row in rows:f.write(json.dumps({'collected_at':stamp,**row},ensure_ascii=False)+'\n')
    print('Collected',len(rows),'tokens at',stamp)
if __name__=='__main__':main()
