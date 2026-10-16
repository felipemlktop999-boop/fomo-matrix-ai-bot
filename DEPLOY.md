# FOMO MATRIX V8 — implantação estática

1. Teste `index.html` em navegador moderno. A consulta DexScreener requer conexão de rede e pode ser bloqueada por CORS ou limites de API.
2. Para publicar, crie um repositório privado no GitHub e faça upload de `index.html` e `README.md`.
3. No Cloudflare Pages ou GitHub Pages, configure a publicação de arquivos estáticos na raiz do projeto. Revise se deseja torná-lo público antes de habilitar.
4. Não insira segredos, tokens de API, senhas ou chaves privadas no HTML.
5. O site é estático: não existe serviço de monitoramento 24/7, alertas de servidor, autenticação, nem negociação automática.
6. Para produção, criar backend com autenticação, banco de dados, limites de API, trilha de auditoria, validação histórica e autorização explícita da plataforma de negociação.
