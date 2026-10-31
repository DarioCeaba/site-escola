# Integrações e conteúdo complementar

## Instagram / SnapWidget

Configuração pública: `content/site.json`, chave `instagram.widget_url`. Atualmente `null`, pois o widget antigo `1040959` respondeu HTTP 401, com mensagem “Your widget needs to be updated” e diagnóstico “Token Expired”. Não há senha ou token a recuperar pelo código público.

A Home exibe uma seção com link real ao Instagram oficial, sem imitar publicações. O gerador já aceita uma URL pública `https://snapwidget.com/embed/NUMERO`; ao configurar um widget válido, inclui iframe com título acessível e carregamento tardio, além do script de ajuste de tamanho do SnapWidget. O link ao perfil permanece disponível. A URL é validada; não aceitar código HTML arbitrário, credenciais, query strings ou URLs de outro host nessa configuração.

Para ativar: o responsável cria um novo widget em conta da escola e autoriza o Instagram pelo fluxo do fornecedor. Não inserir senha ou token no JSON nem no Git. Após obter a URL pública, configurar e executar `scripts/build_site.py`, conferir em computador/celular e publicar. Feed não será declarado ativo até haver verificação real.

## Portal do Aluno

- Plurall: https://login.plurall.net/ — resposta HTTP 200.
- LIV: https://portal.inteligenciadevida.com.br/auth/login — resposta HTTP 200.
- Meu Bernoulli: link antigo retorna 404; endereço atual pendente. O site oficial do Sistema de Ensino também aponta ao endereço antigo. O cartão permanece com ação de pedir orientação à escola pelo WhatsApp, sem publicar link sabidamente quebrado.

As plataformas abrem em nova aba, com `noopener noreferrer`. O site não recebe credenciais dos estudantes. Não foram testados acessos autenticados, apenas os endereços públicos de login.

## Conteúdo confirmado

Dados do contato e os três depoimentos do site antigo aprovados pelo usuário. Textos dos depoimentos preservados, inclusive as reticências existentes; nenhuma avaliação em estrelas ou data foi inventada. Página Integral baseada no conteúdo antigo: acompanhamento de tarefas, leitura, arte, música e movimento. Não foram inventados horários, mensalidades, idades atendidas ou inclusão contratual de atividades; orientar consulta à equipe para programação e condições.

Tour 360 não implementado, por solicitação do usuário.
