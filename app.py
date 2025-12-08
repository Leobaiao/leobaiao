"""
Portfólio Flask - Leonardo Baião
Um portfólio moderno e dinâmico com dados do GitHub
"""

from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# Dados do desenvolvedor
GITHUB_USERNAME = "Leobaiao"
GITHUB_API_URL = f"https://api.github.com/users/{GITHUB_USERNAME}"

def get_github_data():
    """Busca dados do usuário no GitHub"""
    try:
        user_response = requests.get(GITHUB_API_URL)
        repos_response = requests.get(f"{GITHUB_API_URL}/repos?sort=updated&per_page=6")
        
        if user_response.status_code == 200 and repos_response.status_code == 200:
            return {
                "user": user_response.json(),
                "repos": repos_response.json()
            }
    except Exception as e:
        print(f"Erro ao buscar dados do GitHub: {e}")
    
    return None

# Dados do desenvolvedor (fallback)
DEVELOPER_DATA = {
    "name": "Leonardo Baião",
    "username": "Leobaiao",
    "bio": "🧑🏽‍💻 Desenvolvedor focado em resolver problemas com automação 🧑🏽‍💻\n\n🤖 Atualmente explorando Appium, Web Drivers e APIs 🤖",
    "avatar_url": "https://avatars.githubusercontent.com/u/143014306?v=4",
    "github_url": "https://github.com/Leobaiao",
    "skills": [
        {"name": "Python", "level": 90, "icon": "fab fa-python"},
        {"name": "Automação", "level": 85, "icon": "fas fa-robot"},
        {"name": "Selenium/Appium", "level": 80, "icon": "fas fa-cogs"},
        {"name": "TypeScript", "level": 75, "icon": "fab fa-js"},
        {"name": "APIs REST", "level": 85, "icon": "fas fa-plug"},
        {"name": "C#", "level": 70, "icon": "fas fa-code"},
        {"name": "Flask", "level": 80, "icon": "fas fa-flask"},
        {"name": "HTML/CSS", "level": 85, "icon": "fab fa-html5"}
    ],
    "projects": [
        {
            "name": "confeitariaEuforia",
            "description": "Site para confeitaria Euforia - E-commerce completo com carrinho e integração WhatsApp",
            "url": "https://github.com/Leobaiao/confeitariaEuforia",
            "demo_url": "https://confeitariaeuforia.vercel.app",
            "language": "TypeScript",
            "icon": "fas fa-birthday-cake"
        },
        {
            "name": "whatsapp-automacao",
            "description": "Projeto de automação avançado para WhatsApp com integração de APIs",
            "url": "https://github.com/Leobaiao/whatsapp-automacao",
            "demo_url": None,
            "language": "Python",
            "icon": "fab fa-whatsapp"
        },
        {
            "name": "Desbloqueio",
            "description": "Projeto de automação para cadastro de WhatsApp com Appium",
            "url": "https://github.com/Leobaiao/Desbloqueio",
            "demo_url": None,
            "language": "Python",
            "icon": "fas fa-unlock"
        },
        {
            "name": "maturacao",
            "description": "Serviço de maturação de chips com uso de IA e API de envios",
            "url": "https://github.com/Leobaiao/maturacao",
            "demo_url": None,
            "language": "Python",
            "icon": "fas fa-sim-card"
        },
        {
            "name": "saas-envio",
            "description": "Plataforma SaaS para gerenciamento de envios em massa",
            "url": "https://github.com/Leobaiao/saas-envio",
            "demo_url": "https://v0-duplicate-of-minimalist-wirefram.vercel.app",
            "language": "TypeScript",
            "icon": "fas fa-paper-plane"
        },
        {
            "name": "WebApiLivro",
            "description": "Web API com CRUD completo - Estudo de .NET Core",
            "url": "https://github.com/Leobaiao/WebApiLivro",
            "demo_url": None,
            "language": "C#",
            "icon": "fas fa-book"
        }
    ],
    "services": [
        {
            "title": "Automação de Processos",
            "description": "Desenvolvimento de bots e scripts para automatizar tarefas repetitivas, economizando tempo e recursos.",
            "icon": "fas fa-robot"
        },
        {
            "title": "Integração de APIs",
            "description": "Conexão entre sistemas através de APIs REST, webhooks e integrações customizadas.",
            "icon": "fas fa-plug"
        },
        {
            "title": "Web Scraping",
            "description": "Extração automatizada de dados de websites para análise e processamento.",
            "icon": "fas fa-spider"
        },
        {
            "title": "Desenvolvimento Web",
            "description": "Criação de sites e aplicações web modernas com foco em performance e experiência do usuário.",
            "icon": "fas fa-globe"
        }
    ]
}

@app.route('/')
def index():
    """Página principal do portfólio"""
    github_data = get_github_data()
    
    if github_data:
        # Atualiza dados com informações do GitHub
        DEVELOPER_DATA["public_repos"] = github_data["user"].get("public_repos", 13)
        DEVELOPER_DATA["followers"] = github_data["user"].get("followers", 0)
        DEVELOPER_DATA["following"] = github_data["user"].get("following", 0)
    
    return render_template('index.html', data=DEVELOPER_DATA)

@app.route('/api/github')
def api_github():
    """API endpoint para dados do GitHub"""
    github_data = get_github_data()
    if github_data:
        return jsonify(github_data)
    return jsonify({"error": "Não foi possível carregar dados do GitHub"}), 500

if __name__ == '__main__':
    import os
    debug = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=debug, host='0.0.0.0', port=port)

