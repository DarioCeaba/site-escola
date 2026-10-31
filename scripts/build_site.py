"""Gera as páginas estáticas; não é necessário Python na hospedagem."""
from pathlib import Path
from html import escape
from urllib.parse import quote
import json

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'public'
WA = 'https://wa.me/5562998325890?text=' + quote('Olá! Estou entrando em contato através do SITE para agendar uma visita.')
ARROW = '<span class="arrow" aria-hidden="true">↗</span>'

STAGES = [
 dict(slug='educacao-infantil', name='Educação Infantil', age='Maternal I ao Nível II · 1 a 5 anos', image='infantil',
      headline='Grandes descobertas começam com pequenos passos.',
      intro='Brincar, sentir, conviver e descobrir. Uma infância vivida com acolhimento, respeitando o tempo e a singularidade de cada criança.',
      description='Na Educação Infantil, o brincar é o ponto de partida para aprender. As experiências são orientadas pela BNCC e valorizam a autonomia, os vínculos e a participação da criança na construção do próprio conhecimento.',
      hours=[('Matutino','7h30 às 11h30'),('Vespertino','13h30 às 17h30')],
      projects=[('Brincar para aprender','Os campos de experiência integram corpo, linguagem, convivência, imaginação e descobertas sobre o mundo.'),('LIV: espaço para sentir','Histórias e situações do cotidiano ajudam a reconhecer emoções, construir vínculos e encontrar formas de se expressar.'),('Programa Bilíngue','O contato ampliado com a língua inglesa acontece com metodologias ativas, materiais voltados ao bilinguismo e participação da criança.'),('Estimulação sensorial','Texturas, cores, sons e diferentes materiais convidam a explorar os sentidos e conhecer o mundo.'),('Arte e expressão','Traços, formas e cores ampliam a imaginação, a sensibilidade e a coordenação motora fina.'),('Hora do Conto','A escuta de histórias enriquece o vocabulário, estimula a atenção e abre espaço para a imaginação.'),('Quadro das Cores','Uma rotina visual e acessível ajuda a antecipar as atividades da semana e desenvolver autonomia.'),('Vivências que aproximam','O Dia do Brinquedo, o Espelho D’Água e o Projeto Acolher integram brincadeira, investigação, convivência e solidariedade.')]),
 dict(slug='anos-iniciais', name='Ensino Fundamental · Anos Iniciais', age='1º ao 5º ano', image='iniciais',
      headline='Aprender faz sentido quando a criança faz parte.',
      intro='Conhecimento, criatividade e vínculos para construir uma base sólida. Aqui, cada experiência é uma oportunidade de aprender com o outro e com o mundo.',
      description='Nossa proposta sociointeracionista aproxima o ensino da prática. Ao trocar ideias, investigar e criar, o estudante participa ativamente da aprendizagem e amplia suas possibilidades de expressão.',
      hours=[('Matutino','7h30 às 11h30'),('Vespertino','13h30 às 17h30')],
      projects=[('Reconto','Desenhos, escrita e oralidade dão novas formas às histórias. Cada estudante reconta uma obra com seu próprio olhar.'),('Só Letrando','Um projeto que valoriza a escrita como caminho para ampliar conhecimentos e se comunicar com clareza.'),('Xadrez','Atenção, memória e pensamento estratégico se desenvolvem junto à capacidade de lidar com desafios, escolhas e frustrações.'),('Oficinas pedagógicas','Dobraduras, modelagem, pinturas e experimentos conectam o conteúdo às descobertas feitas com as próprias mãos.'),('Musicalização e arte','Ritmo, movimento e expressão artística estimulam a criatividade, a convivência e a coordenação motora.'),('LIV e Programa Bilíngue','O cuidado com as emoções caminha ao lado de novas formas de se comunicar, com LIV e Eduall.'),('Aprendizagem com Bernoulli','Os recursos do Sistema de Ensino Bernoulli apoiam o percurso de aprendizagem e as práticas em sala.'),('Projeto Acolher','Ações solidárias aproximam escola e famílias, promovendo cuidado, participação e responsabilidade com o outro.')]),
 dict(slug='anos-finais', name='Ensino Fundamental · Anos Finais', age='6º ao 9º ano', image='finais',
      headline='Mais autonomia para transformar conhecimento em ação.',
      intro='Uma etapa de novas perguntas, escolhas e possibilidades. Aprendizagem ativa e projetos interdisciplinares ampliam o olhar sobre o mundo.',
      description='Com uma abordagem sociointeracionista, os estudantes conectam diferentes áreas do conhecimento e desenvolvem competências para uma participação consciente na sociedade. Professores especialistas acompanham o percurso acadêmico e socioemocional.',
      hours=[('Matutino','7h às 12h20')],
      projects=[('Rally Cultural','Uma corrida do conhecimento que integra disciplinas, criatividade e trabalho em equipe.'),('Feira de Ciências','Pesquisa, experimentos e descobertas colocam a curiosidade em movimento e aproximam a ciência do cotidiano.'),('Festival Ecológico da Canção','Paródias e apresentações musicais unem criatividade e consciência ambiental em um encontro com a comunidade escolar.'),('Feira do Empreendedorismo','Os conhecimentos de educação financeira ganham uma aplicação prática, com protagonismo, inovação e responsabilidade.'),('Coletânea Literária','Textos originais dos estudantes se transformam em um livro que registra ideias, sentimentos e aprendizados.'),('Jogos Internos CEABA','Diferentes modalidades esportivas fortalecem amizade, espírito esportivo e superação de desafios.'),('Formação integral','LIV, Programa Bilíngue Eduall, Sistema Bernoulli e preparação para olimpíadas compõem o percurso apresentado pela escola.'),('Avaliação contínua','Provas, projetos, atividades e simulados acompanham a aprendizagem ao longo de cada bimestre.')]),
]

