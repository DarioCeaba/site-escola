# Guia da Naiane — imagens do site CEABA

Preparado em 03/11/2026.

## Onde está o projeto

- Código e arquivos: https://github.com/DarioCeaba/site-escola
- Site na HostGator: https://escolaceaba.com.br/
- Prévia privada: https://ceaba-previa-direcao.yummy-sugar-2095.chatgpt.site/

A mesma conta do Codex pode dar acesso às conversas e à prévia privada, conforme a disponibilidade no aplicativo, mas não transfere a pasta local do computador do Dario. No seu computador, é preciso baixar uma cópia do repositório e abrir essa pasta no Codex. Os caminhos locais serão os do seu computador.

## 1. Preparar seu computador

1. Abra o aplicativo Codex e entre na conta autorizada pelo Dario. Não coloque senhas em mensagens ou nos arquivos do projeto.
2. Tenha o Git instalado. Se necessário, peça ao Codex para conferir a instalação antes de baixar o projeto.
3. Crie uma pasta vazia para o projeto, por exemplo, uma pasta `CEABA-site` dentro de Documentos, e abra-a como projeto local no Codex.
4. Envie o pedido abaixo nessa conversa local. Se o aplicativo já trouxer o projeto “web site” da conta compartilhada, verifique qual pasta ele usa; não suponha que o caminho antigo exista no seu computador.

### Pedido inicial para copiar no Codex

> Estou colaborando com Dario como designer do site CEABA. Quero trabalhar nas imagens a partir deste computador. Verifique a pasta atual e o Git. Se a pasta estiver vazia, clone nela o repositório https://github.com/DarioCeaba/site-escola.git. Se já houver arquivos, examine antes e preserve o trabalho existente. Leia AGENTS.md e docs/guia-naiane.md. Confira o estado do Git e prepare uma branch exclusiva para minhas alterações de imagens, a partir da versão atual da main, sem descartar alterações locais. Mostre-me a prévia local e o mapa das imagens. Nesta etapa, não publique nem altere a prévia compartilhada ou a HostGator.

Não é necessário instalar WordPress ou banco de dados para trocar as imagens da versão atual. O Codex poderá conferir Python/Node quando precisar gerar páginas ou abrir a prévia. O gerador Python atual usa apenas a biblioteca padrão para gerar HTML.

## 2. Localizar as imagens

As imagens usadas pelo site ficam em `public/assets/`. O mesmo arquivo pode aparecer em várias páginas. Substituir esse arquivo troca todas as suas aparições; para alterar só uma delas, peça ao Codex para criar uma imagem com outro nome e ajustar apenas a referência correspondente.

| Arquivo | Onde aparece atualmente |
| --- | --- |
| `logo.png` | Cabeçalho, rodapé e ícone da aba do navegador |
| `acolhimento.webp` | Foto principal da Home, abertura da página Integral e conteúdo institucional sobre a proposta pedagógica |
| `infantil.webp` | Foto menor da abertura da Home; cartão e página de Educação Infantil |
| `iniciais.webp` | Cartão da Home e abertura da página de Anos Iniciais |
| `finais.webp` | Cartão da Home e abertura da página de Anos Finais |
| `musica.webp` | Seção da proposta pedagógica e chamada para o Integral, na Home |
| `sensorial.webp` | Conteúdo institucional “Brincar é um jeito de descobrir o mundo” |
| `ciencias.webp` | Conteúdo institucional “Quando a curiosidade vira projeto” |
| `blog-escolher-escola-ideal.webp` | Capa do artigo sobre escolha da escola, no artigo, no Blog e na Home |
| `blog-psicomotricidade.webp` | Capa do artigo de psicomotricidade, no artigo, no Blog e na Home |
| `blog-musicalizacao-infantil.webp` | Capa do artigo de musicalização, no artigo, no Blog e na Home |

Há também arquivos de apoio, como `jogos.webp` e `xadrez.webp`; peça ao Codex para conferir se estão referenciados antes de alterá-los ou removê-los. Os ícones sociais são SVGs no gerador, não imagens dessa pasta.

## 3. Preparar e entregar as novas imagens

- Traga fotos originais em boa resolução, preferencialmente arquivos aprovados para uso no site da escola.
- Para fotos maiores, uma largura de aproximadamente 1600 pixels costuma ser um bom ponto de partida; evite ampliar artificialmente uma imagem pequena. É uma orientação de produção, não uma exigência rígida do site.
- As capas atuais dos três artigos são quadradas. Mantenha o formato quadrado para preservar as artes e seus títulos.
- As demais fotos são recortadas de modo diferente conforme a tela. Deixe espaço nas bordas e mantenha rostos e informações essenciais numa área segura. Confira computador e celular.
- Use WebP para as fotos finais e PNG com transparência para o logo, quando aplicável. Não basta mudar a extensão do nome: o arquivo precisa ser convertido para o formato correto.
- Preserve a proporção do logo e deixe uma margem visual adequada. O logo também é usado no ícone da aba; uma mudança pode exigir uma versão específica para esse uso.
- Envie JPG, PNG ou WebP ao Codex como anexo ou coloque os arquivos numa pasta `tmp/recebidos-naiane/` dentro do projeto e informe os nomes. Essa pasta está fora do histórico Git pelas regras atuais. Guarde os editáveis originais em seu local habitual de trabalho; somente as versões necessárias ao site devem ir para `public/assets/`.
- Como o repositório é público, os arquivos que forem enviados para ele poderão ser vistos por qualquer pessoa. Não adicione documentos internos, credenciais ou materiais sem aprovação para esse destino.

