function confirmarEliminar() {
    var confirmacion = confirm("¿Estás seguro de que deseas eliminar?");

    if (confirmacion) {
      // Aquí puedes realizar la acción de eliminación
      // Por ejemplo, enviar una solicitud al servidor para eliminar el elemento
      console.log("Elemento eliminado");
    }
}