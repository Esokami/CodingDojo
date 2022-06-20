import React, {useEffect, useState} from 'react';
import axios from 'axios';
import {Link, useNavigate} from 'react-router-dom';
import DeleteButton from '../components/DeleteButton';
import Table from 'react-bootstrap/Table';
import Container from 'react-bootstrap/Container';
import Button from 'react-bootstrap/Button';

const AuthorList = (props) => {
    const [authors, setAuthors] = useState([])
    const navigate = useNavigate();

    useEffect( () => {
        axios.get("http://localhost:8000/api/authors")
            .then((res) => {
                console.log(res.data);
                setAuthors(res.data);
            })
            .catch((err) => {
                console.log(err);
            })
    },[])

    const removeFromDom = authorId => {
        setAuthors(authors.filter(author => author._id !== authorId))
    }

    return (
        <Container>
            <h1>Favorite Authors</h1>
            <Link to="/authors/new">Add an author</Link>
            <h5>We have quotes by:</h5>
            <Table striped bordered hover>
                <thead>
                    <tr>
                        <th>Author</th>
                        <th colSpan={2}>Actions Available</th>
                    </tr>
                </thead>
                <tbody>
                    {authors.map((author, index) => {
                        return (
                            <tr key={index}>
                                <td>{author.name}</td>
                                <td><Button variant="primary" onClick={() => navigate(`/authors/edit/${author._id}`)}>Edit</Button></td>
                                <td><DeleteButton authorId={author._id} successCallBack={() => removeFromDom(author._id)}/></td>
                            </tr>
                        )
                        })}
                </tbody>
            </Table>
        </Container>
                )
}

export default AuthorList;