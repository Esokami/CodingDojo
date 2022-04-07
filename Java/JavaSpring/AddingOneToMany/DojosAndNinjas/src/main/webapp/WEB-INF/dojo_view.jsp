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

<title>Dojo</title>
</head>
<body class="bg-secondary">
	<div class="bg-dark text-light m-5 p-3 border border-dark w-75">
	<h1 class="text-info"><c:out value="${dojo.name}"/> Location Ninjas</h1>
	<table class="table table-striped table-secondary">
		<thead>
			<tr>
				<th scope="col">First Name:</th>
				<th scope="col">Last Name:</th>
				<th scope="col">Age:</th>
			</tr>
		</thead>
		<tbody>
			<c:forEach var="ninja" items="${dojo.ninjas}">
			<tr>
				<td><c:out value="${ninja.firstName}"/></td>
				<td><c:out value="${ninja.lastName}"/></td>
				<td><c:out value="${ninja.age}"/></td>
			</tr>
			</c:forEach>
		</tbody>
	</table>
	</div>
</body>
</html>