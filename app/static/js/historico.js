// ABRIR E FECHAR MENU.
$('#icon_abrirMenu').click(function(){
    $(".menu").show(500);
    $('#icon_abrirMenu').hide();
})
$('.icon_fecharMenu').click(function(){
    $(".menu").hide(300);
    $('#icon_abrirMenu').show();
})

// VER MAIS
function verMais(id_div){
    $(id_div).toggle()
}
function apagar(confirmarExclusao){
    $(confirmarExclusao).show()
}

function cancelar(div_cancelar){
    $(div_cancelar).hide()
}

function editar(editardados){
    $(".container").hide()
    $(editardados).show()
}