let currentPage = 1;
const itemsPerPage = 50; // 10 linhas * 5 colunas = 50 filmes por página

function displayPage(page) {
    const grid = document.getElementById('movielistGrid');
    const items = grid.getElementsByClassName('movielist-item');
    const totalItems = items.length;
    const totalPages = Math.ceil(totalItems / itemsPerPage);

    // Calcula o início e o fim dos itens a serem exibidos
    const startIndex = (page - 1) * itemsPerPage;
    const endIndex = Math.min(startIndex + itemsPerPage, totalItems);

    // Exibe apenas os itens da página atual
    for (let i = 0; i < totalItems; i++) {
        items[i].style.display = (i >= startIndex && i < endIndex) ? 'flex' : 'none';
    }

    // Atualiza a página atual
    currentPage = page;

    // Atualiza a numeração das páginas
    updatePageNumbers(totalPages);
}

function updatePageNumbers(totalPages) {
    const pageNumbersContainer = document.getElementById('pageNumbers');
    pageNumbersContainer.innerHTML = ''; // Limpa números antigos

    for (let i = 1; i <= totalPages; i++) {
        const pageNumber = document.createElement('button');
        pageNumber.textContent = i;
        pageNumber.className = 'page-number';
        if (i === currentPage) {
            pageNumber.classList.add('active');
        }
        pageNumber.onclick = () => displayPage(i);
        pageNumbersContainer.appendChild(pageNumber);
    }
}

function changePage(direction) {
    const totalItems = document.getElementById('movielistGrid').getElementsByClassName('movielist-item').length;
    const totalPages = Math.ceil(totalItems / itemsPerPage);

    let newPage = currentPage + direction;

    if (newPage < 1) newPage = 1;
    if (newPage > totalPages) newPage = totalPages;

    displayPage(newPage);
}

// Exibe a primeira página ao carregar
document.addEventListener('DOMContentLoaded', () => {
    const totalItems = document.getElementById('movielistGrid').getElementsByClassName('movielist-item').length;
    const totalPages = Math.ceil(totalItems / itemsPerPage);
    displayPage(currentPage);
    updatePageNumbers(totalPages);
});