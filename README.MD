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

LibraLink is designed to address the inefficiencies of traditional library management systems.

The LibraLink Library Management System is being developed to solve the problem of effectively managing the operations of a library. Specifically, the key problems this app aims to address are:
- **Efficient Book Management:** Providing a centralized system to track and manage the library's book inventory, including details like book titles, authors, categories, and availability status.
- **Streamlined Borrowing Process:** Enabling members to borrow and return books seamlessly, while also tracking the borrowing history and any associated fines.
- **Improved Data Organization:** Organizing the library's data, such as member information, book categories, and borrowing records, in a structured and easily accessible manner.
- **Enhanced Reporting and Analytics:** Generating reports and analytics to help the library staff make informed decisions about book acquisitions, member engagement, and overall operational efficiency.


### R2 - Why is it a problem that needs solving?

The problems mentioned above are common challenges faced by many libraries, especially as their collections and member base grow. Without a centralized and well-organized library management system, libraries can struggle with the following issues:

- Difficulty in tracking book inventory and availability.
- Inefficient borrowing and return processes, leading to delays and confusion.
- Fragmented and disorganized data, making it hard to retrieve information and generate meaningful reports.
- Lack of visibility into library operations, hindering data-driven decision-making.

By addressing these problems, the LibraLink Library Management System aims to improve the overall efficiency, user experience, and data-driven decision-making capabilities of the library.


### R3 - Why have you chosen this database system. What are the drawbacks compared to others?

The LibraLink Library Management System will use a relational database, specifically PostgreSQL, to store and manage the data. The choice of PostgreSQL is based on the following key factors:

1. **Scalability:** PostgreSQL is highly scalable and can handle large amounts of data and high traffic loads, making it suitable for a growing library management system.

2. **Data Integrity:** PostgreSQL provides strong data integrity features, such as ACID (Atomicity, Consistency, Isolation, Durability) compliance, which ensures the reliability and consistency of the data.

3. **Extensibility:** PostgreSQL has a rich ecosystem of extensions and plugins, allowing for the addition of specialized features and functionalities as the project evolves.

4. **SQL Compliance:** PostgreSQL closely adheres to the SQL standard, making it easier to work with and integrate with other applications and tools.

5. **Community and Support:** PostgreSQL has a large and active community of developers and users, providing extensive documentation, resources, and support.

Compared to other database systems, such as MySQL or SQLite, the potential drawbacks of using PostgreSQL for the LibraLink project may include:

1. **Complexity:** PostgreSQL is a more feature-rich and complex database system, which may require a steeper learning curve for some developers.

2. **Performance:** While PostgreSQL is highly scalable, for certain workloads or use cases, other database systems like MySQL may offer slightly better performance, especially for read-heavy applications.

3. **Cost:** Depending on the scale and requirements of the project, the cost of running and maintaining a PostgreSQL database may be higher than some other open-source or cloud-based database options.

However, the benefits of using PostgreSQL, such as its data integrity, scalability, and strong community support, outweigh the potential drawbacks for the LibraLink Library Management System. The project team believes that PostgreSQL is the most suitable choice to meet the long-term needs and requirements of the library's data management needs.



### R4 - Identify and discuss the key functionalities and benefits of an ORM

Object-Relational Mapping (ORM) libraries, such as SQLAlchemy in the case of the LibraLink Library Management System, offer several key functionalities and benefits:

- Abstraction: ORMs abstract the underlying database implementation, allowing developers to work with the database using an object-oriented approach rather than writing raw SQL queries. This abstraction simplifies data manipulation and enhances code readability.
- Data Mapping: ORMs map database tables to Python classes, enabling developers to interact with database entities as objects in their code. This simplifies data access and manipulation by providing a more intuitive interface.
- Query Optimization: ORMs can optimize database queries, reducing the need for manual query optimization. They can generate efficient SQL queries based on high-level object-oriented operations, improving performance.
- Portability: ORMs provide a layer of abstraction that allows applications to be easily ported to different database systems without significant changes to the codebase. This portability enhances flexibility and reduces vendor lock-in.
- Automatic Schema Management: ORMs handle database schema changes, such as adding or modifying tables, columns, and relationships. This simplifies database management tasks and ensures data consistency across schema changes.
- Relationship Management: ORMs facilitate managing relationships between database entities, such as one-to-many, many-to-many, and one-to-one relationships. This simplifies complex data modeling and ensures data integrity.
- Data Validation: ORMs can handle data validation at the model level, enforcing constraints and ensuring data integrity before interacting with the database. This reduces the risk of data corruption or inconsistency.
- Lazy Loading: ORMs support lazy loading, where related data is loaded only when needed, reducing unnecessary database queries and improving performance by fetching data on-demand.

By leveraging these functionalities and benefits of an ORM like SQLAlchemy in the LibraLink project, developers can streamline database interactions, improve code maintainability, enhance performance, and simplify complex data modeling tasks.



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

