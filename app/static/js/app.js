// [START gae_flex_websockets_js]
$(function()
{
  /* If the main page is served via https, the WebSocket must be served via
     "wss" (WebSocket Secure) */
  var scheme = window.location.protocol == "https:" ? 'wss://' : 'ws://';
  var webSocketUri =  scheme
                      + window.location.hostname
                      + (location.port ? ':'+location.port: '')
                      + '/chat';

  /* Get elements from the page */
  var form = $('#chat-form');
  var textarea = $('#chat-text');
  var output = $('#chat-response');
  var status = $('#chat-status');

  /* Helper to keep an activity log on the page. */
  function log(text)
  {
    status.append($('<li>').text(text))
  }

  /* Establish the WebSocket connection and register event handlers. */
  var websocket = new WebSocket(webSocketUri);

  websocket.onopen = function()
  {
    log('Connected');
  };

  websocket.onclose = function()
  {
    log('Closed');
  };

  websocket.onmessage = function(e)
  {
    log('Message received');
    output.append($('<li>').text(e.data));
  };

  websocket.onerror = function(e)
  {
    log('Error (see console)');
    console.log(e);
  };

  /* Handle form submission and send a message to the websocket. */
  form.submit(function(e)
  {
    e.preventDefault();
    var data = textarea.val();
    websocket.send(data);
  });
});
// [END gae_flex_websockets_js]