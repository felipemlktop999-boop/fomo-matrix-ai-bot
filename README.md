# FOMO MATRIX AI BOT V10 — Protótipo experimental

## O que é real
- `collector.py` consulta dados públicos DexScreener de tokens **promovidos** e grava `data/latest.json` e `data/history.jsonl`.
- `.github/workflows/collect.yml` agenda coleta aproximadamente a cada 30 minutos via GitHub Actions (execuções podem atrasar ou ser suspensas).
- `index.html` oferece botão **Carregar última coleta na nuvem**. O navegador recusa dados com mais de 90 minutos.
- O painel V9 permanece disponível com radar sob demanda, instantâneos locais e simulador sintético.

## Como publicar sem servidor próprio
1. Crie um repositório GitHub e envie **todos** os arquivos, incluindo `.github/workflows/collect.yml`.
2. Em **Settings > Actions > General**, permita workflows e conceda permissão de escrita ao token do workflow, se necessário.
3. Na aba **Actions**, execute manualmente **Collect public market snapshots** para criar `data/latest.json`. Verifique o log.
4. Ative GitHub Pages para publicar a pasta raiz da branch principal (Settings > Pages). Aguarde a publicação.
5. Abra o endereço HTTPS do Pages e clique em **Carregar última coleta na nuvem**.
6. Verifique periodicamente falhas, atrasos, limites e crescimento do `history.jsonl`. Em produção, mover histórico para banco de dados com retenção.

## Limitações críticas
- Ainda **não hospedado**, nem ativado em conta GitHub. É necessário publicar e executar o workflow.
- Coleta de tokens promovidos não é radar completo nem recomendação de investimento.
- Sem verificação on-chain, honeypot, concentração de holders, inteligência artificial preditiva, ordens ou conexão com FOMO Family.
- O histórico coletado é amostrado, não é backtesting confiável. Não há lucro garantido.
- Não envie frases-semente, chaves privadas ou senhas para este projeto.
