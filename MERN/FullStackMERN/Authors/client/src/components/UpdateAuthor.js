import React, {useEffect, useState} from 'react';
import axios from 'axios';
import {Link, useNavigate, useParams} from 'react-router-dom';
import Form from 'react-bootstrap/Form';
import Container from 'react-bootstrap/Container';
import Button from 'react-bootstrap/Button';

const Update = (props) => {
    const {id} = useParams();
    const [name, setName] = useState("");
    const navigate = useNavigate();

    const [errors, setErrors] =useState({});

    useEffect(() => {
        axios.get('http://localhost:8000/api/authors/' + id)
            .then((res) => {
                console.log(res);
                setName(res.data.name);
            })
            .catch((err) =>{
                console.log(err);
            });
    }, [])

    const updateAuthor = (e) => {
        e.preventDefault();
        axios.put('http://localhost:8000/api/authors/' + id, {
            name
        })
            .then((res) => {
                console.log(res);
                navigate("/");
            })
            .catch((err) =>{
                console.log(err);
                setErrors(err.response.data.errors);
            } );
    }

    return (
        <Container>
            <h1>Favorite Authors</h1>
            <Link to="/">Home</Link>
            <h5>Edit this author:</h5>
            <Form onSubmit={updateAuthor}>
                <Form.Group>
                    <Form.Label>Name</Form.Label>
                    <Form.Control type="text" name="name" value={name} onChange={(e) => {setName(e.target.value)}}/>
                    {
                    errors.name ? (
                        <p className="text-danger">{errors.name.message}</p>
                    ) : null
                    }
                </Form.Group>
                <Button variant='warning' className='m-2' onClick={() => navigate("/")}>Cancel</Button>
                <Button variant='success' className='m-2' type="submit">Submit</Button>
            </Form>
        </Container>
    )
}

export default Update;