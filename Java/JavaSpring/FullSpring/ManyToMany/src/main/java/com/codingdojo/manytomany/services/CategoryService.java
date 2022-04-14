package com.codingdojo.manytomany.services;

import java.util.List;
import java.util.Optional;

import org.springframework.stereotype.Service;

import com.codingdojo.manytomany.models.Category;
import com.codingdojo.manytomany.repositories.CategoryRepository;

@Service
public class CategoryService {

	private final CategoryRepository categoryRepo;
	
	public CategoryService(CategoryRepository categoryRepo) {
		this.categoryRepo = categoryRepo;
	}
	
	// returns all
	public List<Category> allCategories(){
		return categoryRepo.findAll();
	}
	
	// creates
	public Category createCategory(Category x) {
		return categoryRepo.save(x);
	}
	
	// retrieves
	public Category findCategory(Long id) {
		Optional<Category> optionalCategory = categoryRepo.findById(id);
		if (optionalCategory.isPresent()) {
			return optionalCategory.get();
		}
		else {
			return null;
		}
	}
	
	// updates
	public Category updateCategory(Category x) {
		return categoryRepo.save(x);
	}
	
	// deletes
	public void deleteCategory(Category x) {
		categoryRepo.delete(x);
	}
	

}
