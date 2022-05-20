import React, {useState} from 'react';
import styles from './Todo.module.css';

const Todo = (props) => {
    const [todo, setTodo] = useState("");
    const [todoArr, setTodoArr] = useState([]);

    const handleSubmit = (e) => {
        e.preventDefault();

        const newTodo = {
            text: todo,
            done: false
        }

        const newTodoArr = [...todoArr, newTodo];
        setTodoArr(newTodoArr);
        setTodo("");
    }

    const handleDone = (id) => {
        const checkTodo = todoArr.map((todo, n) => {
            if (n == id){
                todo.done = !todo.done;
            }
            return todo;
        })
        setTodoArr(checkTodo);
    }

    const handleDelete = (id) => {
        const deleteTodos = todoArr.filter((todo, n) => {
            return n != id;
        })

        setTodoArr(deleteTodos);
    }

    return (
        <div className={styles.container}>
            <form className={styles.form} onSubmit={handleSubmit}>
                <label>Add Todo</label>
                <input className={styles.input} type="text" onChange={(e) => setTodo(e.target.value)} value={todo}></input>
                <button className={styles.btn} type="submit">Add</button>
            </form>

            {todoArr.map((n, index) => {
                return (
                    <div className={styles.task} key={index}>
                        <ul className={styles.list}>
                            <li>
                                <label style={{textDecoration: n.done ? 'line-through' : 'none'}}>{n.text}</label>
                                <input type="checkbox"  onChange={(e) => handleDone(index)} checked={todo.done}></input>
                                <button className={styles.delete} type="submit" onClick={(e) => handleDelete(index)}>Delete</button>
                            </li>
                        </ul>
                    </div>
                )
            })}
        </div>
    )
}

export default Todo;