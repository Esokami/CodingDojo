package com.codingdojo.manytomany.services;

import java.util.List;
import java.util.Optional;

import org.springframework.stereotype.Service;

import com.codingdojo.manytomany.models.Product;
import com.codingdojo.manytomany.repositories.ProductRepository;

@Service
public class ProductService {
	private final ProductRepository productRepo;
	
	public ProductService(ProductRepository productRepo) {
		this.productRepo = productRepo;
	}
	
	// returns all
	public List<Product> allProducts(){
		return productRepo.findAll();
	}
	
	// creates
	public Product createProduct(Product x) {
		return productRepo.save(x);
	}
	
	// retrieves
	public Product findProduct(Long id) {
		Optional<Product> optionalProduct = productRepo.findById(id);
		if (optionalProduct.isPresent()) {
			return optionalProduct.get();
		}
		else {
			return null;
		}
	}
	
	// updates
	public Product updateProduct(Product x) {
		return productRepo.save(x);
	}
	
	// deletes
	public void deleteProduct(Product x) {
		productRepo.delete(x);
	}
}
