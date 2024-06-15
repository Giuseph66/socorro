document.addEventListener('DOMContentLoaded', function() {
    var modal = document.getElementById('welcomeModal');
    var span = document.getElementsByClassName('close')[0];
    modal.style.display = 'block';
    setTimeout(function() {
        modal.style.display = 'none';
    }, 10000);
    span.onclick = function() {
        modal.style.display = 'none'; 
    }
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = 'none';
        }
    }
});
