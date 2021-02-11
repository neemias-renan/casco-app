// ABRIR E FECHAR MENU.
    $('#btn_abrirmenu').click(function(){
        $(".menu").show(500);
    })
    $('#btn_fecharmenu').click(function(){
        $(".menu").hide(300);
    })

// ADICIONAR NOVA TARTARUGA

    $('#btn_addtartaruga').click(function(){
        $("#tela_principal").hide();
        $(".registrartartaruga").show()
        $("#primeira_sessao").show()
    })

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
}

$('.btn_ver').click(function(){
    $("#tela_principal").hide()
})
