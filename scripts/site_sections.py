"""Seções e páginas de apoio do site. Produz apenas HTML estático."""
from html import escape
from urllib.parse import quote, urlsplit
import re


def testimonials(data):
    cards = ''.join(f'<figure class="testimonial"><span class="quote-mark" aria-hidden="true">“</span><blockquote>{escape(item["quote"])}</blockquote><figcaption>{escape(item["name"])}</figcaption></figure>' for item in data['testimonials'])
    return f'<section class="section" id="depoimentos"><div class="wrap"><div class="section-head"><div><span class="eyebrow">VÍNCULOS QUE FAZEM PARTE</span><h2>Quem vive o CEABA<br>tem o que contar.</h2></div><p>Palavras de famílias que fazem parte da nossa história.</p></div><div class="testimonials">{cards}</div></div></section>'


def instagram(data, button):
    profile = escape(data['instagram']['profile_url'], quote=True)
    widget = data['instagram'].get('widget_url')
    frame = ''
    if widget:
        parts = urlsplit(widget)
        if parts.scheme != 'https' or parts.netloc != 'snapwidget.com' or not re.fullmatch(r'/embed/\d+', parts.path) or parts.query or parts.fragment:
            raise ValueError('O widget deve ser um endereço público https://snapwidget.com/embed/NUMERO, sem credenciais.')
        frame = f'<div class="instagram-widget"><iframe src="{escape(widget, quote=True)}" class="snapwidget-widget" title="Publicações do Instagram da Escola CEABA" loading="lazy" referrerpolicy="strict-origin-when-cross-origin" style="border:0;width:100%;height:640px" scrolling="no"></iframe></div><script src="https://snapwidget.com/js/snapwidget.js" async></script>'
    return f'<section class="section soft" id="instagram"><div class="wrap"><div class="section-head"><div><span class="eyebrow">ACONTECE NO CEABA</span><h2>Um cotidiano cheio<br>de descobertas.</h2></div><p>Projetos, encontros e momentos que aproximam nossa comunidade. Acompanhe a escola também no Instagram.</p></div>{frame}<div class="instagram-invite"><div><span class="eyebrow">@ESCOLA.CEABA</span><h3>Mais perto da nossa rotina.</h3><p>Veja as publicações da escola e acompanhe as novidades no perfil oficial.</p></div>{button("Acompanhar no Instagram", "outline", profile)}</div></div></section>'


def integral_promo(button, img):
    return f'<section class="section soft"><div class="wrap split"><div><span class="eyebrow">PERÍODO INTEGRAL</span><h2>Mais tempo para<br>aprender e conviver.</h2><p>Uma rotina que amplia as experiências da escola, com acompanhamento das tarefas, oficinas e atividades que conectam conhecimento, movimento e criatividade.</p>{button("Conhecer o Integral", "", "integral.html")}</div><div class="split-photo">{img("musica", "Crianças em uma atividade coletiva na Escola CEABA")}</div></div></section>'


def integral(button, img, cta):
    activities = [
        ('Aprendizagem acompanhada', 'A lição de casa é realizada na escola de forma orientada, com acompanhamento pedagógico.'),
        ('Oficinas de leitura', 'Histórias e diferentes formas de ler convidam a imaginar, compartilhar ideias e ampliar o repertório.'),
        ('Arte e música', 'Oficinas que abrem espaço para a expressão, a criatividade e novas formas de perceber o mundo.'),
        ('Corpo e movimento', 'Atividades como dança livre, jiu-jítsu e natação integram a proposta apresentada pela escola. Consulte a programação de cada turma.')
    ]
    cards = ''.join(f'<article class="project"><h3>{title}</h3><p>{text}</p></article>' for title, text in activities)
    return f'<section class="page-hero"><div class="wrap"><div class="crumb"><a href="index.html">Início</a> / Integral</div><div class="split"><div><span class="eyebrow">PERÍODO INTEGRAL</span><h1>Mais tempo para crescer.<br>Mais espaço para descobrir.</h1><p class="lead">Um dia de experiências que conectam aprendizagem, convivência, movimento e criatividade.</p>{button("Conversar sobre o Integral")}</div>{img("acolhimento", "Vivência coletiva de estudantes da Escola CEABA", eager=True)}</div></div></section><section class="section"><div class="wrap"><div class="section-head"><div><span class="eyebrow">UMA ROTINA COM SIGNIFICADO</span><h2>Cuidar do aprender.<br>Valorizar o conviver.</h2></div><p>A proposta do Integral amplia as oportunidades de aprendizagem e diálogo. As experiências são articuladas ao projeto pedagógico e conduzidas por profissionais qualificados.</p></div><div class="projects">{cards}</div></div></section><section class="section soft"><div class="wrap content"><span class="eyebrow">CADA CRIANÇA, UM PERCURSO</span><h2>Conheça a rotina para a sua família.</h2><p>As atividades buscam estimular a coordenação motora, a sociabilidade, os valores e o pensamento de forma lúdica e responsável.</p><p>Converse com a equipe para conhecer as turmas atendidas, os horários, a alimentação, as atividades disponíveis e as condições de participação no Integral.</p>{button("Tirar dúvidas sobre o Integral")}<div class="faq"><details><summary>Há acompanhamento das tarefas escolares?</summary><p>Sim. A proposta inclui acompanhamento pedagógico para a realização orientada da lição de casa na escola.</p></details><details><summary>Como saber a programação e os horários?</summary><p>A equipe da escola orienta sobre a rotina de cada turma, as atividades oferecidas e a disponibilidade. Agende uma conversa pelo WhatsApp.</p></details></div></div></section>{cta()}'


