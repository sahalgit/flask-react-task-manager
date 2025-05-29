import React, { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
  const [tasks, setTasks] = useState([]);
  const [newTask, setNewTask] = useState('');

  // Fetch tasks on load
  useEffect(() => {
    fetchTasks();
  }, []);

  const fetchTasks = async () => {
    try {
      const res = await axios.get('/tasks');
      setTasks(res.data);
    } catch (err) {
      console.error('Error fetching tasks:', err);
    }
  };

const handleAddTask = async () => {
  if (!newTask.trim()) return;

  try {
    await axios.post(
      '/tasks',
      JSON.stringify({ task: newTask }), // 🔥 stringify the body
      {
        headers: {
          'Content-Type': 'application/json',
        },
      }
    );
    setNewTask('');
    fetchTasks();
  } catch (err) {
    console.error('Error adding task:', err);
  }
};


  const handleDeleteTask = async (id) => {
    try {
      await axios.delete(`/tasks/${id}`);
      fetchTasks();
    } catch (err) {
      console.error('Error deleting task:', err);
    }
  };

  return (
    <div style={{ padding: '2rem', fontFamily: 'sans-serif' }}>
      <h2>Task Manager</h2>
      <input
        type="text"
        placeholder="Enter new task"
        value={newTask}
        onChange={(e) => setNewTask(e.target.value)}
      />
      <button onClick={handleAddTask} style={{ marginLeft: '1rem' }}>
        Add Task
      </button>

      <ul style={{ marginTop: '2rem' }}>
        {tasks.map((task) => (
          <li key={task.id} style={{ marginBottom: '0.5rem' }}>
            {task.title}
            <button
              style={{ marginLeft: '1rem' }}
              onClick={() => handleDeleteTask(task.id)}
            >
              Delete
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
