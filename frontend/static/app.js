let messagesEl;
let inputEl;
let sendBtn;
let clearBtn;
let quickButtons;

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

function setLoading(isLoading){
  if(isLoading){
    sendBtn.disabled = true;
    sendBtn.textContent = 'Sending...';
  } else {
    sendBtn.disabled = false;
    sendBtn.textContent = 'Send';
  }
}

async function sendMessage(command){
  const text = (command || inputEl.value).trim();
  if(!text) return;

  addMessage(`> ${text}`, 'user');
  if(!command){
    inputEl.value = '';
  }

  setLoading(true);
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
  } finally {
    setLoading(false);
  }
}

function clearConsole(){
  messagesEl.innerHTML = '';
  addMessage('Console cleared. Ready for new input.');
}

function initializeConsole(){
  messagesEl = document.getElementById('messages');
  inputEl = document.getElementById('input');
  sendBtn = document.getElementById('send');
  clearBtn = document.getElementById('clear');
  quickButtons = document.querySelectorAll('[data-command]');

  if(!messagesEl || !inputEl || !sendBtn){
    console.error('Jarvis UI failed to initialize. Missing required DOM elements.');
    return;
  }

  sendBtn.addEventListener('click', () => sendMessage());
  inputEl.addEventListener('keydown', (e)=>{ if(e.key === 'Enter') sendMessage(); });
  clearBtn?.addEventListener('click', clearConsole);
  quickButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      const command = btn.getAttribute('data-command');
      if(command){
        sendMessage(command);
      }
    });
  });

  addMessage('Jarvis online. Use the quick actions or type a command.');
}

if (document.readyState !== 'loading') {
  initializeConsole();
} else {
  document.addEventListener('DOMContentLoaded', initializeConsole);
}
