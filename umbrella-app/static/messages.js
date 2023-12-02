document.addEventListener('DOMContentLoaded', function() {
    fetch('/fetch_messages')
        .then(response => response.json())
        .then(messages => {
            const messageTable = document.getElementById('messages-table');  // Add an ID to your users table
            users.forEach(message => {
                const tr = document.createElement('tr');
                const trContent = `
                    <td>${message.messageID}</td>
                    <td>${message.userID}</td>
                    <td>${message.messageText}</td>
                `;
                tr.innerHTML = trContent;
                usersTable.querySelector('tbody').appendChild(tr);
            });
        })
        .catch(error => console.error('Error fetching users:', error));
});