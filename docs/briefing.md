# Briefing do website

## Confirmado

- Será um novo website para uma escola.
- Dario conduz a preparação com auxílio do Codex.
- A fase atual inclui construção da primeira versão local, autorizada em 31/10/2026.
- O repositório no GitHub deverá ser privado.
- Conta proprietária: `DarioCeaba`; nome do repositório: `site-escola`.
- Cinco documentos de diretrizes e conteúdo pedagógico recebidos e lidos. Consolidação em `docs/diretrizes-site.md`.
- Hospedagem final na HostGator; primeira versão em HTML, CSS e JavaScript estáticos.

## Pendente

- Nome oficial da escola, localização e contatos públicos.
- Objetivos, público e prioridades do site.
- Endereço do site atual, domínio e hospedagem existentes.
- Páginas, conteúdos, idiomas e recursos necessários.
- Identidade visual, logotipo, cores, tipografia e referências.
- Quem editará conteúdos e se será necessário um painel de edição.
- Formulários, área restrita e integrações com serviços da escola.
- Materiais aprovados para publicação e regras para uso de imagens.
- Requisitos de acessibilidade, privacidade e manutenção.
- Orçamento, cronograma e responsáveis pela aprovação.
- Materiais adicionais das fontes do ChatGPT precisam ser trazidos explicitamente, quando necessários.

## Decisões técnicas

Primeira versão estática na pasta `public/`; conteúdo editável pelo gerador `scripts/build_site.py`. Painel para blog ainda depende do fluxo de edição desejado. Não será exigido Node.js no servidor HostGator. Pendências antigas desta lista devem ser lidas junto da consolidação atual em `docs/diretrizes-site.md`.

## Atualização de 31/10/2026

WhatsApp principal e redes sociais confirmados. Painel de edição desejável para múltiplos responsáveis. Plano básico HostGator, provável cPanel; conferência do plano e envio de mídias previstos para 03/11/2026. Ver detalhes em `docs/diretrizes-site.md`.

## Ampliação autorizada após análise do site antigo

- Página Integral, Portal do Aluno e depoimentos autorizados. Tour 360 adiado por decisão do usuário.
- Dados da página antiga de Contato confirmados: Rua 1134, nº 183, Setor Marista, Goiânia-GO; quadra 241/lote 25; telefone 62 3281-3342; atendimento de segunda a sexta, 7h–18h.
- Manter exclusivamente o YouTube já confirmado, ignorando variantes no antigo site.
- Usuário informa que o site já está no ar em `escolaceaba.com.br`, na HostGator. Alterações feitas aqui são publicadas na prévia privada e entregues em ZIP para envio ao cPanel; não presumir sincronização automática com a HostGator.
- SnapWidget antigo retorna HTTP 401 e “Token Expired”; requer autorização da conta no provedor ou criação de novo widget. Código de incorporação preparado, porém sem widget inativo em produção.
- Plurall e LIV responderam HTTP 200 na conferência. Meu Bernoulli antigo (`https://mb4.bernoulli.com.br/login`) respondeu HTTP 404, inclusive sendo destino indicado no site oficial. Portal oferece orientação da escola para esse acesso até receber endereço válido; pergunta enviada ao usuário.
