# Website da escola

Primeira versão local do website da Escola CEABA, baseada nos documentos fornecidos em 31/10/2026. A hospedagem final será na HostGator.

## Organização

- `docs/briefing.md`: informações confirmadas e pendentes.
- `AGENTS.md`: orientações para trabalhar neste projeto.
- `docs/preparacao.md`: estado da preparação e próximos passos.
- `docs/diretrizes-site.md`: requisitos consolidados e pendências de lançamento.
- `public/`: nove páginas estáticas, estilos, comportamento e imagens da prévia. Somente o conteúdo desta pasta será destinado à hospedagem.
- `scripts/build_site.py`: gerador das páginas; não é necessário na hospedagem.

## Etapas

1. Preparar ferramentas e histórico Git local.
2. Autenticar o computador no GitHub e criar um repositório privado.
3. Reunir referências e definir o escopo.
4. Escolher as tecnologias e implementar após as diretrizes.

## Desenvolvimento local

Regerar páginas: `python scripts/build_site.py`.

Abrir prévia: `python -m http.server 4173 --bind 127.0.0.1 --directory public`, depois acessar `http://127.0.0.1:4173`.

Tecnologia: HTML, CSS e JavaScript. Sem dependências de execução externas ou servidor Node em produção. Plano HostGator e domínio ainda a confirmar. A prévia bloqueia indexação e identifica conteúdo em revisão. Consulte `public/LEIA-ME-HOSPEDAGEM.txt` antes do lançamento.
