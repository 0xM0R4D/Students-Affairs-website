var EditLink = document.getElementById('EditLink');



document.getElementById('namefield').onkeyup = function() {
    if (document.getElementById('byName').checked == false) {
        return;
    }
    if (this.value != '') {
        EditLink.style.visibility = 'visible';
    } else {
        EditLink.style.visibility = 'hidden';
    }
}
document.getElementById('idfield').onkeyup = function() {
    if (document.getElementById('byID').checked == false) {
        return;
    }
    if (this.value != '') {
        EditLink.style.visibility = 'visible';
    } else {
        EditLink.style.visibility = 'hidden';
    }
}