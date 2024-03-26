# T2A2 - API Webserver Project
## LibraLink - Library Management System

**LibraLink** is a comprehensive library management system designed to streamline the administration of library resources.


[Github Link]() | [Trello Link]()

## Table of Contents:

- Installation
- R1: Identification of the problem you are trying to solve by building this particular app.
- R2: Why is it a problem that needs solving?
- R3: Why have you chosen this database system? What are the drawbacks compared to others?
- R4: Identify and discuss the key functionalities and benefits of an ORM.
- R5: Document all endpoints for your API.
- R6: An ERD for your app.
- R7: Detail any third-party services that your app will use.
- R8: Describe your project’s models in terms of the relationships they have with each other.
- R9: Discuss the database relations to be implemented in your application.
- R10: Describe the way tasks are allocated and tracked in your project.



## Installation Instructions:
Step-by-step guide on how to install and run the application.


### R1 - Identification of the problem you are trying to solve by building this particular app.

LibraLink aims to solve the problem of managing library operations digitally.

LibraLink is designed to address the inefficiencies of traditional library management systems.

It will streamline the process of tracking books, managing loans, improving inventory management, and enhancing user engagement with the library

### R2 - Why is it a problem that needs solving?

Manual library management is prone to errors, inefficient, and cannot easily scale. By digitizing these processes, LibraLink will improve accuracy, efficiency, and provide a better user experience for library staff and members.


### R3 - Why have you chosen this database system. What are the drawbacks compared to others?

PostgreSQL is chosen for its reliability, ACID compliance, and support for complex queries and data types. While it may not be as lightweight as SQLite or offer the distributed features of NoSQL databases like MongoDB, its robustness makes it ideal for transactional systems like LibraLink.


### R4 - Identify and discuss the key functionalities and benefits of an ORM

An ORM (Object-Relational Mapping) like SQLAlchemy abstracts the database into objects, making it easier to interact with data programmatically. It automates CRUD operations, reduces SQL injection risks, and can improve development speed.


### R5 - Document all endpoints for your API

The API will have endpoints for books, members, borrowing records, categories, and staff, each supporting GET, POST, PUT, and DELETE methods as appropriate for full CRUD functionality.

The API will include endpoints such as:

/books (GET, POST, PUT, DELETE)

/members (GET, POST, PUT, DELETE)

/borrowing_records (GET, POST, PUT, DELETE)

/categories (GET, POST, PUT, DELETE)

/staff (GET, POST, PUT, DELETE)



### R6 - An ERD for your app

The ERD will illustrate the relationships between books, members, borrowing records, categories, and staff, showing how these entities interact within the library system.


### R7 - Detail any third party services that your app will use

LibraLink will use Insomnia API Client for testing endpoints, Trello for task management, and potentially email services for notifications; etc.

### R8 - Describe your projects models in terms of the relationships they have with each other

Books are associated with categories and borrowing records. Members are linked to borrowing records. Staff are connected to borrowing records and can update book statuses.

The models in LibraLink reflect real-world library entities and their interactions:

    Books are categorized and involved in borrowing transactions.
    Members engage in borrowing activities.
    Staff oversee borrowing records and manage book statuses.



### R9 - Discuss the database relations to be implemented in your application

The database will implement one-to-many relationships between categories and books, books and borrowing records, and members and borrowing records. Staff will manage borrowing records.

The database will implement relations such as:

    One-to-Many between Categories and Books.
    One-to-Many between Books and Borrowing Records.
    One-to-Many between Members and Borrowing Records.


### R10 - Describe the way tasks are allocated and tracked in your project

I use Trello as my Project Management Tool/Software to manage my Software Development Plan.

First I created a simple Software Development Plan (SDP), this was only for the purpose of giving a high level view of the project as a whole. The estimated time was set at the beginning to be 11 hours, which is highly unlikely but provide a rough idea of how I expect myself to do this type of project in the future once becoming experienced. It also show a bigger picture and the idea of how should I spend most of my time in the project (Setup 10-15%, Documentation 10-15%, SDP 10%, Coding 30-35%, Endpoint Doc 10%, Error handling/Testing 10-15%, Review and Deployment Prep 5-10%)

Day 1 - 25/03/2024

Got Idea approved, ERD done

