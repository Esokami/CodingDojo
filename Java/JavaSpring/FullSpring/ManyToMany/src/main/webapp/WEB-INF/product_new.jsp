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

<title>New Product</title>
</head>
<body class="bg-warning">
	<div class="bg-dark text-light m-5 p-3 border border-dark w-75 rounded">
		<div class="d-flex justify-content-between">
			<h1 class="text-warning">New Product</h1>
			<a href="/">Home</a>
		</div>
		<form:form class="d-flex flex-column mb-3 text-light w-50" action="/newProduct" method="POST" modelAttribute="product">
			<div class="p-2 d-flex flex-column justify-content-between">
				<form:label path="name">Name:</form:label>
				<form:errors path="name" class="text-danger"/>
				<form:input path="name"/>
			</div>
			<div class="p-2 d-flex flex-column justify-content-between">
				<form:label path="description">Description</form:label>
				<form:errors path="description" class="text-danger"/>
				<form:input path="description"/>
			</div>
			<div class="p-2 d-flex flex-column justify-content-between">
				<form:label path="price">Price:</form:label>
				<form:errors path="price" class="text-danger"/>
				<form:input type="number" step="any" min="0" path="price"/>
			</div>
			<button class="btn btn-success w-25 align-self-end" type="submit">Submit</button>
		</form:form>
	</div>
</body>
</html>