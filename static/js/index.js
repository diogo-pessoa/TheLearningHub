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