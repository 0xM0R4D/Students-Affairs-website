var random_color = Math.floor(Math.random() * 6);
var random_color_list = [
    '#d1ecf1',
    '#f8d7da',
    '#192bd1',
    '#04aa6d',
    '#ff3dd1',
    '#96d4d4',
];

window.onload = function() {
    randomColor();
    readMore();

}



function randomColor() {
    var number_of_children = document.getElementById('par_container').childElementCount,
        par_container = document.getElementById('par_container');
    for (var i = 0; i < number_of_children; i++) {
        par_container.children[i].style.borderColor = random_color_list[Math.floor(Math.random() * 6)];
    }
}

function readless() {
    var number_of_children = document.getElementById('par_container').childElementCount;
    for (var i = 0; i < number_of_children; i++) {
        document.getElementsByClassName('read-more')[i].onclick = function() {
            this.parentElement.style.height = "100px";
            this.addEventListener('click', readMore());
        }
    }
}

function readMore() {
    var number_of_children = document.getElementById('par_container').childElementCount;
    for (var i = 0; i < number_of_children; i++) {
        document.getElementsByClassName('read-more')[i].onclick = function() {
            this.parentElement.style.height = "fit-content";
            this.addEventListener('click', readless());
        }
    }
}