ARTICLES = [
 dict(slug='aprender-com-o-outro', title='Aprender com o outro. Crescer do seu jeito.', category='Proposta pedagógica', image='acolhimento',
      summary='Como a abordagem sociointeracionista aproxima conhecimento, experiências e vínculos.',
      sections=[('O conhecimento se constrói nas relações','Na proposta sociointeracionista do CEABA, aprender envolve agir, trocar ideias e dar significado às experiências. A criança chega à escola com sua própria história, suas referências e suas perguntas. Esse repertório faz parte da aprendizagem.'),('O professor como mediador','O professor organiza situações que convidam a investigar, conversar e construir novas respostas. A mediação reconhece o que cada estudante já sabe e cria oportunidades para avançar junto aos colegas.'),('Da experiência ao significado','Brincadeiras, oficinas, projetos e atividades coletivas conectam o conteúdo ao mundo vivido pelos estudantes. Esse percurso valoriza o protagonismo e o desenvolvimento cognitivo, social e emocional.')]),
 dict(slug='brincar-e-descobrir', title='Brincar é um jeito de descobrir o mundo.', category='Educação Infantil', image='sensorial',
      summary='Texturas, histórias e brincadeiras que abrem caminhos para a aprendizagem na infância.',
      sections=[('Uma infância de experiências','Na Educação Infantil, brincar é uma base essencial para o desenvolvimento. Ao explorar materiais, ouvir histórias e conviver com outras crianças, os pequenos ampliam suas formas de perceber e participar do mundo.'),('Sentir, experimentar e expressar','A estimulação sensorial convida a explorar texturas, sons, cores e sensações. As propostas de arte favorecem a expressão, a imaginação e a coordenação motora. Cada experiência respeita a criança como participante do próprio desenvolvimento.'),('Rotina que acolhe','O Quadro das Cores ajuda a antecipar as atividades da semana. Com referências visuais simples, a criança compreende a rotina e constrói autonomia. A Hora do Conto e o Dia do Brinquedo ampliam os momentos de escuta, partilha e imaginação.')]),
 dict(slug='conhecimento-em-acao', title='Quando a curiosidade vira projeto.', category='Anos Finais', image='ciencias',
      summary='Ciência, literatura e empreendedorismo levam o aprendizado para além da sala de aula.',
      sections=[('Aprender fazendo conexões','Nos Anos Finais, a aprendizagem ativa e interdisciplinar convida os estudantes a relacionar conhecimentos e trabalhar em equipe. Os projetos abrem espaço para pesquisa, autoria e experiências práticas.'),('Investigar e compartilhar','Na Feira de Ciências, experimentos e pesquisas são compartilhados com a comunidade. O Rally Cultural integra saberes em uma dinâmica de desafios coletivos. Na Coletânea Literária, a autoria dos estudantes ganha a forma de um livro.'),('Criatividade e responsabilidade','O Festival Ecológico da Canção aproxima música e consciência ambiental. A Feira do Empreendedorismo transforma os conhecimentos de educação financeira em vivências práticas. São caminhos para desenvolver protagonismo e responsabilidade.')]),
]

