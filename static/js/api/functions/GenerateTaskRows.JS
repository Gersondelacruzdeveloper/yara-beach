
import { formatIsoDate } from './formatIsoDate.js'

const generateTaskRows = (data) => {
  return data.map(task => `
      <tr>
        <td>${task.completed ? '✅' : '❌'}</td>
        <td>${task.title}</td>
        <td>${task.description.substring(0, 50) + '...'}</td>
        <td>${formatIsoDate(task.created_at)}</td>
        <td>${formatIsoDate(task.updated_at)}</td>
        <td>${formatIsoDate(task.deadline)}</td>
        <td><a href=""><button class="btn btn-sm btn-primary"><i class="far fa-edit">
        Edit</i></button></a> </td>
       <td><a href=""><i class="fas fa-trash-alt">
        Delete</i></button></a>
       </tr>
    `).join('');
};

export { generateTaskRows }