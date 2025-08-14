// Bloqueio botão direito
document.addEventListener('contextmenu', function(e) {
    e.preventDefault();
});

// CLI interativo
const input = document.getElementById('cli-input');
const output = document.getElementById('cli-output');

input.addEventListener('keypress', function(e){
    if(e.key === 'Enter'){
        const command = input.value.trim();
        let response = '';

        switch(command){
            case 'help':
                response = 'Comandos disponíveis: whoami, show projects, show tech, contact';
                break;
            case 'whoami':
                response = 'Gustavo Franco - Redes, Automação, Python, Flask';
                break;
            case 'show projects':
                response = '- Meu Site / Portfolio\n- Coletor de Notícias de Cripto\n- Coleta de OLTs\n- Crypto Trends / Crypto Bubbles';
                break;
            case 'show tech':
                response = 'HTML, CSS, Python, Flask, Juniper, ZTE, Linux, CLI';
                break;
            case 'contact':
                response = 'LinkedIn: gustavofrs\nEmail: gustavo.franco@example.com';
                break;
            default:
                response = 'Comando não encontrado. Digite help';
        }

        output.textContent += `\n> ${command}\n${response}`;
        input.value = '';
        output.scrollTop = output.scrollHeight;
    }
});