def button(label='Agendar uma visita', cls='', href=WA):
    external = ' target="_blank" rel="noopener noreferrer"' if href.startswith('https:') else ''
    return f'<a class="button {cls}" href="{href}"{external}>{label}{ARROW}</a>'

def img(name, alt, cls='', eager=False):
    return f'<img src="assets/{name}.webp" alt="{escape(alt)}" class="{cls}" loading="{"eager" if eager else "lazy"}" decoding="async">'

def social_links():
    links = [('Instagram', 'https://www.instagram.com/escola.ceaba'),
             ('Facebook', 'https://www.facebook.com/ceabagoiania'),
             ('YouTube', 'https://www.youtube.com/@escolaceaba/videos')]
    return '<div class="social-links" aria-label="Redes sociais da Escola CEABA">' + ''.join(
        f'<a href="{url}" target="_blank" rel="noopener noreferrer" aria-label="{label} da Escola CEABA (abre em nova aba)">{label} ↗</a>'
        for label, url in links) + '</div>'

def shell(title, description, body, page=''):
    nav = lambda key: ' aria-current="page"' if page==key else ''
    return f'''<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{escape(title)} | Escola CEABA</title><meta name="description" content="{escape(description)}">
<meta name="robots" content="noindex,nofollow"><meta name="theme-color" content="#0d4c80">
<meta property="og:title" content="{escape(title)} | Escola CEABA"><meta property="og:description" content="{escape(description)}"><meta property="og:type" content="website"><meta property="og:locale" content="pt_BR">
<link rel="icon" href="assets/logo.png"><link rel="stylesheet" href="assets/style.css"><script src="assets/app.js" defer></script></head>
<body><a class="skip" href="#conteudo">Pular para o conteúdo</a><div class="topline">EDUCAÇÃO INFANTIL E ENSINO FUNDAMENTAL · ESCOLA CEABA</div>
<header class="header"><div class="wrap"><a class="brand" href="index.html" aria-label="Escola CEABA — início"><img src="assets/logo.png" alt="Escola CEABA" width="137" height="91"></a>
<button class="mobile-toggle" aria-controls="navigation" aria-expanded="false">Menu ☰</button>
<nav class="nav" id="navigation" aria-label="Navegação principal"><a href="index.html"{nav('home')}>Início</a><details><summary>Ensino</summary><div class="subnav"><a href="educacao-infantil.html"{nav('educacao-infantil')}>Educação Infantil</a><a href="anos-iniciais.html"{nav('anos-iniciais')}>Anos Iniciais · 1º ao 5º</a><a href="anos-finais.html"{nav('anos-finais')}>Anos Finais · 6º ao 9º</a></div></details><a href="blog.html"{nav('blog')}>Blog</a><a href="contato.html"{nav('contato')}>Contato</a>{button('Agendar visita')}</nav></div></header>
<main id="conteudo">{body}</main>
<footer class="footer"><div class="wrap"><div class="footer-grid"><div><img src="assets/logo.png" alt="Escola CEABA" width="150" height="101" loading="lazy"><p>Uma escola que sente.<br>E que está perto de você.</p></div><div><h3>Cada etapa, um novo mundo.</h3><a href="educacao-infantil.html">Educação Infantil</a><a href="anos-iniciais.html">Ensino Fundamental · Anos Iniciais</a><a href="anos-finais.html">Ensino Fundamental · Anos Finais</a></div><div><h3>Vamos conversar?</h3><a href="{WA}" target="_blank" rel="noopener noreferrer">WhatsApp · (62) 99832-5890 ↗</a><a href="contato.html">Agende uma visita</a><a href="blog.html">Conteúdos da escola</a>{social_links()}</div></div><div class="footer-bottom"><span>Escola CEABA · Educação Infantil e Ensino Fundamental</span><span>Versão de apresentação · conteúdo em revisão</span></div></div></footer>
<a class="whatsapp" href="{WA}" target="_blank" rel="noopener noreferrer" aria-label="Conversar com a Escola CEABA pelo WhatsApp (abre em nova aba)">Vamos conversar? ↗</a></body></html>'''

