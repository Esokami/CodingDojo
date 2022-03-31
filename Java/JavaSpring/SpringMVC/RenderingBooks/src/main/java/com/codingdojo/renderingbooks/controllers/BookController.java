package com.codingdojo.renderingbooks.controllers;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;

import com.codingdojo.renderingbooks.models.Book;
import com.codingdojo.renderingbooks.services.BookService;

@Controller
public class BookController {
	
	@Autowired
	BookService bookService;
	
	@RequestMapping("/")
	public String index() {
		
		return "redirect:/books";
	}
	
	@GetMapping("/books")
	public String dashboard(Model model) {
		
		List<Book> books = bookService.allBooks();
		model.addAttribute("books", books);
		
		return "index.jsp";
	}
	
	@GetMapping("/books/{bookId}")
	public String showBook(Model model, @PathVariable("bookId") Long bookId) {
		
		Book book = bookService.findBook(bookId);
	
		model.addAttribute("book", book);
		
		return "show.jsp";
	}
}
