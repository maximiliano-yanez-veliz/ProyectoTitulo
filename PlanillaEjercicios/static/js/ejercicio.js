setTimeout(function () {

    // Closing the alert
    $('.alert').alert('close');
}, 4000);

function eliminarEjercicio(id_ejercicio){
    swal("¿Esta seguro que desea eliminar este ejercicio? los datos no se podrán volver a recuperar.", {
        buttons: {
            Confirmar: true
        }
    }).then(function(value) {
        switch (value) {
            case "Confirmar":
                var csrftoken = $("[name=csrfmiddlewaretoken]").val();
                // make POST ajax call
                $.ajax({
                    type: 'POST',
                    url: "/eliminar_ejercicio/"+id_ejercicio,
                    //contentType: "application/json",
                    dataType: 'json',
                    data: {'data': JSON.stringify({"id_ejercicio":id_ejercicio})},
                    headers:{
                        "X-CSRFToken": csrftoken
                    },
                    success: function (response) {
                        // on successfull creating object
                        console.log(response)
                        $('html').scrollTop(0);
                        $("#tablaEjercicio").load(location.href + " #tablaEjercicio");
                        $("#messageEliminar").html('<div class="alert alert-success">'+response.message+'</div>');
                        setTimeout(function () {
                            // Closing the alert
                            $('.alert').alert('close');
                        }, 4000);
                    },
                    error: function (response) {
                        // alert the error if any error occured
                        console.log("error");
                    }
                })
            break;
            case "Cancelar":
                console.log("Accion Cancelada");
            break;
            default:
        }
    });
}