def cta():
    return f'<section class="section"><div class="wrap"><div class="wide-cta"><div><span class="eyebrow" style="color:#bce3ed">ESCOLA E FAMÍLIA, MAIS PERTO</span><h2>A próxima descoberta começa com uma visita.</h2><p>Venha conhecer nossa proposta, conversar com a equipe e sentir de perto o que faz parte do dia a dia CEABA.</p></div>{button(cls="yellow")}</div></div></section>'

def stories():
    return '<div class="story-grid">'+''.join(f'<article class="story"><a href="blog-{a["slug"]}.html">{img(a["image"],a["title"])}<span class="eyebrow">{a["category"]}</span><h3>{a["title"]}</h3><p>{a["summary"]}</p><span class="text-link">Ler conteúdo {ARROW}</span></a></article>' for a in ARTICLES)+'</div>'

def home():
    stagecards = ''.join(f'<a class="stage" href="{s["slug"]}.html">{img(s["image"],"Vivência pedagógica da Escola CEABA")}<div class="stage-body"><span class="label">{s["age"]}</span><h3>{s["name"].replace("Ensino Fundamental · ", "")}</h3><p>{s["intro"].split(". ")[0]}.</p><span class="more">Conheça esta etapa {ARROW}</span></div></a>' for s in STAGES)
    return f'''<section class="hero"><div class="wrap"><div class="hero-grid"><div><span class="eyebrow">ACOLHER. DESCOBRIR. TRANSFORMAR.</span><h1>Uma escola<br>que sente.<br><em>E que transforma.</em></h1><p class="intro">Da primeira descoberta aos novos desafios, um ensino que acolhe e coloca seu filho no centro da aprendizagem.</p><div class="hero-actions">{button()}<a class="text-link" href="#ensino">Conheça nosso ensino ↓</a></div></div><div class="hero-visual"><span class="visual-circle" aria-hidden="true"></span><span class="sun" aria-hidden="true">✳</span>{img('acolhimento','Crianças em uma atividade coletiva no espaço da Escola CEABA','photo-main',True)}{img('infantil','Criança explorando materiais em uma vivência da Educação Infantil','photo-small',True)}<div class="photo-note"><strong>Aprender com significado.</strong>Crescer com afeto e autonomia.</div></div></div><div class="hero-bottom"><span>Educação Infantil · 1 a 5 anos</span><span>Anos Iniciais · 1º ao 5º ano</span><span>Anos Finais · 6º ao 9º ano</span></div></div></section>
<section class="section" id="ensino"><div class="wrap"><div class="section-head"><div><span class="eyebrow">UM CAMINHO, MUITAS DESCOBERTAS</span><h2>Um olhar especial<br>para cada etapa.</h2></div><p>Respeitamos cada fase do desenvolvimento, com experiências que conectam conhecimento, emoções e vida.</p></div><div class="stages">{stagecards}</div></div></section>
<section class="section soft" id="proposta"><div class="wrap split"><div class="split-photo">{img('musica','Estudantes em uma atividade de musicalização na Escola CEABA')}<div class="caption">VIVÊNCIAS REAIS. APRENDIZADOS QUE FICAM.</div></div><div><span class="eyebrow">NOSSO JEITO DE ENSINAR</span><h2>Conhecimento que faz sentido.<br>Relações que fazem a diferença.</h2><p>Acreditamos que aprender é construir junto. Nossa proposta sociointeracionista valoriza a curiosidade, a troca e a participação de cada estudante.</p><p>O cuidado com as emoções caminha ao lado do desenvolvimento acadêmico. Para crescer com autonomia, confiança e espaço para ser quem se é.</p><a class="text-link" href="blog-aprender-com-o-outro.html">Conheça nossa proposta {ARROW}</a></div></div></section>
<section class="section"><div class="wrap"><div class="section-head"><div><span class="eyebrow">FORMAÇÃO PARA A VIDA</span><h2>Aprender vai além<br>do conteúdo.</h2></div><p>Experiências que integram o pensar, o sentir, o criar e o conviver.</p></div><div class="pillars"><div class="pillar"><span class="pillar-number">01 / CONVIVER</span><h3>Emoções têm espaço.</h3><p>Com o LIV, o reconhecimento dos sentimentos fortalece os vínculos e o cuidado consigo e com o outro.</p></div><div class="pillar"><span class="pillar-number">02 / COMUNICAR</span><h3>Novas formas de ver o mundo.</h3><p>O Programa Bilíngue amplia o contato com a língua inglesa e as possibilidades de comunicação.</p></div><div class="pillar"><span class="pillar-number">03 / EXPERIMENTAR</span><h3>Curiosidade em movimento.</h3><p>Oficinas, arte, ciência e projetos transformam perguntas em experiências e conhecimento.</p></div><div class="pillar"><span class="pillar-number">04 / PERTENCER</span><h3>Escola e família, juntas.</h3><p>Uma relação próxima que acolhe cada trajetória e participa de cada nova conquista.</p></div></div></div></section>
<section class="section soft"><div class="wrap"><div class="section-head"><div><span class="eyebrow">APRENDIZAGEM EM CADA DETALHE</span><h2>Um pouco do nosso<br>universo pedagógico.</h2></div><a class="text-link" href="blog.html">Explorar conteúdos {ARROW}</a></div>{stories()}</div></section>{cta()}'''

