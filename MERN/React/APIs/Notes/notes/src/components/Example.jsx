import React, {useState, useEffect} from 'react';

const Example = (props) => {
    const [pokemon, setPokemon] = useState([]);

    const Capitalize = (str) => {
        return str.charAt(0).toUpperCase() + str.slice(1);
    }
 
    useEffect(() => {
        fetch('https://pokeapi.co/api/v2/pokemon')
            .then(response => response.json())
            .then(response => setPokemon(response.results))
    }, []);
 
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
    );
}
export default Example;

