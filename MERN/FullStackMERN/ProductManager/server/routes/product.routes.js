const ProductController = require('../controllers/product.controller');

module.exports = (app) => {
    //Used to create a product
    app.post('/api/products', ProductController.createProduct);

    //Used to get all products
    app.get('/api/products', ProductController.getAllProducts);

    //Used to see details of a specific product
    app.get('/api/products/:id', ProductController.getProduct);

    // Used to update a product
    app.put('/api/products/:id', ProductController.updateProduct);

    //Used to delete a product
    app.delete('/api/products/:id', ProductController.deleteProduct);
}