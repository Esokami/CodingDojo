import React, { useState} from 'react';

const Form = (props) => {
    const [firstName, setFirstName] = useState("");
    const [lastName, setLastName] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [confirmPassword, setConfirmPassword] = useState("");


    const createUser = (e) => {
        e.preventDefault();

        const newUser = { firstName, lastName, email, password, confirmPassword};
        console.log("Welcome", newUser);
        setFirstName("");
        setLastName("");
        setEmail("");
        setPassword("");
        setConfirmPassword("");
    }

    return (
        <div>
            <div>
                <form onSubmit={ createUser}>
                    <div>
                        <label>First Name: </label>
                        <input type="text" value={firstName} onChange={ (e) => setFirstName(e.target.value)} />
                    </div>
                    <div>
                        <label>Last Name: </label>
                        <input type="text" value={lastName} onChange={ (e) => setLastName(e.target.value)} />
                    </div>
                    <div>
                        <label>Email Address: </label>
                        <input type="email" value={email} onChange={ (e) => setEmail(e.target.value)} />
                    </div>
                    <div>
                        <label>Password: </label>
                        <input type="password" value={password} onChange={ (e) => setPassword(e.target.value)} />
                    </div>
                    <div>
                        <label>Confirm Password: </label>
                        <input type="password" value={confirmPassword} onChange={ (e) => setConfirmPassword(e.target.value)} />
                    </div>
                    <p>Your Form Data</p>
                </form>
            </div>
            <div>
                    <div>
                        <label>First Name: {firstName}</label>
                    </div>
                    <div>
                        <label>Last Name: {lastName}</label>
                    </div>
                    <div>
                        <label>Email Address: {email} </label>
                    </div>
                    <div>
                        <label>Password: {password}</label>
                    </div>
                    <div>
                        <label>Confirm Password: {confirmPassword}</label>
                    </div>
            </div>
        </div>
    )
}

export default Form;