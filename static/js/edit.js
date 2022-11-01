    var editgpa = document.getElementById('editgpa'),
        editName = document.getElementById('editName'),
        editDep = document.getElementById('editDep'),
        editCourse = document.getElementById('editCourse'),
        editLevel = document.getElementById('editLevel');


    function gpaNumber() {
        document.getElementById('spann').innerHTML = document.getElementById('GPA').value;
    }

    window.onclick = function() {

        sowData();
        if (editLevel.checked == true) {
            document.getElementById('level').style.display = 'none';
        } else {
            document.getElementById('level').style.display = 'inline';
        }


        if (editName.checked == true) {
            document.getElementById('Name').style.display = 'none';
        } else {
            document.getElementById('Name').style.display = 'inline';
        }


        if (editDep.checked == true) {
            document.getElementById('department').style.display = 'none';
        } else {
            document.getElementById('department').style.display = 'inline';
        }


        if (editCourse.checked == true) {
            document.getElementById('course').style.display = 'none';
        } else {
            document.getElementById('course').style.display = 'inline';
        }


        if (editgpa.checked == true) {
            document.getElementById('GPA').style.display = 'none';
        } else {
            document.getElementById('GPA').style.display = 'inline';
        }

        if (document.getElementById('level').value == 1 || document.getElementById('level').value == 2) {
            document.getElementById('department').value = 'General';
        }

    }

    window.onload = function() {
        if (document.getElementById('level').value == 1 || document.getElementById('level').value == 2) {
            document.getElementById('department').value = 'General';
        }
    }


    window.onkeydown = function() {
        sowData();
    }

    function sowData() {
        var data_field = document.getElementById('stuInfos').children;
        data_field[0].innerHTML = "Name: " + document.getElementById('Name').value;
        data_field[1].innerHTML = "ID: " + document.getElementById('inputId').value;
        data_field[2].innerHTML = "Level: " + document.getElementById('level').value;
        data_field[3].innerHTML = "Dep: " + document.getElementById('department').value;
        data_field[4].innerHTML = "GPA: " + document.getElementById('GPA').value;
    }