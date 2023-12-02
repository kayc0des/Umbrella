const sideMenu = document.querySelector("aside");
const menuBtn = document.querySelector("#menu-btn");
const closeBtn = document.querySelector("#close-btn");
const themeToggler = document.querySelector(".theme-toggler")


menuBtn.addEventListener('click', () => {
    sideMenu.style.display = 'block';
})

closeBtn.addEventListener('click', () => {
    sideMenu.style.display = 'none';
})

themeToggler.addEventListener('click', () => {
    document.body.classList.toggle('dark-theme-variables');

    themeToggler.querySelector('span:nth-child(1)').classList.toggle('active');
    themeToggler.querySelector('span:nth-child(2)').classList.toggle('active');
})

// Populate Admin Tables

// document.addEventListener('DOMContentLoaded', function() {
//     fetch('/fetch_properties')
//         .then(response => response.json())
//         .then(properties => {
//             properties.forEach(property => {
//                 const tr = document.createElement('tr');
//                 const trContent = `
//                     <td>${property.propertyName}</td>
//                     <td>${property.propertyID}</td>
//                     <td>${property.propertyLocation}</td>
//                     <td>${property.propertyDesc}</td>
//                     <td>${property.propertyStatus}</td>
//                     <td>${property.propertyDateAdded}</td>
//                 `;
//                 tr.innerHTML = trContent;
//                 document.querySelector('table tbody').appendChild(tr);
//             });
//         })
//         .catch(error => console.error('Error fetching properties:', error));

//         // fetch('/fetch_users')
//         // .then(response => response.json())
//         // .then(users => {
//         //     users.forEach(user => {
//         //         const tr = document.createElement('tr');
//         //         const trContent = `
//         //             <td>${user.userName}</td>
//         //             <td>${user.userID}</td>
//         //             <td>${user.userEmail}</td>
//         //         `;
//         //         tr.innerHTML = trContent;
//         //         document.querySelector('table tbody').appendChild(tr);
//         //     });
//         // })
//         // .catch(error => console.error('Error fetching users:', error));
// });

// document.addEventListener('DOMContentLoaded', function() {
//     fetch('/fetch_users')
//         .then(response => response.json())
//         .then(users => {
//             const usersTable = document.getElementById('users-table');  // Add an ID to your users table
//             users.forEach(user => {
//                 const tr = document.createElement('tr');
//                 const trContent = `
//                     <td>${user.userName}</td>
//                     <td>${user.userID}</td>
//                     <td>${user.userEmail}</td>
//                 `;
//                 tr.innerHTML = trContent;
//                 usersTable.querySelector('tbody').appendChild(tr);
//             });
//         })
//         .catch(error => console.error('Error fetching users:', error));
// });

// document.addEventListener('DOMContentLoaded', function() {
//     fetch('/fetch_properties')
//         .then(response => response.json())
//         .then(properties => {
//             const propertiesTable = document.getElementById('properties-table');  // Add an ID to your properties table
//             properties.forEach(property => {
//                 const tr = document.createElement('tr');
//                 const trContent = `
//                     <td>${property.propertyName}</td>
//                     <td>${property.propertyID}</td>
//                     <td>${property.propertyLocation}</td>
//                     <td>${property.propertyDesc}</td>
//                     <td>${property.propertyStatus}</td>
//                     <td>${property.propertyDateAdded}</td>
//                 `;
//                 tr.innerHTML = trContent;
//                 propertiesTable.querySelector('tbody').appendChild(tr);
//             });
//         })
//         .catch(error => console.error('Error fetching properties:', error));

//     // fetch('/fetch_users')
//     //     .then(response => response.json())
//     //     .then(users => {
//     //         const usersTable = document.getElementById('users-table');  // Add an ID to your users table
//     //         users.forEach(user => {
//     //             const tr = document.createElement('tr');
//     //             const trContent = `
//     //                 <td>${user.userName}</td>
//     //                 <td>${user.userID}</td>
//     //                 <td>${user.userEmail}</td>
//     //             `;
//     //             tr.innerHTML = trContent;
//     //             usersTable.querySelector('tbody').appendChild(tr);
//     //         });
//     //     })
//     //     .catch(error => console.error('Error fetching users:', error));
// });
