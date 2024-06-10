function addTopic() {
  const topicsDiv = document.getElementById('topics');
  const newTopicDiv = document.createElement('div');

  const newLabel = document.createElement('label');
  newLabel.textContent = 'Novo Tópico:';
  const newInput = document.createElement('input');
  newInput.type = 'text';
  newInput.name = 'newTopicName';
  newInput.placeholder = 'Nome do Tópico';

  const newAmountInput = document.createElement('input');
  newAmountInput.type = 'number';
  newAmountInput.step = '0.01';
  newAmountInput.name = 'newTopicAmount';
  newAmountInput.placeholder = 'Valor';

  newTopicDiv.appendChild(newLabel);
  newTopicDiv.appendChild(newInput);
  newTopicDiv.appendChild(newAmountInput);
  topicsDiv.appendChild(newTopicDiv);
}