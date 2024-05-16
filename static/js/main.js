document.getElementById('answerForm').addEventListener('submit', function(event) {
    event.preventDefault();
    var answer = document.getElementById('answer').value;
    fetch('/submit_answer', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: 'answer=' + encodeURIComponent(answer)
    }).then(response => response.json())
      .then(data => {
          alert(data.message);
          location.reload();
      });
});

document.getElementById('clearAnswersButton').addEventListener('click', function(event) {
    event.preventDefault();
    fetch('/clear_answers', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        }
    }).then(response => response.json())
      .then(data => {
          alert(data.message);
          location.reload();
      });
});
