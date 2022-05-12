import React, { useState} from 'react';

const Form = (props) => {
    const [firstName, setFirstName] = useState("");
    const [lastName, setLastName] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [confirmPassword, setConfirmPassword] = useState("");
    const [hasBeenSubmitted, setHasBeenSubmitted] = useState(false);

    const createUser = (e) => {
        e.preventDefault();

        const newUser = { firstName, lastName, email, password, confirmPassword};
        console.log("Welcome", newUser);
        setFirstName("");
        setLastName("");
        setEmail("");
        setPassword("");
        setConfirmPassword("");
    
        setHasBeenSubmitted(true);
    }

    const formMessage = () => {
        if (hasBeenSubmitted){
            return "Thank you for submitting the form!";
        }
        else{
            return "Welcome, please submit the form.";
        }
    }

    return (
        <form onSubmit={ createUser}>
        {
            hasBeenSubmitted ?
            <h3>Thank you for submitting the form!</h3>:
            <h3>Welcome, please submit the form.</h3>
        }
        <div>
            <label>First Name: </label>
            <input type="text" value={firstName} onChange={ (e) => setFirstName(e.target.value)} />
        </div>
        {firstName.length < 2 && <h5>First name is less than 2</h5>}
        <div>
            <label>Last Name: </label>
            <input type="text" value={lastName} onChange={ (e) => setLastName(e.target.value)} />
        </div>
        {lastName.length < 2 && <h5>Last name is less than 2</h5>}
        <div>
            <label>Email Address: </label>
            <input type="email" value={email} onChange={ (e) => setEmail(e.target.value)} />
        </div>
        {email.length < 2 && <h5>Email is less than 2</h5>}
        <div>
            <label>Password: </label>
            <input type="password" value={password} onChange={ (e) => setPassword(e.target.value)} />
        </div>
        {password.length < 8 && <h5>Password is less than 8</h5>}
        <div>
            <label>Confirm Password: </label>
            <input type="password" value={confirmPassword} onChange={ (e) => setConfirmPassword(e.target.value)} />
        </div>
        {confirmPassword === password && <h5>Passwords must match</h5>}
        <input type="submit" value="Create User"></input>
    </form>
    )
}

export default Form;