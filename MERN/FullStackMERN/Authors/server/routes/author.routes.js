const AuthorController = require('../controllers/author.controller');

module.exports = (app) => {
    //Used to create
    app.post('/api/authors/', AuthorController.createAuthor);

    //Used to get all 
    app.get('/api/authors', AuthorController.getAllAuthors);

    //Used to see one
    app.get('/api/authors/:id', AuthorController.getOneAuthor);

    // Used to update 
    app.put('/api/authors/:id', AuthorController.updateAuthor);

    //Used to delete
    app.delete('/api/authors/:id', AuthorController.deleteAuthor);
}