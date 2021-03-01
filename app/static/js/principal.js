// ABRIR E FECHAR MENU.
    $('#icon_abrirMenu').click(function(){
        $(".menu").show(500);
        $('#icon_abrirMenu').hide();
    })
    $('.icon_fecharMenu').click(function(){
        $(".menu").hide(300);
        $('#icon_abrirMenu').show();
    })

// ADICIONAR NOVA TARTARUGA
    $('#btn_continuar').click(function(){
        $("#primeira_sessao").hide();
        $("#segunda_sessao").show()
    })

    $('#btn_voltar').click(function(){
        $("#segunda_sessao").hide();
        $("#primeira_sessao").show()
    })
// VER DETALHES - NOTIFICAÇÕES
function btn_abrir(id_div){
    $(id_div).show()
    // $(".visualizar_notificacao").show()
    $("#inicio-section").hide()
}
