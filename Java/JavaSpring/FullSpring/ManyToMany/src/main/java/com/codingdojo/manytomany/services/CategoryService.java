package com.codingdojo.manytomany.services;

import java.util.List;

import java.util.Optional;

import org.springframework.stereotype.Service;

import com.codingdojo.manytomany.models.Category;
import com.codingdojo.manytomany.models.Product;
import com.codingdojo.manytomany.repositories.CategoryRepository;

@Service
public class CategoryService {

	private final CategoryRepository categoryRepository;
	
	public CategoryService(CategoryRepository categoryRepository) {
		this.categoryRepository = categoryRepository;
	}
	
	// returns all
	public List<Category> allCategories(){
		return categoryRepository.findAll();
	}
	
	// creates
	public Category createCategory(Category x) {
		return categoryRepository.save(x);
	}
	
	// retrieves
	public Category findCategory(Long id) {
		Optional<Category> optionalCategory = categoryRepository.findById(id);
		if (optionalCategory.isPresent()) {
			return optionalCategory.get();
		}
		else {
			return null;
		}
	}
	
	// updates
	public Category updateCategory(Category x) {
		return categoryRepository.save(x);
	}
	
	// deletes
	public void deleteCategory(Category x) {
		categoryRepository.delete(x);
	}
	
	// get products in category
	public List<Category> getProducts(Product product)
	{
		return categoryRepository.findAllByProducts(product);
	}
	
	// get products not in category
	public List<Category> getUnusedProducts(Product product)
	{
		return categoryRepository.findByProductsNotContains(product);
	}
	
}
