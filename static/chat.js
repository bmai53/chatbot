function reduceCapstoneHeight() {
  var el = document.getElementById("capstone");
  var height = el.offsetHeight;
  var newHeight = height - 60;
  el.style.height = newHeight + "px";
}

function scrollToBottom() {
  var objDiv = document.getElementById("chatbox");
  objDiv.scrollTop = objDiv.scrollHeight;
}

function getResponse() {
  reduceCapstoneHeight();
  let userText = $("#textInput").val();
  let userHtml =
    '<div class="userText chatBubble"><span>' + userText + "</span></div>";
  $("#textInput").val("");
  $("#chatbox").append(userHtml);
  scrollToBottom();
  document
    .getElementById("userInput")
    .scrollIntoView({ block: "start", behavior: "smooth" });

  fetch("/chat", {
    headers: {
      "Content-Type": "application/json",
    },
    method: "POST",
    body: JSON.stringify({
      sentence: userText,
    }),
  })
    .then(function (res) {
      return res.json();
    })
    .then(function (data) {
      reduceCapstoneHeight();
      // console.log(data)
      var botHtml =
        '<div class="botText chatBubble"><span>' + data.msg + "</span></div>";

      if (data.link !== undefined) {
        var botHtml =
          '<div class="botText chatBubble"><span>' +
          data.msg +
          '</span> <div><a class="link" href = "' +
          data.link +
          '">' +
          data.link +
          "</a></div></div>";
      }
      $("#chatbox").append(botHtml);
      scrollToBottom();
      document
        .getElementById("userInput")
        .scrollIntoView({ block: "start", behavior: "smooth" });
    });
}
