// [START gae_flex_websockets_js]
$(function()
{
    /* If the main page is served via https, the WebSocket must be served via "wss" (WebSocket Secure) */
    var scheme = window.location.protocol == "https:" ? 'wss://' : 'ws://';
    var webSocketUri =  scheme
                      + window.location.hostname
                      + (location.port ? ':'+location.port: '')
                      + '/chat';

    /* Get elements from the page */
    var userInput        = $('#user-input');
    var userInputButton  = $("#user-input-submit");
    var messageWrapper   = $('#messages-wrapper');
    var status           = $('#chat-status');
    var userInputHistory = [];

    setupChat();

    function setupChat()
    {
        userInput.focus();

        $(userInput).keyup(function(event)
        {
            if(event.which == 13)
                 inputSubmit(event);
        });

        $(userInputButton).click(inputSubmit);
    }

    /* Helper to keep an activity log on the page. */
    function log(text)
    {
        status.append($('<li>').text(text))
    }

    /* Establish the WebSocket connection and register event handlers. */
    var webSocket = new WebSocket(webSocketUri);

    webSocket.onopen = function()
    {
        log('Connected');
    };

    webSocket.onclose = function()
    {
        log('Closed');
    };

    webSocket.onmessage = function(e)
    {
        log('Message received');
        let clone = $("#message-template").clone();
        clone.attr('id', null).removeClass('d-none');
        clone.find('.message-bubble-text').text(e.data);

        // Get the actual height to animate.
        clone.css({
            position: 'absolute',
            top: -1000
        });
        clone.appendTo('body');
        let cloneHeight = clone.height();
        clone.css({
            position: '',
            top: '',
            height: 0
        });

        clone.appendTo(messageWrapper)

        clone.animate({height: cloneHeight}, 'fast');
    };

    webSocket.onerror = function(e)
    {
        log('Error (see console)');
        console.log(e);
    };

    /* Handle form submission and send a message to the websocket. */
    var inputSubmit = function(event)
    {
        event.preventDefault();

        var inputValue = userInput.val();
        webSocket.send(inputValue);
        userInputHistory.push(inputValue);

        userInput.val('');
    }
});
// [END gae_flex_websockets_js]