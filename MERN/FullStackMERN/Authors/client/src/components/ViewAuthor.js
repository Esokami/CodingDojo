import React, {useEffect, useState} from 'react';
import axios from 'axios';
import {useParams, useNavigate} from 'react-router-dom';
import Container from 'react-bootstrap/Container';
import Table from 'react-bootstrap/Table';
import Button from 'react-bootstrap/Button';

const ViewAuthor = (props) => {
    const [author, setAuthor] = useState({});
    const { id } = useParams();
    const navigate = useNavigate();

    useEffect( () => {
        axios.get("http://localhost:8000/api/authors/" + id )
            .then((res) => {
                console.log(res.data);
                setAuthor(res.data);
            })
            .catch((err) => {
                console.log(err);
            });
    },);

    const deleteAuthor = (authorId) => {
        axios.delete('http://localhost:8000/api/authors/' + authorId)
            .then((res) => {
                navigate("/");
            })
            .catch((err) => {
                console.log(err);
            });
    }

    return (
        <Container>
            <Table striped bordered hover>
                <tbody>
                    <tr>
                        <td>Name:</td>
                        <td>{author.name}</td>
                    </tr>
                    <Button variant='danger' onClick={(e) => {deleteAuthor(author._id)}}>Delete</Button>
                </tbody>
            </Table>
        </Container>
    )
}

export default ViewAuthor;