$(document).ready(function () {

    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
    });

});


// ADICIONAR NOVA TARTARUGA
$('#btn_continuar').click(function(){
    $("#primeira_sessao").hide();
    $("#segunda_sessao").show()
})

$('#btn_voltar_sessao').click(function(){
    $("#segunda_sessao").hide();
    $("#primeira_sessao").show();
})
// VER DETALHES - NOTIFICAÇÕES
function btn_abrir(id_div){
    $(id_div).show();
    $("#inicio-section").hide();
}

$('#btn_fechar').click(function(){
    $('.div_detalhes').hide();
    $("#inicio-section").show();
})

// BOTÃO - CONFIRMAR EXCLUSÃO DE MEMBROS
function apagar(confirmarExclusao){
    $(confirmarExclusao).show()
}

function cancelar(div_cancelar){
    $(div_cancelar).hide()
}
// BOTÃO VER MAIS DO HISTORICO
function verMais(id_div){
    $(id_div).toggle()
}

// ESCONDER ALERTAS DE ERROS
$("#add_email").click(function(){
    $("#alert_email").hide()
});

$("#add_senha").click(function(){
    $("#alert_senha").hide()
});
$("#add_nomedaequipe").click(function(){
    $("#alert_equipe").hide()
});
$("#add_codigo").click(function(){
    $("#alert_codigo").hide()
});