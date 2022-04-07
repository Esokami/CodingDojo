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

<title>Dojos</title>
</head>
<body class="bg-secondary">
	<div class="bg-dark m-5 p-3 w-50">
		<h1 class="text-info">All Dojos</h1>

		<div class="col-sm-5"> 
			<table class="table table-striped table-secondary">
				<thead>
					<tr>
						<th scope="col">Dojos</th>
					</tr>
				</thead>
				<tbody>
					<c:forEach var="oneDojo" items="${dojos}">
					<tr>
						<td><c:out value="${oneDojo.name}"></c:out></td>
					</tr>
					</c:forEach>
				</tbody>
			</table>
		</div>
	</div>
</body>
</html>