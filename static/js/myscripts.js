/* modal element 
const yarnModal = document.getElementById('yarnModal');
yarnModal.addEventListener('show.bs.modal', (e) => {
  // Button that triggered the modal
  const button = e.relatedTarget;
  // Extract info from data-mdb-* attributes
  const yarnName = button.getAttribute('data-bs-yarn-name');
  const yarnBody = button.getAttribute('data-bs-yarn-body');
  const yarnProducer = button.getAttribute('data-bs-yarn-producer');
  // If necessary, you could initiate an AJAX request here
  // and then do the updating in a callback.
  //
  // Update the modal's content.
  const modalTitle = yarnModal.querySelector('.modal-title');
  const modalBody = yarnModal.querySelector('.modal-body');
  const modalBodyInput = yarnModal.querySelector('.modal-body input');

  modalTitle.textContent = `${yarnName} yarn from ${yarnProducer}`;
  modalBody.textContent = `Notes about yarn: ${yarnBody}`;
})
*/


$('#yarnModal').on('show.bs.modal', function (event) {
  var button = $(event.relatedTarget) // Button that triggered the modal
  var yarnName = button.data('yarn-name') // Extract info from data-* attributes
  var yarnBody = button.data('yarn-body')


  var modal = $(this)
  modal.find('.modal-title').text('New message to ' + yarnName)
  modal.find('.modal-body').text('Notes: ' + yarnBody)
  modal.find('.modal-body input').val(yarnName)
})