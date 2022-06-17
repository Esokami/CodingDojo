import React, {useEffect} from 'react';
import axios from 'axios';
import {Link, useNavigate} from 'react-router-dom';
import Table from 'react-bootstrap/Table';
import Container from 'react-bootstrap/Container';
import Button from 'react-bootstrap/Button';

const ProductList = (props) => {
    const {products, setProducts} =props;
    const navigate = useNavigate();

    useEffect( () => {
        axios.get("http://localhost:8000/api/products")
            .then((res) => {
                console.log(res.data);
                setProducts(res.data);
            })
            .catch((err) => {
                console.log(err);
            })
    },[])

    const deleteProduct = (productId) => {
        axios.delete('http://localhost:8000/api/products/' + productId)
            .then((res) => {
                const newProductList = products.filter((product, index) => product._id !== productId);
                setProducts(newProductList);
            })
            .catch((err) => {
                console.log(err);
            });
    }

    return (
        <div>
            {
                products.map((product, index) => {
                    return (
                        <Container>
                            <Table striped bordered hover  key={index}>
                                <tbody>
                                    <tr>
                                        <td><Link to={`/products/${product._id}`}>{product.title} Page</Link></td>
                                        <td><Button variant="primary" onClick={() => navigate(`/products/edit/${product._id}`)}>Edit</Button></td>
                                        <td><Button variant="danger" onClick={() => {deleteProduct(product._id)}}>Delete</Button></td>
                                    </tr>
                                </tbody>
                            </Table>
                        </Container>
                    )
                })
            }
        </div>
    )
}

export default ProductList;