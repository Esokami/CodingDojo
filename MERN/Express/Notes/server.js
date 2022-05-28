const express = require("express");
const app = express();
const port = 8000;

const users = [
    {firstName: "Reimu", lastName: "Hakurei"},
    {firstName: "Marisa", lastName: "Kirisame"},
    {firstName: "Sanae", lastName: "Kochiya"},
    {firstName: "Sakuya", lastName: "Izayoi"},
    {firstName: "Momiji", lastName: "Inubashiri"},
]

//POST
// make sure these lines are boave any app.get or app.post code blocks
app.use(express.json());
app.use(express.urlencoded({extended: true}));

app.post("/api/users", (req, res) => {
    // req.body will contain the form data from Postman or from React
    console.log(req.body);

    // we can push it into the users array for now...
    // later on this will be inserted into a database
    users.push(req.body);

    // we always need to respond with something
    res.json({status: "ok"});
})

//GET
// req is shorthand for request
// res is shorthand for response
app.get("/api", (req, res) => {
    res.json({message: "Testing Nodemon"})
})

app.get("/api/users", (req, res) => {
    res.json(users)
})

// Getting data from URL
app.get("/api/users/:id", (req,res) => {
    console.log(req.params.id);

    res.json( users[req.params.id]);
})

// Update data
app.put("/api/users/:id", (req,res) => {
    const id = req.params.id;

    users[id] = req.body;

    res.json({status: "okd"});
})

// Deleting data 
app.delete("/api/users/:id", (req, res) => {
    const id = req.params.id;

    users.splice(id, 1);

    res.json({status: "ok"});
})


app.listen( port, () => console.log('Listening on port: ${port}'));