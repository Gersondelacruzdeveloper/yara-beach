// fetchTaskList.js

import { generateTaskRows } from './generateTaskRowsPage.js';

// Get references to HTML elements and model elements
const table = document.getElementById('task_list_data');
const h4TitleSpan = document.getElementById('h4_title_span');
const addBtn = document.getElementById('addbtn');
const closeModalButton = document.getElementById('closeModal');
const modal = document.getElementById('modal');

// Function to fetch and display task list
const fetchTaskList = async (userId) => {
  try {
    const response = await fetch(`${siteUrl}task-list/?user_id=${userId}`, {
      method: 'GET',
      headers: {
        'Accept': 'application/json',
      },
    });

    if (response.status !== 200) {
      throw new Error('Failed to fetch data');
    }

    const data = await response.json();
    h4TitleSpan.textContent = data.length;

    // Generate task rows and set them once
    table.innerHTML += generateTaskRows(data);

    // Event handling for the "Add" button and modal
    addBtn.addEventListener('click', () => modal.style.display = 'block');
    closeModalButton.addEventListener('click', () => modal.style.display = 'none');
    modal.addEventListener('click', (event) => {
      if (event.target === modal) {
        modal.style.display = 'none';
      }
    });

  } catch (error) {
    console.error('Error:', error.message);
    // You can display an error message to the user here if needed.
  }
};

// Export the fetchTaskList function
export { fetchTaskList };
