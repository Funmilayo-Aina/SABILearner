
let currentQuestion = {};

async function getQuestion() {
  const res = await fetch("http://127.0.0.1:5000/question");
  currentQuestion = await res.json();

  document.getElementById("question").innerText =
    currentQuestion.question;
}

async function submitAnswer() {
  let userAnswer = document.getElementById("answer").value;

  const res = await fetch("http://127.0.0.1:5000/answer", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({
      answer: userAnswer
    })
  });

  const data = await res.json();
  document.getElementById("feedback").innerText = data.feedback;

  getQuestion();
}

getQuestion();