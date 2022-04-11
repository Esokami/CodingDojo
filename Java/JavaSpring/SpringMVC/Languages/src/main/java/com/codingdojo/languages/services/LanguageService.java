package com.codingdojo.languages.services;

import java.util.List;
import java.util.Optional;

import org.springframework.stereotype.Service;

import com.codingdojo.languages.models.Language;
import com.codingdojo.languages.repositories.LanguageRepository;

@Service
public class LanguageService {
	
	private final LanguageRepository languageRepository;
	
	public LanguageService(LanguageRepository languageRepository) {
		this.languageRepository = languageRepository;
	}
	
	// returns all languages
	public List<Language> allLanguages(){
		return languageRepository.findAll();
	}
	
	// creates a new language
	public Language create(Language l) {
		return languageRepository.save(l);
	}
	
	// retrieves language
	public Language findLanguage(Long id) {
		Optional<Language> optionalLanguage = languageRepository.findById(id);
		if (optionalLanguage.isPresent()) {
			return optionalLanguage.get();
		}
		else {
			return null;
		}
	}
	
	// updates language
	public Language updateLanguage(Language l) {
		return languageRepository.save(l);
	}
	
	// delete language
	public void delete(Long id) {
		Optional<Language> optionalLanguage = languageRepository.findById(id);
		if (optionalLanguage.isPresent()) {
			languageRepository.deleteById(id);
		}
	}
}
