import {fetchTaskList} from './functions/fetchTaskList.js'
import { handleAddTaskFormSubmit } from './functions/handleAddTaskFormSubmit.js';
import { updateTask } from './functions/updateTask.js'

// display functions
// You might want to wait for fetchTaskList to complete before executing other functions
fetchTaskList(userId)
handleAddTaskFormSubmit();
updateTask();
