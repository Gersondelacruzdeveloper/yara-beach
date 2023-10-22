
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

    return `
      <tr>
        <td>${task.completed ? '✅' : '❌'}</td>
        <td>${task.title}</td>
        <td>${task.description.substring(0, 50) + '...'}</td>
        <td>${formatIsoDate(task.deadline)}</td>
        <td>${countdown}</td>
        <td><a href=""><button class="btn btn-sm btn-primary"><i class="far fa-edit"> Edit</i></button></a></td>
        <td><a href=""><i class="fas fa-trash-alt"> Delete</i></button></a></td>
      </tr>
    `;
  });

  return rows.join('');
};

export { generateTaskRows };
