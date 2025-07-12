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