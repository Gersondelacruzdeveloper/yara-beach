import { formatIsoDate } from './formatIsoDate.js';

const generateTaskRows = (data) => {
  const now = new Date(); // Get the current date and time

  const rows = data.map(task => {
    const deadlineDate = new Date(task.deadline);
    const timeRemaining = deadlineDate - now;
    const daysRemaining = Math.floor(timeRemaining / (1000 * 60 * 60 * 24));

    const countdown = daysRemaining >= 0
      ? `${daysRemaining} day(s) remaining`
      : 'Deadline passed';

    let tableRows = `
    <tr>
      <td>${task.completed ? '✅' : '❌'}</td>
      <td>${task.title}</td>
      <td>${task.description.substring(0, 50) + '...'}</td>
      <td>${countdown}</td>
      <td class="btn btn-sm btn-primary edit-task" data-edit-task-id="${task.id}"><i class="far fa-edit"> Edit</i></td>
      <td class"btn btn-sm btn-danger delete-task" data-delete-task-id="${task.id}> <i class="fas fa-trash-alt"> Delete</td>
    </tr>
  `;

    return tableRows
  });
  
  return rows.join('');
};


export { generateTaskRows };
