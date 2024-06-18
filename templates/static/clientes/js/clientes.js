function add_carro(){
    container = document.getElementById("form-carro");

    html = "<br> <div class='row'> <div class='col-md'> <input type='text' placeholder='carro' class='form-control' name='carro' > </div> <div class='col-md'> <input type='text' placeholder='Placa' class='form-control' name='placa' > </div> <div class='col-md'> <input type='number' placeholder='ano' class='form-control' name='ano'> </div>"

    container.innerHTML += html
}

function exibir_form(tipo){
    
    add_cliente = document.getElementById('adicionar-cliente');
    att_cliente = document.getElementById('att-cliente');

    if(tipo == "1"){
        add_cliente.style.display =  "block";
        att_cliente.style.display = "none";
    }else if(tipo == "2"){
        add_cliente.style.display = "none";
        att_cliente.style.display = "block";
    }
function dados_cliente(){
    cliente = document.getElementById('cliente-select');
    csrf_token = document.querySelector('[name=csrfmiddlewaretoken]').value;
    featch("/clientes/atualiza_cliente/",{
        method: 'POST',
        Headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrf_token
        },
        body: JSON.stringify({
            'cliente': cliente.value
        })
    }).then(function(result){
        return result.json();
    }).then(function(data){
        console.log(teste);
    })
}
}