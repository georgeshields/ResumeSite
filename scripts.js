//These are the scripts to use for the html file(S) in the project
document.addEventListener('DOMContentLoaded', () => {
  const chatMessages = document.getElementById('chat-messages');
  const userInput = document.getElementById('user-input');
  const sendButton = document.getElementById('send-button');
  const darkModeToggle = document.getElementById('dark-mode-toggle');
  const burgerMenu = document.getElementById('burger-menu');
  const navMenu = document.getElementById('nav-menu');
  const body = document.body;

  // Endpoint to your Flask server
  const chatEndpoint = "http://127.0.0.1:5000/chat";

  const savedTheme = localStorage.getItem('theme');

  if (savedTheme === 'dark-mode') {
    document.body.classList.add('dark-mode');
    // Adjust icon to moon if we're in dark mode
    darkModeToggle.querySelector('i').classList.remove('fa-sun');
    darkModeToggle.querySelector('i').classList.add('fa-moon');
  }

  if (sendButton) {
    sendButton.addEventListener('click', sendMessage);
  }

  if (userInput) {
    userInput.addEventListener('keyup', (e) => {
      if (e.key === 'Enter') {
        sendMessage();
      }
    });
  }

  if (darkModeToggle) {
    darkModeToggle.addEventListener('click', () => {
      body.classList.toggle('dark-mode');
      const icon = darkModeToggle.querySelector('i');
      if (body.classList.contains('dark-mode')) {
        icon.classList.remove('fa-moon');
        icon.classList.add('fa-sun');
        localStorage.setItem('theme', 'dark-mode');
      } else {
        icon.classList.remove('fa-sun');
        icon.classList.add('fa-moon');
        localStorage.removeItem('theme');
      }
    });
  }

  if (burgerMenu) {
    burgerMenu.addEventListener('click', () => {
      navMenu.classList.toggle('active');
    });
  }

  // Close the dropdown menu if the user clicks outside of it
  window.addEventListener('click', (event) => {
    if (!burgerMenu.contains(event.target) && !navMenu.contains(event.target)) {
      navMenu.classList.remove('active');
    }
  });

  function sendMessage() {
    const message = userInput.value.trim();
    if (!message) return;

    // Display user's message in the chat box
    appendMessage('user', message);
    userInput.value = '';

    // Send message to server and get response
    fetch(chatEndpoint, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ message }),
    })
    .then(response => response.json())
    .then(data => {
      appendMessage('bot', data.reply);
    })
    .catch(error => {
      console.error('Error:', error);
    });
  }

  function appendMessage(sender, message) {
    const messageElement = document.createElement('div');
    messageElement.classList.add('message', sender);
    messageElement.textContent = message;
    chatMessages.appendChild(messageElement);
    chatMessages.scrollTop = chatMessages.scrollHeight;
  }
});