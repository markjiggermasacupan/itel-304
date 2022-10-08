document.addEventListener("DOMContentLoaded", function(event) {


    document.getElementById("title").addEventListener("click", myfunction);

    function myfunction() {
        document.getElementById("title").innerHTML = "YOU CLICKED ME!";
    }

});