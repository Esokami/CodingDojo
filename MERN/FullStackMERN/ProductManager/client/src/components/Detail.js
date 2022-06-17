import React, {useEffect, useState} from 'react';
import axios from 'axios';
import {useParams, useNavigate} from 'react-router-dom';
import Container from 'react-bootstrap/Container';
import Table from 'react-bootstrap/Table';
import Button from 'react-bootstrap/Button';

const Detail = (props) => {
    const [product, setProduct] = useState({});
    const { id } = useParams();
    const navigate = useNavigate();

    useEffect( () => {
        axios.get("http://localhost:8000/api/products/" + id )
            .then((res) => {
                console.log(res.data);
                setProduct(res.data);
            })
            .catch((err) => {
                console.log(err);
            });
    },);

    const deleteProduct = (productId) => {
        axios.delete('http://localhost:8000/api/products/' + productId)
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
                        <td>Title:</td>
                        <td>{product.title}</td>
                    </tr>
                    <tr>
                        <td>Price:</td>
                        <td>${product.price}</td>
                    </tr>
                    <tr>
                        <td>Description:</td>
                        <td>{product.description}</td>
                    </tr>
                    <Button variant='danger' onClick={(e) => {deleteProduct(product._id)}}>Delete</Button>
                </tbody>
            </Table>
        </Container>
    )
}

export default Detail;