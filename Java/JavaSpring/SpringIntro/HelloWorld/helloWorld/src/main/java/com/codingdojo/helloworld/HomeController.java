package com.codingdojo.helloworld;

import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
//@RequestMapping("/greeting")
public class HomeController {
	
	@RequestMapping("")
	public String index()
	{
		return "This is accessed view http://your_server/simple/root";
	}
	
	@RequestMapping("/")
	public String index(@RequestParam(value="q", required=false) String searchQuery) {
		if (searchQuery == null) {
			return "You searched for: nothing";
		}
		else {
			return "You searched for: " + searchQuery;
		}
		
	}
	
	@RequestMapping("/m/{track}/{module}/{lesson}")
	public String showLesson(@PathVariable("track") String track, @PathVariable("module") String module, @PathVariable("lesson") String lesson) {
		return "Track: " + track + ", Module: " + module + ", Lession: " + lesson;
	}
	
	
	@RequestMapping("/hello")
	public String hello() {
		return "Hello world! What route did you use to access me?";
	}
	
	@RequestMapping("/goodbye")
	public String world() {
		return "Goodbye world!";
	}
}
