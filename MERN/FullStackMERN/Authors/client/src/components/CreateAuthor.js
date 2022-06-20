import React, {useState} from 'react';
import axios from 'axios';
import {Link, useNavigate} from 'react-router-dom'
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button'
import Container from 'react-bootstrap/Container';

const AuthorForm = (props) => {
    const {authors, setAuthors} = props;
    const [name, setName] = useState("");
    const navigate = useNavigate();

    const [errors, setErrors] = useState({});

    const onSubmitHandler = (e) => {
        e.preventDefault();

        axios.post('http://localhost:8000/api/authors', {
            name: name
        })
            .then((res) => {
                console.log(res);
                console.log(res.data);
                navigate("/");
                setAuthors([...authors, res.data]);
            })
            .catch((err) => {
                console.log(err);
                setErrors(err.response.data.errors);
            });
    }

    return (
        <Container>
            <h1>Favorite Authors</h1>
            <Link to={"/"}>Home</Link>
            <h5>Add a new author:</h5>
            <Form onSubmit={(onSubmitHandler)}>
            <Form.Group className="p-2">
                <Form.Label>Name</Form.Label>
                <Form.Control type="text" onChange={(e) => setName(e.target.value)}/>
                {
                    errors.name ? (
                        <p className="text-danger">{errors.name.message}</p>
                    ) : null
                }
            </Form.Group>
            <Button className='m-2' variant="warning" onClick={() => navigate("/")}>Cancel</Button> 
            <Button className='m-2' variant="success" type="submit">Submit</Button> 
        </Form>
        </Container>
    )
}

export default AuthorForm;