### Pedido para substituir imagens

> Quero substituir estas imagens do site CEABA: [liste cada arquivo ou seção e a imagem que deve entrar no lugar]. Use os arquivos que anexei ou indiquei na pasta do projeto. Preserve textos, links, layout e conteúdo pedagógico, salvo os ajustes de proporção necessários às imagens. Antes de substituir um arquivo compartilhado, identifique em quais páginas ele aparece. Converta e otimize as imagens para os formatos corretos, sem distorcer nem cortar rostos ou títulos importantes. Ajuste o texto alternativo para descrever a nova foto. Mostre a prévia em computador e celular e registre os arquivos alterados. Trabalhe nesta branch e não publique na HostGator nem na prévia compartilhada nesta etapa.

## 4. Como conferir sem perder alterações

- Antes de cada sessão, peça ao Codex para verificar a branch, as alterações locais e se existem novidades no GitHub. Atualizar o projeto não deve apagar o trabalho ainda não salvo.
- A versão de desenvolvimento usa `public/`. Não edite `dist/`: ela é gerada para publicação.
- Os arquivos HTML em `public/` são gerados. Se precisar trocar nomes de imagens ou textos alternativos, altere a fonte correspondente e gere os HTMLs novamente. Não faça uma correção que será perdida na próxima geração.
- Estrutura e páginas: `scripts/build_site.py` e `scripts/site_sections.py`.
- Textos e capas dos artigos: `content/artigos/*.json`.
- Contatos, depoimentos e integrações: `content/site.json`.
- Estilos e recortes das fotos: `public/assets/style.css`.
- Uma troca apenas do arquivo de imagem, mantendo nome e formato, não exige gerar os HTMLs novamente. O Codex pode ajudar a conferir isso.

Peça uma verificação das páginas afetadas, das imagens carregadas e da leitura no celular. Confira também recortes, nitidez, peso dos arquivos e nomes dos textos alternativos. Uma atualização forçada do navegador pode ser necessária para ver uma imagem substituída com o mesmo nome.

## 5. Entregar para o Dario

1. Peça ao Codex para mostrar um resumo das alterações e registrar uma versão na sua branch.
2. Para enviar diretamente ao repositório, sua sessão do GitHub precisa ter permissão de escrita. Estar na mesma conta do Codex não autentica o GitHub automaticamente.
3. Se você usar sua própria conta GitHub, o Dario pode conceder acesso como colaboradora. A clonagem do repositório público não exige esse acesso; o envio de alterações ao repositório dele exige. Um fork com pull request também é uma alternativa.
4. Com acesso configurado, peça ao Codex para enviar a branch e abrir um pull request com as imagens antes/depois e as páginas conferidas. Compartilhe o link com o Dario para revisão. Não envie alterações diretamente para `main` durante a colaboração.
5. Se ainda não houver acesso de escrita, entregue as imagens finais e a lista dos arquivos/seções alterados ao Dario para integração. Não tente contornar a autenticação.

### Pedido para concluir sua entrega

> Revise as alterações de imagens desta branch. Confirme que textos, links e arquivos de outras pessoas foram preservados. Gere novamente os HTMLs se as fontes tiverem mudado, confira as páginas afetadas e prepare um resumo com capturas antes/depois. Se houver acesso autorizado ao GitHub, registre as alterações, envie esta branch e abra um pull request para revisão do Dario. Caso contrário, prepare uma entrega local e explique como o Dario pode incorporá-la. Não altere a visibilidade do repositório nem publique o site.

## 6. Como a mudança chega ao site no ar

Depois da revisão e integração no projeto, a prévia privada pode ser atualizada e um novo ZIP pode ser preparado para a HostGator. Salvar uma imagem no computador ou enviar alterações ao GitHub não atualiza automaticamente `escolaceaba.com.br`.

Não é necessário compartilhar acesso ao cPanel para trabalhar nas imagens. A publicação pode continuar com o Dario. Evitem extrair pacotes antigos depois de uma atualização, pois isso pode restaurar versões anteriores de imagens e páginas.

## Referência oficial sobre arquivos locais

A documentação diferencia sincronização de conversas e acesso à pasta: https://learn.chatgpt.com/docs/projects
