// test.js
const boton = document.querySelector(".btn");

boton.addEventListener("click", function () {
    alert("¡Gracias por hacer clic!");

    const nombre = prompt("¿Cuál es tu nombre?");
    if (nombre) {
        const confirmar = confirm(`¿Deseas suscribirte como ${nombre}?`);
        if (confirmar) {
            alert(`¡Suscripción completada! Bienvenido, ${nombre}.`);
        } else {
            alert("Suscripción cancelada.");
        }
    } else {
        alert("No ingresaste un nombre.");
    }
});