const messagesEl = document.getElementById('messages');
const inputEl = document.getElementById('input');
const sendBtn = document.getElementById('send');

function createMessage(text, cls='jarvis'){
  const div = document.createElement('div');
  div.className = 'message ' + (cls === 'user' ? 'user' : 'jarvis');
  div.textContent = text;
  return div;
}

function addMessage(text, cls='jarvis'){
  const message = createMessage(text, cls);
  messagesEl.appendChild(message);
  messagesEl.scrollTop = messagesEl.scrollHeight;
}

async function sendMessage(){
  const text = inputEl.value.trim();
  if(!text) return;
  addMessage(`> ${text}`, 'user');
  inputEl.value = '';

  try{
    const res = await fetch('/api/ask', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: text })
    });

    const data = await res.json();
    if(data.error){
      addMessage(`Error: ${data.error}`);
    } else {
      const answer = data.answer || data.formatted_result || JSON.stringify(data.result || data, null, 2);
      addMessage(answer, 'jarvis');
    }
  } catch(err){
    addMessage(`Network error: ${err.message}`);
  }
}

sendBtn.addEventListener('click', sendMessage);
inputEl.addEventListener('keydown', (e)=>{ if(e.key === 'Enter') sendMessage(); });

addMessage('Jarvis online. Type a command to begin.');
