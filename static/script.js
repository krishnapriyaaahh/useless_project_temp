document.getElementById('send-button').onclick = function() {
    const userInput = document.getElementById('user-input').value;
    if (!userInput) return;

    // Display user message
    displayMessage(userInput, 'user');
    document.getElementById('user-input').value = '';

    // Send request to the Flask server
    fetch('http://127.0.0.1:5000/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: userInput })
    })
    .then(response => response.json())
    .then(data => {
        // Display bot response
        displayMessage(data.response, 'bot');
    });
};

function displayMessage(message, sender) {
    const chatBox = document.getElementById('chat-box');
    const messageElement = document.createElement('div');
    messageElement.classList.add('message', sender);
    messageElement.textContent = message;
    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight; // Auto-scroll to bottom
}
