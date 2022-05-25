import React, {useEffect, useState} from 'react';
import axios from 'axios';

const Pokemon = props => {
    const [pokemon, setPokemon] = useState(null);

    const Capitalize = (str) => {
        return str.charAt(0).toUpperCase() + str.slice(1);
    }

    useEffect( () => {
        axios.get('https://pokeapi.co/api/v2/pokemon')
            .then(response => {setPokemon(response.data.results)})
    }, []);

    if (!pokemon) return null;

    return (
        <div>
            {pokemon.length > 0 && pokemon.map((pokemon, index)=>{
                return (
                <div key={index}>
                    <ul>
                        <li> {Capitalize(pokemon.name)}</li>
                    </ul>
                </div>
                )
            })}
        </div>
    )
}

export default Pokemon;