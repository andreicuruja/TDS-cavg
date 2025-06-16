

<!-- ISSO É O LOGIN.HTML TROCADO PRA INDEX PQ SE NAO N CONSIGO FAZER FUNCIONAR KKKKKKKKKKKKKKKKKK -->


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="src/css/indexstyle.css">
    <title>Sun Sprinter</title>
</head>
<body>
    <header>
        <div class="header-left">
            <img src="src/img/logo.png" alt="Logo" class="logo">

            <button id="toggle-dark" class="nightmode">
                <img src="src/img/moon.png" alt="moon"
                class="moon">
            </button>
            <!-- 🌙 Modo Noturno e o Script pra ele na linha 33 -->
        </div>
    
        <div class="header-center">
            <nav class="nav-links">

            </nav>
        </div>
    
        <div class="header-right">
            <h1>Sun Sprinter<br>Locadora de Veículos</h1>
        </div>
    </header>
    <div class="header-underline"></div>
    <script>
        function setCookie(nome, valor, dias) {
            const d = new Date();
            d.setTime(d.getTime() + (dias * 24 * 60 * 60 * 1000));
            const expira = "expires=" + d.toUTCString();
            document.cookie = nome + "=" + valor + ";" + expira + ";path=/";
        }
        function getCookie(nome) {
            const nomeEQ = nome + "=";
            const cookies = decodeURIComponent(document.cookie).split(';');
            for (let i = 0; i < cookies.length; i++) {
                let c = cookies[i].trim();
                if (c.indexOf(nomeEQ) === 0) return c.substring(nomeEQ.length, c.length);
            }
            return "";
        }
        if (getCookie("modoNoturno") === "true") {
            document.body.classList.add("dark-mode");
        }
        const toggleButton = document.getElementById("toggle-dark");
        toggleButton.addEventListener("click", () => {
            document.body.classList.toggle("dark-mode");
            const modoAtivo = document.body.classList.contains("dark-mode");
            setCookie("modoNoturno", modoAtivo, 30); // 30 dias de validade pro cookie
        });
        </script>
<form action="src/php/routes/login.php" method="post">
    <label>Login: <input type="text" name="login" required></label><br>
    <label>Senha: <input type="password" name="senha" required></label><br>
    <input type="submit" name="botao" value="Entrar">
</form>
</body>
</html>