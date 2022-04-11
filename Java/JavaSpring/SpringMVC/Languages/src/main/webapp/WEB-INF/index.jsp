<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
    
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>  

<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form" %>

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

<title>Languages</title>
</head>
<body class="bg-secondary">
	<div class="m-5 p-3 bg-dark w-75 rounded">
		<h1 class="text-info">Languages</h1>
		<div class="bg-dark"> 
			<table class="table table-hover table-dark">
				<thead>
					<tr>
						<th scope="col">Name</th>
						<th scope="col">Creator</th>
						<th scope="col">Version</th>
						<th scope="col" colspan="2">Actions</th>
					</tr>
				</thead>
				<tbody>
				<c:forEach var="language" items="${languages}">
					<tr>
						<td><a href="/languages/${language.id}"><c:out value="${language.name}"></c:out></a></td>
						<td><c:out value="${language.creator}"></c:out></td>
						<td><c:out value="${language.version}"></c:out></td>
						<td><a href="/languages/edit/${language.id}">edit</a></td>
						<td>
							<form action="/languages/${language.id}" method="POST">
							<input type="hidden" name="_method" value="delete">
							<button class="btn btn-danger" type="submit">delete</button>
							</form>
						</td>
					</tr>
				</c:forEach>
				</tbody>
			</table>
		</div>
	</div>
	<div class="m-5 p-3 bg-dark text-light w-75 rounded">
		<h2 class="text-success">Add a language:</h2>
		<form:form class="d-flex flex-column align-items-center" action="/languages" method="POST" modelAttribute="language">
			<div class="d-flex flex-column w-50">
				<form:label path="name">Name:</form:label>
				<form:errors path="name" class="text-danger"/>
				<form:input path="name"/>
			</div>
			<div class="d-flex flex-column w-50">
				<form:label path="creator">Creator:</form:label>
				<form:errors path="creator" class="text-danger"/>
				<form:input path="creator"/>
			</div>
			<div class="d-flex flex-column w-50">
				<form:label path="version">Version:</form:label>
				<form:errors path="version" class="text-danger"/>
				<form:input type="number" step="any" min="0" path="version"/>
			</div>
			<button class="btn btn-success mt-2" type="submit">Submit</button>
		</form:form>
	</div>
</body>
</html>