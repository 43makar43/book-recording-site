function getInfoClient(id){
    $.ajax({
        url: 'ajax/getClient/?id=' + id,
        method: 'get',
        async: false,
        success: function(data){
            let fields = data[0].fields;
            document.getElementById('validateUpdateInfo').style.display = "none";
            insertInfoClientInDiv(fields, id);
        },
        error: function (jqXHR, exception) {
            return;
        }
    });
}

function insertInfoClientInDiv(info, id){
    document.getElementById('full_name_client').value = info.full_name;
    document.getElementById('phone_number_client').value = info.phone_number;

    let buttonUpdateUser = document.getElementById('buttonUpdateUser');
    buttonUpdateUser.innerHTML = 
    `
        <button type="submit" onclick="updateInfoClient(` + id + `)" class="btn btn-success">Изменить</button>
    `;

}

function updateInfoClient(id){
    let inputFullName = document.getElementById('full_name_client').value;
    let inputPhoneNumber = document.getElementById('phone_number_client').value;

    let validateUpdateInfo = document.getElementById('validateUpdateInfo');

    if (!inputPhoneNumber){
        validateUpdateInfo.textContent = "Номер телефона не может содержать символы!";
        validateUpdateInfo.style.display = "block";
        return;
    }

    if (inputFullName.length > 100 || inputFullName.length == 0){
        validateUpdateInfo.textContent = "Имя пользователя не может быть пустым или превышать длину в 100 символов.";
        validateUpdateInfo.style.display = "block";
        return;
    }


    if (inputPhoneNumber.length > 11 || inputPhoneNumber.length < 11){
        validateUpdateInfo.textContent = "Номер телефона не может быть пустым или больше 11 символов";
        validateUpdateInfo.style.display = "block";
        return;
    }

    
    $.ajax({
        url: 'ajax/updateClient/?id=' + id + "&fullName=" + inputFullName + "&number=" + parseInt(inputPhoneNumber),
        method: 'get',
        success: function(data){
            validateUpdateInfo.textContent = "Данные пользователя изменены!";
            validateUpdateInfo.style.display = "block";
        },
        error: function (jqXHR, exception) {
            return;
        }
    });

}

// Order

function getInfoOrder(id){
    $.ajax({
        url: 'ajax/getOrder/?id=' + id,
        method: 'get',
        async: false,
        success: function(data){
            let order = data[0].order;
            let client = data[1].client;
            let librarin = data[2].librarin;
            let books = data[3];

            insertInfoOrderInDiv(order, client,librarin);

            let books_list = document.getElementById('books_list');
            books_list.innerHTML = ``;


            for (const book of books) {
                fillBookList(book, books_list);
            }


        },
        error: function (jqXHR, exception) {
            console.log(exception)
        }
    });
}

function fillBookList(book, books_list){

    books_list.innerHTML +=
    `
    <li>
        <a class="dropdown-item dropdown_custom_item text-wrap">
            <p>` + book.book_author + `</p>
            <p>` + book.book_name + `</p>
        </a>
    </li>
    <hr>
    `
}

function insertInfoOrderInDiv(order, client,librarin){
    document.getElementById('full_name_client').value = client[0].fields.full_name;
    document.getElementById('date_of_taking').value = order[0].fields.date_of_taking;
    document.getElementById('return_date').value = order[0].fields.return_date;
    document.getElementById('full_name_librarian').value = librarin[0].fields.full_name;
}
