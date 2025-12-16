// frontend/script.js

const uploadBtn = document.getElementById('upload')
const fileInput = document.getElementById('file')
const result = document.getElementById('result')
const logs = document.getElementById('logs')
const userIdInput = document.getElementById('userid')

// --------------------
// Refresh Logs
// --------------------
async function refreshLogs() {
  try {
    const r = await fetch('/logs')
    if (!r.ok) throw new Error(`HTTP ${r.status}`)

    const j = await r.json()

    // Always force logs into array
    const arr = Array.isArray(j) ? j : Object.values(j)

    const last = arr.slice(-15).reverse()
    logs.innerText = JSON.stringify(last, null, 2)

  } catch (e) {
    logs.innerText = 'Could not load logs: ' + e.message
  }
}

// --------------------
// Upload + Classify
// --------------------
uploadBtn.onclick = async () => {
  if (!fileInput.files.length) {
    alert("Select an image");
    return;
  }

  const f = fileInput.files[0];
  const fd = new FormData();
  fd.append("file", f);
  fd.append("user_id", userIdInput.value.trim() || "demo_user");

  result.innerText = "Uploading and classifying...";

  try {
    const res = await fetch("/upload-image", {
      method: "POST",
      body: fd,
    });

    // 🚨 IMPORTANT FIX
    const text = await res.text();

    if (!res.ok) {
      result.innerText = "Server error:\n" + text;
      return;
    }

    const data = JSON.parse(text);
    result.innerText = JSON.stringify(data, null, 2);
    await refreshLogs();

  } catch (err) {
    result.innerText = "Unexpected error: " + err.message;
  }
};
