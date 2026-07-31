const messagesEl = document.getElementById('messages');
const inputEl = document.getElementById('input');
const sendBtn = document.getElementById('send');

function addMessage(text, cls='jarvis'){
  const div = document.createElement('div');
  div.className = 'message ' + (cls === 'user' ? 'user' : 'jarvis');
  div.textContent = text;
  messagesEl.appendChild(div);
  messagesEl.scrollTop = messagesEl.scrollHeight;
}

async function sendMessage(){
  const text = inputEl.value.trim();
  if(!text) return;
  addMessage('You: ' + text, 'user');
  inputEl.value = '';

  try{
    const res = await fetch('/api/ask', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: text })
    });

    const data = await res.json();
    if(data.error){
      addMessage('Error: ' + data.error);
    } else {
      // Print formatted result or answer
      const answer = data.answer || JSON.stringify(data.result || data, null, 2);
      addMessage('Jarvis: ' + (typeof answer === 'string' ? answer : JSON.stringify(answer)));
    }
  } catch(err){
    addMessage('Network error: ' + err.message);
  }
}

sendBtn.addEventListener('click', sendMessage);
inputEl.addEventListener('keydown', (e)=>{ if(e.key === 'Enter') sendMessage(); });

// Welcome
addMessage('Welcome to Jarvis UI. Type a command and press Send.');
