const express = require("express");
const app = express();
const port = 8000;

const {faker} = require("@faker-js/faker");

const createUser = () => {
    const newUser = {
        password: faker.internet.password(),
        email: faker.internet.email(),
        phoneNumber: faker.phone.phoneNumber(),
        lastName: faker.name.lastName(),
        firstName: faker.name.firstName(),
        id: faker.database.mongodbObjectId()
    }
    return newUser;
}

const createCompany = () => {
    const newCompany = {
        id: faker.database.mongodbObjectId(),
        companyName: faker.company.companyName(),
        address: {
            street: faker.address.streetAddress(),
            city: faker.address.city(),
            state: faker.address.state(),
            zipCode: faker.address.zipCode(),
            country: faker.address.country()
        }
    }
    return newCompany;
}

const newUserObject = createUser();
const newCompanyObject = createCompany();

app.get("/api/users/new", (req,res) => {
    res.json(newUserObject)
})

app.get("/api/companies/new", (req, res) => {
    res.json(newCompanyObject)
})

app.get("/api/user/company", (req, res) => {
    const newUser = createUser();
    const newCompany = createCompany();

    const newObject = {
        user: newUser,
        company: newCompany
    }
    
    res.json(newObject)
}
)

app.listen( port, () => console.log("Listening on port: ${port}"));