import React, {useEffect, useState} from 'react';
import axios from 'axios';
import {useNavigate, useParams} from 'react-router-dom';

const Update = (props) => {
    const {id} = useParams;
    const [title, setTitle] = useState();
    const [price, setPrice] = useState();
    const [description, setDescription] = useState();
    const navigate = useNavigate();

    useEffect(() => {
        axios.get('http://localhost:8000/api/products/' + id)
            .then(res => {
                setTitle(res.data.setTitle)
                setPrice(res.data.setPrice)
                setDescription(res.data.setDescription)
            })
            .catch(err => console.log(err))
    })

    const updateProduct = (e) => {
        e.preventDefault();
        axios.put('http://localhost:8000/api/people/' + id, {
            title,
            price,
            description
        })
            .then(res => {
                console.log(res)
                navigate("/")
            })
            .catch(err => console.log(err))
    }

    return (
        <div>
            <h1>Update a Product</h1>
            <form onSubmit={updateProduct}>
                <p>
                    <label>Title</label>
                    <input type="text" name="title" value={title} onChange={(e) => setTitle(e.target.value)}/>
                </p>
                <p>
                    <label>Price</label>
                    <input type="number" name="price" step="0.01" min="0" value={price} onChange={(e) => setTitle(e.target.value)}/>
                </p>
                <p>
                    <label>Description</label>
                    <input type="text" name="descriptioin" value={description} onChange={(e) => setDescription(e.target.value)}/>
                </p>
                <input type="submit"/>
            </form>
        </div>
    )
}

export default Update;