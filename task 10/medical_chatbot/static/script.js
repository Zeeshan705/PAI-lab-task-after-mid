const messagesContainer = document.getElementById("messages");
const userInput = document.getElementById("userInput");

document.getElementById("init-time").textContent = getCurrentTime();

function getCurrentTime() {
    const now = new Date();
    let hours = now.getHours();
    const minutes = now.getMinutes().toString().padStart(2, "0");
    const ampm = hours >= 12 ? "PM" : "AM";
    hours = hours % 12 || 12;
    return `${hours}:${minutes} ${ampm}`;
}

function scrollToBottom() {
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
}

function appendMessage(text, sender) {
    const wrapper = document.createElement("div");
    wrapper.classList.add("message", sender === "user" ? "user-message" : "bot-message");

    const avatar = document.createElement("div");
    avatar.classList.add("avatar");

    if (sender === "user") {
        avatar.classList.add("user-avatar");
        avatar.textContent = "U";
    } else {
        avatar.classList.add("bot-avatar");
        avatar.innerHTML = `<svg viewBox="0 0 30 30" fill="none" xmlns="http://www.w3.org/2000/svg">
            <circle cx="15" cy="15" r="15" fill="#2a7d6b"/>
            <rect x="12" y="7" width="5" height="16" rx="1.5" fill="white"/>
            <rect x="7" y="12" width="16" height="5" rx="1.5" fill="white"/>
        </svg>`;
    }

    const bubble = document.createElement("div");
    bubble.classList.add("bubble");

    const para = document.createElement("p");
    para.textContent = text;

    const time = document.createElement("span");
    time.classList.add("timestamp");
    time.textContent = getCurrentTime();

    bubble.appendChild(para);
    bubble.appendChild(time);
    wrapper.appendChild(avatar);
    wrapper.appendChild(bubble);
    messagesContainer.appendChild(wrapper);
    scrollToBottom();
}

function showTyping() {
    const wrapper = document.createElement("div");
    wrapper.classList.add("message", "bot-message", "typing-bubble");
    wrapper.id = "typing-indicator";

    const avatar = document.createElement("div");
    avatar.classList.add("avatar", "bot-avatar");
    avatar.innerHTML = `<svg viewBox="0 0 30 30" fill="none" xmlns="http://www.w3.org/2000/svg">
        <circle cx="15" cy="15" r="15" fill="#2a7d6b"/>
        <rect x="12" y="7" width="5" height="16" rx="1.5" fill="white"/>
        <rect x="7" y="12" width="16" height="5" rx="1.5" fill="white"/>
    </svg>`;

    const bubble = document.createElement("div");
    bubble.classList.add("bubble");
    bubble.innerHTML = `<span class="dot"></span><span class="dot"></span><span class="dot"></span>`;

    wrapper.appendChild(avatar);
    wrapper.appendChild(bubble);
    messagesContainer.appendChild(wrapper);
    scrollToBottom();
}

function removeTyping() {
    const indicator = document.getElementById("typing-indicator");
    if (indicator) indicator.remove();
}

async function sendMessage() {
    const message = userInput.value.trim();
    if (!message) return;

    appendMessage(message, "user");
    userInput.value = "";
    showTyping();

    try {
        const response = await fetch("/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: message })
        });

        const data = await response.json();
        setTimeout(() => {
            removeTyping();
            appendMessage(data.reply, "bot");
        }, 800);
    } catch (error) {
        removeTyping();
        appendMessage("Sorry, something went wrong. Please try again.", "bot");
    }
}

function sendQuick(text) {
    userInput.value = text;
    sendMessage();
}

function handleKey(event) {
    if (event.key === "Enter") sendMessage();
}

function clearChat() {
    messagesContainer.innerHTML = "";
    const wrapper = document.createElement("div");
    wrapper.classList.add("message", "bot-message");

    const avatar = document.createElement("div");
    avatar.classList.add("avatar", "bot-avatar");
    avatar.innerHTML = `<svg viewBox="0 0 30 30" fill="none" xmlns="http://www.w3.org/2000/svg">
        <circle cx="15" cy="15" r="15" fill="#2a7d6b"/>
        <rect x="12" y="7" width="5" height="16" rx="1.5" fill="white"/>
        <rect x="7" y="12" width="16" height="5" rx="1.5" fill="white"/>
    </svg>`;

    const bubble = document.createElement("div");
    bubble.classList.add("bubble");
    bubble.innerHTML = `<p>Chat has been cleared. How may I help you?</p><span class="timestamp">${getCurrentTime()}</span>`;

    wrapper.appendChild(avatar);
    wrapper.appendChild(bubble);
    messagesContainer.appendChild(wrapper);
}
