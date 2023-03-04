/* Place your JavaScript in this file */
var loadFile = function(event) {
    var image = document.getElementById('output');
    image.src = URL.createObjectURL(event.target.files[0]);
};
var submitFunc = function() {
    let reqJSON = {}
    reqJSON.ListOfActions = document.getElementById('ListOfActions').value
    reqJSON.image = document.getElementById("Original_Image_File").files[0]
    console.log('reqJSON --', reqJSON)
    xhr.send(formData);
}
