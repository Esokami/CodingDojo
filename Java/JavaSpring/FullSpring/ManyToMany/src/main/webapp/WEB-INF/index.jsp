<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!-- c:out ; c:forEach etc. --> 
<%@taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
<!-- Formatting (dates) --> 
<%@taglib uri="http://java.sun.com/jsp/jstl/fmt" prefix="fmt"%>
<!-- form:form -->
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form"%>
<!-- for rendering errors on PUT routes -->
<%@ page isErrorPage="true" %>

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">

<!-- for Bootstrap CSS -->
<link rel="stylesheet" href="/webjars/bootstrap/css/bootstrap.min.css" />
<!-- For any Bootstrap that uses JS or jQuery-->
<script src="/webjars/jquery/jquery.min.js"></script>
<script src="/webjars/bootstrap/js/bootstrap.min.js"></script>

<title>Login/Register</title>
</head>
<body class="bg-secondary">
	<div class="container p-3 text-light bg-dark">
 		<div>
 			<h1 class="text-primary text-center">Home Page</h1>
 		</div>
 		<div class="d-flex flex-column">
 			<a href="#">New Product</a>
 			<a href="#">New Category</a>
 		</div>
		<div class="container d-flex justify-content-evenly bg-secondary border border-light w-75 my-3">
			<div class="p-1">
				<h3>Products</h3>
				<ul class="p-0 m-0">
					<li>product 1</li>
				</ul>
			</div>
			<div class="p-1">
				<h3>Categories</h3>
				<ul class="p-0 m-0">
					<li>category 1</li>
				</ul>
			</div>
		</div>
    </div>
</body>
</html>