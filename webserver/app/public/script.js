// const fetch = window.fetch;

function makePrediction(){

    let xhr = new XMLHttpRequest();
    xhr.open("POST", "http://localhost:5000/predictor");

    xhr.setRequestHeader("Accept", "application/json");
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
    xhr.setRequestHeader('Access-Control-Allow-Origin', '*');

    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
            console.log(xhr.status);
            console.log(xhr.responseText);
        }};

    let age = document.getElementById("age").value;
    let genderM, genderF;
    if(document.getElementById('genderM').checked) {
        genderM = 1;
        genderF = 0;
    }else if(document.getElementById('genderF').checked) {
        genderM = 0;
        genderF = 1;
    }
    let height = document.getElementById("height").value;
    let weight = document.getElementById("weight").value;
    let body_fat = document.getElementById("body_fat").value;
    let diastolic = document.getElementById("diastolic").value;
    let systolic = document.getElementById("systolic").value;
    let bend_forward = document.getElementById("bend_forward").value;
    let grip_force = document.getElementById("grip_force").value;
    let sit_ups = document.getElementById("sit_ups").value;
    let broad_jump = document.getElementById("broad_jump").value;

    let data = `{
      "age": ${age},
      "genderM": ${genderM},
      "genderF": ${genderF},
      "height": ${height},
      "weight": ${weight},
      "body_fat": ${body_fat},
      "diastolic": ${diastolic},
      "systolic": ${systolic},
      "grip_force": ${grip_force},
      "bend_forward": ${bend_forward},
      "sit_ups": ${sit_ups},
      "broad_jump": ${broad_jump}
    }`;

    xhr.send(data);

}

