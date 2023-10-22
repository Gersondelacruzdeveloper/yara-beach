const table = document.getElementById('task_list_data');
const h4 = document.getElementById('h4_title');

import {generateTaskRows} from '.GenerateTaskRows.js'
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
      console.log(data)
      h4.innerHTML += ` <span class="badge bg-site-color">${data.length}</span>`
      const rows = generateTaskRows(data);
      table.innerHTML += rows;
    } catch (error) {
      console.error('Error:', error.message);
      // You can display an error message to the user here if needed.
    }
  };

export {fetchTaskList}