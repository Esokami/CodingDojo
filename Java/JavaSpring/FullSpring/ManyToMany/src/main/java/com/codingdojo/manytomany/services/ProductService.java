package com.codingdojo.manytomany.services;

import java.util.List;
import java.util.Optional;

import org.springframework.stereotype.Service;

import com.codingdojo.manytomany.models.Category;
import com.codingdojo.manytomany.models.Product;
import com.codingdojo.manytomany.repositories.ProductRepository;

@Service
public class ProductService {
	private final ProductRepository productRepository;
	
	public ProductService(ProductRepository productRepository) {
		this.productRepository = productRepository;
	}
	
	// returns all
	public List<Product> allProducts(){
		return productRepository.findAll();
	}
	
	// creates
	public Product createProduct(Product x) {
		return productRepository.save(x);
	}
	
	// retrieves
	public Product findProduct(Long id) {
		Optional<Product> optionalProduct = productRepository.findById(id);
		if (optionalProduct.isPresent()) {
			return optionalProduct.get();
		}
		else {
			return null;
		}
	}
	
	// updates
	public Product updateProduct(Product x) {
		return productRepository.save(x);
	}
	
	// deletes
	public void deleteProduct(Product x) {
		productRepository.delete(x);
	}
	
	public List<Product> getCategory(Category category)
	{
		return productRepository.findAllByCategories(category);
	}
	
	public List<Product> getUnusedCategory(Category category)
	{
		return productRepository.findByCategoriesNotContains(category);
	}

	
}