def stage_page(s):
    projects=''.join(f'<article class="project"><h3>{title}</h3><p>{text}</p></article>' for title,text in s['projects'])
    hours=''.join(f'<div><strong>{label}</strong>{time}</div>' for label,time in s['hours'])
    return f'''<section class="page-hero"><div class="wrap"><div class="crumb"><a href="index.html">Início</a> / Ensino / {s['name']}</div><div class="split"><div><span class="eyebrow">{s['name']}</span><span class="age">{s['age']}</span><h1>{s['headline']}</h1><p class="lead">{s['intro']}</p>{button()}</div>{img(s['image'],'Vivência pedagógica da Escola CEABA',eager=True)}</div></div></section><section class="section"><div class="wrap"><div class="section-head"><div><span class="eyebrow">APRENDIZAGEM COM SIGNIFICADO</span><h2>Uma proposta para<br>crescer por inteiro.</h2></div><p>{s['description']}</p></div><div class="projects">{projects}</div></div></section><section class="section soft"><div class="wrap content"><span class="eyebrow">ORGANIZE SUA VISITA</span><h2>Vamos conhecer essa etapa de perto?</h2><p>Converse com a equipe sobre a rotina, as turmas e as experiências que fazem parte do dia a dia.</p><div class="schedule">{hours}</div><p style="font-size:14px">Horários apresentados no material pedagógico. Confirme com a equipe as turmas e a disponibilidade para o próximo período letivo.</p><div class="faq"><details><summary>Como posso conhecer a escola?</summary><p>Agende uma visita pelo WhatsApp. Nossa equipe poderá conversar sobre a proposta pedagógica e combinar um horário para receber sua família.</p></details><details><summary>Como funciona a abordagem sociointeracionista?</summary><p>A aprendizagem é construída por meio das interações, das experiências e da participação ativa dos estudantes. O professor faz a mediação, reconhecendo o repertório e o desenvolvimento de cada aluno.</p></details></div></div></section>{cta()}'''

