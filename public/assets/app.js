const menuButton = document.querySelector('.mobile-toggle');
const navigation = document.querySelector('#navigation');
function closeMenu() {
  navigation.classList.remove('open');
  menuButton.setAttribute('aria-expanded', 'false');
}
menuButton?.addEventListener('click', () => {
  const open = menuButton.getAttribute('aria-expanded') !== 'true';
  menuButton.setAttribute('aria-expanded', String(open));
  navigation.classList.toggle('open', open);
});
document.addEventListener('keydown', (event) => {
  if (event.key === 'Escape') {
    document.querySelectorAll('.nav details[open]').forEach(item => item.open = false);
    if (navigation?.classList.contains('open')) { closeMenu(); menuButton.focus(); }
  }
});
navigation?.querySelectorAll('a').forEach(link => link.addEventListener('click', closeMenu));
document.addEventListener('click', (event) => {
  document.querySelectorAll('.nav details[open]').forEach(item => {
    if (!item.contains(event.target)) item.open = false;
  });
});
