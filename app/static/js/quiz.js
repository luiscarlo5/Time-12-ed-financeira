function checkAnswer(answer) {

  let resposta = document.querySelectorAll('.quiz main.ativo article.ativo .resposta div'); 
  resposta[0].classList.remove('ativo');
  resposta[1].classList.remove('ativo');

  if (answer === 'certo') {
    resposta[0].classList.add('ativo');
    resposta[1].classList.remove('ativo');

  } else {
    resposta[1].classList.add('ativo');
    resposta[0].classList.remove('ativo');
  }
}
function deleteAnswer(){
  let resposta = document.querySelectorAll('.quiz .questions main.ativo article.ativo .resposta div'); 
  resposta[0].classList.remove('ativo');
  resposta[1].classList.remove('ativo');
}

function initTabQuestions() {
  const tabButton1 = document.querySelector('.quiz .aux1 button');
  const tabTopicos = document.querySelectorAll('.quiz .questions main');

  const tabButton2 = document.querySelector('.quiz .aux2 button');
  let tabPerguntas = document.querySelectorAll('.quiz .questions main article');

  let posicao1 = 0; // topicos
  let posicao2 = 0; // perguntas
  if ( tabTopicos.length && tabPerguntas.length ) {
    tabTopicos[0].classList.add('ativo');
    tabPerguntas[0].classList.add('ativo');
    tabPerguntas = document.querySelectorAll('.quiz .questions main.ativo article');

    function activeTopics(posicao) {
      tabTopicos.forEach((main) => {
        main.classList.remove('ativo');
      });
      tabTopicos[posicao].classList.add('ativo');
      tabPerguntas = document.querySelectorAll('.quiz .questions main.ativo article');
      resposta = document.querySelectorAll('.quiz main.ativo article.ativo .resposta div'); 
      tabPerguntas[0].classList.add('ativo');
      posicao2 = 0; // pergunta
    }

    function activeQuestions(posicao) {
      console.log('ai cachorro');
      tabPerguntas.forEach((article) => {
        article.classList.remove('ativo');
      });
      tabPerguntas[posicao].classList.add('ativo');
    }

    tabButton1.addEventListener('click', () =>{
      posicao1 = (posicao1 + 1) % tabTopicos.length; 
      activeTopics(posicao1);
    });

    tabButton2.addEventListener('click', () =>{
      console.log("aaah cachorro");
      deleteAnswer();
      posicao2 = (posicao2 + 1) % tabPerguntas.length;
      activeQuestions(posicao2);
    });

  }
}
document.addEventListener('DOMContentLoaded', initTabQuestions);
