<?php 
include_once '../config/logout.php';
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../../css/indexstyle.css">
    <title>Sun Sprinter</title>
</head>
<body>
    <header>
        <div class="header-left">
            <img src="../../img/logo.png" alt="Logo" class="logo">

            <button id="toggle-dark" class="nightmode">
                <img src="../../img/moon.png" alt="moon"
                class="moon">
            </button>
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

    <main>
        <main>
            <div class="container">
                <a href="registros.php" class="card">
                    <h5>Registros</h5>
                </a>
                <a href="form.php" class="card">
                    <h5>Cadastros</h5>
                </a>
            </div>
        </main>
<script src="../../js/darkmode.js"></script>    
</body>
</html>