import { fetchTaskList } from './fetchTaskList.js';
import { csrftoken } from '../functions/crfToken.js';

const handleAddTaskFormSubmit = () => {
  // Get the form element and relevant form fields outside of the event listener
  const addTaskForm = document.getElementById('addTaskForm');
  const taskTitleInput = document.getElementById('taskTitle');
  const taskDescriptionInput = document.getElementsByClassName("ck-content")[0].children[0].innerHTML
  console.log('taskDescriptionInput', taskDescriptionInput)
  const taskDeadlineInput = document.getElementById('taskDeadline');
  const taskCompletedInput = document.getElementById('taskCompleted');

  addTaskForm.addEventListener('submit', async (event) => {
    event.preventDefault();

    // Get task details from the form
    const taskTitle = taskTitleInput.value;
    const taskDescription = taskDescriptionInput;
    const taskDeadline = taskDeadlineInput.value;
    const taskCompleted = taskCompletedInput.checked;

    const data = {
      user: userId,
      title: taskTitle,
      description: String(taskDescription),
      deadline: taskDeadline,
      completed: taskCompleted,
    };

    const apiUrl = `${siteUrl}add_task/`;

    try {
      const response = await fetch(apiUrl, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify(data),
      });

      if (!response.ok) {
        throw new Error(`Failed to fetch data. Status: ${response.status}`);
      }

      console.log('Response:', response);

      fetchTaskList(userId);
      addTaskForm.reset();
      modal.style.display = 'none';
    } catch (error) {
      console.error('Error:', error);
    }
  });
};

export { handleAddTaskFormSubmit };