def blog():
    return f'<section class="page-hero"><div class="wrap"><span class="eyebrow">UNIVERSO CEABA</span><h1>Ideias que aproximam.<br>Aprendizados que inspiram.</h1><p class="lead">Conheça as experiências e os princípios que dão vida à nossa proposta pedagógica.</p></div></section><section class="section"><div class="wrap">{stories()}<p class="caption" style="margin-top:40px">Conteúdos institucionais baseados nos materiais pedagógicos da escola. Notícias e eventos serão incluídos após a seleção das publicações.</p></div></section>{cta()}'

def article(a):
    text=''.join(f'<h2>{heading}</h2><p>{paragraph}</p>' for heading,paragraph in a['sections'])
    return f'<section class="page-hero"><div class="wrap content"><div class="article-nav"><a class="text-link" href="blog.html">← Voltar aos conteúdos</a></div><span class="eyebrow">{a["category"]}</span><h1>{a["title"]}</h1><p class="lead">{a["summary"]}</p><span class="article-meta">ESCOLA CEABA · PROPOSTA PEDAGÓGICA</span></div></section><section class="section"><article class="wrap content">{img(a["image"],"Vivência pedagógica da Escola CEABA","article-cover")}{text}<p class="caption">Texto institucional elaborado a partir das apresentações pedagógicas fornecidas pela Escola CEABA.</p></article></section>{cta()}'

def contact():
    return f'''<section class="page-hero"><div class="wrap"><span class="eyebrow">ESTAMOS PERTO</span><h1>Vamos conversar sobre<br>o próximo passo?</h1><p class="lead">Uma visita é o começo de uma relação. Conheça a escola, tire suas dúvidas e descubra nossa proposta.</p></div></section><section class="section"><div class="wrap contact-grid"><div class="contact-box"><span class="eyebrow">ATENDIMENTO PELO WHATSAPP</span><h2>Sua família é bem-vinda.</h2><p>Fale com nossa equipe para agendar uma visita e saber mais sobre as etapas de ensino.</p><p><strong>(62) 99832-5890</strong></p>{button('Conversar com a equipe')}<p class="caption">O botão abre o WhatsApp com uma mensagem pronta. O envio é confirmado por você no aplicativo.</p></div><div><h2>O que você pode<br>conhecer na visita?</h2><ul><li>A proposta pedagógica de cada etapa.</li><li>Os ambientes e a rotina da escola.</li><li>Os programas e projetos desenvolvidos.</li><li>Informações sobre turmas e horários.</li></ul><h3>Acompanhe o CEABA</h3>{social_links()}<div class="notice">Endereço completo, localização e e-mail serão incluídos após a confirmação dos dados de contato da escola.</div></div></div></section>'''

def save(name, title, desc, body, page=''):
    (OUT/name).write_text(shell(title,desc,body,page),encoding='utf-8')

save('index.html','Uma escola que sente. E que transforma.','Conheça a proposta da Escola CEABA: Educação Infantil e Ensino Fundamental com acolhimento, aprendizagem e desenvolvimento integral.',home(),'home')
for s in STAGES:
    save(s['slug']+'.html',s['name'],s['intro'],stage_page(s),s['slug'])
save('blog.html','Universo CEABA', 'Conheça a proposta pedagógica e as experiências de aprendizagem da Escola CEABA.',blog(),'blog')
for a in ARTICLES:
    save('blog-'+a['slug']+'.html',a['title'],a['summary'],article(a),'blog')
save('contato.html','Agende uma visita','Converse com a equipe da Escola CEABA pelo WhatsApp e agende uma visita para conhecer a escola.',contact(),'contato')
(OUT/'robots.txt').write_text('User-agent: *\nDisallow: /\n',encoding='utf-8')
print('9 páginas HTML geradas em public/. Prévia com indexação bloqueada até a revisão e configuração do domínio.')
