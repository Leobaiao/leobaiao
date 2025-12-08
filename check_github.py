import requests

# Perfil
r = requests.get('https://api.github.com/users/Leobaiao')
u = r.json()

print('=== PERFIL GITHUB ===')
print(f"Nome: {u.get('name')}")
print(f"Bio: {u.get('bio')}")
print(f"Localizacao: {u.get('location')}")
print(f"Website: {u.get('blog')}")
print(f"Empresa: {u.get('company')}")
print(f"Repos publicos: {u.get('public_repos')}")
print(f"Followers: {u.get('followers')}")
print(f"Following: {u.get('following')}")
print(f"Hireable: {u.get('hireable')}")

# Repos
r2 = requests.get('https://api.github.com/users/Leobaiao/repos?sort=updated&per_page=15')
repos = r2.json()

print('\n=== REPOSITORIOS ===')
for i, repo in enumerate(repos):
    lang = repo['language'] or 'N/A'
    stars = repo['stargazers_count']
    forks = repo['forks_count']
    print(f"{i+1}. {repo['name']} | {lang} | Stars: {stars} | Forks: {forks}")