def portal(data, button, wa):
    cards = []
    for item in data['platforms']:
        if item['url']:
            action = button('Acessar '+item['name'], '', escape(item['url'], quote=True))
        else:
            support = 'https://wa.me/5562998325890?text='+quote('Olá! Preciso de orientação para acessar o Meu Bernoulli da Escola CEABA.')
            action = button('Pedir orientação de acesso', 'outline', support)
        cards.append(f'<article class="platform-card"><span class="eyebrow">{escape(item["tag"])}</span><h2>{escape(item["name"])}</h2><p>{escape(item["description"])}</p>{action}</article>')
    return '<section class="page-hero"><div class="wrap"><span class="eyebrow">PARA ESTUDANTES E FAMÍLIAS</span><h1>Seus caminhos de aprendizagem,<br>em um só lugar.</h1><p class="lead">Encontre os acessos às plataformas utilizadas pela comunidade CEABA.</p></div></section><section class="section"><div class="wrap"><div class="platforms">'+''.join(cards)+'</div><div class="portal-help"><h2>Precisa de ajuda para entrar?</h2><p>Se ainda não recebeu seu cadastro ou não consegue acessar, fale com a equipe da escola. Os acessos às plataformas são feitos nos próprios serviços, com o cadastro correspondente.</p>'+button('Falar com a escola', 'outline', wa)+'</div></div></section>'


def contact(data, button, social_links):
    c = data['contact']
    return f'<section class="page-hero"><div class="wrap"><span class="eyebrow">ESTAMOS PERTO</span><h1>Vamos conversar sobre<br>o próximo passo?</h1><p class="lead">Uma visita é o começo de uma relação. Conheça a escola, tire suas dúvidas e descubra nossa proposta.</p></div></section><section class="section"><div class="wrap contact-grid"><div class="contact-box"><span class="eyebrow">SUA FAMÍLIA É BEM-VINDA</span><h2>Agende uma visita.</h2><p>Fale com nossa equipe para conhecer a escola, a rotina e as etapas de ensino.</p><p class="contact-number">WhatsApp<br><strong>(62) 99832-5890</strong></p>{button("Conversar com a equipe")}<p class="caption">O botão abre o WhatsApp com uma mensagem pronta. O envio é confirmado por você no aplicativo.</p><div class="contact-separator"></div><h3>Telefone da escola</h3><a class="text-link" href="{c["phone_uri"]}">{escape(c["phone"])}</a></div><div class="contact-location"><span class="eyebrow">ONDE ESTAMOS</span><h2>Venha nos conhecer.</h2><address>{escape(c["address"])}<br><span>{escape(c["address_detail"])}</span></address>{button("Ver localização no Maps", "outline", c["maps_url"])}<h3>Atendimento</h3><p>{escape(c["hours"])}</p><h3>Acompanhe o CEABA</h3>{social_links()}<a class="text-link" href="portal-do-aluno.html">Já faz parte da escola? Acesse as plataformas ↗</a></div></div></section>'
