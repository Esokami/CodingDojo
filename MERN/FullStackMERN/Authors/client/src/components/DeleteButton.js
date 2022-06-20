import React from "react";
import axios from 'axios';
import Button from 'react-bootstrap/Button';

const DeleteButton = (props) => {
    const {authorId, successCallBack} = props;
    const deleteAuthor = (e) => {
        axios.delete('http://localhost:8000/api/authors/' + authorId)
            .then((res) => {
                successCallBack();
            })
            .catch((err) => {
                console.log(err);
            })
    }

    return (
        <Button variant="danger" onClick={deleteAuthor}>
            Delete
        </Button>
    )
}

export default DeleteButton;