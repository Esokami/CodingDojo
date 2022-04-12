package com.codingdojo.loginandregistration.repositories;

import java.util.List;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import com.codingdojo.loginandregistration.models.Book;

@Repository
public interface BookRepository extends CrudRepository<Book, Long>{
	List<Book> findAll();
	List<Book> findByUserId(Long userId);
	List<Book> findByBorrowerId(Long userId);
	List<Book> findByBorrowerOrUserId(Long borrowerId, Long userId);
}
