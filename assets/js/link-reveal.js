// Wrap text links so the reveal sits under their label, not the full hit area.
document.querySelectorAll('a').forEach((link) => {
    if (link.matches('.entry-link, .project-line') ||
        link.querySelector('.link-label, img, picture, pre, div, p, h1, h2, h3, h4') ||
        !link.textContent.trim()) return;

    const label = document.createElement('span');
    label.className = 'link-label';
    while (link.firstChild) label.appendChild(link.firstChild);
    link.appendChild(label);
});
