function initTabNav() {
  const tabButton = document.querySelector('.quem-somos button')
  const tabContent = document.querySelectorAll('.apresentacao-equipe-text section');
  const tabImages = document.querySelectorAll('.apresentacao-equipe-img li');

  const tabButtonGrafico = document.querySelectorAll('.funcionalidades-informativo .grafico-botoes a')
  const tabGrafico = document.querySelectorAll('.funcionalidades-informativo .grafico-img img')

  let posicao = 0;
  if (tabButton && tabContent.length && tabImages.length) {
    tabContent[0].classList.add('ativo');
    tabImages[0].classList.add('ativo');

    function activeTab(posicao) {
      tabContent.forEach((section) => {
        section.classList.remove('ativo');
      });
      tabContent[posicao].classList.add('ativo');

      tabImages.forEach((li) => {
        li.classList.remove('ativo');
      });
      tabImages[posicao].classList.add('ativo');
    }
    function activeGraf(index) {
      tabGrafico.forEach((img) => {
        img.classList.remove('ativo');
      });
      tabGrafico[index].classList.add('ativo');
    }

    tabButton.addEventListener('click', () =>{
      posicao = (posicao + 1) % tabContent.length; 
      activeTab(posicao);
    });

    tabButtonGrafico.forEach((itemMenu, index) => {
      itemMenu.addEventListener('click', () => {
        activeGraf(index);
      });
    });
  }
}
document.addEventListener('DOMContentLoaded', initTabNav);

function rolardevagar(sectionId) {
  var section = document.getElementById(sectionId);
  var topPos = section.offsetTop;
  var currentPos = window.pageYOffset;
  var distance = topPos - currentPos;
  var duration = 1000; // Tempo total da animação em milissegundos (1 segundo)

  var startTime = null;

  function animation(currentTime) {
    if (startTime === null) startTime = currentTime;
    var elapsedTime = currentTime - startTime;
    var scrollAmount = ease(elapsedTime, currentPos, distance, duration);
    window.scrollTo(0, scrollAmount);
    if (elapsedTime < duration) requestAnimationFrame(animation);
  }

  // Função de interpolação para uma rolagem mais suave
  function ease(t, b, c, d) {
    t /= d / 2;
    if (t < 1) return c / 2 * t * t + b;
    t--;
    return -c / 2 * (t * (t - 2) - 1) + b;
  }

  requestAnimationFrame(animation);
}
