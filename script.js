const BASE_URL = "https://your-backend-url.onrender.com";

let chart;

// ======================
// START SESSION
// ======================
async function startSession() {
    const res = await fetch(`${BASE_URL}/question`);
    const data = await res.json();

    document.getElementById("question").innerText = data.question;
    document.getElementById("skill").innerText = "Skill: " + data.skill;
    document.getElementById("level").innerText = "Level: " + data.level;
    document.getElementById("knowledge").innerText =
        "Knowledge: " + data.knowledge;
}

// ======================
// SUBMIT ANSWER
// ======================
async function submitAnswer() {
    const answer = document.getElementById("answer").value;

    const res = await fetch(`${BASE_URL}/answer`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ answer: answer })
    });

    const data = await res.json();

    document.getElementById("feedback").innerText = data.feedback;
    document.getElementById("knowledge").innerText =
        "Updated: " + data.updated_knowledge;

    loadProgress();
}

// ======================
// LOAD PROGRESS GRAPH
// ======================
async function loadProgress() {
    const res = await fetch(`${BASE_URL}/progress`);
    const data = await res.json();

    const labels = data.Addition.map((_, i) => i + 1);

    if (chart) chart.destroy();

    chart = new Chart(document.getElementById("chart"), {
        type: "line",
        data: {
            labels: labels,
            datasets: Object.keys(data).map(skill => ({
                label: skill,
                data: data[skill],
                borderWidth: 2
            }))
        }
    });
}

// ======================
// LOAD INSIGHTS (XAI)
// ======================
async function loadInsights() {
    const res = await fetch(`${BASE_URL}/insights`);
    const data = await res.json();

    const list = document.getElementById("insightsList");
    list.innerHTML = "";

    data.insights.forEach(item => {
        const li = document.createElement("li");
        li.innerText = item;
        list.appendChild(li);
    });

    document.getElementById("summary").innerText =
        "Summary: " + data.summary;
}