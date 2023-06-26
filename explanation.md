# Explicações para dinis futuros que nunca mecheram com webscraping.

- Resolvemos duas categorias de problemas no beecrowd: Iniciante (1) e Strings(3)
    - Acessamos os problemas de cada categoria na URL `https://www.beecrowd.com.br/judge/pt/problems/index/<Número Categoria>`
    - Para acessar esses problemas precisamos estar autenticados

## Autenticação com `requests`

Primeiro fazemos o login e analisamos as requisições enviadas pelo navegador com o painel de desenvolvedor do navegador mesmo.
Percebe-se que ao apertar o botão de login, o navegador envia um POST para `https://www.beecrowd.com.br/judge/pt/login`, no painel mesmo conseguimos ver o que é enviado nessa requisição:

- `_csrfToken`
- `email`
- `password`
- `remember_me`
- `_Token[fields]`
- `_Token[unlocked]`

Com a exceção do último, todos os outros dados estão preenchidos com **alguma** coisa, mas eu só entendo o que 3 desses significam. Interessante também que os outros três têm um `_` sublinhado.

Aparentemente um token CSRF tem como objetivo evitar certos tipos de ataques, e é um valor único gerado pelo servidor para cada usuário. Analisando o html da página de login conseguimos ver que existe de fato um input escondido chamado `_csrfToken` que devemos obter e passar no nosso POST.

Usamos o BS para obter esse token, e quanto aos `_Token`, parecem que são valores gerados pela framework interna utilizada deles, e deve permanecer igual sempre. Mas acho que não faz mal buscar da mesma maneira que fizemos com o csrf.

Com isso conseguimos fazer login no beecrowd e acessar as páginas restritas.