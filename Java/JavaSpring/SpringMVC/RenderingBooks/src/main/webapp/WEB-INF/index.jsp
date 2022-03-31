<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
    
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>  

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">

<!-- for Bootstrap CSS -->
<link rel="stylesheet" href="/webjars/bootstrap/css/bootstrap.min.css" />
<!-- For any Bootstrap that uses JS or jQuery-->
<script src="/webjars/jquery/jquery.min.js"></script>
<script src="/webjars/bootstrap/js/bootstrap.min.js"></script>

<title>Rendering Books</title>
</head>
<body class="bg-secondary">
	<div class="m-5">
		<h1 class="text-info">All Books</h1>
		<c:forEach var="oneBook" items="${books}">
		<div class="col-sm-5"> 
			<table class="table table-hover table-dark">
				<thead>
					<tr>
						<th scope="col">ID</th>
						<th scope="col">Title</th>
						<th scope="col">Language</th>
						<th scope="col"># Pages</th>
					</tr>
				</thead>
				<tbody>
					<tr>
						<td><c:out value="${oneBook.id}"></c:out></td>
						<td class="w-50"><c:out value="${oneBook.title}"></c:out></td>
						<td><c:out value="${oneBook.language}"></c:out></td>
						<td><c:out value="${oneBook.numberOfPages}"></c:out></td>
					</tr>
				</tbody>
			</table>
		</div>
		</c:forEach>
	</div>
</body>
</html>