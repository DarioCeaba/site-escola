# Comparação do site antigo com o novo — 31/10/2026

## Escopo e evidência

Leitura do HTML público da Home, Integral, Projetos, Tour 360, Contato e Portal do Aluno em `https://sitepressbr.com/site/escola-ceaba/`. As páginas responderam HTTP 200. A análise é de conteúdo e estrutura do HTML; a inspeção visual interativa do site antigo não pôde ser concluída. Não confundir conteúdo presente no HTML com validação de formulários, serviços, disponibilidade atual de atividades ou vigência de informações.

## O que vale recuperar

| Conteúdo no antigo | Situação no novo | Proposta e confirmação necessária |
| --- | --- | --- |
| Integral: acompanhamento de tarefas, oficinas e atividades esportivas | Sem página específica | Prioridade alta. Confirmar etapas atendidas, horários, refeições, rotina e atividades incluídas/opcionais antes de criar página. |
| Estrutura por faixa etária, entradas nas ruas 1134 e 1135, estacionamento, segurança | Fotos pedagógicas e menção geral à estrutura | Criar seção “Conheça a escola”, com fotos atuais e descrições curtas de cada ambiente. Validar afirmações de segurança e acessibilidade. |
| Tour 360 com ambientes como laboratório, sala Maker, Corpo e Movimento, pátio e refeitório | Ainda não incluído | Há embeds públicos de panoramas do Google Maps no HTML. Podemos selecionar os ambientes atuais e carregar sob demanda; evitar carregar todos na Home. Confirmar se os espaços e as imagens permanecem atuais. “Berçário” aparece no tour antigo e não confirma oferta atual dessa etapa. |
| Depoimentos com nomes de três responsáveis | Sem depoimentos reais publicados | Recuperar após confirmação de autorização e vigência. Preservar o texto aprovado; não inventar novos relatos. |
| Portal do Aluno com Bernoulli, Plurall e LIV | Não incluído | Criar área “Para as famílias” com links oficiais após confirmar quais plataformas a escola usa. Não armazenar senhas ou reproduzir formulários de login. |
| Projetos com Maker, natação, dança livre, jiu-jítsu e Olimpíada Canguru | Parte dos projetos já está nas páginas por etapa | Completar o conteúdo após validar faixa etária, frequência e se a atividade é curricular ou opcional. Evitar uma listagem extensa repetindo todas as etapas na Home. |
| Endereço, telefone fixo, horário de atendimento e link do Maps | Contato ainda incompleto | Alta prioridade. Antigo Contato informa R. 1134, 183, Setor Marista, Goiânia-GO; Home informa Qd. 241, Lt. 25. Conferir forma postal final. Telefone 62 3281-3342 e atendimento seg–sex 7h–18h aguardam validação. |
| Eventos e canal de currículos | Blog e WhatsApp de visitas | Eventos podem entrar como notícias com datas reais. Canal de currículos requer confirmação do responsável/número; não reutilizar automaticamente número distinto do atendimento. |

## Problemas a não copiar

- A listagem de Projetos repete o texto de Dança Livre sob o título “JIU JITSU” na Educação Infantil.
- Home e outras áreas apresentam variantes do canal de YouTube; manter o endereço já confirmado pelo usuário: `https://www.youtube.com/@escolaceaba/videos`.
- Alguns textos mencionam anos antigos (por exemplo, Mostra Cultural de 2021/2022) e exigem revisão temporal.
- Texto do tour tem erro “FAÇA UM UMA TURNÊ”; usar “Conheça a escola em um tour 360°”.
- Não recuperar pop-up/campanha anual de matrícula automaticamente.
- Mensagens de sucesso/erro dos formulários estão presentes no HTML, mas não comprovam envio. Manter WhatsApp até definir um formulário com destinatário e processamento verificados.
- Não importar o identificador do Google Tag Manager da agência, código de rastreamento ou scripts desconhecidos para o novo site.

## Instagram

O antigo usa `https://snapwidget.com/embed/1040959` e referência ao script de widgets do fornecedor. O iframe não pôde ser carregado nas tentativas de verificação; isso não prova que esteja desativado para todos os visitantes.

O SnapWidget disponibiliza grade gratuita de Instagram e incorporação por iframe, compatível com páginas HTML na HostGator. Para ativar: conferir acesso ao widget antigo ou criar um widget na conta controlada pela escola, conectar o Instagram oficial pelo fluxo do provedor e fornecer o código de incorporação. Não solicitar senha/token pelo chat. Não reutilizar um identificador sem confirmar funcionamento e conta proprietária.

O plano escolhido determina apresentação, frequência de atualização e destino dos cliques. A página comercial atual distingue recursos gratuitos de recursos Pro, incluindo links diretos às publicações nos planos pagos. Não prometer atualização instantânea. Fonte: https://snapwidget.com/

Proposta de posição: seção “Acontece no CEABA” após os artigos do blog e antes do convite final para visita. Feed com carregamento tardio, tamanho responsivo, título acessível e link independente para o Instagram caso o fornecedor falhe. Ativação pendente de widget verificado; não há feed simulado no novo site.

## Alteração concluída nesta etapa

Links de Instagram, Facebook e YouTube do rodapé convertidos para ícones SVG locais, com rótulos acessíveis, foco por teclado e identificação ao passar o mouse. Sem biblioteca de ícones externa. Links de texto mantidos na página de contato.

## Próxima decisão de conteúdo

Confirmar primeiro Integral, endereço/atendimento, plataformas e materiais atuais da estrutura/tour. Os dados antigos foram catalogados, mas não adicionados automaticamente como oferta atual.
