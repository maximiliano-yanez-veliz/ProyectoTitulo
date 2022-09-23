const $formularioEjercicio = document.getElementById('formularioEjercicio');
const $txtTitulo = document.getElementById('txtTitulo');
const $txtDescripcion = document.getElementById('txtDescripcion');
const btnsEliminacion = document.querySelectorAll('.btnEliminacion');


(function () {

    notificacionSwal(document.title, "Listado de Ejercicios", "success", "Ok");

    $formularioEjercicio.addEventListener('submit' ,function(e){
        let titulo=String($txtTitulo.value).trim();
        let descripcion=String($txtDescripcion.value).trim();
        if(titulo.length===0){
            notificacionSwal(document.title, "el nombre no puede ir vacio....", "warning", "Ok");
            e.preventDefault();}
                else if(descripcion.length ===0){
                    notificacionSwal(document.title, "La descripcion no puede ir vacio....", "warning", "Ok");
                    e.preventDefault();
                }   else{
                    notificacionSwal(document.title, "Ejercicio Guardado Exitosamente", "warning", "Ok");
            } 
    } );

    btnsEliminacion.forEach(btn => {
        btn.addEventListener("click", function (e) {
                e.preventDefault();
                Swal.fire({
                    title:"¿Confirma la Eliminacion del Ejercicio?",
                    showCancelButton:true,
                    confirmButtonText:"Eliminar",
                    confirmButtonColor: "#d33",
                    backdrop: true,
                    showLoaderOnConfirm: true,
                    preConfirm: () => {
                        location.href = e.target.href;
                    },
                    allowOutsideClick: () =>false,
                    allowEscapeKey: () =>false,

                });
            });

        });

})();