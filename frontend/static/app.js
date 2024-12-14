$(document).ready(function () {
    var chatHistory = [];

    // Funkcja dostosowująca pozycję chat-bubble
    function adjustChatPosition() {
        var menuHeight = $('.navbar').outerHeight(); // Pobierz wysokość menu
        if ($('.navbar-collapse').hasClass('show')) {
            // Jeśli menu jest otwarte, przesuwamy chat w dół
            $('#chat-bubble').css('top', menuHeight + 20 + 'px'); // Dodaj 20px odstępu
        } else {
            // Jeśli menu jest zamknięte, ustawiamy standardową pozycję
            $('#chat-bubble').css('top', '80px');
        }
    }

    // Obsługa otwierania/zamykania menu nawigacyjnego
    $('.navbar-toggler').on('click', function () {
        var chatBubble = $('#chat-bubble');

        if ($('.navbar-collapse').hasClass('show')) {
            // Jeśli menu się zamyka, dostosuj pozycję chatu
            adjustChatPosition();
        } else {
            // Jeśli menu się otwiera, zamknij chat i dostosuj pozycję
            chatBubble.css('visibility', 'hidden');
            adjustChatPosition();
        }
    });

    // Obsługa otwierania/zamykania chatu
    $('#chat-toggle-button').on('click', function () {
        var chatBubble = $('#chat-bubble');
        if ($('.navbar-collapse').hasClass('show')) {
            // Zamknij menu, jeśli jest otwarte
            $('.navbar-collapse').collapse('hide');
        }

        // Przełącz widoczność chatu
        if (chatBubble.css('visibility') === 'hidden') {
            chatBubble.css('visibility', 'visible');
            adjustChatPosition(); // Dopasuj pozycję po otwarciu
        } else {
            chatBubble.css('visibility', 'hidden');
        }
    });

    // Obsługa wysyłania wiadomości w chacie
    $('#chat-form').on('submit', function (event) {
        event.preventDefault();
        var prompt = $('#prompt').val();
        $.ajax({
            url: '/ask_ai',
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ prompt: prompt }),
            success: function (response) {
                chatHistory.push({ prompt: prompt, response: response.result });
                updateChatHistory();
                $('#prompt').val('');
            },
            error: function (xhr, status, error) {
                $('#response').html('<p>An error occurred: ' + xhr.responseJSON.error + '</p>');
            }
        });
    });

    // Aktualizacja historii chatu
    function updateChatHistory() {
        var chatHistoryDiv = $('#chat-history');
        chatHistoryDiv.empty();
        chatHistory.forEach(function (entry) {
            chatHistoryDiv.append('<p><strong>You:</strong> ' + entry.prompt + '</p>');
            chatHistoryDiv.append('<p><strong>Bot:</strong> ' + entry.response + '</p>');
        });
        $('#chat-bubble-body').scrollTop($('#chat-bubble-body')[0].scrollHeight);
    }

    // Dopasuj pozycję chatu na starcie
    adjustChatPosition();

    // Zmień pozycję chatu przy zmianie rozmiaru okna
    $(window).on('resize', function () {
        adjustChatPosition();
    });
});