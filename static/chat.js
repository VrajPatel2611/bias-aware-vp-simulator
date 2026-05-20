// chat.js
// Handles all browser interaction for the consultation interface.
// Sends messages to Flask backend and displays responses.
// No frameworks — plain JavaScript only.

async function sendMessage() {
  const input = document.getElementById("user-input");
  const message = input.value.trim();
  if (!message) return;

  // Show user's message immediately
  addMessage("You", message, "user");
  input.value = "";

  // Disable button while waiting for response
  const askBtn = document.getElementById("ask-btn");
  askBtn.disabled = true;
  askBtn.textContent = "...";

  try {
    const response = await fetch("/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: message })
    });

    const data = await response.json();

    if (data.error) {
      addMessage("System", "Error: " + data.error, "error");
    } else {
      addMessage("Patient", data.response, "patient");
      document.getElementById("q-count").textContent = data.question_count;
    }

  } catch (err) {
    addMessage("System", "Connection error. Is Flask running?", "error");
  }

  askBtn.disabled = false;
  askBtn.textContent = "Ask";
  input.focus();
}


async function submitDiagnosis() {
  const diagInput = document.getElementById("diagnosis-input");
  const diagnosis = diagInput.value.trim();

  if (!diagnosis) {
    alert("Please enter a diagnosis before submitting.");
    return;
  }

  const btn = document.getElementById("conclude-btn");
  btn.disabled = true;
  btn.textContent = "Analysing your reasoning...";

  try {
    const response = await fetch("/conclude", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ diagnosis: diagnosis })
    });

    const data = await response.json();
    displayFeedback(data);

  } catch (err) {
    alert("Error getting feedback. Check that Flask is running.");
    btn.disabled = false;
    btn.textContent = "Submit Diagnosis and Get Feedback";
  }
}


function displayFeedback(data) {
  const area = document.getElementById("feedback-area");
  area.style.display = "block";

  let html = `<h3>Session Feedback</h3>`;
  html += `<p><strong>Your diagnosis:</strong> ${data.diagnosis_given}</p>`;
  html += `<p><strong>Questions asked:</strong> ${data.questions_asked}</p>`;

  if (data.session_summary) {
    const s = data.session_summary;
    html += `<p><strong>Topics covered:</strong> `;
    html += `${s.topics_covered_count} of ${s.topics_required_count} `;
    html += `(${s.coverage_percent}%)</p>`;
  }

  html += `<h4 style="margin: 14px 0 8px;">Reasoning Analysis</h4>`;

  for (const [biasName, result] of Object.entries(data.biases_detected)) {
    const statusIcon = result.detected ? "⚠️" : "✓";
    const statusText = result.detected ? "Detected" : "Not detected";
    const cssClass = result.detected ? "detected" : "clean";
    const displayName = biasName.replace(/_/g, " ");

    html += `<div class="bias-result ${cssClass}">`;
    html += `<strong>${displayName}:</strong> ${statusIcon} ${statusText}`;
    html += ` (score: ${result.score})`;
    html += `<p>${result.reason}</p>`;
    html += `</div>`;
  }

  if (data.feedback_messages && data.feedback_messages.length > 0) {
    html += `<h4 style="margin: 14px 0 8px;">Reflective Questions</h4>`;
    html += `<ul style="padding-left: 18px;">`;
    data.feedback_messages.forEach(msg => {
      html += `<li style="margin-bottom: 6px; font-size: 13px;">${msg}</li>`;
    });
    html += `</ul>`;
  }

  html += `<a href="/" class="btn" style="margin-top: 16px; display: inline-block;">
    Try Another Case
  </a>`;

  area.innerHTML = html;
  area.scrollIntoView({ behavior: "smooth" });
}


function addMessage(speaker, text, type) {
  const box = document.getElementById("chat-box");
  const div = document.createElement("div");
  div.className = `msg ${type}`;
  div.innerHTML = `<strong>${speaker}:</strong> ${text}`;
  box.appendChild(div);
  box.scrollTop = box.scrollHeight;
}


// Press Enter in the input box to send message
document.addEventListener("DOMContentLoaded", function () {
  const input = document.getElementById("user-input");
  if (input) {
    input.addEventListener("keypress", function (e) {
      if (e.key === "Enter") sendMessage();
    });
  }
});