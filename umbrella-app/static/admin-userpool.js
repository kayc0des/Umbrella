document.addEventListener('DOMContentLoaded', function() {
    fetch('/fetch_users')
        .then(response => response.json())
        .then(users => {
            const usersTable = document.getElementById('users-table');  // Add an ID to your users table
            users.forEach(user => {
                const tr = document.createElement('tr');
                const trContent = `
                    <td>${user.userName}</td>
                    <td>${user.userID}</td>
                    <td>${user.userEmail}</td>
                `;
                tr.innerHTML = trContent;
                usersTable.querySelector('tbody').appendChild(tr);
            });
        })
        .catch(error => console.error('Error fetching users:', error));
});