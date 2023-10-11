document.addEventListener("DOMContentLoaded", function() {
    // Encuentra el enlace y el contenido de productos
    var enlaceProductos = document.querySelector('a[href="#productos"]');
    var contenidoProductos = document.getElementById('productos');

    // Agrega un evento de clic al enlace si se encuentra
    if (enlaceProductos && contenidoProductos) {
        enlaceProductos.addEventListener('click', function(e) {
            // Previene el comportamiento predeterminado del enlace
            e.preventDefault();

            // Cambia la visibilidad del contenido de productos
            contenidoProductos.style.display = contenidoProductos.style.display === 'none' ? 'block' : 'none';
        });
    }

    // Esto solo se ejecutará una vez, no es necesario repetirlo
    console.log("tas mal cabron");
}); 
