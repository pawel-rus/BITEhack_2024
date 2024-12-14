$(document).ready(function () {
    var chatHistory = [];

    $('#chat-toggle-button').on('click', function () {
        var chatBubble = $('#chat-bubble');
        if (chatBubble.css('visibility') === 'hidden') {
            chatBubble.css('visibility', 'visible');
        } else {
            chatBubble.css('visibility', 'hidden');
        }
    });

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

    function updateChatHistory() {
        var chatHistoryDiv = $('#chat-history');
        chatHistoryDiv.empty();
        chatHistory.forEach(function (entry) {
            chatHistoryDiv.append('<p><strong>You:</strong> ' + entry.prompt + '</p>');
            chatHistoryDiv.append('<p><strong>Bot:</strong> ' + entry.response + '</p>');
        });
        $('#chat-bubble-body').scrollTop($('#chat-bubble-body')[0].scrollHeight);
    }
});