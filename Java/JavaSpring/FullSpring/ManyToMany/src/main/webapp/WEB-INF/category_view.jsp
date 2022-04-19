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

<title>View Category</title>
</head>
<body class="bg-danger">
	<div class="bg-dark text-light m-5 p-3 border border-dark rounded">
		<div class="d-flex flex-column">
			<h1 class="text-danger text-center"><c:out value="${category.name}"/></h1>
			<a href="/">Home</a>
		</div>
		<div class="d-flex flex-column border-top border-light mt-2">
			<h4 class="text-info mt-2">Products</h4>
			<ul>
			<c:forEach var="product" items="${usedProducts}">
				<li><c:out value="${product.name}"></c:out></li>
			</c:forEach>
			</ul>
		</div>
		<div class="border-top border-light mt-2">
			<h4 class="text-success mt-2">Add Product:</h4>
			<form:form class="d-flex flex-column mb-3 text-light" action="/categories/${id}" method="POST">
				<select name="productId" id="productId" class="input w-25">
					<c:forEach var="product" items="${unusedProducts}">
						<option value="${product.id}">${product.name}</option>
					</c:forEach>
				</select>
				<button class="btn btn-success w-25 mt-2" type="submit">Add</button>
			</form:form>
		</div>
	</div>
</body>
</html>