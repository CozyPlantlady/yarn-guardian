// Modal code from Bootstrap
$('#yarnModal').on('show.bs.modal', function (event) {
  var button = $(event.relatedTarget) // Button that triggered the modal
  var yarnName = button.data('yarn-name') // Extract info from data-* attributes
  var yarnBody = button.data('yarn-body')


  var modal = $(this)
  modal.find('.modal-title').text('Notes about ' + yarnName)
  modal.find('.modal-body').text(yarnBody)
  modal.find('.modal-body input').val(yarnName)
})


$('#projectModal').on('show.bs.modal', function (event) {
  var button = $(event.relatedTarget) // Button that triggered the modal
  var projectName = button.data('project-name') // Extract info from data-* attributes
  var projectBody = button.data('project-body')


  var modal = $(this)
  modal.find('.modal-title').text('Notes about ' + projectName)
  modal.find('.modal-body').text(projectBody)
  modal.find('.modal-body input').val(projectName)
})
