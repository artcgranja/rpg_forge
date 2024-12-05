function updateClassInfo(classeId) {
    if (!classeId) {
        document.getElementById('classe-info').style.display = 'none';
        return;
    }

    fetch(`/get-classe-info/${classeId}/`)
        .then(response => response.json())
        .then(data => {
            document.getElementById('vida-base').textContent = data.vida_base;
            document.getElementById('mana-base').textContent = data.mana_base || 'N/A';
            document.getElementById('classe-info').style.display = 'block';
        })
        .catch(error => console.error('Erro:', error));
}