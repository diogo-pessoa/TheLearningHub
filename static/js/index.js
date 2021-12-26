function readClipBoardText() {
    // navigator.clipboard.readText().then(text => {
    //     document.getElementById("file_path").innerHTML = text;
    // })
    /* Get the text field */
    var copyText = document.getElementById("file_path");

    /* Select the text field */
    copyText.select();
    copyText.setSelectionRange(0, 99999); /* For mobile devices */

    /* Copy the text inside the text field */
    navigator.clipboard.writeText(copyText.value);
}

$('#collapsable_file_form_info').hide();
$('#file_upload_description').click(function(e) {
  e.preventDefault();
  $('#collapsable_file_form_info').toggle('slow');
});


// Form validation for file size in video_class upload form
$('#video_class_form').submit(function() {
  if (window.File && window.FileReader && window.FileList && window.Blob) {
    let file = $('#id_video_path')[0].files[0];

    if (file && file.size > 7 * 1024 * 1024) {
      alert("File " + file.name + " of type " + file.type + " is too big");
      return false;
    }
  }
});

// Form validation for file size in upload file form
$('#file_upload_form').submit(function() {
  if (window.File && window.FileReader && window.FileList && window.Blob) {
    let file = $('#id_file')[0].files[0];

    if (file && file.size > 2 * 1024 * 1024) {
      alert("File " + file.name + " of type " + file.type + " is too big");
      return false;
    }
  }
});