/* modal element */
const exampleModal = document.getElementById('exampleModal');
exampleModal.addEventListener('show.bs.modal', (e) => {
  // Button that triggered the modal
  const button = e.relatedTarget;
  // Extract info from data-mdb-* attributes
  const yarn = button.getAttribute('data-bs-whatever');
  // If necessary, you could initiate an AJAX request here
  // and then do the updating in a callback.
  //
  // Update the modal's content.
  const modalTitle = exampleModal.querySelector('.modal-title');
  const modalBodyInput = exampleModal.querySelector('.modal-body input');

  modalTitle.textContent = `New message to ${yarn}`;
  modalBodyInput.value = recipient;
})