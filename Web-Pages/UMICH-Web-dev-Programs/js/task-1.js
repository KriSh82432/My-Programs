function upDate(previewPic) {
    document.getElementById("image").innerHTML=previewPic.alt;
    var x = previewPic.src
    document.getElementById("image").style.backgroundImage = "url("+x+")";
}

function unDo() {
    document.getElementById("image").innerHTML="Hover over an image below to display here."
    document.getElementById("image").style.backgroundImage = "url('')";
}