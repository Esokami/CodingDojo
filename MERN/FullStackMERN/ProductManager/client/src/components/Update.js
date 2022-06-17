import React, {useEffect, useState} from 'react';
import axios from 'axios';
import {useNavigate, useParams} from 'react-router-dom';
import Form from 'react-bootstrap/Form';
import Container from 'react-bootstrap/Container';
import Button from 'react-bootstrap/Button';

const Update = (props) => {
    const {id} = useParams();
    const [title, setTitle] = useState("");
    const [price, setPrice] = useState("");
    const [description, setDescription] = useState("");
    const navigate = useNavigate();

    useEffect(() => {
        axios.get('http://localhost:8000/api/products/' + id)
            .then((res) => {
                console.log(res);
                setTitle(res.data.title);
                setPrice(res.data.price);
                setDescription(res.data.description);
            })
            .catch((err) =>{
                console.log(err);
            });
    }, [])

    const updateProduct = (e) => {
        e.preventDefault();
        axios.put('http://localhost:8000/api/products/' + id, {
            title,
            price,
            description
        })
            .then((res) => {
                console.log(res);
                navigate("/");
            })
            .catch((err) =>{
                console.log(err);
            } );
    }

    return (
        <Container>
            <h1>Update a Product</h1>
            <Form onSubmit={updateProduct}>
                <Form.Group>
                    <Form.Label>Title</Form.Label>
                    <Form.Control type="text" name="title" value={title} onChange={(e) => {setTitle(e.target.value)}}/>
                </Form.Group>
                <Form.Group>
                    <Form.Label>Price</Form.Label>
                    <Form.Control type="number" name="price" step="0.01" min="0" value={price} onChange={(e) => {setPrice(e.target.value)}}/>
                </Form.Group>
                <Form.Group>
                    <Form.Label>Description</Form.Label>
                    <Form.Control type="text" name="descriptioin" value={description} onChange={(e) => {setDescription(e.target.value)}}/>
                </Form.Group>
                <Button variant='success' className='mt-2' type="submit">Update</Button>
            </Form>
        </Container>
    )
}

export default Update;