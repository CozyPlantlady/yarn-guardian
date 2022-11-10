// Modal code from Bootstrap
$('#yarnModal').on('show.bs.modal', function (event) {
  var button = $(event.relatedTarget) // Button that triggered the modal
  var yarnName = button.data('yarn-name') // Extract info from data-* attributes
  var yarnBody = button.data('yarn-body')


  var modal = $(this)
  modal.find('.modal-title').text('New message to ' + yarnName)
  modal.find('.modal-body').text('Notes: ' + yarnBody)
  modal.find('.modal-body input').val(yarnName)
})
