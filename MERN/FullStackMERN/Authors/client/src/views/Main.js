import React, {useEffect, useState} from 'react';
import axios from 'axios';
import AuthorList from '../components/AuthorList';

const Main = () => {
    const [authors, setAuthors] = useState([]);

    useEffect(() => {
        axios.get('http://localhost:8000/api/authors')
            .then((res) => {
                setAuthors(res.data);
            })
            .catch((err) => {
                console.log(err);
            })
    }, [])

    const removeFromDom = authorId => {
        axios.delete('http://localhost:8000/api/authors/' + authorId)
            .then((res) => {
                console.log(res);
                console.log(res.data);
                setAuthors(authors.filter(author => author._id !== authorId));
            })
            .catch((err) => {
                console.log(err);
            })
    }


    return (
        <div>
            <AuthorList authors={authors} removeFromDom={removeFromDom}/>
        </div>
    )
}

export default Main;