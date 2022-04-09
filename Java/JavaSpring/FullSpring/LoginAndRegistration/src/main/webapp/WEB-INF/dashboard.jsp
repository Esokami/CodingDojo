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

<title>Dashboard</title>
</head>
<body class="bg-secondary">
	<div class="container d-flex flex-column align-items-left text-light bg-dark p-3">
		<div>
			<div class="d-flex justify-content-between">
				<h1 class="text-info">Welcome, <c:out value="${user.username}"></c:out>!</h1>
				<a href="/logout">Logout</a>
			</div>
			<div class="d-flex justify-content-between">
				<h5>Books from everyone's shelves:</h5>
				<a href="/dashboard/new">+Add a book to my shelf</a>
			</div>

			<div>
			<table class="table table-hover table-dark">
				<thead>
					<tr>
						<th scope="col">ID</th>
						<th scope="col">Title</th>
						<th scope="col">Author</th>
						<th scope="col">Posted By</th>
					</tr>
				</thead>
				<tbody>
					<c:forEach var="oneBook" items="${books}">
					<tr>
						<td><c:out value="${oneBook.id}"></c:out></td>
						<td class="w-50"><a href="/dashboard/${oneBook.id}"><c:out value="${oneBook.title}"></c:out></a></td>
						<td><c:out value="${oneBook.author}"></c:out></td>
						<td><c:out value="${oneBook.user.username}"></c:out></td>
					</tr>
					</c:forEach>
				</tbody>
			</table>
			</div>
		</div>
	</div>
</body>
</html>