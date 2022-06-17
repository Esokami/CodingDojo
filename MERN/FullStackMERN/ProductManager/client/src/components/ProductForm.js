import React, {useState} from 'react';
import axios from 'axios';
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button'
import Container from 'react-bootstrap/Container';

const ProductForm = (props) => {
    const {products, setProducts} = props;
    const [title, setTitle] = useState("");
    const [price, setPrice] = useState("");
    const [description, setDescription] = useState("");

    const [errors, setErrors] = useState({});

    const onSubmitHandler = (e) => {
        e.preventDefault();

        axios.post('http://localhost:8000/api/products', {
            title,
            price,
            description
        })

            .then((res) => {
                console.log(res);
                console.log(res.data);
                setProducts([...products, res.data]);
            })
            .catch((err) => {
                console.log(err);
                setErrors(err.response.data.errors);
            });
    }

    return (
        <Container>
            <Form onSubmit={(onSubmitHandler)}>
            <Form.Group className='p-2'>
                <Form.Label>Title</Form.Label>
                <Form.Control type="text" onChange={(e) => setTitle(e.target.value)}/>
                {
                    errors.title ? (
                        <p>{errors.title.message}</p>
                    ) : null
                }
            </Form.Group>
            <Form.Group className='p-2'>
                <Form.Label>Price</Form.Label>
                <Form.Control type="number" placeholder="0.00" step="0.01" min="0" onChange={(e) => setPrice(e.target.value)}/>
                {
                    errors.price ? (
                        <p>{errors.price.message}</p>
                    ) : null
                }
            </Form.Group>
            <Form.Group className='p-2'>
                <Form.Label>Description</Form.Label>
                <Form.Control type="text" onChange={(e) => setDescription(e.target.value)}/>
                {
                    errors.description ? (
                        <p>{errors.description.message}</p>
                    ) : null
                }
            </Form.Group>
            <Button className='m-2' variant="info" type="submit">Submit</Button> 
        </Form>
        </Container>
    )
}

export default ProductForm;