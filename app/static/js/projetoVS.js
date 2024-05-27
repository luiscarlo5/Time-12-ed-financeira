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
