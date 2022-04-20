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
	<div class="container d-flex flex-column align-items-left text-light bg-dark p-3 mt-3">
		<div>
			<div class="d-flex justify-content-between">
				<h1 class="text-info">Welcome, <c:out value="${user.firstName}"></c:out>!</h1>
				<a href="/logout">Logout</a>
			</div>
			<div class="d-flex justify-content-between">
				<h5 class="text-danger">All Projects</h5>
				<a href="/dashboard/new">+New Project</a>
			</div>
			<div>
			<table class="table table-danger table-striped">
				<thead>
					<tr>
						<th scope="col">Project</th>
						<th scope="col">Team Lead</th>
						<th scope="col">Due Date</th>
						<th scope="col">Actions</th>
					</tr>
				</thead>
				<tbody>
					<c:forEach var="project" items="${notInProjects}">
					<tr>
						<c:if test="${project.lead.id != user.id}">
						<td><a href="/dashboard/${project.id}"><c:out value="${project.title}"></c:out></a></td>
						<td><c:out value="${project.lead.firstName}"></c:out></td>
						<td><fmt:formatDate value="${project.dueDate}" pattern="MMM dd"/></td>
						<td><a href="/dashboard/join/${project.id}">Join Team</a></td>
						</c:if>
					</tr>
					</c:forEach>
				</tbody>
			</table>
			</div>
			<div class="">
			<h5 class="text-success">Your Projects</h5>
			<table class="table table-success table-striped">
				<thead>
					<tr>
						<th scope="col">Project</th>
						<th scope="col">Lead</th>
						<th scope="col">Due Date</th>
						<th scope="col">Actions</th>
					</tr>
				</thead>
				<tbody>
					<c:forEach var="project" items="${inProjects}">
					<tr>
						<td><a href="/dashboard/${project.id}"><c:out value="${project.title}"></c:out></a></td>
						<td><c:out value="${project.lead.firstName}"></c:out></td>
						<td><fmt:formatDate value="${project.dueDate}" pattern="MMM dd"/></td>
						<c:if test="${project.lead.id == user.id}">
							<td><a href="/dashboard/edit/${project.id}">Edit</a></td>
						</c:if>
						<c:if test="${project.lead.id != user.id}">
							<td><a href="/dashboard/leave/${project.id}">Leave Team</a></td>
						</c:if>
					</tr>
					</c:forEach>
				</tbody>
			</table>
			</div>
		</div>
	</div>
</body>
</html>