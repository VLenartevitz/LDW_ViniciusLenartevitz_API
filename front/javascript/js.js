// Capturar o botão de cadastrar
const createBtn = document.getElementById("createBtn")
// Escuta ao evento de clique do usuário no botão
createBtn.addEventListener("click", cadastrarLivro)
// Capturar o botão de alterar
const updateBtn = document.getElementById("updateBtn")
// Escuta ao evento de clique do usuário no botão
updateBtn.addEventListener("click", atualizarLivro)

// Enviando uma requisição GET para API para listar todos os livros
axios.get("http://localhost:5000/livros").then((response) => {
    const livros = response.data
    const listaLivros = document.getElementById("books")

    livros.forEach((livro) => {
      let item = document.createElement("li")

      // Setando o atributo ID para cada livro
      item.setAttribute("data-id", livro._id)
      item.setAttribute("data-titulo", livro.titulo)
      item.setAttribute("data-autor", livro.autor)
      item.setAttribute("data-ano", livro.ano)
      item.setAttribute("data-descricao", livro.descricao)

      item.innerHTML = `<h4>${livro.titulo}</h4>
        <p>Autor: ${livro.autor}</p>
        <p>Descrição: ${livro.descricao}</p> 
        <p>Ano: ${livro.ano}</p>
        <p>ID: ${livro._id}</p>`

        var deleteBtn = document.createElement("button")
        deleteBtn.innerHTML = "Deletar"
        deleteBtn.classList.add("btn", "btn-danger", "mb-3")
        deleteBtn.addEventListener("click", () => {
          deletarLivro(item)
        })

        var editBtn = document.createElement("button")
        editBtn.innerHTML = "Editar"
        editBtn.classList.add("btn", "btn-warning", "mb-3")
        editBtn.addEventListener("click", function(){
          carregarFormulario(item)
        })

        item.appendChild(deleteBtn)
        item.appendChild(editBtn)
        listaLivros.appendChild(item)
      })
    }).catch((error) => {
      console.log(error)
    })

// Função para DELETAR livros
function deletarLivro(listItem) {
  const id = listItem.getAttribute("data-id")
  axios.delete(`http://localhost:5000/livros/${id}`).then(response => {
      alert("Livro deletado!")
      location.reload()
  }).catch(err => {
      console.log(err)
  })
}

// Função para CADASTRAR livros
function cadastrarLivro(){
  const form = document.getElementById("createForm")
  form.addEventListener("submit", function(event) {
    event.preventDefault() // Evita o envio padrão do formulário
  })

  const tituloInput = document.getElementById("titulo")
  const autorInput = document.getElementById("autor")
  const descricaoInput = document.getElementById("descricao")
  const anoInput = document.getElementById("ano")

  const livro = {
    titulo : tituloInput.value,
    autor: autorInput.value,
    descricao : descricaoInput.value,
    ano : anoInput.value,
  }
  // Enviando as informações do livro para API
  axios.post("http://localhost:5000/livros", livro).then(response => {
    if (response.status == 201) {
      alert("Livro cadastrado com sucesso!")
      location.reload()
    }
  }).catch(error => {
    console.log(error)
  })

}

// Função para carregar o formulário de edição
function carregarFormulario(listItem) {
  const id = listItem.getAttribute("data-id")
  const titulo = listItem.getAttribute("data-titulo")
  const autor = listItem.getAttribute("data-autor")
  const ano = listItem.getAttribute("data-ano")
  const descricao = listItem.getAttribute("data-descricao")
  document.getElementById("idEdit").value = id
  document.getElementById("tituloEdit").value = titulo
  document.getElementById("autorEdit").value = autor
  document.getElementById("anoEdit").value = ano
  document.getElementById("descricaoEdit").value = descricao
}

// Função para ALTERAR o livro
function atualizarLivro() {
  const form = document.getElementById("editForm")
  form.addEventListener("submit", function(event) {
    event.preventDefault() // Evita o envio padrão do formulário
  })

  // Aqui será enviado as informações para atualizar o livro
  const idInput = document.getElementById("idEdit")
  const tituloInput = document.getElementById("tituloEdit")
  const autorInput = document.getElementById("autorEdit")
  const anoInput = document.getElementById("anoEdit")
  const descricaoInput = document.getElementById("descricaoEdit")

  const livro = {
    titulo : tituloInput.value,
    autor: autorInput.value,
    descricao : descricaoInput.value,
    ano : anoInput.value
  }

  var id = idInput.value

  axios.put(`http://localhost:5000/livros/${id}`, livro).then(response => {
    if (response.status == 200) {
      alert("Livro atualizado com sucesso!")
      location.reload()
    }
  }).catch(error => {
    console.log(error)
  })

}
