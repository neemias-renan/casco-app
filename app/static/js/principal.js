$('#btn_registerTartaruga').click(function(){
    $(".primeira_sessao").show();
    $("#principal").hide()
})

$('#btn_voltar1').click(function(){
    $(".primeira_sessao").hide();
    $("#principal").show()
})

$('#btn_voltar2').click(function(){
    $(".segunda_sessao").hide();
    $(".primeira_sessao").show()
})

$('#btn_continuar').click(function(){
    $(".primeira_sessao").hide();
    $(".segunda_sessao").show()
});

$('#detalhar').click(function(){
    $("#detalhes").toggle()
})

$('#checkboxMonitoria').click(function(){
    $("#informacoesMonitoria").toggle()
})

$('#atribuirCoordenadas').click(function(){
    $("#checkboxCoordenadas").toggle()
})