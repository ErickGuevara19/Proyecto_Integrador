const formulario = document.getElementById('formulario');
const inputs = document.querySelectorAll('#formulario input');

const expresiones = {
    id_usuario :  /^.{4,10}$/,
    nom_us1 : /^[a-zA-ZÀ-ÿ\s]{3,25}$/,
    nom_us2 : /^[a-zA-ZÀ-ÿ\s]{3,25}$/,
    ape_us1 : /^[a-zA-ZÀ-ÿ\s]{3,25}$/,
    ape_us2 : /^[a-zA-ZÀ-ÿ\s]{3,25}$/,
    calle_pri: /^[a-zA-Z0-9\_\-]{4,10}$/,
    calle_secu: /^[a-zA-Z0-9\_\-]{4,10}$/,
    nro_casa : /^[a-zA-Z0-9\_\-]{4,10}$/,
    parroquia : /^[a-zA-ZÀ-ÿ\s]{3,25}$/,
    telefono : /^\d{7,10}$/,
    email : /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/,
    password : /^.{4,12}$/,
    validacion : /^.{4,12}$/,
    id_rol : /^\d{1,4}$/
}

const campos = {
    id_usuario: false,
    nom_us1: false,
    nom_us2 : false,
    ape_us1: false,
    ape_us2 :  false,
    calle_pri: false,
    calle_secu : false,
    nro_casa: false,
    parroquia: false,
    telefono : false,
    email : false,
    password : false,
    validacion : false,
    id_rol : false,

}

const ValidarFormulario =(e) =>{
    switch (e.target.name) {
        case "id_usuario":
            validarCampo(expresiones.id_usuario, e.target,'id_usuario');
            break;
        case "nom_us1":
            validarCampo(expresiones.nom_us1, e.target,'nom_us1');
            break;
        case "nombre_us2":
            validarCampo(expresiones.nombre_us2, e.target,'nombre_us2');
            break;
        case "ape_us1":
            validarCampo(expresiones.ape_us1, e. target,'ape_us1');
            break;
        case "ape_us2":
            validarCampo(expresiones.ape_us2, e.target,'ape_us2');
            break;
        case "calle_pri":
            validarCampo(expresiones.calle_pri, e.target,'calle_pri');
            break;
        case "calle_secu":
            validarCampo(expresiones.calle_secu, e.target,'calle_secu');
            break;
        case "nro_casa":
            validarCampo(expresiones.nro_casa, e.target,'nro_casa');
            break;
        case "parroquia":
            validarCampo(expresiones.parroquia, e.target,'parroquia');
            break;
        case "telefono":
            validarCampo(expresiones.telefono, e.target,'telefono');
            break;
        case "email":
            validarCampo(expresiones.email, e.target,'email');
            break;
        case "password":
            validarCampo(expresiones.password, e.target,'password');
            break;
        case "validacion":
            validarCampo(expresiones.validacion, e.target,'validacion');
            break;
        case "id_rol":
            validarCampo(expresiones.id_rol, e.target,'id_rol');
            break;
    }



    
}

