package com.codingdojo.loginandregistration.controllers;

import javax.servlet.http.HttpSession;
import javax.validation.Valid;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;

import com.codingdojo.loginandregistration.models.Book;
import com.codingdojo.loginandregistration.models.User;
import com.codingdojo.loginandregistration.services.BookService;
import com.codingdojo.loginandregistration.services.UserService;

@Controller
public class BookController {
	@Autowired
	BookService bookService;
	@Autowired
	private UserService userService;

	//***GET MAPPINGS***
	
	@GetMapping("/dashboard/{bookId}")
	public String showBook(Model model, 
			@PathVariable("bookId") Long bookId,
			HttpSession session) {
		
		if(session.getAttribute("id")==null) {
			return "redirect:/";
		}
		
		Book book = bookService.findBook(bookId);
	
		model.addAttribute("book", book);
		
		Long id = (Long)session.getAttribute("id");
		User user = userService.findById(id);
		model.addAttribute("user", user);
		
		return "book_view.jsp";
	}
	
	@GetMapping("/dashboard/new")
	public String newBook(@ModelAttribute("book") Book book,
			Model model,
			HttpSession session) {
		
		Long id = (Long)session.getAttribute("id");
		User user = userService.findById(id);
		model.addAttribute("user", user);
		
		return "book_new.jsp";
	}
	
	
	@GetMapping("/dashboard/edit/{bookId}")
	public String editBook(@PathVariable("bookId") Long bookId,
			Model model,
			HttpSession session) {
		
		if(session.getAttribute("id") == null) {
			return "redirect:/";
		}
		
		Book book = bookService.findBook(bookId);
		model.addAttribute("book", book);
		return "book_edit.jsp";
	}
	
	//***POST MAPPINGS***
	
	@PostMapping("/createBook")
	public String create(@Valid @ModelAttribute("book") Book book,
			BindingResult result) {
		
		if (result.hasErrors()) {
			return "book_new.jsp";
		}
		
		bookService.createBook(book);
		return "redirect:/dashboard";
		
	}
	
	@PutMapping("/dashboard/edit/{bookId}")
	public String updateBook(
			@PathVariable("bookId") Long bookId,
			Model model,
			@Valid @ModelAttribute("book") Book book, 
			BindingResult result) {
		if (result.hasErrors()) {
			return "redirect:/dashboard/edit/{bookId}";
		}
		else {
			bookService.updateBook(book);
			return "redirect:/dashboard";
		}
	}
}
