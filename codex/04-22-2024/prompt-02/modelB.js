const socket = io(); // Connect to server

const messageInput = document.getElementById('message');
const sendButton = document.getElementById('send');
const chatBox = document.getElementById('chat-box');

sendButton.addEventListener('click', () => {
    socket.emit('chat message', messageInput.value);
    messageInput.value = '';
});

socket.on('chat message', (msg) => {
    const messageElement = document.createElement('p');
    messageElement.textContent = msg;
    chatBox.appendChild(messageElement);
});