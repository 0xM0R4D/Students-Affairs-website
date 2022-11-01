var names = ['Abdallah Mohsen ',
    'Islam Abd-Elglil',
    'Mohamed Mahmoud mourad ',
    'Shrouq Ahmed Basiony Ali',
    'Shadia Hussein Mahmoud',
    'Ali Mohamed Abdelaty Mohamed'
];

let ids = [
    20200304,
    20200079,
    20200475,
    20200250,
    20200249,
    20200334,
];

let Sections = [7, 7, 7, 7, 19, 7, ];


window.onload = function() {
    'use strict';
    creatBoxes()
    parent = document.getElementById('parent');
    for (var i = 0; i < 6; i++) {
        document.getElementsByClassName('name')[i].innerHTML = names[i];
        document.getElementsByClassName('id')[i].innerHTML = ids[i];
        document.getElementsByClassName('section')[i].innerHTML = 'S' + Sections[i];
    }

}

function creatBoxes() {
    parent = document.getElementById('parent');
    for (var i = 0; i < 6; i++) {
        var pname = document.createElement('p'),
            pid = document.createElement('p'),
            psec = document.createElement('p'),
            box = document.createElement('div');

        pname.classList.add('name');
        pid.classList.add('id');
        psec.classList.add('section');
        box.classList.add('box');

        box.appendChild(pname);
        box.appendChild(pid);
        box.appendChild(psec);

        parent.appendChild(box);

    }

}